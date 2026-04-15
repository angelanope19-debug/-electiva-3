# Guía de Prueba: Data Quality Analysis & Reporting Skill

**Objetivo:** Demostrar funcionamiento de la skill en Claude con evidencia práctica.

---

## Parte 1: Preparación del Entorno

### Paso 1A: Crear Dataset de Prueba

Crea un archivo `customers_test.csv` con datos propósito para demostrar la skill:

```csv
customer_id,name,email,phone,registration_date,total_spent,status
1,John Doe,john@example.com,555-0101,2023-01-15,1500.00,active
2,Jane Smith,jane@example.com,,2023-02-20,2300.50,active
3,Bob Johnson,bob.johnson@example,555-0103,2023-03-10,450.00,inactive
4,Alice Brown,alice@example.com,555-0104,2023-04-05,5000.00,active
5,John Doe,john@example.com,555-0101,2023-01-15,1500.00,active
6,Charlie Wilson,,555-0106,2025-13-45,750.00,pending
7,Diana Lee,diana@example.com,555-0107,2023-06-12,3200.00,active
8,Eva Martinez,eva@example.com,invalid-phone,2023-07-22,,active
9,Frank Davis,frank@@example.com,555-0109,2023-08-30,999999.00,active
10,Grace Taylor,grace@example.com,555-0110,2023-09-14,1200.00,unknown
```

**Por qué este dataset es útil para demostración:**
- ✅ Row 2: Email vacío (null value)
- ✅ Row 3: Email malformado (falta @)
- ✅ Rows 1 & 5: Duplicados exactos
- ✅ Row 6: Fecha imposible (2025-13-45)
- ✅ Row 8: Total spent vacío
- ✅ Row 9: Email doble @@ y TotalSpent outlier (999999)
- ✅ Row 10: Status value inválido ("unknown")

### Paso 1B: Acceder a Claude

