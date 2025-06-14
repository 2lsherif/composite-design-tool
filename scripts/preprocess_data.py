import pandas as pd
import os

# === FIBER DATA CLEANING ===
print("=== Cleaning Fiber Data ===")

fiber_path = os.path.join("data", "raw_fibers.csv")
fibers = pd.read_csv(fiber_path)

# Ensure numeric types
fiber_numeric_cols = [
    'tensile_strength_MPa',
    'youngs_modulus_GPa',
    'density_g_cm3',
    'elongation_percent',
    'flexural_strength_MPa',
    'impact_strength_kJ_m2',
    'moisture_content_percent',
    'fiber_diameter_um'
]

for col in fiber_numeric_cols:
    fibers[col] = pd.to_numeric(fibers[col], errors='coerce')

# Handle missing values
fibers.fillna(method='ffill', inplace=True)
fibers.fillna(method='bfill', inplace=True)

# Save cleaned fiber data
clean_fiber_path = os.path.join("data", "clean_fibers.csv")
fibers.to_csv(clean_fiber_path, index=False)

print(f"✅ Cleaned fiber data saved to {clean_fiber_path}")
print(fibers.info())
print(fibers.head())


# === RESIN DATA CLEANING ===
print("\n=== Cleaning Resin Data ===")

resin_path = os.path.join("data", "raw_resins.csv")
resins = pd.read_csv(resin_path)

# Ensure numeric types
resin_numeric_cols = [
    'glass_transition_temp_C',
    'curing_temp_C',
    'density_g_cm3',
    'viscosity_Pa_s',
    'cost_usd_kg'
]

for col in resin_numeric_cols:
    resins[col] = pd.to_numeric(resins[col], errors='coerce')

# Handle missing values
resins.fillna(method='ffill', inplace=True)
resins.fillna(method='bfill', inplace=True)

# Save cleaned resin data
clean_resin_path = os.path.join("data", "clean_resins.csv")
resins.to_csv(clean_resin_path, index=False)

print(f"✅ Cleaned resin data saved to {clean_resin_path}")
print(resins.info())
print(resins.head())
