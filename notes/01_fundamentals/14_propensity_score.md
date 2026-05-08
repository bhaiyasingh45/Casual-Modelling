# Propensity Score Methods

## Definition

A propensity score is the probability of receiving treatment given observed characteristics:

```
e(X) = P(Treatment = 1 | X)
```

Where X is a vector of observed covariates (features).

Propensity scores help create comparable groups when randomization is not possible.

---

## The Key Insight

If two customers have the same propensity score but different treatment status, they are comparable. The treatment they received was essentially "random" given their characteristics.

```
Customer A: Propensity = 0.7, Treated = Yes
Customer B: Propensity = 0.7, Treated = No

These customers are comparable for causal inference.
```

---

## L'Oreal India: Why Propensity Scores Help

### Scenario: Beauty Advisor Effectiveness

**Problem**: We want to know if beauty advisors increase sales, but:
- Advisors are placed in high-traffic stores
- High-traffic stores already have high sales
- Direct comparison is biased

**Solution**: Use propensity scores to compare similar stores.

---

## Step-by-Step Propensity Score Analysis

### Step 1: Define Treatment and Outcome

**Treatment**: Has beauty advisor (Yes/No)
**Outcome**: Monthly sales (Rs Lakhs)

### Step 2: Identify Confounders

Variables that affect BOTH treatment assignment AND outcome:
- Store footfall
- Store size
- Location (mall/standalone)
- City tier
- Competitor presence
- Store age

### Step 3: Estimate Propensity Scores

Build a model to predict treatment assignment:

```python
from sklearn.linear_model import LogisticRegression

# Features that affect advisor assignment
X = stores[['footfall', 'store_size', 'is_mall', 'city_tier', 
            'competitor_count', 'store_age']]

# Treatment indicator
T = stores['has_advisor']

# Fit propensity model
propensity_model = LogisticRegression()
propensity_model.fit(X, T)

# Get propensity scores
stores['propensity_score'] = propensity_model.predict_proba(X)[:, 1]
```

### Step 4: Check Propensity Score Distribution

**Before Adjustment**:
```
Propensity Score Distribution:

Treated stores:     [==========]  Mean = 0.72
Control stores:     [===]         Mean = 0.28

Poor overlap - groups are very different!
```

**Goal**: Find region of "common support" where both groups have observations.

### Step 5: Apply Propensity Score Method

Choose one of:
- Matching
- Stratification
- Inverse Probability Weighting
- Doubly Robust Methods

---

## Propensity Score Methods

### Method 1: Propensity Score Matching (PSM)

Match each treated unit with similar control unit based on propensity score.

**Types of Matching**:

| Type | Description | Pros | Cons |
|------|-------------|------|------|
| Nearest Neighbor | Match to closest propensity | Simple | May use bad matches |
| Caliper | Only match within threshold | Better quality | May lose observations |
| With Replacement | Control can match multiple times | More matches | Reduces effective N |
| Without Replacement | Each control used once | Clean sample | May lose observations |

**L'Oreal Implementation**:

```python
from sklearn.neighbors import NearestNeighbors

# Treated and control propensity scores
treated_ps = stores[stores['has_advisor']==1]['propensity_score'].values
control_ps = stores[stores['has_advisor']==0]['propensity_score'].values

# Find nearest control for each treated
nn = NearestNeighbors(n_neighbors=1)
nn.fit(control_ps.reshape(-1, 1))
distances, indices = nn.kneighbors(treated_ps.reshape(-1, 1))

# Create matched sample
matched_treated = stores[stores['has_advisor']==1]
matched_control = stores[stores['has_advisor']==0].iloc[indices.flatten()]
```

**Result**:
- Unmatched: Advisor stores have Rs 15L higher sales
- Matched: Advisor stores have Rs 5L higher sales

True advisor effect is Rs 5L, not Rs 15L.

### Method 2: Stratification (Subclassification)

Divide observations into strata based on propensity scores.

