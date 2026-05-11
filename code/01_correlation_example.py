"""
Correlation Analysis - L'Oreal India Example

This script demonstrates correlation calculation and visualization
using L'Oreal India sales and marketing data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def generate_loreal_data(n_months=24, seed=42):
    """Generate synthetic L'Oreal India monthly data."""
    np.random.seed(seed)

    data = {
        'month': pd.date_range('2024-01', periods=n_months, freq='M'),
        'ad_spend_lakhs': np.random.normal(60, 15, n_months).clip(20, 100),
        'season_factor': np.tile([0.8, 0.9, 1.0, 1.1, 1.0, 0.9,
                                   0.85, 0.9, 1.0, 1.3, 1.4, 1.2], 2)[:n_months],
    }

    # Sales influenced by both ad spend AND season (confounder)
    base_sales = 100
    data['sales_crores'] = (
        base_sales
        + 0.3 * data['ad_spend_lakhs']  # True ad effect
        + 50 * data['season_factor']     # Season effect
        + np.random.normal(0, 5, n_months)  # Noise
    )

    return pd.DataFrame(data)


def calculate_correlation(x, y):
    """Calculate Pearson correlation with p-value."""
    r, p_value = stats.pearsonr(x, y)
    return r, p_value


def interpret_correlation(r):
    """Interpret correlation strength."""
    abs_r = abs(r)
    if abs_r >= 0.7:
        strength = "strong"
    elif abs_r >= 0.4:
        strength = "moderate"
    elif abs_r >= 0.1:
        strength = "weak"
    else:
        strength = "negligible"

    direction = "positive" if r > 0 else "negative"
    return f"{strength} {direction}"


def main():
    # Generate data
    df = generate_loreal_data()

    print("L'Oreal India - Correlation Analysis")
    print("=" * 50)
    print("\nSample Data (first 6 months):")
    print(df[['month', 'ad_spend_lakhs', 'sales_crores']].head(6).to_string(index=False))

    # Calculate correlations
    r_ads_sales, p_ads = calculate_correlation(df['ad_spend_lakhs'], df['sales_crores'])
    r_season_sales, p_season = calculate_correlation(df['season_factor'], df['sales_crores'])
    r_ads_season, p_ads_season = calculate_correlation(df['ad_spend_lakhs'], df['season_factor'])

    print("\n" + "=" * 50)
    print("Correlation Results:")
    print("=" * 50)

    print(f"\n1. Ad Spend vs Sales:")
    print(f"   r = {r_ads_sales:.3f} ({interpret_correlation(r_ads_sales)})")
    print(f"   p-value = {p_ads:.4f}")

    print(f"\n2. Season vs Sales:")
    print(f"   r = {r_season_sales:.3f} ({interpret_correlation(r_season_sales)})")
    print(f"   p-value = {p_season:.4f}")

    print(f"\n3. Ad Spend vs Season (confounder check):")
    print(f"   r = {r_ads_season:.3f} ({interpret_correlation(r_ads_season)})")
    print(f"   p-value = {p_ads_season:.4f}")

    print("\n" + "=" * 50)
    print("Key Insight:")
    print("=" * 50)
    print("""
    The correlation between Ad Spend and Sales appears strong,
    but Season affects BOTH variables (confounder).

    - During Diwali (Oct-Nov): Ad spend is HIGH, Sales are HIGH
    - During off-season: Ad spend is LOW, Sales are LOW

    This inflates the observed correlation beyond the true causal effect.
    Correlation != Causation!
    """)

    return df


if __name__ == "__main__":
    df = main()
