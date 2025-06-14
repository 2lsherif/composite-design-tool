-- Fiber Table
CREATE TABLE IF NOT EXISTS fibers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    tensile_strength_MPa REAL,
    youngs_modulus_GPa REAL,
    density_g_cm3 REAL,
    elongation_percent REAL,
    flexural_strength_MPa REAL,
    impact_strength_kJ_m2 REAL,
    moisture_content_percent REAL,
    fiber_diameter_um REAL
);

-- Resin Table
CREATE TABLE IF NOT EXISTS resins (
    id SERIAL PRIMARY KEY,
    name TEXT,
    glass_transition_temp_C REAL,
    curing_temp_C REAL,
    density_g_cm3 REAL,
    viscosity_Pa_s REAL,
    cost_usd_kg REAL
);
