# 📊 Guía de Manipulación de Datos en MongoDB con `mongosh`

Este documento sirve como una guía de referencia rápida para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y gestionar colecciones en MongoDB a través de su shell, `mongosh`. ¡Vamos allá! 🚀

## 1. 🔌 Conexión a la Base de Datos

Para empezar a trabajar, primero necesitas conectarte a tu instancia de MongoDB. El siguiente comando se conecta a una base de datos local, especificando usuario, contraseña y la base de datos de autenticación.

```bash
# Formato: mongosh "mongodb://<usuario>:<contraseña>@<host>:<puerto>/<db>?authSource=<db_auth>"
mongosh "mongodb://admin:secret123@127.0.0.1:27017/local?authSource=admin"
```

Una vez dentro de `mongosh`, todos los comandos se ejecutan en el contexto de la base de datos a la que te has conectado o a la que cambies con `use <nombre_db>`.

## 2. ✨ Operaciones de Creación (Create)

### Insertar un solo documento

El comando `insertOne()` se utiliza para añadir un único documento a una colección. Si la colección no existe, MongoDB la creará automáticamente. ¡Magia! 🪄

```javascript
// Inserta un nuevo documento en la colección 'tweets'
db.tweets.insertOne({
  _id: 1,
  usuario: {
    nick: "bertoldo",
    seguidores: 1320
  },
  texto: "@herminia: hoy, excursión a la sierra con @aniceto!",
  menciones: ["herminia", "aniceto"],
  RT: false,
  fecha: new Date() //💡 Es buena práctica añadir una fecha de creación
});
```

### Insertar múltiples documentos

Para insertar varios documentos a la vez de forma eficiente, se utiliza `insertMany()`. ¡Más es más! 📚

```javascript
// Inserta un array de documentos en la colección 'tweets'
db.tweets.insertMany([
  {
    _id: 2,
    usuario: { nick: "herminia", seguidores: 2500 },
    texto: "¡Qué ganas de excursión!",
    menciones: [],
    RT: false,
    fecha: new Date()
  },
  {
    _id: 3,
    usuario: { nick: "aniceto", seguidores: 980 },
    texto: "Confirmado, nos vemos en la sierra @bertoldo @herminia",
    menciones: ["bertoldo", "herminia"],
    RT: false,
    fecha: new Date()
  }
]);
```

## 3. 🔎 Operaciones de Lectura (Read)

### Buscar todos los documentos

Para obtener todos los documentos de una colección, se utiliza `find()` con un objeto de consulta vacío `{}`.

```javascript
// Devuelve un cursor con todos los documentos de la colección 'tweets'
db.tweets.find({});
```

### Buscar documentos con un filtro 🎯

Puedes pasar un objeto de consulta a `find()` para filtrar los documentos según ciertos criterios.

```javascript
// Encuentra todos los tweets del usuario con nick 'bertoldo'
db.tweets.find({ "usuario.nick": "bertoldo" });

// Encuentra tweets que mencionen a 'herminia'
db.tweets.find({ menciones: "herminia" });
```

### Buscar un solo documento ☝️

Si solo esperas un resultado o solo te interesa el primero que coincida, `findOne()` es más eficiente. Devuelve el documento directamente, no un cursor.

```javascript
// Busca un único tweet por su _id
var tweet = db.tweets.findOne({ _id: 1 });

// Para imprimir el resultado en la consola de mongosh
print(tweet);
```

### Proyección: Seleccionar campos específicos ✂️

Para limitar los campos que devuelve una consulta, se añade un segundo objeto al método `find()`, llamado proyección. Usa `1` para incluir un campo y `0` para excluirlo.

```javascript
// Busca todos los tweets, pero solo devuelve el texto y el nick del usuario
// El campo _id se devuelve por defecto, hay que excluirlo explícitamente si no se quiere
db.tweets.find({}, { texto: 1, "usuario.nick": 1, _id: 0 });
```

## 4. ✏️ Operaciones de Actualización (Update)

### Actualizar un solo documento

`updateOne()` modifica el primer documento que coincide con el filtro. Es crucial usar **operadores de actualización** como `$set` para modificar solo los campos especificados sin reemplazar todo el documento.

