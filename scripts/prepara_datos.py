"""Prepara data/site_temperatura.csv para la presentación.

Entrada: el parquet crudo del repo site_temperatura (6 sensores, una lectura cada ~30 s).
Salida:  promedios de 5 minutos por sensor, sin las lecturas inválidas (0.00 °C).

Uso:  uv run --with pyarrow python scripts/prepara_datos.py RUTA/Tis.parquet
"""
import sys
import pandas as pd

crudo = pd.read_parquet(sys.argv[1])
total = int(crudo.notna().sum().sum())
ceros = int((crudo == 0).sum().sum())

limpio = crudo.where(crudo > 5)                 # un 0.00 °C en un cuarto de servidores es un error del sensor
T = limpio.resample("5min").mean().round(2)
T = T.loc["2026-05-26":]                        # el 25 de mayo fue la instalación de los sensores
T = T.loc[T.dropna(how="all").index.min():]     # quita el hueco inicial sin datos
T.index.name = "fecha"
T.columns = [f"S{i}" for i in range(1, len(T.columns) + 1)]   # T1,T2,T3,T4,T6,T7 -> S1..S6
T.to_csv("data/site_temperatura.csv")

print(f"lecturas crudas: {total:,} | ceros descartados: {ceros:,}")
print(f"csv: {len(T):,} filas de 5 min, {T.index.min()} a {T.index.max()}")
