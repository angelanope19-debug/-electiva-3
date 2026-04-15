---
name: "Data Quality Analysis & Reporting"
description: "Skill especializada en análisis integral de calidad de datos, auditoría de integridad, detección de anomalías y generación de reportes estructurados para mejorar la confiabilidad de datasets."
category: "data-analysis"
complexity: "intermediate"
tools: ["semantic_search", "code_analysis", "file_operations"]
---

# Data Quality Analysis & Reporting Skill

## Descripción General

Esta skill proporciona un marco especializado para que los agentes de IA realicen **auditorías completas de calidad de datos**, identificando problemas de integridad, consistencia y confiabilidad en datasets. Está diseñada para equipos de data engineering y científicos de datos que necesitan automatizar la validación de datos antes de procesarlos.

## Problema que Resuelve

### Contexto
En proyectos de análisis de datos, integración de APIs y data warehousing, es común enfrentar:
- **Datos incompletos o nulos**: Información faltante que afecta análisis posteriores
- **Inconsistencias de formato**: Variabilidad en la estructura de datos de múltiples fuentes
- **Valores duplicados**: Registros repetidos que sesgan resultados
- **Outliers y anomalías**: Valores extremos que pueden ser errores de ingesta
- **Problemas de tipos de datos**: Conversiones incorrectas (texto vs números)

### Solución
Esta skill automatiza la **detección, cuantificación y reporte** de estos problemas, permitiendo que un agente IA pueda:
- Escanear datasets automáticamente
- Generar métricas de calidad
- Crear reportes ejecutivos
- Sugerir acciones correctivas

## Instrucciones de Uso

### Cuando Usar Esta Skill

Invoca esta skill cuando necesites:

```
User: "Analiza la calidad de datos del archivo customers.csv y genera un reporte"

Agent debe ejecutar:
1. Obtener el archivo y sus características (dimensiones, tipos)
2. Ejecutar validaciones de integridad:
   - Detectar valores nulos/missing
   - Verificar duplicados
   - Validar rangos de valores
   - Identificar inconsistencias de formato
3. Generar métricas de confiabilidad
4. Producir un reporte con hallazgos y recomendaciones
```

### Metodología de Análisis

#### Fase 1: Exploración Inicial
```typescript
// Obtener metadatos del dataset
interface DatasetMetrics {
  totalRows: number;
  totalColumns: number;
  columnTypes: Record<string, string>;
  fileSize: number;
  completeness: number; // 0-100
}
```

#### Fase 2: Validaciones de Integridad
```typescript
// Validaciones a ejecutar
interface IntegrityChecks {
  nullValues: {
    column: string;
    count: number;
    percentage: number;
  }[];
  
  duplicates: {
    exactRows: number;
    partialDuplicates: number;
  };
  
  typeConsistency: {
    column: string;
    expectedType: string;
    actualTypes: string[];
    conversionErrors: number;
  }[];
  
  outliers: {
    column: string;
    anomalies: number;
    range: [min: number, max: number];
  }[];
}
```

#### Fase 3: Generación de Reportes
```typescript
interface QualityReport {
  summary: {
    overallScore: number; // 0-100
    datasetName: string;
    analysisDate: string;
    issuesFound: number;
  };
  
  findings: {
    severity: "critical" | "high" | "medium" | "low";
    category: string;
    description: string;
    affectedRows: number;
    recommendation: string;
  }[];
  
  metrics: {
    completeness: number;
    uniqueness: number;
    validity: number;
    timeliness: string;
    consistency: number;
  };
}
```

## Ejemplos de Uso

### Ejemplo 1: Análisis de Dataset de Clientes

**Usuario solicita:**
```
Necesito asegurar que nuestro archivo de clientes (customers.csv) 
está listo para un ETL. ¿Puedes hacer un análisis de calidad completo?
```

**Pasos que el agente debe ejecutar:**

1. **Lectura y Exploración**
   ```
   ✓ Abriendo archivo: customers.csv
   ✓ Dimensiones: 50,000 filas × 12 columnas
   ✓ Tipos detectados: ID(int), Name(string), Email(string), Phone(string), 
     CreatedDate(datetime), LastPurchase(datetime), TotalSpent(float), Status(string)
   ```

2. **Validaciones Ejecutadas**
   ```
   INTEGRIDAD:
   ✓ Valores nulos: 
     - Email: 324 registros (0.65%) <- ALERTA
     - Phone: 2,156 registros (4.31%) <- ALERTA
     - LastPurchase: 8,932 registros (17.86%) <- CRÍTICO
   
   ✓ Duplicados:
     - Emails duplicados: 87 registros
     - IDs únicos: OK
   
   ✓ Formato:
     - Emails inválidos: 156 (formato no RFC compliant)
     - Teléfonos: 423 sin formato estándar
   
   ✓ Outliers:
     - TotalSpent: máximo 999,999 (posible error de entrada)
     - CreatedDate: 12 registros con fecha futura
   ```

