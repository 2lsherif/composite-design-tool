import pandas as pd
import psycopg2
import os

# === Database Connection ===
conn = psycopg2.connect(
    dbname="composite_db",
    user="postgres",
    password="mypostgres123",  # make sure this matches the password you set
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# === Insert Fiber Data ===
print("Inserting fiber data...")
fiber_df = pd.read_csv(os.path.join("data", "clean_fibers.csv"))

for _, row in fiber_df.iterrows():
    cur.execute("""
        INSERT INTO fibers (
            name, tensile_strength_MPa, youngs_modulus_GPa, density_g_cm3,
            elongation_percent, flexural_strength_MPa, impact_strength_kJ_m2,
            moisture_content_percent, fiber_diameter_um
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['fiber_name'], row['tensile_strength_MPa'], row['youngs_modulus_GPa'],
        row['density_g_cm3'], row['elongation_percent'],
        row['flexural_strength_MPa'], row['impact_strength_kJ_m2'],
        row['moisture_content_percent'], row['fiber_diameter_um']
    ))

# === Insert Resin Data ===
print("Inserting resin data...")
resin_df = pd.read_csv(os.path.join("data", "clean_resins.csv"))

for _, row in resin_df.iterrows():
    cur.execute("""
        INSERT INTO resins (
            name, glass_transition_temp_C, curing_temp_C,
            density_g_cm3, viscosity_Pa_s, cost_usd_kg
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['resin_name'], row['glass_transition_temp_C'], row['curing_temp_C'],
        row['density_g_cm3'], row['viscosity_Pa_s'], row['cost_usd_kg']
    ))

# === Finalize ===
conn.commit()
cur.close()
conn.close()

print("✅ Data insertion complete.")

