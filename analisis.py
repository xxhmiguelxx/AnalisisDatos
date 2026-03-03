import pandas as pd

# Cargar datos
df = pd.read_csv("datos_rendimiento_universidad.csv")

# LIMPIEZA
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df = df.dropna()

print("\n=== PRIMERAS FILAS ===")
print(df.head())

# PROMEDIO GENERAL
promedio_general = df["calificacion"].mean()
print("\nPromedio general:", round(promedio_general, 2))

# MATERIAS CON MAYOR REPROBACIÓN (<7)
reprobacion = df.groupby("materia").apply(
    lambda x: (x["calificacion"] < 7).mean() * 100
).sort_values(ascending=False)

print("\n=== Índice de reprobación por materia (%) ===")
print(reprobacion)

# CARRERAS CON MAYOR PROMEDIO
promedio_carrera = df.groupby("carrera")["calificacion"].mean().sort_values(ascending=False)

print("\n=== Promedio por carrera ===")
print(promedio_carrera)

# TENDENCIA POR SEMESTRE
promedio_semestre = df.groupby("semestre")["calificacion"].mean().sort_index()

print("\n=== Promedio por semestre ===")
print(promedio_semestre)

# ESTUDIANTES EN RIESGO (<7)
promedio_estudiante = df.groupby("id_estudiante")["calificacion"].mean()
riesgo = promedio_estudiante[promedio_estudiante < 7]

print("\n=== Estudiantes en riesgo académico ===")
print(riesgo)

print("\nAnálisis completado correctamente.")