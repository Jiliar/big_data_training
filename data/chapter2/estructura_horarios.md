# Estructura del archivo `horarios.txt`

Este archivo contiene mediciones horarias de calidad del aire con el siguiente formato delimitado por `;` (punto y coma):

## Columnas

- **Columnas 0, 1, 2**: Identifican la estación de medición.  
  Estas tres columnas se concatenan para formar el código de estación.  
  **Ejemplo:** `28;079;004` representa la estación ubicada en **Plaza de España**.

- **Columnas 3, 4, 5**: Representan el tipo de contaminante medido.  
  La columna 3 indica el **código del contaminante**.  
  **Ejemplo:** Si la columna 3 tiene el valor `12`, significa que se ha medido **óxido de nitrógeno**.  
  Las columnas 4 y 5 contienen metadatos que pueden ignorarse.

- **Columnas 6, 7, 8**: Fecha de la medición.  
  Representan respectivamente:
  - Año
  - Mes
  - Día  
  **Ejemplo:** `2024;05;15` representa el **15 de mayo de 2024**.

- **Columnas 9 – 56**: Mediciones horarias y su validez.  
  Estas columnas están organizadas en **pares consecutivos** para cada hora del día:
  - La primera columna del par contiene la **medición numérica**
  - La segunda columna indica su **validez**:
    - `"V"` si es válida
    - `"N"` si **no** debe considerarse

  **Ejemplo de columnas 9-12**:
  ```
  45;V;63;V
  ```
  - `45` es el valor a las 00:00 horas, válido (`V`)
  - `63` es el valor a la 01:00 horas, válido (`V`)

  En la práctica, el primer valor marcado como `"N"` corresponde a la **hora actual**, para la cual aún no hay medición registrada.

## Notas adicionales

- El archivo contiene **una línea por combinación** de estación, contaminante y fecha.
- El separador utilizado es el `;` (punto y coma).
