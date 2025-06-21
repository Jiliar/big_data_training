# Apache Spark - Instalación en Windows, Linux y macOS

## ✨ Introducción a Apache Spark

Apache Spark es un motor de procesamiento de datos de código abierto, diseñado para ser rápido y general. Se utiliza ampliamente para tareas de Big Data como procesamiento por lotes, procesamiento en tiempo real (streaming), aprendizaje automático (MLlib) y análisis interactivo.

Permite trabajar con grandes volúmenes de datos distribuidos en un clúster, aprovechando la memoria RAM para acelerar el procesamiento frente a otros motores como Hadoop MapReduce.

---

## 💻 Instalación en Windows

### 1. Requisitos previos
- Java 8 o superior (JDK)
- Python (opcional, para usar PySpark)

### 2. Pasos
1. Descarga Apache Spark desde: https://spark.apache.org/downloads.html
2. Selecciona versión de Spark y Hadoop.
3. Extrae el `.tgz` en una carpeta.
4. Configura variables de entorno:
   - `SPARK_HOME`
   - Agrega `%SPARK_HOME%\bin` al `PATH`
5. Descarga `winutils.exe` compatible con tu versión de Hadoop y colócalo en `SPARK_HOME\bin`
6. Verifica con:

```sh
spark-shell
```

---

## 💪 Instalación en Linux

### 1. Requisitos previos

```bash
sudo apt update
sudo apt install openjdk-11-jdk python3-pip -y
```

### 2. Instalar Spark

```bash
wget https://downloads.apache.org/spark/spark-<versión>/spark-<versión>-bin-hadoop<versión>.tgz
sudo tar -xvzf spark-*.tgz -C /opt/
echo "export SPARK_HOME=/opt/spark-<versión>-bin-hadoop<versión>" >> ~/.bashrc
echo "export PATH=$SPARK_HOME/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
```

### 3. Verificar

```bash
spark-shell
```

---

## 🍏 Instalación en macOS

### 1. Requisitos

- Tener [Homebrew](https://brew.sh/) instalado

### 2. Instalar Java y Spark

```bash
brew install openjdk@17
brew install apache-spark
```

### 3. Configurar entorno

Agrega a tu `~/.zprofile` o `~/.zshrc`:

```bash
export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"
export JAVA_HOME=$(/opt/homebrew/opt/openjdk@17/bin/java -XshowSettings:properties -version 2>&1 | grep "java.home" | awk -F "= " '{print $2}')
export PATH="/opt/homebrew/opt/apache-spark/bin:$PATH"
```

### 4. Verificar

```bash
spark-submit --version
```

---

## 🔗 Recursos adicionales

- [Documentación oficial de Spark](https://spark.apache.org/docs/latest/)
- [API PySpark](https://spark.apache.org/docs/latest/api/python/)
