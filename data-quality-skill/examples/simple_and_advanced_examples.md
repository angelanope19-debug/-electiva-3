# Ejemplo Simple: Análisis Básico

## Solicitud al Agente

```
Necesito verificar rápidamente si el archivo de clientes está listo para usar.
Tengo estos datos:

customer_id,name,email,phone
1,John Doe,john@example.com,555-0101
2,Jane Smith,jane@example.com,
3,Bob Johnson,bob.johnson@example,555-0103
4,Alice Brown,alice@example.com,555-0104
5,John Doe,john@example.com,555-0101
```

Usa la skill Data Quality Analysis & Reporting para un análisis rápido.
```

## Respuesta Esperada

```
🔍 ANÁLISIS RÁPIDO DE CALIDAD
─────────────────────────────

Dataset: 5 clientes
Score Rápido: 68/100 ⚠️ PROBLEMAS DETECTADOS

ISSUES ENCONTRADOS:
─────────────────────
1. ❌ Duplicado: Row 1 y 5 (john@example.com) - CRÍTICO
2. ❌ Email inválido: Row 3 (bob.johnson@example) - ALTO
3. ❌ Phone nulo: Row 2 - MEDIO

RECOMENDACIÓN:
✅ NO LISTO para usar
⚠️ Necesita limpieza prioritaria (10 min max)

ACCIONES:
1. Remover row 5 (duplicado)
2. Validar email row 3
3. Llenar phone row 2 o marcar como opcional
```

## Pasos para el Usuario

1. Copiar dataset arriba
2. Pegar en Claude con la skill cargada
3. Esperar respuesta
4. Actuar según recomendaciones

**Tiempo total:** 90 segundos

---

# Ejemplo Avanzado: Análisis Completo

## Solicitud

```
Tengo un dataset de 1,000 transacciones que necesito validar antes 
de cargar a nuestro data warehouse. Necesito:

1. Análisis completo de integridad
2. Detectar TODAS las anomalías
3. Reporte detallado con prioridades
4. Código Python para limpiar

[Pega aquí el CSV de 1,000 registros...]
```

## Respuesta Esperada

```
📊 ANÁLISIS PROFUNDO - DATOS TRANSACCIONALES
═════════════════════════════════════════════

Dataset: transactions.csv (1,000 filas × 8 columnas)
Análisis Completo: 94 segundos

▸ PUNTUACIÓN GENERAL: 74/100 ⚠️ ACCIÓN REQUERIDA

ANÁLISIS DE ESTRUCTURA:
├─ 1,000 registros válidos (100%)
├─ 1 registro con estructura incorrecta (0.1%)
└─ 7 columnas de tipos mixtos

VALIDACIÓN DE INTEGRIDAD (FASE 1):
───────────────────────────────────

Valores Nulos Detectados:
├─ transaction_date: 3 nulos (0.3%)
├─ amount: 0 nulos (0%)
└─ customer_id: 12 nulos (1.2%)

Impacto: -1.5% completitud (Moderado)

DEDECTOS DE FORMATO (FASE 2):
─────────────────────────────

Email Validation:
├─ Válidos: 987 (98.7%) ✓
├─ Inválidos: 13 (1.3%) ⚠️
│  └─ Ejemplos: user@, @domain.com, .double@@
└─ Acción: Regex validation + corrección manual

Phone Numbers:
├─ Formato estándar: 945 (94.5%)
├─ Inconsistente: 55 (5.5%) ⚠️
└─ Acción: Normalizar a E.164

DETECCIÓN DE DUPLICADOS (FASE 3):
──────────────────────────────────

├─ Duplicados exactos: 8 registros (0.8%)
├─ Duplicados parciales: 23 registros (2.3%)
└─ Impacto: Reduce unicidad a 97%

Recomendó: Usar columna customer_id como PK

ANÁLISIS DE OUTLIERS (FASE 4):
──────────────────────────────

Amount (Float):
├─ Media: $1,250
├─ Mediana: $890
├─ Desviación típica: $523
├─ Outliers detectados: 12 (1.2%)
│  └─ Rango: $0.01 - $99,999
│  └─ Posible error: cliente con $99,999
└─ % Fuera de 3σ: 1.2%

Transaction Dates:
├─ Rango: 2024-01-01 a 2024-12-31 ✓
├─ Fechas en el futuro: 0 ✓
├─ Fechas imposibles: 0 ✓
└─ Gaps detectados: 3 (días sin datos)

VALIDACIÓN BUSINESSUA (FASE 5):
───────────────────────────────

├─ Enumeraciones válidas:
│  └─ status: ['completed', 'pending', 'failed', 'unknown'(2)]
├─ Reglas de negocio:
│  └─ amount > 0: 998/1000 (99.8%) ✓
│  └─ customer_id present: 988/1000 (98.8%) ⚠️
└─ Impacto: -1.2% validez

═════════════════════════════════════════════

📊 MÉTRICAS FINALES (DAMA-DMBOK):
─────────────────────────────────

Completitud:        98.5% ✓ (Excelente)
Validez:            98.8% ✓ (Excelente)
Unicidad:           97.0% ✓ (Buena)
Consistencia:       99.0% ✓ (Excelente)
Oportunidad:        100% ✓ (Datos actuales)

═════════════════════════════════════════════

🎯 HALLAZGOS PRIORIZADOS:
─────────────────────────

🔴 CRÍTICO (Bloquea ETL):
1. 12 valores nulos customer_id
   └─ Cannot load sin PK definida
   
2. 1 registro estructura incorrecta
   └─ Verificar formato fuente

🟠 ALTO (Requiere atención):
3. 13 emails inválidos (1.3%)
   └─ Revisar y corregir

4. 55 teléfonos mal formateados
   └─ Normalizar a E.164

🟡 MEDIO (Nice-to-have):
5. 8 duplicados exactos
   └─ Investigar origen

6. 12 outliers en amount (1.2%)
   └─ Revisar si es legítimo

═════════════════════════════════════════════

💻 CÓDIGO PYTHON PARA LIMPIAR:
──────────────────────────────

import pandas as pd
import re

# Cargar dataset
df = pd.read_csv('transactions.csv')

# 1. Remover nulos del PK
df = df.dropna(subset=['customer_id'])

# 2. Remover duplicados exactos
df = df.drop_duplicates()

# 3. Validar emails
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, str(email)) is not None

df = df[df['email'].apply(validate_email)]

# 4. Normalizar teléfonos
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)
df['phone'] = df.apply(
    lambda row: f"+1{row['phone']}" if len(row['phone'])==10 else row['phone'], 
    axis=1
)

# 5. Guardar limpio
df.to_csv('transactions_cleaned.csv', index=False)
print("✅ Limpieza completada!")
print(f"Registros: {len(df)} (antes: 1000)")

═══════════════════════════════════════════

✅ RECOMENDACIÓN FINAL:

Score después de limpieza estimado: 94/100
⚠️ CASI LISTO PARA ETL

Próximos pasos:
1. Ejecutar script Python arriba
2. Validar manualmente 12 outliers amount
3. Re-analizar dataset limpio
4. Cargar a DW

Tiempo estimado limpieza: 15-30 min
```

---

## Cómo Usar Este Ejemplo

1. Adaptar el solicitud a tu dataset
2. Incluir datos reales o muestra
3. Pedir análisis similar
4. Copiar el código Python generado
5. Ejecutar limpieza

**Documentar todo en tu entrega como evidencia de funcionamiento**
