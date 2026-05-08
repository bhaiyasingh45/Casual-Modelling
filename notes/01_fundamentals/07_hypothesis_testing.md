# Hypothesis Testing

## Definition

Hypothesis testing is a statistical method to make decisions about population parameters based on sample data. It provides a framework to determine whether observed differences or effects are likely real or could have occurred by random chance.

---

## The Core Components

### 1. Null Hypothesis (H0)
The default assumption - typically "no effect" or "no difference."

### 2. Alternative Hypothesis (H1 or Ha)
What we're trying to prove - typically "there IS an effect" or "there IS a difference."

### 3. Test Statistic
A number calculated from data that measures how far the observed result is from the null hypothesis.

### 4. P-value
The probability of observing results as extreme as (or more extreme than) the actual results, assuming the null hypothesis is true.

### 5. Significance Level (alpha)
The threshold for rejecting the null hypothesis, typically 0.05 (5%).

---

## L'Oreal India Example: Testing Campaign Effectiveness

### Business Question
Did the new Instagram campaign increase sales?

### Setting Up the Hypothesis Test

**Null Hypothesis (H0)**: The Instagram campaign had no effect on sales.
- Mean sales with campaign = Mean sales without campaign
- Campaign effect = 0

**Alternative Hypothesis (H1)**: The Instagram campaign increased sales.
- Mean sales with campaign > Mean sales without campaign
- Campaign effect > 0

### The Data

| Group | Sample Size | Mean Sales | Std Dev |
|-------|-------------|------------|---------|
| With Campaign (Test) | 50 stores | Rs 42 Lakhs | Rs 8 Lakhs |
| Without Campaign (Control) | 50 stores | Rs 38 Lakhs | Rs 10 Lakhs |

**Observed difference**: 42 - 38 = Rs 4 Lakhs

### The Question
Is this Rs 4 Lakh difference REAL or just random variation?

---

## Step-by-Step Hypothesis Testing Process

### Step 1: State Hypotheses
```
H0: mu_test - mu_control = 0 (no difference)
H1: mu_test - mu_control > 0 (test is higher)
```

### Step 2: Choose Significance Level
alpha = 0.05 (5% chance of false positive)

### Step 3: Calculate Test Statistic

For two-sample t-test:
```
t = (X1 - X2) / sqrt(s1^2/n1 + s2^2/n2)
t = (42 - 38) / sqrt(64/50 + 100/50)
t = 4 / sqrt(1.28 + 2)
t = 4 / 1.81
t = 2.21
```

### Step 4: Find P-value
With df ~ 98, t = 2.21 corresponds to p-value = 0.015

### Step 5: Make Decision
- p-value (0.015) < alpha (0.05)
- Reject null hypothesis
- Conclude: Campaign likely had a positive effect

### Step 6: Interpret Result
"The Instagram campaign increased average store sales by Rs 4 Lakhs (t=2.21, p=0.015). This difference is statistically significant at the 5% level."

---

## Types of Errors

### Type I Error (False Positive)
Rejecting H0 when it's actually true.

**L'Oreal Example**: Concluding the campaign worked when it actually didn't.
- Consequence: Waste money on ineffective campaigns
- Probability: alpha (significance level)

### Type II Error (False Negative)
Failing to reject H0 when it's actually false.

**L'Oreal Example**: Concluding the campaign didn't work when it actually did.
- Consequence: Abandon effective campaigns
- Probability: beta

### Power
Probability of correctly detecting a real effect.
```
Power = 1 - beta
```

---

## Statistical Significance vs Practical Significance

### L'Oreal Example: Statistically Significant but Impractical

**Finding**: New packaging increases sales by 0.5% (p = 0.02)

**Statistically significant?** Yes (p < 0.05)

**Practically significant?** 
- Packaging redesign cost: Rs 50 Lakhs
- Sales lift: 0.5% of Rs 1000 Cr = Rs 5 Cr
- ROI: 10x... actually practical!

But what if:
- Packaging redesign cost: Rs 50 Lakhs
- Sales lift: 0.5% of Rs 10 Cr = Rs 5 Lakhs
- ROI: 1x... not worth it

**Key Point**: Statistical significance doesn't mean business significance.

---

## Common Hypothesis Tests

### 1. One-Sample t-test
Compare sample mean to known value.

**L'Oreal Example**: "Is our customer satisfaction score above 4.0?"
```
H0: mu = 4.0
H1: mu > 4.0
```

### 2. Two-Sample t-test
Compare means of two groups.

**L'Oreal Example**: "Do premium stores have higher sales than regular stores?"
```
H0: mu_premium = mu_regular
H1: mu_premium > mu_regular
```

### 3. Paired t-test
Compare before and after in same units.

**L'Oreal Example**: "Did sales increase after adding beauty advisor?"
```
H0: mu_after - mu_before = 0
H1: mu_after - mu_before > 0
```

### 4. Chi-square test
Test association between categorical variables.

**L'Oreal Example**: "Is there association between region and product preference?"
```
H0: No association (independent)
H1: There is association
```

### 5. ANOVA (F-test)
Compare means across multiple groups.

**L'Oreal Example**: "Do sales differ across North, South, East, West regions?"
```
H0: mu_N = mu_S = mu_E = mu_W
H1: At least one differs
```

