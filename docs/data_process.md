
# Data Cleaning Process Documentation

This document describes how the raw fiber and resin data was processed and cleaned for use in the Custom Composite Design Tool.

---

## Files

| File | Description |
|------|-------------|
| `data/raw_fibers.csv` | Raw input data for natural fibers |
| `data/raw_resins.csv` | Raw input data for resins |
| `data/clean_fibers.csv` | Cleaned fiber data |
| `data/clean_resins.csv` | Cleaned resin data |
| `scripts/preprocess_data.py` | Script used to clean both datasets |

---

## Fiber Data Cleaning

### Columns Processed:
- `tensile_strength_MPa`
- `youngs_modulus_GPa`
- `density_g_cm3`
- `elongation_percent`
- `flexural_strength_MPa`
- `impact_strength_kJ_m2`
- `moisture_content_percent`
- `fiber_diameter_um`

### Cleaning Actions:
- Converted all numeric columns using `pandas.to_numeric(..., errors='coerce')`
- Applied forward fill (`ffill`) and backward fill (`bfill`) to fill missing values
- Saved the cleaned file as `data/clean_fibers.csv`

---

## Resin Data Cleaning

### Columns Processed:
- `glass_transition_temp_C`
- `curing_temp_C`
- `density_g_cm3`
- `viscosity_Pa_s`
- `cost_usd_kg`

### Cleaning Actions:
- Converted all numeric columns using `pandas.to_numeric(..., errors='coerce')`
- Applied forward fill (`ffill`) and backward fill (`bfill`) to fill in missing values
- Saved the cleaned file as `data/clean_resins.csv`

---

## Missing Value Strategy

- **Forward fill** (`.fillna(method='ffill')`) was used to carry values down from above
- **Backward fill** (`.fillna(method='bfill')`) was used to fill in remaining blanks
- This ensures no column remains entirely empty, but assumptions should be verified before production deployment

---

## Script Used

See [`scripts/preprocess_data.py`](../scripts/preprocess_data.py) for full implementation.

---

## Last Updated

This document was generated based on the files provided and the cleaning script created on behalf of Elsherif Emad.

