import os
import uuid
from pyspark import SparkConf, SparkContext

# Configuración del SparkContext en modo local utilizando todos los núcleos disponibles
conf = SparkConf().setAppName("MiApp").setMaster("local[*]")
sc = SparkContext(conf=conf)

# Creación de RDDs básicos desde listas locales
print("SparkContext creado:", sc)

r1 = sc.parallelize([1, 2, 3, 4, 5])  # RDD con números enteros
print(type(r1))

r2 = sc.parallelize(["hola", "hi","ciao"])  # RDD con cadenas de texto
print(type(r2))

r3 = sc.parallelize([i*i for i in range(1,101)])  # RDD con cuadrados del 1 al 100
print(type(r3))

print('----------------------------------------------------------------------')
# Lectura de un archivo TXT en modo texto plano
base_dir = os.path.dirname(__file__)
ruta = os.path.join(base_dir, '..', '..', 'data', 'chapter6', 'file.txt')
r4 = sc.textFile(ruta)  # Cada línea del archivo se convierte en un elemento del RDD
print(type(r4))
print(r4.collect())

# Alternativas para leer desde HDFS o S3
# r = sc.textFile("hdfs://node:port/data/file.txt")
# r = sc.textFile("s3n://bucket/file.txt")
print('----------------------------------------------------------------------')
# Lectura de múltiples archivos TXT utilizando comodín (*.txt)
path1 = os.path.join(base_dir, '..', '..', 'data', 'chapter6', '*.txt')
r5 = sc.textFile(path1)
print(type(r5))
print(r5.collect())

print('----------------------------------------------------------------------')
# Lectura de todos los archivos del directorio (todos los archivos de texto plano en el folder)
path2 = os.path.join(base_dir, '..', '..', 'data', 'chapter6')
r6 = sc.textFile(path2)
print(type(r6))
print(r6.collect())

print('----------------------------------------------------------------------')
# Lectura del contenido de archivos junto con sus rutas como clave (formato clave-valor)
r7 = sc.wholeTextFiles(path1)
print(r7.take(3))
print('----------------------------------------------------------------------')

# Obtener los primeros 2 elementos en orden (alfabético o numérico dependiendo del contenido)
print(r6.takeOrdered(2))
print('----------------------------------------------------------------------')
# Muestreo de 2 elementos sin reemplazo del RDD
# “Con reemplazo” (withReplacement=True) permite repetir elementos en la muestra
print(r6.takeSample(False, 2))

print('----------------------------------------------------------------------')
print(r6.count()) # Contar el número total de elementos en el RDD

print('----------------------------------------------------------------------')
def add(x, y):
    return x + y  
# Sumar todos los elementos del RDD utilizando reduce
r8 = sc.parallelize(range(1, 6))  # RDD con números del 1 al 1000
print(r8.reduce(add))
print(r8.reduce(lambda x, y: x + y))  # Alternativa con lambda
print('----------------------------------------------------------------------')
def multiply_positive(x, y):
    if x > 0 and y > 0:
        return x * y
    elif x > 0:
        return x
    elif y > 0:
        return y
    else:
        return 0

r9 = sc.parallelize([-1, 2, 1, -5, 8])  # RDD con números enteros positivos y negativos
print(r9.reduce(multiply_positive))

print('----------------------------------------------------------------------')
# problema operativo con reduce se da con la resta si variamos el número de particiones de un RDD
r10 = sc.parallelize(range(3), 1) #   RDD con 3 elementos y 1 partición
print(r10.reduce(lambda x,y: x-y))

r11 = sc.parallelize(range(3), 2) #   RDD con 3 elementos y 2 particiones
print(r11.reduce(lambda x,y: x-y))

print('----------------------------------------------------------------------')
r12 = sc.parallelize(["hola", "hi" , "ciao"])
r_aux = r12.aggregate(0, lambda c, s : c + s.count('h'), lambda c1, c2: c1 + c2)
print("Número de palabras que contienen 'h':", r_aux)

# Generar un UUID aleatorio (versión 4)
uuid_str = str(uuid.uuid4())
r13 = sc.parallelize(range(1000), 2) 
path13 = os.path.join(base_dir, '..', '..', 'data', 'chapter6', uuid_str)
r13.saveAsTextFile(path13) # Guardar el RDD como archivos de texto en el directorio especificado

print('----------------------------------------------------------------------')
r14 = sc.parallelize([1,2,3,4])
r15 = r14.map(lambda x: x + 1)  # Multiplicar cada elemento por 2
print(r15.collect())

print('----------------------------------------------------------------------')
def increment(x):
    return x + 1
