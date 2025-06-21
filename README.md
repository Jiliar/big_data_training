# 📊 big-data-training

Proyecto de entrenamiento en análisis de datos con herramientas de Big Data. Este repositorio contiene ejemplos prácticos usando `pandas`, `NumPy`, `Spark`, `MongoDB`, `Selenium`, `Tweepy`, entre otros.

## 📁 Estructura del Proyecto

```
big-data-training/
├── code/                  # Scripts y notebooks organizados por capítulos
│   ├── chapter1/          # Manejo de archivos: CSV, JSON, Excel, ODS, XML
│   ├── chapter2/          # Web scraping (HTML, requests, Selenium)
│   ├── chapter3/          # Consumo de APIs (Twitter, Google Maps, OMDb)
│   ├── chapter4/          # Integración con MongoDB
│   ├── chapter5/          # Fundamentos de NumPy y pandas
│   ├── chapter6/          # Instalación y uso básico de Apache Spark
│   └── chapter7/          # Spark con MongoDB y SQL
├── data/                  # Datos fuente por capítulo
├── artifacts/             # Salidas y modelos entrenados
└── pyproject.toml         # Definición del entorno con Poetry
```

## ⚙️ Dependencias

Instaladas mediante [Poetry](https://python-poetry.org/):

```toml
[tool.poetry.dependencies]
python = "^3.12"
xlrd = "^2.0.1"
xlwt = "^1.3.0"
openpyxl = "^3.1.5"
pandas = "^2.2.3"
ezodf = "^0.3.2"
matplotlib = "^3.10.3"
html5lib = "^1.1"
selenium = "^4.33.0"
tweepy = "^4.15.0"
pymongo = "^4.13.0"
numpy = "^2.3.0"
xlsxwriter = "^3.2.3"
pyspark = "^4.0.0"
```

## 🚀 Uso rápido

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/big-data-training.git
   cd big-data-training
   ```

2. **Instala Poetry y las dependencias**:

   ```bash
   poetry install
   ```

3. **Activa el entorno**:

   ```bash
   poetry shell
   ```

4. **Ejecuta un script**:

   ```bash
   python code/chapter1/data_handling/csv.py
   ```

## 🚰 Requisitos adicionales

* **Java JDK 8+**: para Apache Spark.
* **Docker**: para usar MongoDB o Spark en contenedores.
* **Navegador + WebDriver (e.g., Chrome + chromedriver)**: para `selenium`.

## 📚 Capítulos destacados

* **Capítulo 1**: lectura y escritura de archivos (CSV, JSON, Excel, XML, ODS)
* **Capítulo 2**: scraping desde HTML o sitios en vivo
* **Capítulo 3**: conexión a APIs reales
* **Capítulo 4**: interacción con bases de datos NoSQL (MongoDB)
* **Capítulo 6–7**: procesamiento distribuido con Apache Spark

## ✍️ Autor

**Jiliar Silgado**
[jiliar.silgado@gmail.com](mailto:jiliar.silgado@gmail.com)
