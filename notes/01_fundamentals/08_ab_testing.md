# A/B Testing

## Definition

A/B testing (also called split testing or randomized controlled trial) is an experimental method where two or more variants are randomly assigned to users/units to determine which performs better on a given metric. It is the gold standard for establishing causation.

---

## Why A/B Testing is Powerful

A/B testing solves the fundamental problem of causal inference through randomization:

| Challenge | How A/B Testing Solves It |
|-----------|--------------------------|
| Confounders | Random assignment balances confounders across groups |
| Selection bias | Users don't self-select into treatment |
| Counterfactual | Control group serves as counterfactual |
| Temporal effects | Both groups experience same time period |

---

## Anatomy of an A/B Test

### 1. Control Group (A)
The baseline experience - no change from current state.

### 2. Treatment Group (B)
The variant being tested - the change we want to evaluate.

### 3. Randomization
Each unit has equal probability of being in A or B.

### 4. Primary Metric
The main outcome we're measuring (KPI).

### 5. Sample Size
Number of units in each group.

### 6. Duration
How long the test runs.

---

## L'Oreal India: A/B Test Example

### Business Question
Does adding product reviews to the e-commerce page increase conversion?

### Test Design

**Control (A)**: Current product page without reviews
**Treatment (B)**: Product page with customer reviews section

**Randomization**: 
- Every visitor to L'Oreal India website
- 50% see version A, 50% see version B
- Assigned randomly by cookie

**Primary Metric**: Conversion rate (purchases / visitors)

**Secondary Metrics**:
- Average order value
- Time on page
- Add to cart rate
- Return rate (long-term)

**Sample Size**: 50,000 visitors per group

**Duration**: 2 weeks

### Results

| Metric | Control (A) | Treatment (B) | Difference | P-value |
|--------|-------------|---------------|------------|---------|
| Visitors | 52,341 | 51,876 | - | - |
| Conversions | 1,047 | 1,245 | +198 | - |
| Conversion Rate | 2.00% | 2.40% | +0.40pp | 0.003 |
| Avg Order Value | Rs 1,850 | Rs 1,920 | +Rs 70 | 0.12 |

### Interpretation
- Reviews increased conversion by 0.4 percentage points (20% relative lift)
- This is statistically significant (p = 0.003)
- Average order value increased but not significantly
- Recommendation: Implement reviews feature

---

## A/B Testing Process

### Phase 1: Planning

**Step 1: Define Hypothesis**
```
H0: Reviews have no effect on conversion
H1: Reviews increase conversion
```

