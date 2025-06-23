import pandas as pd
import os


def recommend_materials(
    min_tensile_strength=100,
    max_density=1.5,
    max_cost=3.0,
):
    fiber_path = os.path.join("data", "clean_fibers.csv")
    resin_path = os.path.join("data", "clean_resins.csv")

    fibers = pd.read_csv(fiber_path)
    resins = pd.read_csv(resin_path)

    # Filter fibers based on strength and density
    filtered_fibers = fibers[
        (fibers["tensile_strength_MPa"] >= min_tensile_strength)
        & (fibers["density_g_cm3"] <= max_density)
    ]

    # Filter resins based on cost and density
    filtered_resins = resins[
        (resins["cost_usd_kg"] <= max_cost)
        & (resins["density_g_cm3"] <= max_density)
    ]

    recommendations = []

    for _, fiber in filtered_fibers.iterrows():
        for _, resin in filtered_resins.iterrows():
            combo = {
                "fiber": fiber["fiber_name"],
                "resin": resin["resin_name"],
                "combo_density": round(
                    (fiber["density_g_cm3"] + resin["density_g_cm3"]) / 2, 3
                ),
                "combo_strength": fiber["tensile_strength_MPa"],
            }
            recommendations.append(combo)

    return sorted(
        recommendations,
        key=lambda x: (-x["combo_strength"], x["combo_density"]),
    )


if __name__ == "__main__":
    results = recommend_materials()
    for rec in results:
        print(rec)
