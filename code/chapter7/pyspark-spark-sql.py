import os
import uuid
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType

conf = SparkConf().setAppName("MiApp").setMaster("local[*]")
spark = SparkSession.builder.config(conf=conf).getOrCreate()

l = [('a', 3.14), ('b', 9.4), ('a', 2.7)]
df = spark.createDataFrame(l, ['key', 'value'])

df.show()

print('----------------------------------------------------------------------')
df.printSchema()  # Imprimir el esquema del DataFrame
print('----------------------------------------------------------------------')
schema = StructType([
    StructField("key", StringType(), True),
    StructField("value", FloatType(), True)
])

df = spark.createDataFrame(l, schema=schema)
df.show()
print('----------------------------------------------------------------------')
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'titanic.csv')
df = spark.read.csv(path, header=True, inferSchema=True)
df.printSchema()  # Imprimir el esquema del DataFrame
print('----------------------------------------------------------------------')
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'tweets.json')
df = spark.read.json(path, multiLine=True)
df.printSchema()  # Imprimir el esquema del DataFrame
df.show()
print('----------------------------------------------------------------------')
l = [('a', 3.14), ('b', 9.4), ('a', 2.7)] * 50
df = spark.createDataFrame(l, ['key', 'value'])
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'tmp', 'csv')
df.write.csv(path, header=True, mode='overwrite')
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'tmp', 'json')
df.write.json(path, mode='overwrite')