**Step 2: Choose Metrics**
- Primary: Conversion rate (decision will be based on this)
- Secondary: AOV, time on page (for learning)
- Guardrail: Site speed, error rate (shouldn't get worse)

**Step 3: Calculate Sample Size**
Based on:
- Baseline conversion rate: 2%
- Minimum detectable effect: 0.3 percentage points (15% relative)
- Significance level: 5%
- Power: 80%

Formula result: ~45,000 visitors per variant

**Step 4: Determine Duration**
- Daily traffic: 10,000 visitors
- Sample needed: 90,000 total
- Duration: ~9-14 days (account for day-of-week effects)

### Phase 2: Execution

**Step 5: Implement Variants**
- Build version A (control)
- Build version B (treatment)
- Set up randomization logic

**Step 6: Quality Assurance**
- Verify random assignment is working
- Check tracking is accurate
- Confirm no bugs in either variant

**Step 7: Launch**
- Start with small traffic (5%) to catch issues
- Ramp to full traffic once stable

**Step 8: Monitor**
- Check for data quality issues
- Watch guardrail metrics
- Don't peek at results for decision (leads to false positives)

### Phase 3: Analysis

**Step 9: Statistical Analysis**
- Calculate conversion rates
- Run hypothesis test
- Compute confidence intervals

**Step 10: Interpret Results**
- Statistical significance?
- Practical significance?
- Consistent across segments?

**Step 11: Decision**
- Ship treatment
- Keep control
- Run follow-up test

---

## Common A/B Test Scenarios at L'Oreal India

### 1. Website/App Tests

| Test | Control | Treatment | Metric |
|------|---------|-----------|--------|
| Homepage layout | Current | New design | Engagement |
| Product page | Without reviews | With reviews | Conversion |
| Checkout flow | 4 steps | 2 steps | Completion |
| Search results | Relevance ranking | Personalized | Click-through |

### 2. Marketing Tests

| Test | Control | Treatment | Metric |
|------|---------|-----------|--------|
| Email subject | Standard | Personalized | Open rate |
| Ad creative | Image A | Image B | Click rate |
| Landing page | Generic | Segment-specific | Conversion |
| Offer | 10% off | Free shipping | Response |

### 3. Pricing Tests

| Test | Control | Treatment | Metric |
|------|---------|-----------|--------|
| Price point | Rs 999 | Rs 899 | Revenue/customer |
| Discount depth | 15% off | 20% off | Incremental profit |
| Bundle pricing | Individual | Bundle deal | Units per order |

### 4. Operational Tests

| Test | Control | Treatment | Metric |
|------|---------|-----------|--------|
| Delivery promise | 5-7 days | 3-5 days | Conversion |
| Returns policy | 7 days | 15 days | Purchase rate |
| Packaging | Standard | Premium | NPS, repeat |

---

## Randomization Unit

### User-Level Randomization
Each user is assigned to one variant consistently.

**L'Oreal Example**: Customer sees same homepage version across visits.

**Pros**: Clean measurement, good user experience
**Cons**: Slower to reach sample size

### Session-Level Randomization
Each session may see different variant.

**L'Oreal Example**: Same customer might see different product page layouts.

**Pros**: Faster to reach sample size
**Cons**: Confusing user experience, harder to analyze

### Region/Store-Level Randomization
Geographic regions or stores are assigned to variants.

**L'Oreal Example**: Maharashtra stores get new display, Gujarat stores keep current.

**Pros**: Only option for physical interventions
**Cons**: Fewer units, regional confounders possible

---

## A/B Testing Pitfalls

### Pitfall 1: Peeking at Results
Looking at results before planned duration and making early decisions.

**Problem**: Increases false positive rate dramatically.

**L'Oreal Example**:
- Day 3: Treatment winning by 0.3pp (p = 0.04)
- Decision: "It's significant! Ship it!"
- Day 14 (if waited): Difference narrowed to 0.1pp (p = 0.35)
- Reality: No real effect, early result was noise

**Solution**: Set duration in advance, don't peek for decisions.

### Pitfall 2: Multiple Comparisons
Testing many variants or metrics increases false positives.

**L'Oreal Example**:
Testing 10 different button colors. At 5% significance:
- Expected false positives: 0.5
- One shows significant - but likely false positive

**Solution**: Correct for multiple testing (Bonferroni, FDR).

### Pitfall 3: Selection Bias in Analysis
Analyzing only users who completed the journey.

**L'Oreal Example**:
Comparing conversion among users who clicked "Add to Cart":
- Ignores that treatment may have had more add-to-carts
- Biased comparison

**Solution**: Analyze all randomized users (intent-to-treat).

### Pitfall 4: Novelty Effects
Initial results don't reflect long-term behavior.

**L'Oreal Example**:
New feature gets high engagement initially because it's new.
After 2 weeks, engagement drops to baseline.

**Solution**: Run tests long enough to pass novelty phase.

### Pitfall 5: Contamination
Users in control group exposed to treatment effects.

**L'Oreal Example**:
Testing influencer campaign - but control users follow same influencers.

**Solution**: Use geographic or other clean separation when needed.

---

## A/B Test Analysis

### Step 1: Check Randomization Quality

| Metric | Control | Treatment | Expected |
|--------|---------|-----------|----------|
| Sample Size | 52,341 | 51,876 | ~Equal |
| % Mobile | 68% | 67% | ~Equal |
| % New Users | 45% | 46% | ~Equal |
| Avg Past Purchases | 2.3 | 2.4 | ~Equal |

If groups differ significantly on pre-treatment characteristics, randomization may have failed.

### Step 2: Calculate Effect Size

```
Effect = Treatment Rate - Control Rate
       = 2.40% - 2.00%
       = 0.40 percentage points

Relative Lift = (2.40 - 2.00) / 2.00 = 20%
```

### Step 3: Statistical Significance

```
Standard Error = sqrt(p*(1-p)*(1/n1 + 1/n2))
               = sqrt(0.022*0.978*(1/52341 + 1/51876))
               = 0.00129

Z-score = 0.004 / 0.00129 = 3.10
P-value = 0.002
```

### Step 4: Confidence Interval

```
95% CI = Effect +/- 1.96 * SE
       = 0.40% +/- 1.96 * 0.129%
       = [0.15%, 0.65%]
```

The true effect is likely between 0.15 and 0.65 percentage points.

### Step 5: Segment Analysis

| Segment | Control | Treatment | Effect | P-value |
|---------|---------|-----------|--------|---------|
| Mobile | 1.8% | 2.3% | +0.5pp | 0.01 |
| Desktop | 2.5% | 2.7% | +0.2pp | 0.25 |
| New Users | 1.2% | 1.8% | +0.6pp | 0.005 |
| Returning | 3.1% | 3.3% | +0.2pp | 0.40 |

Insight: Reviews help more on mobile and for new users.

---

## A/B Testing vs Observational Studies

| Aspect | A/B Test | Observational |
|--------|----------|---------------|
| Causation | Can establish | Cannot establish |
| Confounders | Balanced by randomization | Must control statistically |
| Selection bias | Eliminated | Often present |
| Cost | Requires implementation | Uses existing data |
| Time | Must wait for experiment | Can analyze immediately |
| External validity | Limited to test context | Broader but biased |

---

## When A/B Testing is Not Possible

### Ethical Constraints
Cannot randomly withhold beneficial treatments.

**L'Oreal Example**: Cannot deny customer service to test its impact.

### Operational Constraints
Cannot separate treatment and control.

**L'Oreal Example**: TV ad seen by everyone in the region.

### Sample Size Constraints
Not enough units for statistical power.

**L'Oreal Example**: Only 20 stores in a region - too few to randomize.

### Alternatives
- Quasi-experiments
- Natural experiments
- Difference-in-differences
- Regression discontinuity

---

## Key Takeaways

1. **A/B testing is the gold standard** for causal inference through randomization
2. **Random assignment** balances confounders between groups
3. **Sample size** must be calculated in advance based on expected effect
4. **Don't peek** at results before planned duration
5. **Statistical significance** is necessary but not sufficient - check practical impact
6. **Segment analysis** reveals heterogeneous effects
7. **Guardrail metrics** ensure no unintended harm
8. **Not always possible** - need alternatives for some questions

---

## A/B Testing Checklist

Before launching:
- [ ] Clear hypothesis documented
- [ ] Primary metric defined
- [ ] Sample size calculated
- [ ] Duration determined
- [ ] Randomization unit chosen
- [ ] Randomization verified working
- [ ] No interaction with other tests
- [ ] Guardrail metrics identified

After completion:
- [ ] Randomization balance checked
- [ ] Statistical significance calculated
- [ ] Confidence intervals reported
- [ ] Segment analysis performed
- [ ] Practical significance evaluated
- [ ] Long-term effects considered
- [ ] Decision documented
