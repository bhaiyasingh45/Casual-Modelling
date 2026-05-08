# Correlation

## Definition

Correlation is a statistical measure that describes the strength and direction of a relationship between two variables. It tells us how two things move together, but NOT whether one causes the other.

---

## Mathematical Definition

Pearson Correlation Coefficient (r):

```
r = Cov(X, Y) / (SD(X) * SD(Y))
```

Where:
- Cov(X, Y) = Covariance between X and Y
- SD(X) = Standard deviation of X
- SD(Y) = Standard deviation of Y

**Range**: -1 to +1

| Value | Interpretation |
|-------|----------------|
| +1 | Perfect positive correlation |
| +0.7 to +0.9 | Strong positive correlation |
| +0.4 to +0.6 | Moderate positive correlation |
| +0.1 to +0.3 | Weak positive correlation |
| 0 | No correlation |
| -0.1 to -0.3 | Weak negative correlation |
| -0.4 to -0.6 | Moderate negative correlation |
| -0.7 to -0.9 | Strong negative correlation |
| -1 | Perfect negative correlation |

---

## L'Oreal India Example

### Scenario: Ad Spend and Sales

L'Oreal India observes the following monthly data:

| Month | TV Ad Spend (Lakhs) | Sales (Crores) |
|-------|---------------------|----------------|
| Jan | 50 | 12 |
| Feb | 55 | 13 |
| Mar | 60 | 14 |
| Apr | 45 | 11 |
| May | 70 | 16 |
| Jun | 40 | 10 |
| Jul | 65 | 15 |
| Aug | 75 | 17 |
| Sep | 80 | 18 |
| Oct | 100 | 25 |
| Nov | 110 | 28 |
| Dec | 90 | 22 |

**Correlation coefficient**: r = 0.98 (very strong positive correlation)

### What This Tells Us

- When ad spend increases, sales tend to increase
- When ad spend decreases, sales tend to decrease
- The relationship is very consistent (high correlation)

### What This Does NOT Tell Us

- Whether ads CAUSE sales to increase
- Whether there's something else driving both
- The direction of causality

---

## Types of Correlation

### 1. Positive Correlation
Both variables move in the same direction.

**L'Oreal Example**: Temperature and sunscreen sales
- As temperature increases, sunscreen sales increase
- As temperature decreases, sunscreen sales decrease

### 2. Negative Correlation
Variables move in opposite directions.

**L'Oreal Example**: Price and demand
- As price increases, units sold decrease
- As price decreases, units sold increase

### 3. Zero/No Correlation
No relationship between variables.

**L'Oreal Example**: Stock price of unrelated company and lipstick sales
- Changes in one do not predict changes in the other

---

## Spurious Correlations

Sometimes two variables are correlated purely by coincidence or because both are affected by a third variable.

### L'Oreal Example: Ice Cream and Shampoo Sales

**Observation**: Ice cream sales and anti-dandruff shampoo sales are positively correlated.

**Wrong Conclusion**: Eating ice cream causes dandruff?

**Reality**: Both are affected by summer season (heat causes both ice cream consumption and scalp issues).

---

## Why Correlation is Not Enough

### The Hidden Variable Problem

Consider L'Oreal India's observation:

**Data**: Regions with more beauty advisors have higher sales.
**Correlation**: r = 0.85

**Possible Interpretations**:

1. Beauty advisors cause higher sales (advisors -> sales)
2. High sales regions get more advisors (sales -> advisors)
3. Wealthy regions have both more advisors AND higher sales (wealth -> both)

Correlation alone cannot distinguish between these!

---

## Correlation in Business Context

### When Correlation is Useful

1. **Prediction**: If correlation is stable, we can predict one variable from another
2. **Hypothesis Generation**: Correlations suggest relationships to investigate
3. **Anomaly Detection**: Breaking correlations may indicate problems
4. **Feature Selection**: Correlated features may be redundant in ML models

### When Correlation is Misleading

1. **Decision Making**: "Spend more on ads because they correlate with sales"
2. **Attribution**: "Instagram caused the sale because visitors from Instagram buy more"
3. **Intervention Planning**: "Hire more beauty advisors to increase sales"

---

## Key Takeaways

1. Correlation measures relationship strength, not causation
2. High correlation does not imply one variable causes another
3. Hidden variables (confounders) can create spurious correlations
4. Correlation is symmetric: Corr(X,Y) = Corr(Y,X)
5. Causation is directional: X causes Y is different from Y causes X
6. Use correlation for prediction and hypothesis generation, not causal claims

---

## Common Mistakes to Avoid

| Mistake | Example | Problem |
|---------|---------|---------|
| Assuming causation | "Ads correlate with sales, so ads cause sales" | Ignores confounders |
| Ignoring direction | "Sales and ads are related" | Which causes which? |
| Overgeneralizing | "This correlation holds everywhere" | May vary by region/time |
| Cherry-picking | Reporting only significant correlations | Statistical coincidence |

---

## Moving Beyond Correlation

To establish causation, we need:

1. **Temporal precedence**: Cause must come before effect
2. **Mechanism**: Plausible explanation for how X affects Y
3. **Rule out confounders**: Ensure no hidden variables explain the relationship
4. **Experimental evidence**: Ideally, manipulate X and observe Y

These are the foundations of causal inference, which we will explore in subsequent notes.