```javascript
// Actualiza el nick del usuario en el tweet con _id: 1
db.tweets.updateOne(
  { _id: 1 }, // Filtro para encontrar el documento
  { $set: { "usuario.nick": "bertoldo_el_explorador" } } // Operador y datos a actualizar
);

// Incrementa el número de seguidores en 10 🔼
db.tweets.updateOne(
  { _id: 1 },
  { $inc: { "usuario.seguidores": 10 } }
);
```

### Actualizar múltiples documentos 🔄

`updateMany()` modifica **todos** los documentos que coinciden con el filtro.

```javascript
// Añade un campo 'verificado: false' a todos los tweets que no lo tengan
db.tweets.updateMany(
  { verificado: { $exists: false } }, // Filtro: documentos donde el campo 'verificado' no existe
  { $set: { verificado: false } }     // Acción: añadir el campo con valor 'false'
);
```

> **💡 Nota:** El método `update()` es un método más antiguo. En versiones modernas de MongoDB, se recomienda usar explícitamente `updateOne()` o `updateMany()` para evitar actualizaciones accidentales.

## 5. 🗑️ Operaciones de Eliminación (Delete)

### Eliminar un solo documento

`deleteOne()` elimina el primer documento que coincide con el filtro proporcionado.

```javascript
// Elimina el tweet con _id: 3
db.tweets.deleteOne({ _id: 3 });
```

### Eliminar múltiples documentos

`deleteMany()` elimina **todos** los documentos que coinciden con el filtro.

```javascript
// Elimina todos los tweets que sean un RT
db.tweets.deleteMany({ RT: true });
```

Para eliminar **todos los documentos** de una colección, se usa un filtro vacío.

```javascript
// 🚨 ¡CUIDADO! 🚨 Esto elimina todos los documentos de la colección 'tweets'
db.tweets.deleteMany({});
```

> **📜 Nota sobre `remove()`**: El método `db.collection.remove()` está obsoleto (deprecated). Aunque todavía puede funcionar, la práctica recomendada es usar `deleteOne()` o `deleteMany()` por su claridad y seguridad.

## 6. 🗄️ Gestión de Colecciones

Estos comandos te permiten administrar las colecciones dentro de una base de datos.

### Crear una colección explícitamente 🆕

Aunque MongoDB crea colecciones al insertar el primer documento, puedes crear una explícitamente con `createCollection()`. Esto es útil para configurar opciones avanzadas.

```javascript
db.createCollection("logs");
```

### Mostrar colecciones 📋

Para ver una lista de todas las colecciones en la base de datos actual:

```javascript
show collections;
```

### Eliminar una colección 🔥

Para eliminar una colección y **todos sus documentos e índices de forma permanente**:

```javascript
// Elimina la colección 'logs'
db.logs.drop();
```

# 📊 Guía de Importación y Consulta de Datos en MongoDB

Este documento es una guía práctica para instalar las herramientas de MongoDB, importar datos en formatos JSON y CSV, y realizar consultas avanzadas utilizando `mongosh`. Usaremos como ejemplo dos conjuntos de datos que simulan tweets sobre las finales de la Copa del Mundo de Rusia 2018 y Catar 2022.


## 1. Instalación de Herramientas (MongoDB CLI)

Para usar `mongoimport`, primero necesitamos instalar las herramientas de línea de comandos de MongoDB. Si usas macOS con Homebrew, el proceso es el siguiente.

```bash
# 1. Añadir el "tap" oficial de MongoDB a Homebrew
brew tap mongodb/brew

# 2. Instalar las herramientas de la base de datos
brew install mongodb-database-tools
```

> ℹ️ **¿Qué son las `mongodb-database-tools`?**
> Es un paquete que contiene utilidades de línea de comandos como `mongoimport`, `mongoexport`, `mongodump` y `mongorestore` para trabajar con tu base de datos desde la terminal.

## 2. Importación de Datos

Vamos a importar nuestros dos conjuntos de datos en la base de datos `worldcups` y en colecciones separadas.

### Importar JSON (Rusia 2018)

