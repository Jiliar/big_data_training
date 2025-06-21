import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, stddev, min, max

spark = SparkSession.builder \
    .appName("MongoDBIntegrationCorrected") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.13:10.3.0") \
    .getOrCreate()

# CAMBIO: Datos de población corregidos a números enteros y realistas
ciudades_corregido = [
    ("Madrid", 3140000, 40.4168, -3.7038),
    ("Barcelona", 1600000, 41.3851, 2.1734),
    ("Valencia", 800000, 39.4699, -0.3763),
    ("Sevilla", 688000, 37.3886, -5.9823),
    ("Bilbao", 345000, 43.2630, -2.9349),
    ("Zaragoza", 38000, 41.6488, -0.8891), 
    ("Málaga", 29000, 36.7213, -4.4214), 
    ("Murcia", 18000, 37.9922, -1.1307),
    ("Palma de Mallorca", 416000, 39.5696, 2.6502),
    ("Las Palmas de Gran Canaria", 378000, 28.1235, -15.4363)
]

# Crear DataFrame con los datos
df_corregido = spark.createDataFrame(ciudades_corregido, ['Ciudad', 'Poblacion', 'Latitud', 'Longitud'])

print("DataFrame con datos corregidos:")
df_corregido.show()

# Escribir en MongoDB, SOBREESCRIBIENDO los datos anteriores para limpiar
(df_corregido.write
    .format("mongodb")
    .mode("overwrite")  # Usamos overwrite para empezar de cero con datos buenos
    .option("connection.uri", "mongodb://admin:secret123@localhost:27017/?authSource=admin")
    .option("database", "geo")
    .option("collection", "cities")
    .save())

print("Datos escritos en MongoDB.")
print("----------------------------------------------------------------------")


# El pipeline ahora encontrará documentos que coincidan
# El campo en MongoDB es "Poblacion" (sin tilde), ya que Spark lo normaliza al escribir.
pipeline = "[{ '$match': { 'Poblacion': { '$gt': 500000 } } }]" # Buscamos > 500,000

mas_de_500k = (
    spark.read
    .format("mongodb")
    .option("connection.uri", "mongodb://admin:secret123@localhost:27017/?authSource=admin")
    .option("database", "geo")
    .option("collection", "cities")
    .option("aggregation.pipeline", pipeline)
    .load()
)

print("Ciudades con más de 500,000 habitantes (filtrado en MongoDB):")
mas_de_500k.show()
print(mas_de_500k.count(), "ciudades encontradas.")
mas_de_500k.select(mean("Poblacion")).show()
mas_de_500k.select(stddev("Poblacion")).show()
mas_de_500k.select(min("Poblacion")).show()
mas_de_500k.select(max("Poblacion")).show()
print("----------------------------------------------------------------------")
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'titanic.csv')
titanic = spark.read.csv(path, header=True, inferSchema=True)


# Escribir en MongoDB, SOBREESCRIBIENDO los datos anteriores para limpiar
(titanic.write
    .format("mongodb")
    .mode("overwrite")  # Usamos overwrite para empezar de cero con datos buenos
    .option("connection.uri", "mongodb://admin:secret123@localhost:27017/?authSource=admin")
    .option("database", "data")
    .option("collection", "titanic")
    .save())

print("Datos escritos en MongoDB.")
print("----------------------------------------------------------------------")


def scale(n, minv, maxv):
    return (n - minv) / (maxv - minv)

# Calculate min_age and max_age from the titanic DataFrame
age_stats_row = titanic.selectExpr("min(Age) as min_age", "max(Age) as max_age").collect()[0]
min_age = age_stats_row["min_age"]
max_age = age_stats_row["max_age"]

from pyspark.sql.types import DoubleType
spark.udf.register('scale_Age', lambda x: scale(x, min_age, max_age), DoubleType())
titanic.selectExpr('Age', 'scale_Age(Age) AS Scaled_Age').show(3)