print("----------------------------------------------------------------------")
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'titanic.csv')
df2 = spark.read.csv(path, header=True, inferSchema=True)
df2.printSchema()  # Imprimir el esquema del DataFrame
df2.describe(['Age', 'Fare', 'Sex', 'Cabin']).show()  # Estadísticas descriptivas de las columnas 'Age' y 'Fare'
print("----------------------------------------------------------------------")
print(df2.columns)  # Imprimir los nombres de las columnas
print(df2.dtypes)  # Imprimir los tipos de datos de las columnas
df3 = df2.drop('PassengerId', 'Name', 'Cabin')  # Eliminar columnas innecesarias
print("DataFrame después de eliminar columnas:" )
print(df3.columns)  # Verificar las columnas restantes
df3.printSchema()  # Imprimir el esquema del DataFrame después de eliminar columnas
print("----------------------------------------------------------------------")
df4 = df2.select('Survived','Pclass', 'Age')
print("DataFrame con columnas seleccionadas:")
df4.show()
print("----------------------------------------------------------------------")
print('Eliminar duplicados:')
print("Número de filas antes de eliminar duplicados:", df2.count())
df5 = df2.dropDuplicates()
print("DataFrame sin duplicados:")
print(df5.count())  # Contar el número de filas después de eliminar duplicados
df6 = df2.dropDuplicates(['Sex'])
print("DataFrame sin duplicados:")
print(df6.count())  # Contar el número de filas después de eliminar duplicados
print("----------------------------------------------------------------------")
print('Dataframe sin nulos:')
df7 = df2.dropna()
print("Número de filas antes de eliminar nulos:", df2.count())
print("Número de filas después de eliminar nulos:", df7.count())
print("-----------------------------------------------------------------------")
df8 = df2.filter('Survived = 1')
df8.count()  # Contar el número de sobrevivientes
print("Número de sobrevivientes:", df8.count())
print("----------------------------------------------------------------------")
df9 = df2.filter(df2['Age'] > 30)
print("DataFrame con pasajeros mayores de 30 años:")
df9.show()
print("Número de pasajeros mayores de 30 años:", df9.count())
df10 = df2.filter('Survived = 1 AND Sex = "female" AND Age > 20')
print(df10.count(), "mujeres sobrevivientes mayores de 20 años.")
df11 = df2.filter( ( df2.Survived == 1 ) & (df2['Sex'] == 'female') & (df2.Age > 20) )
print(df11.count(), "mujeres sobrevivientes mayores de 20 años (con &).")
print("----------------------------------------------------------------------")
df12 = spark.createDataFrame([(str(uuid.uuid4()), 'Ana'),(str(uuid.uuid4()), 'Jose'),(str(uuid.uuid4()), 'Luis')], ['id', 'nombre'])
df13 = spark.createDataFrame([(str(uuid.uuid4()), 'Pedro'),(str(uuid.uuid4()), 'Pedro'),(str(uuid.uuid4()), 'Juan')], ['id', 'nombre'])
df14 = df12.union(df13)
print("DataFrame después de unirse:")
df14.show()
print("Número de filas después de unirse:", df14.count())
print("----------------------------------------------------------------------")
df15 = spark.createDataFrame([(1, 'Ana'),(2, 'Jose'),(3, 'Luis')], ['id', 'nombre'])
df16 = spark.createDataFrame([(4, 'Pedro'),(1, 'Ana'),(5, 'Juan')], ['id', 'nombre'])
df17 = df15.intersect(df16)
print("DataFrame después de intersectar:")
df17.show()
print("Número de filas después de intersectar:", df17.count())
print("----------------------------------------------------------------------")
df18 = spark.createDataFrame([(1, 'Ana'),(2, 'Jose'),(3, 'Luis')], ['id', 'nombre'])
df19 = spark.createDataFrame([(1, 25),(2, 32),(3, 27)], ['id', 'edad'])
df20 = df18.join(df19, on='id', how='inner')
print("DataFrame después de hacer un join:")
df20.show()
print("Número de filas después de hacer un join:", df20.count())
df20.printSchema()  # Imprimir el esquema del DataFrame después del join
df21 = spark.createDataFrame([(1, 'Ana', 'tennis'),(2, 'Jose', 'football'),(3, 'Luis', 'baseball')], ['id', 'nombre', 'deporte'])
df22 = df20.join(df21, ['id', 'nombre'], 'inner')
df22.show()
df22.printSchema()  # Imprimir el esquema del DataFrame después del join con múltiples columnas
print("Número de filas después de hacer un join con múltiples columnas:", df22.count()) 
print("----------------------------------------------------------------------")
age = spark.createDataFrame([(None, 1, 33), (2, 5, 30),(3, None, 42)],['id1', 'id2', 'edad'])
condition = ( ( (age.id1.isNotNull()) & (df18.id == age.id1) ) | ( (age.id2.isNull()) & (df18.id == age.id2) ) )
df23 = df18.join(age, condition)
df23.show()
print("DataFrame después de hacer un join con condición compleja:")
print("Número de filas después de hacer un join con condición compleja:", df23.count())
print("----------------------------------------------------------------------")
path = os.path.join(base_dir, '..', '..', 'data', 'chapter7', 'titanic.csv')
titanic = spark.read.csv(path, header=True, inferSchema=True).drop('Cabin').dropna()
titanic.selectExpr('Survived', 'SibSp + Parch As Family', 'Age * 12 AS Age').show(10)
print("----------------------------------------------------------------------")
titanic.groupBy('Survived').count().show()
titanic.groupBy().sum('Survived').show()
titanic.groupBy('Pclass').sum('Survived').show()
titanic.groupBy('Pclass').sum('Survived', 'Fare').orderBy('Pclass').show()
print("----------------------------------------------------------------------")
users = spark.createDataFrame(
    [(1, 'Alice'), (2, 'Bob'), (3, 'Cathy')],
    ['id', 'name']
)
ages = spark.createDataFrame(
    [(1, 30), (2, 25), (3, 28)],
    ['id', 'age']
)
users.createOrReplaceTempView("users")
ages.createOrReplaceTempView("ages")
spark.sql("""
    SELECT u.id, u.name, a.age
    FROM users u
    JOIN ages a ON u.id = a.id
""").show()
print("----------------------------------------------------------------------")
def sex_to_num(s):
    ret = None
    if s == 'female':
        ret = 0
    elif s == 'male':
        ret = 1
    return ret

from pyspark.sql.types import IntegerType
spark.udf.register('sex_to_num', sex_to_num, IntegerType())
titanic.selectExpr('Name', 'Sex', 'sex_to_num(Sex) AS Sex_num').show(5)