r16 = r14.map(increment)  # Alternativa con función definida por el usuario
print(r16.collect())

print('----------------------------------------------------------------------')
r17 = sc.parallelize(["hola", "hi", "ciao"])
r18 = r17.map(lambda x: (x, len(x)))  # Crear un RDD de tuplas (palabra, longitud)
print(r18.collect())

print('----------------------------------------------------------------------')
import csv
r19 = sc.parallelize(["1,5,7","8,2,4"])
r20 = r19.mapPartitions(lambda x: csv.reader(x))  # Leer CSV desde cada partición
print(r20.collect())    

print('----------------------------------------------------------------------')
def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
r21 = sc.parallelize(range(2, 31))  # RDD con números de 2 a 30
r22 = r21.filter(es_primo)  # Filtrar números primos
print(r22.collect())

print('----------------------------------------------------------------------')
r23 = sc.parallelize([('a', 0),('b', 1),('c',2)])
r24 = r23.mapValues(lambda x: x + 1)  # Incrementar el valor de cada tupla
print(r24.collect())

r25 = sc.parallelize([('a', 0),('b', 1),('c',2)])
r26 = r25.map(lambda x: (x[0], x[1] + 1))  # Alternativa con función lambda
print(r26.collect())

print('----------------------------------------------------------------------')
r27 = sc.parallelize([('a', '1,5,7'),('b', '8,2')])
r28 = r27.flatMapValues(lambda x: list(csv.reader([x]))[0])  # Descomponer cadenas CSV en valores individuales
print(r28.collect())

print('----------------------------------------------------------------------')
r29 = sc.parallelize([('a', 3.14),('b', 9.4), ('a', 2.7)])
r30 = r29.groupByKey()  # Agrupar por clave
print(r30.collect())
r31 = r30.mapValues(lambda x: list(x))  # Convertir los valores agrupados en listas
print(r31.collect())

print('----------------------------------------------------------------------')
r32 = sc.parallelize([('a', 3.14),('b', 9.4), ('a', 2.7)])
r33 = r32.reduceByKey(lambda x, y: x + y)  # Sumar valores por clave
print(r33.collect())

print('----------------------------------------------------------------------')
r34 = sc.parallelize([1,2,3,4,5])
r35 = sc.parallelize([2,4,6])
r36 = r34.union(r35)  # Unir dos RDDs
print(r36.collect())
print('----------------------------------------------------------------------')
r37 = r36.distinct()  # Eliminar duplicados
print(r37.collect())
print('----------------------------------------------------------------------')
r38 = r36.intersection(r35)  # Intersección entre dos RDDs
print(r38.collect())
print('----------------------------------------------------------------------')
r39 = r36.subtract(r35)  # Diferencia entre dos RDDs primero menos segundo
print(r39.collect())
print('----------------------------------------------------------------------')
r40 = sc.parallelize([1,2,3,4,5])
r41 = sc.parallelize([2,4,6])
r42 = r40.cartesian(r41)  # Producto cartesiano entre dos RDD
print(r42.collect())
print('----------------------------------------------------------------------')
r43 = sc.parallelize([('a',1),('b',2),('c',3)])
r44 = sc.parallelize([('b',8),('d',7), ('b',5)])
r45 = r43.join(r44)  # Unión de dos RDDs por clave
print(r45.collect())
print('----------------------------------------------------------------------')
path = os.path.join(base_dir, '..', '..', 'data', 'chapter6', 'titanic.csv')
raw = (
    sc.textFile(path)
    .map(lambda s: list(csv.reader([s]))[0])  # Leer CSV desde el archivo
    .filter(lambda x: x[0] != 'PassengerId')  # Filtrar encabezados
)
print(raw.take(5))  # Mostrar las primeras 5 filas del RDD
print(raw.count())  # Contar el número total de filas en el RDD
print('----------------------------------------------------------------------')
def complete(l):
    for i in [1,2,4,5,6,7,9,11]:
        if l[i] == '':
            return False
    return True

def proyect_and_parse(l):
    return {
        'PassengerId': int(l[1]),
        'Pclass': int(l[2]),
        'Sex': l[4],
        'Age': float(l[5]) if l[5] else None,
        'SibSp': int(l[6]),
        'Parch': int(l[7]),
        'Fare': float(l[9]) if l[9] else None,
        'Embarked': l[11]
    }

non_null = (
    raw
    .filter(complete)  # Filtrar filas completas
    .map(proyect_and_parse)  # Proyectar y parsear las columnas relevantes
)

print(non_null.take(5))  # Mostrar las primeras 5 filas del RDD procesado
print(non_null.count())