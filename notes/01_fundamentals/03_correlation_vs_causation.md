# Correlation vs Causation: The Complete Comparison

## The Fundamental Question

When we observe that two things happen together, we must ask:
- Are they just moving together by coincidence?
- Is one causing the other?
- Is something else causing both?

---

## Side-by-Side Comparison

| Aspect | Correlation | Causation |
|--------|-------------|-----------|
| Definition | Two variables move together | One variable produces change in another |
| Symbol | X ~ Y | X -> Y |
| Symmetry | Symmetric (X~Y = Y~X) | Asymmetric (X->Y != Y->X) |
| Evidence | Observational data sufficient | Requires intervention or careful design |
| Statement | "X and Y are related" | "X makes Y happen" |
| Action implication | Predict Y from X | Change X to change Y |
| Business use | Forecasting | Decision making |
| Risk of misuse | Confusing with causation | Assuming mechanism exists |

---

## L'Oreal India: Complete Example

### The Observation

L'Oreal India marketing team presents this data:

| Region | Influencer Posts | Monthly Sales (Cr) |
|--------|-----------------|-------------------|
| Mumbai | 150 | 45 |
| Delhi | 120 | 38 |
| Bangalore | 100 | 32 |
| Chennai | 80 | 28 |
| Kolkata | 60 | 22 |
| Hyderabad | 90 | 30 |

**Correlation**: r = 0.97 (very strong)

**Marketing Team's Claim**: "Influencer marketing causes sales. We should invest heavily in influencers."

### Breaking Down the Possibilities

**Possibility 1: Influencers Cause Sales (X -> Y)**
```
Influencer Post -> Customer Sees -> Buys Product
```
If true: Increasing influencer posts will increase sales.

**Possibility 2: Sales Cause Influencer Activity (Y -> X)**
```
High Sales -> Buzzworthy Products -> Influencers Naturally Post
```
If true: Popular products attract influencer attention organically.

**Possibility 3: Common Cause (Z -> X and Z -> Y)**
```
                   -> Influencer Posts
Large Market Size
                   -> High Sales
```
If true: Big cities have both more influencers AND more buyers. Influencer posts don't cause sales.

**Possibility 4: Complex Relationship**
```
Market Size -> More Influencers -> Some Sales
     |
     +------> Direct Sales (unrelated to influencers)
```
If true: Influencers have small effect, most sales are from market size.

### How to Determine True Relationship

**Test 1: Hold Market Size Constant**
Compare influencer effect within similar-sized markets.

| City Pair | Influencer Posts | Sales | Market Size |
|-----------|-----------------|-------|-------------|
| Pune | 40 | 15 Cr | Similar |
| Ahmedabad | 80 | 16 Cr | Similar |

Doubling influencer posts increased sales by only 7%, not 100%.

**Test 2: Natural Experiment**
An influencer campaign was delayed in Hyderabad due to approval issues.

| Period | Hyderabad (No Campaign) | Chennai (Campaign) |
|--------|------------------------|-------------------|
| Before | 28 Cr | 27 Cr |
| After | 29 Cr | 32 Cr |

Chennai gained 5 Cr more, suggesting some causal effect.

**Test 3: Time Series Analysis**
Do sales increase AFTER influencer posts, or are they simultaneous?

| Week | Influencer Posts | Sales |
|------|-----------------|-------|
| 1 | 20 | 5 Cr |
| 2 | 50 (campaign) | 5.2 Cr |
| 3 | 10 | 7 Cr |
| 4 | 10 | 6.5 Cr |
| 5 | 10 | 5.5 Cr |

Sales increase AFTER posts, with decay. Suggests causation.

### Conclusion

Original correlation: r = 0.97 (influencers explain 94% of sales variation)
True causal effect: Influencers explain ~15-20% of sales variation

Most of the correlation was due to market size (confounder).

---

## Common Correlation-Causation Traps

