# Guía de Prueba: Data Quality Analysis & Reporting Skill

**Objetivo:** Demostrar funcionamiento de la skill en Claude con evidencia práctica.

---

## Parte 1: Preparación del Entorno

### Paso 1A: Dataset de Prueba

El archivo `test-data/customers.csv` contiene datos propósito con anomalías para demostrar la skill:

**Problemas incluidos:**
- ✅ Row 2: Email vacío (null value)
- ✅ Row 3: Email malformado (falta @)
- ✅ Rows 1 & 5: Duplicados exactos
- ✅ Row 6: Fecha imposible (2025-13-45)
- ✅ Row 8: Total spent vacío
- ✅ Row 9: Email doble @@ y TotalSpent outlier
- ✅ Row 10: Status value inválido

### Paso 1B: Acceso a Claude

1. Ir a [claude.ai](https://claude.ai)
2. Crear nuevo Chat
3. Puntero: "Nuevo Chat" → Crear

---

## Parte 2: Cargar la Skill en Claude

### Opción A: Copiar-Pegar Directamente (Recomendado)

1. Abre `SKILL.md` en tu editor
2. Selecciona TODO (Ctrl+A)
3. Copia (Ctrl+C)
4. En Claude, pega el contenido:

```
[Contenido completo de SKILL.md]
```

5. Envía el mensaje

**Respuesta esperada:**

> "He recibido la skill 'Data Quality Analysis & Reporting'. 
> Identifico:
> - Nombre: Data Quality Analysis & Reporting
> - Categoría: data-analysis
> - Complejidad: intermedia
> 
> Estoy listo para ejecutar análisis de calidad de datos."

---

## Parte 3: Ejecutar el Análisis

### Paso 3A: Primera Solicitud

Copia el contenido de `customers.csv`:

```csv
customer_id,name,email,phone,registration_date,total_spent,status
1,John Doe,john@example.com,555-0101,2023-01-15,1500.00,active
[... resto de registros ...]
```

**Envía a Claude:**

```
He cargado la skill Data Quality Analysis & Reporting.

Ahora, analiza este dataset de clientes usando la skill:

[Pega aquí el contenido del CSV]

Por favor ejecuta:
1. Análisis de estructura
2. Validación de integridad
3. Detección de anomalías
4. Generación de reporte con hallazgos
5. Recomendaciones prioritarias
```

### Paso 3B: Respuesta Esperada

Claude debe responder:

```
📊 REPORTE DE CALIDAD DE DATOS
═════════════════════════════════

Dataset: customers.csv
Análisis: [timestamp]
Total Registros: 10 filas
Columnas: 7

▸ PUNTUACIÓN GENERAL: 62/100 ⚠️

╔════════════════════════════════════╗
║   HALLAZGOS IDENTIFICADOS          ║
╚════════════════════════════════════╝

🔴 CRÍTICO (1):
1. Duplicados Exactos: 2 registros
   → Filas 1 y 5 (john@example.com)

🟠 ALTO (3):
2. Email Inválido: 2 registros (20%)
3. Fecha Inválida: 1 registro
4. Outlier TotalSpent: 446x promedio

🟡 MEDIO (2):
5. Valores Nulos: 2 registros
6. Status Inválido: 1 registro

╔════════════════════════════════════╗
║     MÉTRICAS DAMA-DMBOK           ║
╚════════════════════════════════════╝

Completitud: 85%
Validez: 87%
Unicidad: 80%

═══════════════════════════════════════

📋 ACCIONES PRIORITARIAS:

1️⃣ CRÍTICO (Esta semana):
   a) Remover/investigar row 5
   b) Validar fecha en Row 6
   c) Revisar TotalSpent row 9

2️⃣ ALTO (2 semanas):
   a) Agregar validación email
   b) Documentar enum status

3️⃣ PREVENTIVO:
   a) Implementar validaciones en tiempo real
```

---

## Parte 4: Demostración de Iteración (Recomendado)

### Paso 4A: Segunda Solicitud

Después del reporte, pide:

```
Basándote en el análisis anterior:

1. Sugiere un script Python que limpie estos datos
2. Muestra el CSV resultante después de limpiar
3. Re-analiza la calidad del dataset limpio
4. ¿Ahora está listo para ETL?
```

### Paso 4B: Resultado Esperado

Claude generará:
1. ✅ Código Python con pandas
2. ✅ CSV limpio
3. ✅ Nuevo análisis
4. ✅ Score mejorado (95/100+)

---

## Parte 5: Captura de Evidencia

**Para tu entrega, captura:**

### Screenshots Recomendadas

1. **Screenshot 1:** Skill cargada en Claude
   - Mostrar mensaje de reconocimiento

2. **Screenshot 2:** Dataset ingresado
   - Ver claramente las anomalías

3. **Screenshot 3:** Reporte generado
   - Mostrar puntuación y hallazgos

4. **Screenshot 4:** Recomendaciones
   - Ver código de limpieza

5. **Screenshot 5:** Dataset limpio + re-análisis
   - Score mejorado

### Video Alternativa (3-5 minutos)

```
00:00 - Intro a la skill
00:20 - Cargar skill en Claude
00:45 - Mostrar dataset problemático
01:15 - Claude ejecuta análisis
02:30 - Reporte completo
03:45 - Limpieza + re-análisis
04:30 - Conclusión
```

---

## Parte 6: Interpretación de Resultados

| Hallazgo | Significado |
|----------|------------|
| Score 62/100 | 38% de problemas detectados |
| Duplicados | Reducen unicidad a 80% |
| Emails malformados | Rompen validez |
| Valores nulos | Lfuerte impacto en completitud |
| Outliers | Posibles errores de ingesta |

---

## Parte 7: Checklist Final

Antes de entregar:

- [ ] SKILL.md creado y funcional
- [ ] Dataset de prueba incluido
- [ ] 5+ screenshots del análisis
- [ ] Reporte antes/después
- [ ] Documentación completa
- [ ] Evidencia de iteración

---

## FAQ

**P: ¿Qué pasa si Claude no reconoce la skill?**
R: Intenta cargar de nuevo o aclarar: "Eres especialista en Data Quality Analysis"

**P: ¿Puedo usar otro dataset?**
R: Sí, funciona con cualquier CSV/JSON

**P: ¿Cuán larga debe ser la sustentación?**
R: 7-8 páginas estándar

---

**Versión:** 1.0 | **Actualización:** 31/03/2024
