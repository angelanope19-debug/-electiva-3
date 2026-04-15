# Integración con Claude

## Paso 1: Setup Inicial

### 1.1 Acceder a Claude

Ir a: https://claude.ai

### 1.2 Crear Nuevo Chat

Click en "New Chat" o "New Conversation"

---

## Paso 2: Cargar la Skill

### Método A: Copy-Paste (Recomendado)

```
1. Abre SKILL.md en tu editor
2. Ctrl+A (selecciona todo)
3. Ctrl+C (copia)
4. En Claude, pega (Ctrl+V)
5. Envía el mensaje
```

**Claude responderá:**

```
He recibido exitosamente la skill:

📋 SKILL LOADED: Data Quality Analysis & Reporting
───────────────────────────────────────────────────

✓ Nombre reconocido
✓ Categoría: data-analysis
✓ Complejidad: intermediate
✓ Targets: Claude, Cursor, VS Code

Estoy listo para:
- Analizar datasets
- Detectar problemas de calidad
- Generar reportes
- Hacer recomendaciones

¿Qué dataset deseas que analice?
```

### Método B: Referenciar via URL

```
He publicado la skill en [URL].

¿Puedes cargarlo desde ahí?
```

---

## Paso 3: Usar la Skill

### Caso de Uso 1: Verificación Rápida

**Tu solicitud:**
```
Tengo un CSV pequeño de clientes.
¿Está listo para usar?

[Dataset CSV]
```

**Claude (con skill):**
```
🔍 ANÁLISIS RÁPIDO
Score: [X]/100
Issues: [N] encontrados
Recomendación: [Acción]
```

### Caso de Uso 2: Análisis Profundo

**Tu solicitud:**
```
Necesito análisis completo con recomendaciones
para limpiar los datos.

[Dataset CSV/JSON/Excel]
```

**Claude (con skill):**
```
📊 ANÁLISIS PROFUNDO
├─ Estructura: OK
├─ Integridad: [Hallazgos]
├─ Anomalías: [Detectadas]
├─ Métricas DAMA-DMBOK: [Valores]
└─ Recomendaciones: [Plan]
```

### Caso de Uso 3: Iteración

**Tu solicitud:**
```
¿Cómo limpio los problemas encontrados?
Dame código Python.
```

**Claude (con skill):**
```
💻 SCRIPT DE LIMPIEZA

[Código Python completo]

Ejecuta esto para:
1. Remover duplicados
2. Validar formatos
3. Llenar nulls
4. [...]

Después, re-analizo el dataset limpio.
```

---

## Paso 4: Capturar Evidencia

### Screenshots Recomendadas

1. **Chat inicial con skill cargada**
   ```
   Mostrar: Message de Claude reconociendo skill
   ```

2. **Dataset ingresado**
   ```
   Mostrar: CSV/JSON con datos
   ```

3. **Reporte completo**
   ```
   Mostrar: Score, hallazgos, métricas
   ```

4. **Código de limpieza**
   ```
   Mostrar: Script Python generado
   ```

5. **Re-análisis después de limpieza**
   ```
   Mostrar: Score mejorado
   ```

---

## Paso 5: Documentar el Flujo

### En tu documento de sustentación, incluye:

```
4.1 INTEGRACIÓN CON CLAUDE
═══════════════════════════

La skill se integra con Claude mediante:

1. CONTEXT INJECTION
   └─ Se carga SKILL.md en el system prompt
   └─ Claude usa ese contexto para especialización

2. MULTI-TURN CONVERSATION
   └─ Usuario solicita análisis
   └─ Claude ejecuta skill internamente
   └─ Produce reporte estructurado
   └─ Usuario puede iterar

3. FORMAT STANDARDIZATION
   └─ JSON schemas definidos
   └─ Reportes reproducibles
   └─ Compatible con pipelines automáticos

EVIDENCIA:
[Incluye 5 screenshots del flujo]
```

---

## Tips para Éxito

### Do's ✅

- ✅ Cargar skill completa en Claude
- ✅ Incluir datos reales en datasets de prueba
- ✅ Solicitar reportes estructurados
- ✅ Pedir código Python ejecutable
- ✅ Capturar cada paso

### Don'ts ❌

- ❌ No cargar skill incompleta
- ❌ No esperar que Claude adivine análisis
- ❌ No usar datasets triviales
- ❌ No omitir pasos en documentación
- ❌ No entregar sin evidencia

---

## Troubleshooting

### Claude no reconoce la skill

**Solución:**
1. Cargar de nuevo SKILL.md completo
2. Aclarar: "Soy especialista en Data Quality Analysis"
3. Dar un ejemplo: "Analiza este CSV..."

### El reporte es muy corto

**Solución:**
1. Pedir: "Análisis profundo con todos los detalles"
2. Solicitar: "Incluye código Python"
3. Indicar: "Genera reportes en formato DAMA-DMBOK"

### No genera recomendaciones

**Solución:**
1. Pedir explícitamente: "Dame 5 recomendaciones"
2. Solicitar: "¿Código para limpiar?"
3. Indicar: "Priorízalas por severidad"

---

## Próximos Pasos

1. ✅ Cargar skill en Claude
2. ✅ Analizar customers.csv
3. ✅ Capturar 5+ screenshots
4. ✅ Documentar en sustentación
5. ✅ Entregar proyecto

**Tiempo total:** 2-3 horas

---

**Versión:** 1.0 | **Actualización:** 31/03/2024