Este comando importa un archivo JSON que contiene un array de documentos.

```bash
mongoimport --uri "mongodb://admin:secret123@127.0.0.1:27017/worldcups?authSource=admin" --collection rus2018 --file data/chapter3/final.json --jsonArray
```

**Desglose del comando:**
*   `--uri "..."`: Especifica la cadena de conexión completa, incluyendo usuario, contraseña, host y la base de datos de autenticación.
*   `--collection rus2018`: Indica que los datos se insertarán en la colección `rus2018`.
*   `--file .../final.json`: La ruta al archivo de datos.
*   `--jsonArray`: **Crucial**. Le dice a `mongoimport` que el archivo es un único array `[...]` que contiene múltiples documentos JSON.

### Importar CSV (Catar 2022)

Este comando importa datos desde un archivo CSV.

```bash
mongoimport --uri "mongodb://admin:secret123@127.0.0.1:27017/worldcups?authSource=admin" -c catar2022 --type csv --headerline --file data/chapter3/final.csv
```

**Desglose del comando:**
*   `-c catar2022`: Forma corta de `--collection catar2022`.
*   `--type csv`: Especifica que el formato del archivo es CSV.
*   `--headerline`: Indica que la primera fila del CSV contiene los nombres de los campos, que se usarán como claves en los documentos de MongoDB.
*   `--file .../final.csv`: La ruta al archivo CSV.

## 3. Consultas Básicas y Modificadores

Una vez dentro de `mongosh`, podemos empezar a consultar los datos.

### Visualizar Documentos

Para ver los documentos de una colección de forma legible.

```javascript
// Ver documentos de la final de Rusia 2018
db.rus2018.find().pretty()

// Ver documentos de la final de Catar 2022
db.catar2022.find().pretty()
```

### Paginación y Ordenamiento (`sort`, `skip`, `limit`)

Estos modificadores nos permiten controlar qué documentos vemos y en qué orden.

*   `sort()`: Ordena los resultados. `1` para ascendente, `-1` para descendente.
*   `skip()`: Omite un número de documentos desde el inicio.
*   `limit()`: Restringe el número de documentos devueltos.

> ⚙️ **El orden importa:** MongoDB aplica los modificadores en este orden: **1º `sort()`**, **2º `skip()`**, **3º `limit()`**, sin importar en qué orden los escribas en la consulta.

```javascript
// Ejemplo 1: Ordena por _id descendente, salta los primeros 5 y muestra los siguientes 2.
db.rus2018.find().sort({_id:-1}).skip(5).limit(2).pretty()

// Ejemplo 2: Salta 5 y muestra 2. El orden no está garantizado sin un `sort()`.
db.rus2018.find().skip(5).limit(2).pretty()
```

## 4. Optimización con Índices

Los índices mejoran drásticamente la velocidad de las consultas, especialmente en colecciones grandes.

```javascript
// Crear un índice compuesto en la colección de Rusia 2018
// Ordena por seguidores (desc) y luego por _id (desc)
db.rus2018.createIndex({"usuario.seguidores":-1, _id:-1})

// Crear un índice similar para la colección de Catar 2022
// Nota: la estructura del usuario es plana en el CSV importado
db.catar2022.createIndex({"usuario_seguidores":-1, _id:-1})
```
Este índice acelerará consultas que ordenen o filtren por el número de seguidores de los usuarios.

## 5. Proyecciones (Selección de Campos)

La proyección nos permite devolver solo los campos que necesitamos, reduciendo la carga de red y haciendo las consultas más eficientes.

```javascript
// Devuelve solo los campos _id y texto.
db.rus2018.find({}, {_id:1, texto:1})

// Devuelve solo el campo texto. El _id se incluye por defecto,
// así que debemos excluirlo explícitamente con `_id:0`.
db.catar2022.find({}, {_id:0, texto:1})

// Combinando filtro y proyección: muestra solo el texto de los retweets (RT).
db.rus2018.find({RT:true}, {texto:1, _id:0})
```

## 6. Operadores de Consulta Avanzados

Los operadores nos permiten crear filtros complejos. Se usan dentro del objeto de consulta de `find()`.

