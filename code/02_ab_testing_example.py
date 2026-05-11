"""
A/B Testing - L'Oreal India Example

This script demonstrates A/B test analysis for testing
product reviews feature on L'Oreal India e-commerce.
"""

import numpy as np
import pandas as pd
from scipy import stats


def generate_ab_test_data(n_control=5000, n_treatment=5000, seed=42):
    """
    Generate synthetic A/B test data.

    Scenario: Testing if adding product reviews increases conversion.
    Control: No reviews | Treatment: With reviews
    """
    np.random.seed(seed)

    # Control group (no reviews)
    control_conversion_rate = 0.020  # 2% baseline
    control_conversions = np.random.binomial(1, control_conversion_rate, n_control)

    # Treatment group (with reviews) - true lift of 20%
    treatment_conversion_rate = 0.024  # 2.4% with reviews
    treatment_conversions = np.random.binomial(1, treatment_conversion_rate, n_treatment)

    control_df = pd.DataFrame({
        'group': 'control',
        'converted': control_conversions,
        'visitor_id': range(n_control)
    })

    treatment_df = pd.DataFrame({
        'group': 'treatment',
        'converted': treatment_conversions,
        'visitor_id': range(n_control, n_control + n_treatment)
    })

    return pd.concat([control_df, treatment_df], ignore_index=True)


def calculate_conversion_rates(df):
    """Calculate conversion rates by group."""
    return df.groupby('group')['converted'].agg(['sum', 'count', 'mean'])


def run_proportion_test(df):
    """Run two-proportion z-test."""
    control = df[df['group'] == 'control']['converted']
    treatment = df[df['group'] == 'treatment']['converted']

    # Counts
    x1, n1 = control.sum(), len(control)
    x2, n2 = treatment.sum(), len(treatment)

    # Proportions
    p1 = x1 / n1
    p2 = x2 / n2

    # Pooled proportion
    p_pooled = (x1 + x2) / (n1 + n2)

    # Standard error
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))

    # Z-score
    z = (p2 - p1) / se

    # P-value (two-tailed)
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    return {
        'control_rate': p1,
        'treatment_rate': p2,
        'absolute_lift': p2 - p1,
        'relative_lift': (p2 - p1) / p1,
        'z_score': z,
        'p_value': p_value
    }


def calculate_confidence_interval(df, confidence=0.95):
    """Calculate confidence interval for the difference."""
    control = df[df['group'] == 'control']['converted']
    treatment = df[df['group'] == 'treatment']['converted']

    p1, n1 = control.mean(), len(control)
    p2, n2 = treatment.mean(), len(treatment)

    diff = p2 - p1

    # Standard error of difference
    se_diff = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)

    # Z-value for confidence level
    z = stats.norm.ppf(1 - (1 - confidence) / 2)

    ci_lower = diff - z * se_diff
    ci_upper = diff + z * se_diff

    return ci_lower, ci_upper


def interpret_results(results, alpha=0.05):
    """Interpret A/B test results."""
    if results['p_value'] < alpha:
        significance = "statistically significant"
        recommendation = "SHIP the treatment (reviews feature)"
    else:
        significance = "NOT statistically significant"
        recommendation = "DO NOT ship - need more data or no real effect"

    return significance, recommendation


def main():
    print("L'Oreal India - A/B Test Analysis")
    print("=" * 60)
    print("\nScenario: Testing product reviews on e-commerce site")
    print("Control: Current page (no reviews)")
    print("Treatment: Page with customer reviews section")
    print("Primary Metric: Conversion rate (purchases / visitors)")

    # Generate data
    df = generate_ab_test_data()

    print("\n" + "=" * 60)
    print("Sample Sizes:")
    print("=" * 60)
    sizes = df.groupby('group').size()
    print(f"Control: {sizes['control']:,} visitors")
    print(f"Treatment: {sizes['treatment']:,} visitors")

    # Calculate results
    results = run_proportion_test(df)
    ci_lower, ci_upper = calculate_confidence_interval(df)
    significance, recommendation = interpret_results(results)

    print("\n" + "=" * 60)
    print("Results:")
    print("=" * 60)
    print(f"\nControl conversion rate:   {results['control_rate']:.2%}")
    print(f"Treatment conversion rate: {results['treatment_rate']:.2%}")
    print(f"\nAbsolute lift: {results['absolute_lift']:.2%} ({results['absolute_lift']*100:.2f} percentage points)")
    print(f"Relative lift: {results['relative_lift']:.1%}")

    print("\n" + "=" * 60)
    print("Statistical Analysis:")
    print("=" * 60)
    print(f"\nZ-score: {results['z_score']:.3f}")
    print(f"P-value: {results['p_value']:.4f}")
    print(f"95% CI for lift: [{ci_lower:.2%}, {ci_upper:.2%}]")
    print(f"\nResult: {significance} at alpha=0.05")

    print("\n" + "=" * 60)
    print("Recommendation:")
    print("=" * 60)
    print(f"\n{recommendation}")

    if results['p_value'] < 0.05:
        print(f"\nBusiness Impact Estimate:")
        print(f"- Current monthly visitors: 500,000")
        print(f"- Current conversions: {500000 * results['control_rate']:,.0f}")
        print(f"- Expected with reviews: {500000 * results['treatment_rate']:,.0f}")
        print(f"- Incremental conversions: {500000 * results['absolute_lift']:,.0f}/month")

    return df, results


if __name__ == "__main__":
    df, results = main()