---

## Multiple Testing Problem

### The Problem
When running many tests, some will be significant by chance.

**L'Oreal Example**: Testing 20 different campaigns
- At alpha = 0.05, expect 1 false positive even if NO campaigns work
- If we test 100 product variants, expect 5 false positives

### Solutions

**Bonferroni Correction**:
Adjust alpha = 0.05 / number of tests

If testing 20 campaigns: alpha = 0.05/20 = 0.0025

**False Discovery Rate (FDR)**:
Control proportion of false positives among all positives.

---

## One-tailed vs Two-tailed Tests

### Two-tailed Test
Testing for difference in either direction.

**L'Oreal Example**: "Did the new formula change customer satisfaction?"
```
H0: mu_new = mu_old
H1: mu_new != mu_old (could be higher or lower)
```

### One-tailed Test
Testing for difference in specific direction.

**L'Oreal Example**: "Did the new formula IMPROVE customer satisfaction?"
```
H0: mu_new <= mu_old
H1: mu_new > mu_old (only testing for improvement)
```

**When to use one-tailed**: When you only care about one direction and would act the same way if there's no effect or negative effect.

---

## Sample Size and Power

### Power Analysis
Before running test, determine sample size needed.

**L'Oreal Example**: Planning a store experiment
- Expected effect: Rs 5 Lakhs difference
- Typical variation: Rs 10 Lakhs
- Desired power: 80%
- Significance level: 5%

**Required sample size**: ~63 stores per group

### Under-powered Studies
With too small a sample:
- May miss real effects (Type II error)
- Significant results may be exaggerated

**L'Oreal Example**: Testing campaign in only 5 stores
- True effect: Rs 4 Lakhs
- But test is not significant (p = 0.15)
- Campaign abandoned incorrectly

---

## Confidence Intervals vs Hypothesis Tests

### Confidence Interval
Range of plausible values for the true effect.

**L'Oreal Example**: 
Campaign effect: Rs 4 Lakhs
95% CI: [Rs 1 Lakh, Rs 7 Lakhs]

Interpretation: We're 95% confident the true effect is between Rs 1 Lakh and Rs 7 Lakhs.

### Relationship to Hypothesis Test
- If 95% CI doesn't include 0, the test is significant at 5%
- If 95% CI includes 0, the test is not significant

**L'Oreal Example**:
- CI: [Rs 1 Lakh, Rs 7 Lakhs] - doesn't include 0 - significant
- CI: [-Rs 2 Lakhs, Rs 6 Lakhs] - includes 0 - not significant

---

## Common Mistakes in Hypothesis Testing

### Mistake 1: P-value Misinterpretation
**Wrong**: "p = 0.03 means 3% chance the null is true"
**Correct**: "p = 0.03 means 3% chance of seeing this result IF null is true"

### Mistake 2: Absence of Evidence vs Evidence of Absence
**Wrong**: "p = 0.08 means the campaign doesn't work"
**Correct**: "p = 0.08 means we don't have enough evidence to conclude it works"

### Mistake 3: P-hacking
Testing multiple ways until finding significance.

**L'Oreal Example**:
- Overall: p = 0.12 (not significant)
- Just North India: p = 0.08 (not significant)
- Just Mumbai: p = 0.04 (significant!)
- "Campaign works in Mumbai" - but this is likely false positive

### Mistake 4: Confusing Statistical and Practical Significance
**Wrong**: "Effect is significant, so we should do it"
**Correct**: "Effect is significant AND large enough to justify cost"

---

## Hypothesis Testing in Causal Inference

### Role in Causal Analysis
Hypothesis testing tells us IF an effect exists (with confidence).
It does NOT tell us:
- Whether the effect is CAUSAL
- The mechanism of the effect
- Whether confounders are controlled

### L'Oreal Example
**Finding**: Campaign group has significantly higher sales (p < 0.05)

This could mean:
1. Campaign caused higher sales (causal) - if properly randomized
2. Campaign was given to better stores (confounding) - if not randomized
3. Random chance (Type I error) - 5% probability

**Key Point**: Hypothesis testing is necessary but not sufficient for causal claims.

---

## Key Takeaways

1. **Hypothesis testing** determines if observed effects are likely real or random chance
2. **P-value** is probability of data given null hypothesis, NOT probability of hypothesis
3. **Statistical significance** (p < 0.05) doesn't imply **practical significance**
4. **Type I error** (false positive) and **Type II error** (false negative) trade off
5. **Power** is probability of detecting real effects - requires adequate sample size
6. **Multiple testing** inflates false positive rate - requires correction
7. **Confidence intervals** provide more information than just significance
8. **Hypothesis testing alone doesn't prove causation** - need proper study design

---

## Hypothesis Testing Checklist

Before interpreting results:

- [ ] Hypotheses clearly stated before looking at data?
- [ ] Significance level chosen in advance?
- [ ] Sample size adequate for expected effect?
- [ ] Assumptions of test satisfied?
- [ ] Multiple testing corrections applied if needed?
- [ ] Effect size reported alongside p-value?
- [ ] Confidence interval reported?
- [ ] Practical significance considered?
- [ ] Confounders controlled (for causal claims)?
