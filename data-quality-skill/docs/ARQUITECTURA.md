# Arquitectura Técnica: Data Quality Analysis & Reporting

## 1. Vision General

```
┌─────────────────────────────────────────────────────┐
│         DATA QUALITY ANALYSIS & REPORTING           │
│                      SKILL v1.0                     │
└─────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════╗
║          NIVELES DE INTEGRACIÓN                  ║
╚═══════════════════════════════════════════════════╝

NIVEL 1: SKILL DEFINITION (SKILL.md)
        ↓
        Define capacidades, ejemplos, schemas
        
NIVEL 2: AGENT CONTEXT (Claude + Context)
        ↓
        Carga skill en system prompt
        
NIVEL 3: EXECUTION LAYER (Analysis Engine)
        ↓
        Ejecuta validaciones, genera reportes
        
NIVEL 4: OUTPUT FORMAT (JSON/Markdown)
        ↓
        Entrega resultados estructurados
```

## 2. Flujo de Datos Completo

```
┌──────────────────┐
│  USER REQUEST    │
│ ("Analyze data") │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────┐
│ CLAUDE + SKILL CONTEXT       │
│ - Lee SKILL.md               │
│ - Entiende metodología       │
│ - Genera plan                │
└────────┬─────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│         ANALYSIS ENGINE (Multi-Phase)   │
│                                         │
│ PHASE 1: EXPLORATION                   │
│ ├─ Read file structure                │
│ ├─ Detect types                       │
│ └─ Get dimensions (rows × cols)       │
│                                         │
│ PHASE 2: VALIDATION                    │
│ ├─ Null detection                     │
│ ├─ Duplicate detection                │
│ ├─ Type consistency                   │
│ └─ Format validation                  │
│                                         │
│ PHASE 3: ANOMALY DETECTION             │
│ ├─ Statistical outliers               │
│ ├─ Business rule violations           │
│ └─ Enum violations                    │
│                                         │
│ PHASE 4: METRICS CALCULATION           │
│ ├─ Completeness %                     │
│ ├─ Validity %                         │
│ ├─ Uniqueness %                       │
│ ├─ Consistency %                      │
│ └─ Timeliness check                   │
│                                         │
│ PHASE 5: SYNTHESIS                     │
│ ├─ Classify by severity               │
│ ├─ Generate recommendations           │
│ └─ Create report                      │
└────────┬─────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  STRUCTURED OUTPUT                 │
│ {                                  │
│   "quality_score": 62,             │
│   "issues": [...],                 │
│   "metrics": {...},                │
│   "recommendations": [...]         │
│ }                                  │
└────────┬───────────────────────────┘
         │
         ▼
┌──────────────────┐
│   USER RECEIVES  │
│  QUALITY REPORT  │
└──────────────────┘
```

## 3. Interfaz de Datos

### 3.1 Input Schema

```typescript
interface AnalysisRequest {
  dataset: {
    path?: string;           // File path or URL
    content?: string;        // Raw CSV/JSON content
    format: "csv" | "json" | "parquet";
    delimiter?: string;      // For CSV
  };
  
  analysisDepth: "quick" | "standard" | "thorough";
  
  validationRules?: {
    requiredColumns?: string[];
    allowedEnums?: Record<string, string[]>;
    rangeConstraints?: Record<string, [min, max]>;
    emailValidation?: boolean;
    phoneValidation?: boolean;
  };
  
  anomalyDetection?: {
    outlierMethod: "zscore" | "iqr";
    threshold?: number;
  };
}
```

### 3.2 Output Schema

```typescript
interface QualityReport {
  metadata: {
    datasetName: string;
    analysisTimestamp: string;
    totalRecords: number;
    totalColumns: number;
    fileSize?: number;
  };
  
  summary: {
    overallQualityScore: number;  // 0-100
    totalIssuesFound: number;
    issuesBySeverity: {
      critical: number;
      high: number;
      medium: number;
      low: number;
    };
  };
  
  metrics: {
    completeness: number;    // % of non-null values
    validity: number;        // % of valid formats
    uniqueness: number;      // % of unique records
    consistency: number;     // Type consistency %
    timeliness: string;      // "Current" | "Stale"
  };
  
  findings: Finding[];  // By severity
  
  recommendations: Recommendation[];
}

interface Finding {
  id: string;
  severity: "critical" | "high" | "medium" | "low";
  category: "integrity" | "format" | "anomaly" | "business";
  description: string;
  affectedRecords: number;
  affectedColumns?: string[];
  details?: Record<string, any>;
}

interface Recommendation {
  priority: number;  // 1 = highest
  action: string;
  estimatedEffort: "quick" | "medium" | "complex";
  cleanupScript?: string;  // Python/SQL code
}
```