**L'Oreal Implementation**:

| Stratum | PS Range | Treated Sales | Control Sales | Effect |
|---------|----------|---------------|---------------|--------|
| 1 | 0.0-0.2 | 22L | 20L | +2L |
| 2 | 0.2-0.4 | 30L | 26L | +4L |
| 3 | 0.4-0.6 | 38L | 32L | +6L |
| 4 | 0.6-0.8 | 45L | 40L | +5L |
| 5 | 0.8-1.0 | 55L | 48L | +7L |

**Weighted Average Effect** = 5L (weighted by stratum size)

### Method 3: Inverse Probability Weighting (IPW)

Weight observations by inverse of propensity score.

**Intuition**: 
- Treated unit with low propensity is rare and informative - upweight
- Control unit with high propensity is rare and informative - upweight

**Weights**:
```
For treated: w = 1 / e(X)
For control: w = 1 / (1 - e(X))
```

**L'Oreal Implementation**:

```python
# Calculate IPW weights
stores['ipw_weight'] = np.where(
    stores['has_advisor'] == 1,
    1 / stores['propensity_score'],
    1 / (1 - stores['propensity_score'])
)

# Weighted means
treated_weighted = np.average(
    stores[stores['has_advisor']==1]['sales'],
    weights=stores[stores['has_advisor']==1]['ipw_weight']
)

control_weighted = np.average(
    stores[stores['has_advisor']==0]['sales'],
    weights=stores[stores['has_advisor']==0]['ipw_weight']
)

ate_ipw = treated_weighted - control_weighted
```

### Method 4: Doubly Robust Methods

Combine propensity scores with outcome modeling.

**Advantage**: Consistent if EITHER the propensity model OR outcome model is correct.

```python
# Outcome model
outcome_model = LinearRegression()
outcome_model.fit(X[control], Y[control])

# Predict counterfactual for treated
predicted_control_outcome = outcome_model.predict(X[treated])

# Doubly robust estimate
dr_effect = np.mean(
    (Y[treated] - predicted_control_outcome) / propensity[treated] -
    (T - propensity) * predicted_control_outcome / (propensity * (1-propensity))
)
```

---

## Assessing Propensity Score Quality

### 1. Covariate Balance

After adjustment, treated and control groups should look similar.

**L'Oreal Example**:

| Covariate | Before Matching | After Matching |
|-----------|-----------------|----------------|
| Footfall | SMD = 0.85 | SMD = 0.05 |
| Store Size | SMD = 0.72 | SMD = 0.08 |
| Mall Location | SMD = 0.65 | SMD = 0.03 |
| City Tier | SMD = 0.58 | SMD = 0.06 |

SMD (Standardized Mean Difference) < 0.1 indicates good balance.

### 2. Common Support

Both groups should have observations across propensity score range.

```
Good:                           Bad:
Treated:  [========]            Treated:      [========]
Control:  [========]            Control: [====]
          0    0.5   1                   0    0.5   1
          
Overlap exists                  No overlap in high PS region
```

### 3. Propensity Score Distribution

```python
import matplotlib.pyplot as plt

plt.hist(stores[stores['has_advisor']==1]['propensity_score'], 
         alpha=0.5, label='Treated')
plt.hist(stores[stores['has_advisor']==0]['propensity_score'], 
         alpha=0.5, label='Control')
plt.legend()
```

---

## L'Oreal India: Complete PSM Analysis

### Case: Discount Email Campaign

**Question**: What is the effect of receiving discount emails on purchase?

**Data**:
- 50,000 customers
- 20,000 received discount email (treated)
- 30,000 did not receive email (control)

### Step 1: Baseline Comparison

| Metric | Email Recipients | Non-Recipients |
|--------|-----------------|----------------|
| Past purchase count | 4.5 | 1.8 |
| Avg order value | Rs 2,200 | Rs 1,100 |
| Account age | 28 months | 14 months |
| Website visits/month | 12 | 4 |

