# 📊 REPORTE DE ANÁLISIS DE CALIDAD DE DATOS
## Data Quality Analysis & Reporting Skill

**Fecha de Análisis:** 31 de Marzo de 2026  
**Versión del Skill:** 1.0  
**Estado:** Análisis Completado ✅

---

## 📋 RESUMEN EJECUTIVO

| Métrica | Valor | Estado |
|---------|-------|--------|
| **Datasets Analizados** | 2 | ✅ |
| **Total Registros** | 20 | ✅ |
| **Problemas Detectados** | 14 | ⚠️ REQUIERE ATENCIÓN |
| **Completitud Promedio** | 96.2% | ⚠️ |
| **Puntuación General** | 78/100 | 🟡 ACEPTABLE |

---

## 🔍 HALLAZGOS CRÍTICOS

### Dataset 1: CUSTOMERS.CSV

**Dimensiones:** 10 filas × 7 columnas  
**Completitud:** 95.7%

#### ❌ PROBLEMAS IDENTIFICADOS

##### 1. **[ALTO]** Valores Nulos/Missing (3 campos)
- **email:** 1 registro (10.0%) → Fila 6
- **phone:** 1 registro (10.0%) → Fila 8  
- **total_spent:** 1 registro (10.0%) → Fila 8

**Impacto:** Datos incompletos que afectarán análisis financieros y comunicaciones

---

##### 2. **[ALTO]** Emails con Formato Inválido
- **Cantidad:** 2 registros (20%)
  - Fila 3: `bob.johnson@example` → Falta extensión de dominio (.com)
  - Fila 9: `frank@@example.com` → Doble arroba (@@)

**Validación esperada:** `[usuario]@[dominio].[ext]`  
**Impacto:** Imposibilidad de enviar comunicaciones

---

##### 3. **[MEDIO]** Teléfono con Formato Inválido
- **Cantidad:** 1 registro (10%)
  - Fila 8: `invalid-phone` → No cumple patrón esperado

**Validación esperada:** `XXX-XXXX`  
**Impacto:** Contacto imposible

---

##### 4. **[CRÍTICO]** Fecha Inválida
- **Cantidad:** 1 registro (10%)
  - Fila 6: `2025-13-45` → Mes 13, Día 45 (imposible)

**Impacto:** Error de ingesta de datos, falsa información temporal

---

##### 5. **[CRÍTICO]** Outlier Extremo
- **Cantidad:** 1 registro (10%)
  - Fila 9: `$999,999.00` → Extremadamente alto

**Rango usual:** $450 - $5,000  
**Recomendación:** Validar si es dato erróneo o legítimo

---

##### 6. **[ALTO]** Status Inesperado
- **Cantidad:** 1 registro (10%)
  - Fila 10: `unknown` → Valor no permitido

**Valores esperados:** `active`, `inactive`, `pending`  
**Impacto:** Segmentación y reporte incompleto

---

### Dataset 2: SALES.CSV

**Dimensiones:** 10 filas × 6 columnas  
**Completitud:** 96.7%

#### ❌ PROBLEMAS IDENTIFICADOS

##### 1. **[ALTO]** Valores Nulos/Missing
- **amount:** 1 registro (10.0%) → Fila 6  
- **customer_id:** 1 registro (10.0%) → Fila 8

**Impacto:** Imposibilidad de conciliar transacciones

---

##### 2. **[ALTO]** Email con Formato Inválido
- **Cantidad:** 1 registro (10%)
  - Fila 9: `frank@@example.com` → Doble arroba

**Impacto:** Datos inconsistentes con tabla CUSTOMERS

---

##### 3. **[CRÍTICO]** Fecha Inválida
- **Cantidad:** 1 registro (10%)
  - Fila 8: `2025-13-45` → Mes/Día inválidos

**Impacto:** Inconsistencia con dataset de clientes

---

##### 4. **[ALTO]** Status Inesperado
- **Cantidad:** 1 registro (10%)
  - Fila 10: `unknown` → Valor no permitido

**Valores esperados:** `completed`, `pending`, `failed`

---

## 📈 MÉTRICAS DE CALIDAD

### CUSTOMERS.CSV
```
Completitud:     95.7% ✅
Validez:         80.0% ⚠️
Consistencia:    90.0% ⚠️
Unicidad:        90.0% ✅
SCORE FINAL:     78/100 🟡
```

### SALES.CSV
```
Completitud:     96.7% ✅
Validez:         85.0% ⚠️
Consistencia:    85.0% ⚠️
Unicidad:        100.0% ✅
SCORE FINAL:     78/100 🟡
```

---

## 🔗 PROBLEMAS CORRELACIONADOS

Se detectó **1 problema común** entre datasets:

| Problema | Customers | Sales | Tipo |
|----------|-----------|-------|------|
| Email: `frank@@example.com` | Fila 9 | Fila 9 | INCONSISTENCIA |
| Fecha: `2025-13-45` | Fila 6 | Fila 8 | ERROR INGESTA |