### Trap 1: The Survivor Bias Correlation

**Observation**: Successful L'Oreal products have extensive testing.
**Wrong Conclusion**: More testing causes success.
**Reality**: We only see successful tested products. Failed tested products were killed. Testing doesn't guarantee success.

### Trap 2: The Reverse Causation Trap

**Observation**: Stores with more shelf space have more sales.
**Wrong Conclusion**: Get more shelf space to increase sales.
**Reality**: High sales earn more shelf space (retailers give space to what sells).

### Trap 3: The Selection Effect Trap

**Observation**: Premium customers who receive personal calls spend more.
**Wrong Conclusion**: Personal calls cause more spending.
**Reality**: Only high-value customers get calls; they already spent more.

### Trap 4: The Trending Together Trap

**Observation**: L'Oreal's digital ad spend and e-commerce sales both grew 2020-2023.
**Wrong Conclusion**: Digital ads drove e-commerce growth.
**Reality**: COVID drove both trends. Everything moved online.

---

## Decision Framework

When you see a correlation, run through this checklist:

### Step 1: Acknowledge the Correlation
"X and Y are correlated with r = ___"

### Step 2: List Possible Explanations
- [ ] X causes Y
- [ ] Y causes X  
- [ ] Z causes both X and Y (list possible Zs)
- [ ] Coincidence
- [ ] Selection bias

### Step 3: Check Temporality
- Does X consistently precede Y?
- Is the time gap plausible for the mechanism?

### Step 4: Identify Confounders
What variables could affect BOTH X and Y?

### Step 5: Look for Natural Experiments
Were there situations where X changed but confounders stayed same?

### Step 6: Consider an Experiment
Can we randomly assign X to test its effect on Y?

### Step 7: Estimate Causal Effect
After controlling for confounders, what is the true effect size?

---

## L'Oreal India Decision Matrix

| Business Question | Correlation Found | Potential Confounders | Causal Test Needed |
|------------------|-------------------|----------------------|-------------------|
| Do TV ads increase sales? | r = 0.85 | Season, competitor activity | Geo-randomized test |
| Do discounts drive volume? | r = 0.72 | Price-sensitive customer selection | Randomized promotion |
| Does fast delivery improve retention? | r = 0.65 | Premium customers get priority | A/B test delivery speeds |
| Do beauty advisors increase basket size? | r = 0.78 | High-traffic stores get advisors | Random advisor assignment |
| Does app usage increase spending? | r = 0.60 | Tech-savvy = affluent customers | New user experiment |

---

## Red Flags: When Correlation is Misused

Watch for these statements:

| Red Flag Statement | Problem |
|-------------------|---------|
| "Studies show X is linked to Y" | Linked means correlated, not caused |
| "X explains 80% of variance in Y" | R-squared is correlation, not causation |
| "Regions with more X have more Y" | Ecological correlation, not individual effect |
| "Users who do X are 3x more likely to Y" | Selection bias likely |
| "Since we started X, Y has improved" | Other things changed too |

---

## Key Takeaways

1. **Correlation is easy to find, causation is hard to prove**
2. **Most business correlations have confounders** (especially market size, seasonality, customer segments)
3. **The true causal effect is usually smaller than the correlation suggests**
4. **Ask "What else could explain this?" before acting on correlations**
5. **Natural experiments and A/B tests reveal true causation**
6. **Decisions based on correlation alone often fail when implemented**

---

## Summary Table

| If you want to... | Use Correlation | Need Causation |
|------------------|-----------------|----------------|
| Predict next month's sales | Yes | No |
| Decide where to invest budget | No | Yes |
| Identify related metrics | Yes | No |
| Change a business outcome | No | Yes |
| Build an ML forecast model | Yes | No |
| Design an intervention | No | Yes |
| Monitor business health | Yes | No |
| Attribute credit to channels | No | Yes |

Understanding this distinction is the foundation of all causal modeling work.
