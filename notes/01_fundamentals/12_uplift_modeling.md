# Uplift Modeling

## Definition

Uplift modeling (also called incremental modeling or true lift modeling) is a technique to predict the INCREMENTAL impact of a treatment on individual units. It identifies who will change their behavior BECAUSE of the treatment, not just who will have a positive outcome.

**Key Question**: "Who will respond ONLY IF we treat them?"

---

## The Core Insight

Not all customers respond to treatments the same way:

| Customer Type | Without Treatment | With Treatment | Uplift |
|---------------|-------------------|----------------|--------|
| Sure Things | Buy | Buy | 0 |
| Lost Causes | Don't Buy | Don't Buy | 0 |
| Persuadables | Don't Buy | Buy | POSITIVE |
| Sleeping Dogs | Buy | Don't Buy | NEGATIVE |

**Traditional targeting**: Focus on likely buyers (Sure Things + Persuadables)
**Uplift targeting**: Focus on ONLY Persuadables

---

## L'Oreal India Example: Discount Campaign

### Scenario
L'Oreal wants to send 20% discount codes to customers. Budget allows 100,000 discounts.

### Traditional Approach (Response Modeling)
Predict: P(Purchase | Customer Features)
Target: Top 100,000 by purchase probability

**Problem**: Many targeted customers would buy ANYWAY without discount.

### Uplift Approach
Predict: P(Purchase | Discount) - P(Purchase | No Discount)
Target: Top 100,000 by INCREMENTAL purchase probability

**Benefit**: Spend discount budget only on customers who need persuading.

---

## The Math Behind Uplift

### Individual Treatment Effect (ITE)

For customer i:
```
Uplift_i = Y_i(1) - Y_i(0)

Where:
Y_i(1) = Outcome if treated
Y_i(0) = Outcome if not treated
```

**Problem**: We can only observe ONE outcome per customer.

### Conditional Average Treatment Effect (CATE)

Average uplift for customers with specific characteristics:
```
CATE(X) = E[Y(1) - Y(0) | X]
        = E[Y(1) | X] - E[Y(0) | X]
```

Uplift modeling estimates CATE for each customer.

---

## Customer Segmentation by Uplift

### The Four Quadrants

```
                    High P(Buy | No Treatment)
                           |
         Sure Things       |       Sleeping Dogs
         (Don't target)    |       (Never target!)
                           |
    -------- Low Uplift ---+--- Negative Uplift --------
                           |
         Lost Causes       |       Persuadables
         (Don't target)    |       (Target these!)
                           |
                    Low P(Buy | No Treatment)
```

### L'Oreal India Customer Examples

**Sure Things** (Uplift ~ 0, High baseline):
- Loyal customers who buy every month
- Already subscribed to auto-replenishment
- Don't need discount to purchase

**Lost Causes** (Uplift ~ 0, Low baseline):
- Not in target demographic
- Never bought beauty products
- Discount won't change behavior

**Persuadables** (Positive Uplift):
- Considered L'Oreal but chose competitor
- Price-sensitive occasional buyers
- Browsed but didn't purchase

**Sleeping Dogs** (Negative Uplift):
- Feel brand is "cheap" if discounted
- Buy premium, discount signals low quality
- Reminder email annoys them, drives away

---

## Uplift Modeling Methods

### 1. Two-Model Approach (T-Learner)

Train two separate models:
- Model 1: P(Y=1 | X) for treated group
- Model 2: P(Y=1 | X) for control group

Uplift = Model1 prediction - Model2 prediction

**L'Oreal Implementation**:
```python
# Model 1: Predict purchase probability with discount
model_treatment = train(X_treated, Y_treated)

# Model 2: Predict purchase probability without discount
model_control = train(X_control, Y_control)

# Uplift score
uplift = model_treatment.predict(X) - model_control.predict(X)
```

**Pros**: Simple, uses standard ML algorithms
**Cons**: Subtracting two noisy estimates increases variance

### 2. Single-Model Approach (S-Learner)

Train one model with treatment as a feature:
```
Y = f(X, Treatment)
```

Uplift = f(X, T=1) - f(X, T=0)

**L'Oreal Implementation**:
```python
# Add treatment indicator to features
X_with_treatment = concat(X, treatment_indicator)

# Train single model
model = train(X_with_treatment, Y)

# Predict with treatment = 1 and treatment = 0
pred_treated = model.predict(X, T=1)
pred_control = model.predict(X, T=0)

uplift = pred_treated - pred_control
```

**Pros**: Single model, captures interactions
**Cons**: Treatment effect may be dominated by other features

### 3. Class Transformation Approach

Transform the problem into standard classification.

For each observation, create transformed outcome:
```
Z = Y * T / P(T) - Y * (1-T) / P(1-T)
```

Then train model to predict Z from X.

**Pros**: Directly optimizes for uplift
**Cons**: High variance when propensity is extreme

### 4. Uplift Trees / Forests

Decision trees that split based on maximizing uplift difference.

Split criterion: Maximize difference in treatment effect between groups.

**Pros**: Directly models heterogeneous effects
**Cons**: Specialized algorithm needed

---

## L'Oreal India: Complete Uplift Analysis

### Data Setup

| Customer | Segment | Received Discount | Purchased | Features |
|----------|---------|-------------------|-----------|----------|
| C001 | Treatment | Yes | Yes | Age=28, City=Mumbai, ... |
| C002 | Control | No | No | Age=35, City=Delhi, ... |
| C003 | Treatment | Yes | No | Age=42, City=Chennai, ... |
| C004 | Control | No | Yes | Age=25, City=Bangalore, ... |
| ... | ... | ... | ... | ... |