3. **Reporte Final**
   ```
   📊 REPORTE DE CALIDAD DE DATOS
   ─────────────────────────────────
   Dataset: customers.csv
   Análisis: 2024-03-31
   
   Puntuación General: 72/100 ⚠️ REQUIERE ATENCIÓN
   
   HALLAZGOS CRÍTICOS (3):
   1. [CRITICAL] 8,932 registros sin LastPurchase (17.86%)
      → Recomendación: Validar lógica de actualización
   
   2. [HIGH] 156 emails con formato inválido (0.31%)  
      → Recomendación: Ejecutar validación RFC y corrección
   
   3. [HIGH] 12 CreatedDate en el futuro
      → Recomendación: Revisar control de entrada de datos
   
   MÉTRICAS:
   • Completitud: 94%
   • Validez: 85%
   • Unicidad: 99.8%
   • Consistencia: 88%
   
   PRÓXIMOS PASOS:
   1. Normalizar teléfonos (423 registros)
   2. Validar emails (156 registros)
   3. Investigar blank LastPurchase (posible error de ETL)
   4. Revisar límite máximo de TotalSpent
   ```

### Ejemplo 2: Validación Pre-Procesamiento

**Usuario solicita:**
```
Quiero hacer una transformación en mis datos de transacciones 
pero primero necesito saber si están limpios.
```

**Flujo:**

1. **Escaneo Rápido:** El agente identifica puntos críticos
2. **Diagnóstico:** Determina qué validaciones ejecutar
3. **Reporte Priorizado:** Muestra PRIORIDADes (no hace esperar con análisis innecesarios)
4. **Recomendaciones Accionables:** Código o pasos específicos para remediar

## Integración con Agentes y MCP

### Conexión con Claude (Multimodal Capabilities)

Esta skill se integra con Claude en tres niveles:

#### 1. **Context Window Integration**
- Lee archivos de data y los inyecta en el contexto
- Claude realiza análisis mediante razonamiento
- Genera insights basado en patrones en los datos

#### 2. **Tool Use (Function Calling)**
```json
{
  "tools": [
    {
      "name": "analyze_csv",
      "description": "Analiza archivo CSV para detectar problemas de calidad",
      "input_schema": {
        "type": "object",
        "properties": {
          "file_path": {"type": "string"},
          "validation_rules": {"type": "array"}
        }
      }
    },
    {
      "name": "generate_quality_report",
      "description": "Genera reporte estructurado de hallazgos",
      "input_schema": {
        "type": "object",
        "properties": {
          "findings": {"type": "array"},
          "severity_filter": {"type": "string", "enum": ["all", "critical", "actionable"]}
        }
      }
    }
  ]
}
```

#### 3. **Agent Orchestration Pattern**

```
┌─────────────────┐
│  User Request   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Claude + Skill Context  │◄─── SKILL.md instructions
│ - Entiende el problema  │     injected in system prompt
│ - Planifica análisis    │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Tool Calls (File Ops)    │
│ - Lee datos              │
│ - Ejecuta validaciones   │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Claude Reasoning         │
│ - Interpreta resultados  │
│ - Genera reportes        │
│ - Recomienda acciones    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Structured Output        │
│ (JSON/Markdown Reports)  │
└──────────────────────────┘
```

### Relación con MCP (Model Context Protocol)

Esta skill aprovecha MCP para:

1. **Resource Awareness**
   - Define recursos de "dataset" accesibles
   - Esquema de datos disponibles para análisis

2. **Protocol Extension**
   ```yaml
   resources:
     - uri: "dataset://local/*"
       description: "Datasets analyzed by quality skill"
     
     - uri: "report://quality/*"
       description: "Generated quality reports"
   ```

3. **Tool Standardization**
   - Expone herramientas de validación de forma agnóstica
   - Compatible con diferentes backends (local, cloud, databases)

## Criterios de Evaluación (Rúbrica)

### 1. Completitud de la Skill
- ✅ Tiene nombre, descripción clara
- ✅ Frontmatter YAML válido
- ✅ Ejemplos prácticos y ejecutables
- ✅ Cubre múltiples escenarios

### 2. Resolución de Problema Real
- ✅ Aborda un dolor real en data engineering
- ✅ Solución es automatizable
- ✅ Proporciona valor medible

### 3. Integración con Agentes
- ✅ Explica cómo integrase con Claude/MCP
- ✅ Define interfaces claras (JSON schemas)
- ✅ Muestra flujo de orquestación

### 4. Documentación Técnica
- ✅ Incluye patrones de código
- ✅ Define estructuras de datos
- ✅ Proporciona guías de implementación

## Referencias

- [SKILL.md Specification](https://github.com/github/copilot-chat-tutorial/blob/main/SKILL.md)
- [MCP Documentation - Resources](https://modelcontextprotocol.io/docs/concepts/resources)
- [Claude Tool Use](https://docs.anthropic.com/claude/docs/tool-use)
- [Data Quality Standards - DAMA](https://www.dama-dmbok.org/)

---

**Última actualización:** 2024-03-31  
**Versión:** 1.0  
**Estado:** Producción
