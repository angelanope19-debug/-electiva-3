import pandas as pd
import re
from datetime import datetime

# Cargar datasets
customers_df = pd.read_csv('test-data/customers.csv')
sales_df = pd.read_csv('test-data/sales.csv')

print("=" * 80)
print("ANÁLISIS DE CALIDAD DE DATOS - DATA QUALITY SKILL")
print("=" * 80)
print()

# ==================== DATASET: CUSTOMERS ====================
print("📊 DATASET 1: CUSTOMERS.CSV")
print("-" * 80)
print(f"Dimensiones: {customers_df.shape[0]} filas × {customers_df.shape[1]} columnas")
print()

# Valores nulos
print("🔍 VALORES NULOS/MISSING:")
null_counts = customers_df.isnull().sum()
for col in null_counts[null_counts > 0].index:
    count = null_counts[col]
    pct = (count / len(customers_df)) * 100
    severity = "CRÍTICO" if pct > 20 else "ALTO" if pct > 5 else "MEDIO"
    print(f"  - {col}: {count} ({pct:.1f}%) [{severity}]")
print()

# Duplicados exactos
print("✓ DUPLICADOS:")
exact_dupes = customers_df.duplicated().sum()
print(f"  - Filas exactamente duplicadas: {exact_dupes}")
if exact_dupes > 0:
    dupe_rows = customers_df[customers_df.duplicated(keep=False)].sort_values('customer_id')
    print(f"    Ejemplo duplicado: ID={dupe_rows.iloc[0]['customer_id']}, Nombre={dupe_rows.iloc[0]['name']}")
print()

# Emails inválidos
print("✓ EMAILS INVÁLIDOS:")
def is_valid_email(email):
    if pd.isna(email):
        return None
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email)))

invalid_emails = customers_df[customers_df['email'].apply(lambda x: is_valid_email(x) == False)]
print(f"  - Total: {len(invalid_emails)}")
for idx, row in invalid_emails.iterrows():
    print(f"    • Fila {idx+1}: \"{row['email']}\"")
print()

# Teléfonos inválidos
print("✓ TELÉFONOS INVÁLIDOS O FALTANTES:")
def is_valid_phone(phone):
    if pd.isna(phone):
        return None
    pattern = r'^\d{3}-\d{4}$'
    return bool(re.match(pattern, str(phone)))

invalid_phones = customers_df[customers_df['phone'].apply(lambda x: is_valid_phone(x) == False)]
print(f"  - Total: {len(invalid_phones)}")
for idx, row in invalid_phones.iterrows():
    phone_val = "VACÍO" if pd.isna(row['phone']) else f"\"{row['phone']}\""
    print(f"    • Fila {idx+1}: {phone_val}")
print()

# Fechas inválidas
print("✓ FECHAS INVÁLIDAS:")
def is_valid_date(date_str):
    if pd.isna(date_str):
        return None
    try:
        date_obj = pd.to_datetime(date_str)
        if date_obj.month > 12 or date_obj.day > 31:
            return False
        return True
    except:
        return False

invalid_dates = customers_df[customers_df['registration_date'].apply(lambda x: is_valid_date(x) == False)]
print(f"  - Total: {len(invalid_dates)}")
for idx, row in invalid_dates.iterrows():
    print(f"    • Fila {idx+1}: \"{row['registration_date']}\"")
print()

# Outliers
print("✓ OUTLIERS Y ANOMALÍAS:")
outliers_spent = customers_df[customers_df['total_spent'] > 10000]
print(f"  - Total_spent > $10,000: {len(outliers_spent)} registros")
for idx, row in outliers_spent.iterrows():
    print(f"    • Fila {idx+1}: ${row['total_spent']:,.2f}")

# Status inesperados
invalid_status = customers_df[~customers_df['status'].isin(['active', 'inactive', 'pending'])]
print(f"  - Status inesperados: {len(invalid_status)} registros")
for idx, row in invalid_status.iterrows():
    print(f"    • Fila {idx+1}: \"{row['status']}\"")
print()

# ==================== DATASET: SALES ====================
print()
print("📊 DATASET 2: SALES.CSV")
print("-" * 80)
print(f"Dimensiones: {sales_df.shape[0]} filas × {sales_df.shape[1]} columnas")
print()

print("🔍 VALIDACIONES INTEGRIDAD (SALES):")
print()

# Valores nulos
print("✓ VALORES NULOS/MISSING:")
null_counts_sales = sales_df.isnull().sum()
for col in null_counts_sales[null_counts_sales > 0].index:
    count = null_counts_sales[col]
    pct = (count / len(sales_df)) * 100
    severity = "CRÍTICO" if pct > 20 else "ALTO" if pct > 5 else "MEDIO"
    print(f"  - {col}: {count} ({pct:.1f}%) [{severity}]")
print()

# Emails inválidos en sales
print("✓ EMAILS INVÁLIDOS:")
invalid_emails_sales = sales_df[sales_df['email'].apply(lambda x: is_valid_email(x) == False)]
print(f"  - Total: {len(invalid_emails_sales)}")
for idx, row in invalid_emails_sales.iterrows():
    print(f"    • Fila {idx+1}: \"{row['email']}\"")
print()

# Fechas inválidas en sales
print("✓ FECHAS INVÁLIDAS:")
invalid_dates_sales = sales_df[sales_df['date'].apply(lambda x: is_valid_date(x) == False)]
print(f"  - Total: {len(invalid_dates_sales)}")
for idx, row in invalid_dates_sales.iterrows():
    print(f"    • Fila {idx+1}: \"{row['date']}\"")
print()

# Status inválidos en sales
print("✓ STATUS INESPERADOS:")
invalid_status_sales = sales_df[~sales_df['status'].isin(['completed', 'pending', 'failed'])]
print(f"  - Total: {len(invalid_status_sales)}")
for idx, row in invalid_status_sales.iterrows():
    print(f"    • Fila {idx+1}: \"{row['status']}\"")
print()

# ==================== REPORTE EJECUTIVO ====================
print()
print("=" * 80)
print("📋 REPORTE EJECUTIVO DE CALIDAD GENERAL")
print("=" * 80)
print()

total_issues_customers = (
    null_counts.sum() +  # Total valores nulos
    len(invalid_emails) +
    len(invalid_phones) +
    len(invalid_dates) +
    len(outliers_spent) +
    len(invalid_status)
)

total_issues_sales = (
    null_counts_sales.sum() +
    len(invalid_emails_sales) +
    len(invalid_dates_sales) +
    len(invalid_status_sales)
)

print("CUSTOMERS.CSV:")
print(f"  Problemas detectados: {total_issues_customers}")
print(f"  Completitud: {((1 - null_counts.sum()/(len(customers_df)*len(customers_df.columns))) * 100):.1f}%")
print()

print("SALES.CSV:")
print(f"  Problemas detectados: {total_issues_sales}")
print(f"  Completitud: {((1 - null_counts_sales.sum()/(len(sales_df)*len(sales_df.columns))) * 100):.1f}%")
print()

print("=" * 80)
print("✅ ANÁLISIS COMPLETADO")
print("=" * 80)