**Recomendación:** Revisar fuente de origen/ETL

---

## 💡 RECOMENDACIONES ACCIONABLES

### Priority 1: CRÍTICO (Actuar Inmediatamente)

1. **Fecha inválida `2025-13-45`**
   ```sql
   -- Identifica registros afectados
   SELECT * FROM customers WHERE registration_date = '2025-13-45'
   SELECT * FROM sales WHERE date = '2025-13-45'
   
   -- Opción A: Usar fecha por defecto
   UPDATE customers SET registration_date = '2024-01-01' WHERE registration_date = '2025-13-45'
   
   -- Opción B: Validar fuente original
   ```

2. **Outlier extremo: $999,999**
   ```python
   # Validar o corregir
   import pandas as pd
   df = pd.read_csv('customers.csv')
   df.loc[df['total_spent'] > 100000, 'total_spent'] = None  # Marcar para revisión
   ```

### Priority 2: ALTO (Resolver en Ciclo Actual)

3. **Emails inválidos**
   ```python
   import re
   
   # Función de validación
   def validate_email(email):
       pattern = r'^[^@]+@[^@]+\.[a-z]{2,}$'
       return bool(re.match(pattern, email))
   
   # Fila 3: bob.johnson@example → bob.johnson@example.com
   # Fila 9: frank@@example.com → frank@example.com
   ```

4. **Status desconocido**
   ```sql
   -- Mapear 'unknown' al valor más frecuente
   UPDATE customers SET status = 'pending' WHERE status = 'unknown'
   UPDATE sales SET status = 'pending' WHERE status = 'unknown'
   ```

5. **Datos nulos**
   ```python
   # Estrategia según contexto
   df['phone'].fillna('Not provided', inplace=True)
   df['total_spent'].fillna(df['total_spent'].median(), inplace=True)
   df['amount'].fillna(0, inplace=True)
   df['customer_id'].fillna('UNKNOWN', inplace=True)
   ```

### Priority 3: MEDIO (Próximas Mejoras)

6. **Validación de teléfono**
   - Normalizar formato: `555-0101` ← estándar
   - Aceptar alternativas: `(555) 0101`, `+1-555-0101`

---

## ✅ PLAN DE ACCIÓN

| # | Tarea | Responsable | Plazo | Estado |
|---|-------|-------------|-------|--------|
| 1 | Corregir fechas inválidas | Data Engineer | Hoy | ⏳ |
| 2 | Revisar outlier $999,999 | Validación Manual | Hoy | ⏳ |
| 3 | Normalizar emails | ETL Script | Mañana | ⏳ |
| 4 | Llenar valores nulos | Data Analyst | 2 días | ⏳ |
| 5 | Implementar validaciones en ingesta | DevOps | Esta semana | ⏳ |

---

## 📊 VISUALIZACIÓN DE PROBLEMAS POR CATEGORÍA

```
TIPO DE PROBLEMA        CANTIDAD    % DEL TOTAL
─────────────────────────────────────────────
Valores Nulos              5          35.7%  ████████
Formato Inválido           4          28.6%  ██████
Fecha Inválida             2          14.3%  ███
Status Inesperado          2          14.3%  ███
Outlier Extremo            1           7.1%  █
─────────────────────────────────────────────
TOTAL                     14         100.0%  ████████████████████
```

---

## 🎯 PRÓXIMOS PASOS

### Inmediato (Hoy)
- [ ] Corregir 2 fechas inválidas (`2025-13-45`)
- [ ] Validar outlier de $999,999
- [ ] Normalizar 3 emails inválidos

### Corto Plazo (Esta Semana)
- [ ] Completar datos nulos (4 campos)
- [ ] Mapear status desconocidos
- [ ] Validar datos fuente en origen

### Mediano Plazo (Este Mes)
- [ ] Implementar validaciones en tiempo de ingesta
- [ ] Crear dashboard de monitoreo de calidad
- [ ] Documentar reglas de negocio

### Largo Plazo (Próximos Meses)
- [ ] Implementar observabilidad de datos (DataObs)
- [ ] Establecer SLA de calidad
- [ ] Automatizar correcciones

---

## 📝 CONCLUSIONES

✅ **Datasets FUNCIONALES pero CON REQUIEREN ATENCIÓN**

- La completitud es ACEPTABLE (96.2% en promedio)
- Los problemas identificados son **SOLUCIONABLES** y de **BAJO VOLUMEN** (14 de 120 campos = 11.7% afectados)
- La mayoría de los problemas son errores de **INGESTA/FORMATO**, no problemas estructurales

### Recomendación Final
**APTO PARA PROCESAMIENTO CON CORRECCIONES** ✅

Los datos pueden ser procesados **DESPUÉS** de aplicar las correcciones de Priority 1 y Priority 2.

---

**Reporte Generado por:** Data Quality Analysis & Reporting Skill v1.0  
**Formato:** Markdown + Ejecutivo  
**Próxima Revisión:** 07 de Abril de 2026

