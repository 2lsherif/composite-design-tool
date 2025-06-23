import pandas as pd
import itertools
import os

fibers = pd.read_csv("data/clean_fibers.csv")
resins = pd.read_csv("data/clean_resins.csv")

combinations = list(itertools.product(fibers.to_dict('records'), resins.to_dict('records')))

rows = []
for f, r in combinations:
    score = (
        0.6 * f['tensile_strength_MPa'] +
        0.3 * r['glass_transition_temp_C'] -
        0.2 * (f['density_g_cm3'] + r['density_g_cm3']) +
        0.1 * (10 - r['cost_usd_kg'])  # lower cost is better
    )
    rows.append({
        **{f'fiber_{k}': v for k, v in f.items()},
        **{f'resin_{k}': v for k, v in r.items()},
        "score": score
    })

df = pd.DataFrame(rows)
os.makedirs("data", exist_ok=True)
df.to_csv("data/composite_training_data.csv", index=False)
print("✅ Training dataset created at data/composite_training_data.csv")