Clear selection bias - groups are very different.

### Step 2: Build Propensity Model

```python
X = customers[['past_purchases', 'avg_order_value', 'account_age', 
               'website_visits', 'category_preference', 'gender']]
T = customers['received_email']

ps_model = LogisticRegression()
ps_model.fit(X, T)
customers['ps'] = ps_model.predict_proba(X)[:, 1]
```

### Step 3: Assess Common Support

```
Propensity Score Overlap:
Email recipients: Range 0.15 - 0.95
Non-recipients:   Range 0.02 - 0.75

Common support: 0.15 - 0.75 (use only observations in this range)
```

### Step 4: Match Customers

```python
# 1:1 nearest neighbor matching within caliper
caliper = 0.05  # Maximum PS difference for match

matched_pairs = []
for idx, treated in email_recipients.iterrows():
    candidates = non_recipients[
        abs(non_recipients['ps'] - treated['ps']) < caliper
    ]
    if len(candidates) > 0:
        match = candidates.iloc[
            (candidates['ps'] - treated['ps']).abs().argmin()
        ]
        matched_pairs.append((treated, match))
```

### Step 5: Check Balance After Matching

| Metric | Matched Recipients | Matched Non-Recipients | SMD |
|--------|-------------------|----------------------|-----|
| Past purchases | 3.2 | 3.1 | 0.04 |
| Avg order value | Rs 1,600 | Rs 1,550 | 0.05 |
| Account age | 22 | 21 | 0.03 |
| Website visits | 8 | 7.5 | 0.06 |

Excellent balance achieved!

### Step 6: Estimate Treatment Effect

| Comparison | Email Recipients | Non-Recipients | Difference |
|------------|-----------------|----------------|------------|
| Unmatched | 32% purchased | 12% purchased | +20pp |
| Matched | 28% purchased | 21% purchased | +7pp |

**Result**: True email effect is +7 percentage points, not +20pp.

---

## When Propensity Scores Fail

### 1. Unmeasured Confounders

Propensity scores only balance OBSERVED covariates.

**L'Oreal Example**: 
Customer "intent to purchase" is unmeasured but affects both email targeting and purchase.

### 2. Model Misspecification

If propensity model is wrong, balance may not be achieved.

**Solution**: Check covariate balance, not just propensity score overlap.

### 3. Positivity Violation

Some regions have no overlap (all treated or all control).

**Solution**: Restrict analysis to common support region.

### 4. Extreme Weights

Very high propensity scores lead to extreme IPW weights.

**Solution**: Trim extreme weights or use stabilized weights.

---

## Key Takeaways

1. **Propensity score = P(Treatment | X)** - probability of treatment given features
2. **Equal propensity scores -> comparable units** - treatment is "as if random"
3. **PSM creates artificial control groups** from observational data
4. **Multiple methods**: Matching, Stratification, IPW, Doubly Robust
5. **Check balance** - covariates should be similar after adjustment
6. **Check overlap** - both groups need observations across PS range
7. **Cannot fix unmeasured confounding** - only balances observed variables
8. **Complement with sensitivity analysis** - how robust to unmeasured confounding?

---

## Propensity Score Checklist

Before analysis:
- [ ] Identified all confounders affecting treatment AND outcome
- [ ] Confounders measured in data

Model building:
- [ ] Fit propensity model (logistic regression or ML)
- [ ] Checked model discrimination (AUC reasonable but not too high)

Diagnostics:
- [ ] Assessed common support / overlap
- [ ] Checked covariate balance (SMD < 0.1)
- [ ] Examined propensity score distributions

Estimation:
- [ ] Chose appropriate method (matching, IPW, etc.)
- [ ] Handled extreme propensities
- [ ] Calculated confidence intervals

Interpretation:
- [ ] Acknowledged unmeasured confounding limitation
- [ ] Conducted sensitivity analysis
- [ ] Compared to other methods for robustness