### Operadores de Comparación

| Operador | Selecciona documentos donde el valor...                   |
| :------- | :-------------------------------------------------------- |
| `$gt`    | es **g**reater **t**han (mayor que) el valor indicado     |
| `$gte`   | es **g**reater **t**han or **e**qual (mayor o igual)      |
| `$lt`    | es **l**ess **t**han (menor que) el valor indicado        |
| `$lte`   | es **l**ess **t**han or **e**qual (menor o igual)         |
| `$eq`    | es **eq**ual (igual) al valor indicado (generalmente implícito) |
| `$ne`    | es **n**ot **e**qual (distinto) del valor indicado        |

**Ejemplos:**

```javascript
// 1. Encontrar usuarios con más de 100,000 seguidores en Catar 2022
db.catar2022.find({ "usuario_seguidores": { $gt: 100000 } })

// 2. Encontrar tweets en Rusia 2018 con 5000 o menos seguidores
db.rus2018.find({ "usuario.seguidores": { $lte: 5000 } })

// 3. Encontrar todos los tweets que NO sean de 'lesbleus_champ'
db.rus2018.find({ "usuario.nick": { $ne: "lesbleus_champ" } })
```

### Operadores Lógicos

| Operador | Selecciona documentos que...                             |
| :------- | :------------------------------------------------------- |
| `$and`   | cumplen **todas** las condiciones de un array.           |
| `$or`    | cumplen **alguna** de las condiciones de un array.       |
| `$not`   | **invierten** el efecto de una consulta.                 |
| `$nor`   | **no cumplen ninguna** de las condiciones de un array.   |

**Ejemplos:**

```javascript
// 1. ($and): Encontrar tweets de Rusia 2018 que SEAN un Retweet Y tengan más de 50,000 seguidores.
db.rus2018.find({
  $and: [
    { RT: true },
    { "usuario.seguidores": { $gt: 50000 } }
  ]
})

// 2. ($or): Encontrar tweets de Catar 2022 que mencionen a 'Messi' O a 'Mbappe' en el texto.
// Se usa una expresión regular para buscar dentro del texto (case-insensitive).
db.catar2022.find({
  $or: [
    { texto: /messi/i },
    { texto: /mbappe/i }
  ]
})

// 3. ($not): Encontrar tweets de Catar 2022 cuyo número de seguidores NO sea mayor que 200,000.
db.catar2022.find({ "usuario_seguidores": { $not: { $gt: 200000 } } }) // Equivalente a $lte: 200000

// 4. ($nor): Encontrar tweets de Rusia 2018 que NO sean un Retweet y que TAMPOCO mencionen a 'Griezmann'.
db.rus2018.find({
  $nor: [
    { RT: true },
    { texto: /griezmann/i }
  ]
})
```

## 7. Introducción a las Agregaciones

El **Aggregation Framework** es una herramienta muy potente para realizar procesamientos de datos complejos en varias etapas (pipeline). Es ideal para generar reportes, estadísticas y transformaciones de datos.

**Ejemplo: Contar cuántos tweets ha publicado cada usuario en la final de Catar 2022 y mostrar los 5 más activos.**

```javascript
db.catar2022.aggregate([
  // Etapa 1: Agrupar documentos por el nick del usuario y contar cuántos hay en cada grupo.
  {
    $group: {
      _id: "$usuario_nick",         // El campo por el que agrupamos
      totalTweets: { $sum: 1 }      // Por cada documento en el grupo, suma 1 al contador
    }
  },

  // Etapa 2: Ordenar los resultados para ver los más activos primero.
  {
    $sort: {
      totalTweets: -1             // Ordenar por el contador en orden descendente
    }
  },

  // Etapa 3: Limitar el resultado a los 5 primeros.
  {
    $limit: 5
  }
])
```

Este pipeline te devolverá un resultado similar a este, mostrándote los 5 usuarios con más tweets en el dataset:
```json
[
  { _id: 'random_fan_arg', totalTweets: 5 },
  { _id: 'user_12345', totalTweets: 4 },
  { _id: 'french_fan_sad', totalTweets: 3 },
  // ... y así sucesivamente.
]
```