## 4. Componentes Principales

### 4.1 Phase Manager

```
┌──────────────────────┐
│  PHASE MANAGER       │
├──────────────────────┤
│ 1. Orchestrate       │
│ 2. Execute sequentially or parallel
│ 3. Aggregate results │
│ 4. Handle errors     │
│ 5. Generate report   │
└──────────────────────┘
```

### 4.2 Validation Engine

```
┌─────────────────────────────────────┐
│     VALIDATION ENGINE               │
├─────────────────────────────────────┤
│ • Null/Missing Detector             │
│ • Duplicate Finder                  │
│ • Type Validator                    │
│ • Format Checker (Email, Phone)     │
│ • Range/Constraint Validator        │
│ • Enum Validator                    │
│ • Outlier Detector (Z-score, IQR)   │
└─────────────────────────────────────┘
```

### 4.3 Metrics Calculator

```
DAMA-DMBOK Framework Implementation:

Completeness = (non-null values / total cells) × 100
Validity = (valid format / total values) × 100
Uniqueness = (unique records / total records) × 100
Consistency = (consistent types / total values) × 100
Timeliness = (current data / total records) × 100
```

### 4.4 Report Generator

```
┌────────────────────────────┐
│   REPORT GENERATOR         │
├────────────────────────────┤
│ Template Engine:           │
│ • Markdown format          │
│ • JSON structured          │
│ • HTML option              │
│ • Excel export option      │
│                            │
│ Sections:                  │
│ 1. Executive Summary       │
│ 2. Detailed Findings       │
│ 3. Quality Metrics         │
│ 4. Recommendations         │
│ 5. Cleanup Scripts         │
│ 6. Appendix (Raw Data)     │
└────────────────────────────┘
```

## 5. Integración con MCP

```
┌─────────────────────────────────┐
│   MODEL CONTEXT PROTOCOL (MCP)  │
├─────────────────────────────────┤
│ RESOURCES:                      │
│ ├─ dataset://local/*            │
│ ├─ report://quality/*           │
│ └─ rules://validation/*         │
│                                 │
│ TOOLS:                          │
│ ├─ analyze_dataset              │
│ ├─ validate_integrity           │
│ ├─ detect_anomalies             │
│ ├─ calculate_metrics            │
│ └─ generate_report              │
│                                 │
│ PROMPTS (Skills):               │
│ └─ data-quality-analysis        │
└─────────────────────────────────┘
```

## 6. Flujo de Ejecución

### Timing Estimate

```
Analysis of 1,000 records × 10 columns:

PHASE          TIME
─────────────────────
1. Exploration    2 sec
2. Validation    15 sec
3. Anomalies      8 sec
4. Metrics        3 sec
5. Report         2 sec
─────────────────────
TOTAL           30 sec (vs. 240 min manual)
```

## 7. Error Handling

```
┌────────────────────────────┐
│   ERROR SCENARIOS          │
├────────────────────────────┤
│ • File not found → Show path
│ • Invalid format → Auto-detect
│ • Large files → Chunking
│ • Memory issues → Sampling
│ • Encoding issues → UTF-8 conversion
└────────────────────────────┘
```

## 8. Escalabilidad

```
Single File Performance:
├─ < 100K rows:     Instant (< 5 sec)
├─ 100K-1M rows:    Fast (10-30 sec)
├─ 1M-10M rows:     Batch (1-5 min)
└─ > 10M rows:      Distributed (custom)
```

## 9. Diagrama de Componentes

```
                    ┌─────────────┐
                    │ SKILL.md    │
                    │ Definition  │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    ┌───▼───┐        ┌──────▼──────┐    ┌────▼────┐
    │Patient│        │Claude Agent │    │Cursor   │
    │Context│        │Integration  │    │Support  │
    └───┬───┘        └──────┬──────┘    └────┬────┘
        │                   │               │
        └───────────────────┼───────────────┘
                            │
                    ┌───────▼────────┐
                    │ Analysis Engine│
                    │ (Multi-Phase)  │
                    └───────┬────────┘
                            │
        ┌───────────────────┼───────────────┬──────────┐
        │                   │               │          │
    ┌───▼────┐  ┌─────▼────┐  ┌────▼────┐ ┌─▼────┐ ┌──▼───┐
    │Validator│  │Detector  │  │Metrics  │ │Report│ │Error │
    │         │  │          │  │Calc     │ │Gen   │ │Handle│
    └─────────┘  └──────────┘  └─────────┘ └──────┘ └──────┘
```

---

**Versión:** 1.0 | **Actualización:** 31/03/2024