1. Ir a [claude.ai](https://claude.ai)
2. Inicia sesión (o crea cuenta si es necesario)
3. Crea nuevo Chat

---

## Parte 2: Cargar la Skill en Claude

### Paso 2A: Opción A - Copiar la Skill Directamente

1. Abre el archivo [DATA_QUALITY_ANALYSIS.md](./DATA_QUALITY_ANALYSIS.md)
2. Copia TODO el contenido (Ctrl+A > Ctrl+C)
3. En Claude, en el nuevo chat, pega el contenido:

```
[Pega aquí el contenido completo de DATA_QUALITY_ANALYSIS.md]
```

4. Envía el mensaje. Claude debería responder reconociendo la skill:

> "He recibido la skill 'Data Quality Analysis & Reporting'. He identificado:
> - Nombre: Data Quality Analysis & Reporting
> - Categoría: data-analysis
> - Complejidad: intermedia
> - Capacidades principales: análisis de integridad, detección de anomalías, generación de reportes
>
> Estoy listo para ejecutar análisis de calidad de datos. ¿Qué dataset deseas que analice?"

### Paso 2B: Opción B - Cargar Vía URL

Si tenés el archivo en GitHub o URL pública:

```
Carga la skill desde esta URL: [URL del archivo]

He descargado y proceado la skill...
```

---

## Parte 3: Ejecutar el Análisis (Evidencia de Funcionamiento)

### Paso 3A: Primera Solicitud

**Envía a Claude:**

```
Tengo un archivo CSV con datos de clientes (customers_test.csv). 
Usando la skill "Data Quality Analysis & Reporting", 
necesito un análisis completo de calidad de datos.

Aquí están los datos:

[Pega el contenido del CSV]

Por favor ejecuta:
1. Análisis de estructura
2. Validación de integridad
3. Detección de anomalías
4. Generación de reporte con hallazgos
```

### Paso 3B: Respuesta Esperada de Claude

Claude debería responder algo similar a:

```
📊 REPORTE DE CALIDAD DE DATOS
═════════════════════════════════

Dataset: customers_test
Análisis Ejecutado: [timestamp]
Total Registros: 10 filas
Columnas: 7

▸ PUNTUACIÓN GENERAL: 62/100 ⚠️ REQUIERE ATENCIÓN

╔════════════════════════════════════════╗
║        HALLAZGOS IDENTIFICADOS         ║
╚════════════════════════════════════════╝

🔴 CRÍFICO (1):
─────────────────
1. Duplicados Exactos: 2 registros
   → Filas 1 y 5 (john@example.com) son idénticas
   → Acción: Eliminar fila 5 o investigar origen

🟠 ALTO (3):
─────────────
2. Formato Email Inválido: 2 registros (20%)
   └─ Row 3: "bob.johnson@example" (falta TLD)
   └─ Row 9: "frank@@example.com" (doble @)
   → Acción: Validar contra RFC 5322

3. Fecha Inválida: 1 registro
   └─ Row 6: "2025-13-45" (mes 13 no existe, día 45)
   → Acción: Retornar a origen, verificar ingesta

4. Valores Outlier: 1 registro (3%)
   └─ Row 9: TotalSpent = 999999.00
   → Media = 2238.95, este es 446x el promedio
   → Acción: Revisar si es ingreso legítimo

🟡 MEDIO (2):
──────────────
5. Valores Nulos: 2 registros
   └─ Row 2: email = NULL (10%)
   └─ Row 8: total_spent = NULL (10%)
   → Acción: Implementar validación requerida en ingesta

6. Valores Status Inválidos: 1 registro (10%)
   └─ Row 10: status = "unknown" (valores válidos: active, inactive, pending)
   → Acción: Documentar enum de valores permitidos

╔════════════════════════════════════════╗
║            MÉTRICAS DAMA-DMBOK        ║
╚════════════════════════════════════════╝

Completitud (% registros sin nulls):
├─ email: 90% ✓
├─ phone: 90% ✓
├─ total_spent: 90% ✓
└─ Promedio: 85% ⚠️ Por debajo del 95% recomendado

Validez (% valores que cumplen reglas):
├─ email format: 80%
├─ date format: 90%
├─ status enum: 90%
└─ Promedio: 87% ⚠️

Unicidad (% registros únicos):
└─ 80% (2 duplicados exactos)

Consistencia (tipos de datos):
└─ 100% ✓ Todos los tipos coinciden

═════════════════════════════════════════

📋 ACCIONES PRIORITARIAS RECOMENDADAS:

1️⃣ CRÍTICO (Esta semana):
   a) Remover/investigar row 5 (duplicado)
   b) Validar fecha en Row 6 contra sistema fuente
   c) Revisar TotalSpent row 9 (¿es cliente VIP?)

2️⃣ ALTO (Próximas 2 semanas):
   a) Agregar validación de formato email en ingesta
   b) Documentar enum de valores "status" 
   c) Hacer campos requeridos: email, total_spent

3️⃣ PREVENTIVO (Mejora continua):
   a) Implementar validaciones en tiempo real
   b) Crear pipeline de MonitorQ para nuevos inserts
   c) Configurar alertas para anomalías diarias

📈 RECOMENDACIÓN FINAL:
⚠️ NO LISTO para ETL en su estado actual
✅ Tomar acciones críticas → Relanzar análisis → Entonces LISTO
```

---

## Parte 4: Demostración de Iteración (Bonificación)

### Paso 4A: Segunda Solicitud (Follow-up)

Después de que Claude genere el reporte, solicita:

```
Basándote en el análisis anterior:

1. Sugiere un script Python que limpie estos datos
2. Muestra el CSV resultante después de limpiar
3. Re-analiza la calidad del dataset limpio
4. ¿Ahora está listo para ETL?
```

### Paso 4B: Respuesta Esperada

Claude debería:
1. Generar código Python con pandas para limpiar
2. Mostrar nuevo CSV
3. Correr análisis nuevamente
4. Mostrar nuevo score (ej: 95/100 ✅ LISTO)

---

## Parte 5: Evidencia para Evidencia de Prueba

Para tu documento final, **captura de pantalla o video:**

### Screenshots Recomendadas:

1. **Pantalla 1:** Chat de Claude mostrando la skill cargada

   ```
   [Screenshot de Claude reconociendo la skill]
   "He recibido la skill Data Quality Analysis & Reporting..."
   ```

2. **Pantalla 2:** Dataset CSV ingresado

   ```
   [Screenshot del CSV de 10 filas]
   Mostrar claramente las anomalías
   ```

3. **Pantalla 3:** Reporte completo generado

   ```
   [Screenshot largo del reporte]
   - Puntuación: 62/100
   - Hallazgos: 6 issues
   - Métricas DAMA-DMBOK
   ```

4. **Pantalla 4:** Recomendaciones de Claude

   ```
   [Screenshot de recomendaciones accionables]
   Con código Python de limpieza
   ```

5. **Pantalla 5:** Dataset limpio y re-análisis

   ```
   [Screenshot del dataset limpio]
   + Nuevo reporte con score mejorado (95/100+)
   ```

### Video Alternativa (Recomendado):

- Duración: 3-5 minutos
- Captura de pantalla de desktop
- Voz en off explicando cada paso
- Mostrar: Skill cargada → Análisis ejecutado → Reporte → Iteración de limpieza

**Contenido del video:**
```
00:00 - Intro: "Voy a demostrar la skill de análisis de calidad"
00:20 - Cargar skill en Claude
00:45 - Mostrar dataset con problemas
01:15 - Claude ejecuta análisis
02:30 - Reporte completo con hallazgos
03:45 - Solicitar limpieza + re-análisis
04:30 - Resultado final + conclusión
```

---

## Parte 6: Interpretación de Resultados

### ¿Qué hace la skill?

| Paso | Lo que hace | Resultado |
|------|-----------|----------|
| 1 | Lee estructura | Identifica 7 columnas, 10 filas |
| 2 | Explora tipos | String, Int, Float, DateTime |
| 3 | Valida nulls | Detecta 2 nulls (20%) |
| 4 | Busca duplicados | Encuentra exactos (rows 1-5) |
| 5 | Valida formatos | 2 emails malformados |
| 6 | Detecta outliers | 1 valor extremo identificado |
| 7 | Calcula métricas | Completitud 85%, Validez 87% |
| 8 | Genera reporte | Score 62/100 con acciones |

### ¿Cómo explicas los resultados?

**Para tu documento:**

> "La skill identificó 6 categorías de problemas en el dataset de prueba:
> 
> 1. **Duplicados (Crítica):** 2 registros idénticos reducen unicidad a 80%
> 2. **Formato emails (Alta):** 2 emails malformados rompen validez
> 3. **Fecha imposible (Alta):** 1 fecha futura e inválida indica error de ingesta
> 4. **Outliers (Alta):** 1 TotalSpent 446x el promedio = anomalía
> 5. **Nulls (Media):** 2 valores faltantes bajan completitud a 85%
> 6. **Enum inválido (Media):** 1 status no documentado
>
> El reporte, basado en estándares DAMA-DMBOK, proporciona:
> - Puntuación agregada: 62/100
> - Clasificación por severidad
> - Recomendaciones accionables
> - Plan de remediación por prioritario
>
> Esto demuestra la capacidad de la skill de **automat

izar auditorías que normalmente tomarían 4 horas a un analista.**"

---

## Parte 7: Checklist para Entrega

Antes de entregar, verifica:

- [ ] Archivo DATA_QUALITY_ANALYSIS.md creado y completo
- [ ] Archivo SUSTENTACION_SKILL.md con explicación detallada
- [ ] Skill cargada en Claude y funcionando
- [ ] Dataset de prueba analizado (CSV con anomalías propósito)
- [ ] 5+ screenshots del análisis (o video 3-5 min)
- [ ] Reporte con score antes/después de limpieza
- [ ] Documento PDF/Word con la sustentación
- [ ] Ev evidencia mostrando iteración (análisis → limpieza → re-análisis)

---

## Preguntas Frecuentes (FAQ)

### P: ¿Qué pasa si Claude no reconoce la skill?
**R:** Intenta:
1. Cargar el archivo de nuevo más claramente
2. Aclarar: "Eres ahora especialista en Data Quality Analysis"
3. Pedir nueva acción: "Analiza este CSV"

### P: ¿Puede ejecutarla fuera de Claude.ai?
**R:** Sí, la skill funciona en:
- Claude.ai (navegador)
- Cursor (IDE)
- API de Claude (con integración)
- Otros agentes vía MCP

### P: ¿Qué tan larga debe ser la sustentación?
**R:** 5-8 páginas es standard akademico. Incluye:
- Problema (1-2 pág)
- Solución (1 pág)
- Conexión con Claude (1-2 pág)
- Relación con conceptos del curso (2-3 pág)
- Impacto/conclusión (1 pág)

### P: ¿Puedo mejorar la skill?
**R:** Claro, ideas:
- Agregar más tipos de validación
- Soportar múltiples formatos (JSON, Parquet, SQL)
- Generar reportes en Excel/PDF
- Integrar visualizaciones
- Incluir machine learning para anomalías avanzadas

---

## Conclusión

Esta guía te proporciona todo lo necesario para:

1. ✅ **Crear** una skill funcional
2. ✅ **Probarla** en Claude con datos reales
3. ✅ **Documentar** el proceso
4. ✅ **Demostrar** competencia en:
   - Agent Skills (SKILL.md)
   - Orquestación multi-agente
   - MCP & integración
   - Automatización

**¡Ahora procede a ejecutar los pasos y captura la evidencia!**

---

**Versión:** 1.0 | **Última actualización:** 31/03/2024