### Building the Model

**Step 1**: Split historical data into treatment/control from past campaigns

**Step 2**: Train uplift model using T-Learner approach

**Step 3**: Score all customers for uplift

### Results by Customer Segment

| Segment | Avg Baseline | Avg with Discount | Uplift | Count | Recommendation |
|---------|--------------|-------------------|--------|-------|----------------|
| Young Urban | 15% | 35% | +20pp | 200K | Target |
| Loyal Premium | 45% | 46% | +1pp | 150K | Don't target |
| Rural Low-Income | 2% | 3% | +1pp | 500K | Don't target |
| Lapsed Customers | 5% | 25% | +20pp | 100K | Target |
| Competitor Users | 3% | 18% | +15pp | 180K | Target |

### Targeting Decision

Budget: 100,000 discount codes

**Traditional approach** (by purchase probability):
- Target top 100K by P(Purchase | Discount)
- Mostly Loyal Premium and Young Urban
- Includes Sure Things who would buy anyway

**Uplift approach**:
- Target top 100K by Uplift score
- Mostly Young Urban, Lapsed, and Competitor Users
- Excludes Sure Things, includes Persuadables

### ROI Comparison

| Approach | Discounts Sent | Purchases | Baseline Purchases | Incremental | ROI |
|----------|---------------|-----------|-------------------|-------------|-----|
| Random | 100K | 20K | 12K | 8K | 1.5x |
| Response Model | 100K | 35K | 28K | 7K | 1.3x |
| Uplift Model | 100K | 28K | 8K | 20K | 3.8x |

Uplift approach generates 2.5x more incremental conversions!

---

## Evaluation Metrics for Uplift Models

### 1. Uplift Curve (Qini Curve)

Plot cumulative uplift vs percentage of population targeted.

```
Cumulative
Uplift
   ^
   |        /-------- Uplift Model
   |      /
   |    /   /--------- Random
   |  /   /
   | / /
   |//
   +-----------------------> % Population Targeted
```

### 2. Qini Coefficient

Area between uplift curve and random baseline.
Higher = better model.

### 3. Uplift by Decile

| Decile | Treatment Conversion | Control Conversion | Uplift |
|--------|---------------------|-------------------|--------|
| 1 (top) | 35% | 8% | +27pp |
| 2 | 28% | 10% | +18pp |
| 3 | 22% | 12% | +10pp |
| ... | ... | ... | ... |
| 10 (bottom) | 5% | 12% | -7pp |

Good model: High uplift in top deciles, low/negative in bottom.

### 4. Cumulative Gain

Total incremental conversions from targeting top X%.

---

## Practical Considerations

### 1. Randomized Control Group is Essential

Uplift modeling REQUIRES data from randomized experiments where:
- Some customers received treatment
- Some customers didn't (control)
- Assignment was random

Without randomization, uplift estimates are biased.

### 2. Sample Size Requirements

Need sufficient data in both treatment AND control groups.
Treatment effects are differences - requires more data than simple prediction.

**Rule of thumb**: At least 10,000 in each group for reliable estimates.

### 3. Feature Engineering

Good features for uplift often differ from response modeling:
- Past response to promotions
- Price sensitivity indicators
- Competitive purchase behavior
- Channel preferences
- Engagement patterns

### 4. Avoiding Negative Uplift Customers

Sleeping Dogs can actively harm business:
- Feel annoyed by contact
- Perceive brand as desperate
- Cheaper positioning hurts brand image

Model should identify and EXCLUDE these customers.

---

## L'Oreal India Uplift Use Cases

### 1. Discount Targeting
Who should receive the 20% off coupon?

### 2. Email Frequency
Who benefits from weekly vs monthly emails?

### 3. Channel Recommendation
Who converts better with beauty advisor vs self-service?

### 4. Product Recommendation
Who will buy recommended product they wouldn't discover otherwise?

### 5. Retention Intervention
Who will churn without intervention but stay with outreach?

### 6. Loyalty Program
Who will increase spending with loyalty enrollment?

---

## Key Takeaways

1. **Uplift = Incremental Effect**, not just positive outcome
2. **Persuadables are the target** - customers who change behavior due to treatment
3. **Sure Things waste budget** - they buy anyway
4. **Sleeping Dogs hurt** - treatment drives them away
5. **Requires randomized data** - need treatment and control groups
6. **Different from response modeling** - predicts change, not level
7. **Dramatically improves ROI** - 2-3x improvement common
8. **Evaluate with uplift curves** - not standard classification metrics

---

## Uplift Modeling Checklist

Before building:
- [ ] Have randomized experiment data?
- [ ] Sufficient sample size in treatment AND control?
- [ ] Clear definition of treatment and outcome?
- [ ] Business metric to optimize (revenue, conversion, retention)?

Model building:
- [ ] Chose appropriate method (T-Learner, S-Learner, etc.)?
- [ ] Included relevant features?
- [ ] Handled class imbalance appropriately?

Evaluation:
- [ ] Computed uplift by decile?
- [ ] Plotted Qini curve?
- [ ] Calculated cumulative gain?
- [ ] Identified Sleeping Dogs?

Deployment:
- [ ] Set targeting threshold?
- [ ] Excluded negative uplift customers?
- [ ] Planned holdout for ongoing measurement?
- [ ] Monitoring for model drift?
