# Treatment Effect

## Definition

Treatment effect is the causal impact of an intervention (treatment) on an outcome. It measures how much the outcome changes BECAUSE of the treatment, compared to what would have happened without it.

```
Treatment Effect = Outcome with Treatment - Outcome without Treatment
                 = Factual Outcome - Counterfactual Outcome
```

---

## Types of Treatment Effects

### 1. Individual Treatment Effect (ITE)

The effect of treatment on a SINGLE unit (customer, store, product).

**L'Oreal Example**:
- Customer Priya received 20% discount
- She bought Rs 2,000 worth of products
- Without discount, she would have bought Rs 1,200 (counterfactual)
- ITE for Priya = 2,000 - 1,200 = Rs 800

**Problem**: We cannot observe individual counterfactuals. ITE is fundamentally unobservable.

### 2. Average Treatment Effect (ATE)

The average effect across ALL units in the population.

**L'Oreal Example**:
Average effect of discount across ALL customers (including those who wouldn't respond).

```
ATE = E[Y(1)] - E[Y(0)]
    = Expected outcome if everyone treated - Expected outcome if no one treated
```

If L'Oreal gave discount to ALL customers:
- Average spend with discount: Rs 1,500
- Average spend without discount: Rs 1,200
- ATE = Rs 300

### 3. Average Treatment Effect on the Treated (ATT)

The average effect on units that ACTUALLY received treatment.

**L'Oreal Example**:
Effect of discount on customers who actually got the discount.

```
ATT = E[Y(1) - Y(0) | Treated]
    = Average effect among those who received treatment
```

Among customers who received discount:
- Average spend with discount: Rs 1,800
- What they would have spent without: Rs 1,300
- ATT = Rs 500

**Note**: ATT > ATE if treatment is given to those who benefit more.

### 4. Average Treatment Effect on the Untreated (ATU)

What would happen if we gave treatment to those currently not treated.

**L'Oreal Example**:
"If we expand discount program to customers not currently getting it, what effect would we see?"

```
ATU = E[Y(1) - Y(0) | Untreated]
```

This is crucial for deciding whether to expand a program.

---

## L'Oreal India: Complete Treatment Effect Analysis

### Scenario: Beauty Advisor Program

L'Oreal wants to know: "What is the effect of placing a beauty advisor in a store?"

### Data

| Store Group | Number | With Advisor Sales | Without Advisor Sales (Counterfactual) |
|-------------|--------|-------------------|----------------------------------------|
| Currently has advisor | 200 | Rs 45L/month | Rs 38L/month (estimated) |
| Never had advisor | 500 | N/A | Rs 25L/month |
| If given advisor | 500 | Rs 30L/month (estimated) | N/A |

### Calculating Different Effects

**ATT (Effect on stores that have advisors)**:
```
ATT = 45L - 38L = Rs 7L per month per store
```
Interpretation: Stores with advisors gain Rs 7L/month because of the advisor.

**ATU (Effect if we give advisors to stores without)**:
```
ATU = 30L - 25L = Rs 5L per month per store
```
Interpretation: Adding advisors to new stores would gain Rs 5L/month.

**ATE (Average effect across all stores)**:
```
ATE = (200 * 7L + 500 * 5L) / 700 = Rs 5.6L per month per store
```

**Why ATT > ATU?**
- High-potential stores already got advisors (selection)
- Remaining stores have lower potential
- Expanding program has diminishing returns

---

## Heterogeneous Treatment Effects

Treatment effects vary across different segments. Understanding this heterogeneity is crucial for targeting.

### L'Oreal India Example: Discount Effectiveness by Segment

| Customer Segment | With Discount | Without Discount | Treatment Effect |
|-----------------|---------------|------------------|------------------|
| Premium loyal | Rs 3,000 | Rs 2,800 | Rs 200 (7%) |
| Occasional buyer | Rs 1,500 | Rs 800 | Rs 700 (88%) |
| Price sensitive | Rs 1,200 | Rs 400 | Rs 800 (200%) |
| Competitor loyal | Rs 500 | Rs 100 | Rs 400 (400%) |
| Non-buyer | Rs 200 | Rs 0 | Rs 200 |

### Insights

1. **Premium loyal**: Small effect - they buy anyway
2. **Occasional buyer**: Large effect - discount triggers purchase
3. **Price sensitive**: Largest absolute effect
4. **Competitor loyal**: Discount helps switch, but from low base
5. **Non-buyer**: Small effect - not interested regardless

### Optimal Targeting

If discount costs Rs 300 per customer:

| Segment | Effect | Cost | Net Benefit | Target? |
|---------|--------|------|-------------|---------|
| Premium loyal | 200 | 300 | -100 | No |
| Occasional | 700 | 300 | +400 | Yes |
| Price sensitive | 800 | 300 | +500 | Yes |
| Competitor loyal | 400 | 300 | +100 | Maybe |
| Non-buyer | 200 | 300 | -100 | No |

---

## Conditional Average Treatment Effect (CATE)

Treatment effect conditioned on observable characteristics.

```
CATE(x) = E[Y(1) - Y(0) | X = x]
```

### L'Oreal Example: CATE by Region

| Region | CATE of TV Ad (Sales Lift) |
|--------|---------------------------|
| North India | +12% |
| South India | +18% |
| West India | +15% |
| East India | +8% |

**Insight**: Same TV ad has different effects across regions. South India responds best.

### CATE by Customer Characteristics

| Age Group | Income | CATE of Influencer Marketing |
|-----------|--------|------------------------------|
| 18-25 | High | +25% |
| 18-25 | Low | +15% |
| 26-35 | High | +12% |
| 26-35 | Low | +8% |
| 36-45 | High | +5% |
| 36-45 | Low | +3% |

**Insight**: Young, high-income customers respond most to influencers.

---

## Estimating Treatment Effects

### Method 1: Randomized Experiment (Gold Standard)

Randomly assign treatment to ensure treated and control groups are comparable.

**L'Oreal Example**:
- Randomly select 1,000 customers for discount
- Keep 1,000 similar customers as control
- Treatment effect = Average(discount group) - Average(control group)

### Method 2: Matching

Match treated units with similar untreated units.

**L'Oreal Example**:
For each customer who got discount:
- Find similar customer (age, income, history) who didn't
- Compare outcomes

### Method 3: Regression Adjustment

Control for confounders in a regression model.

**L'Oreal Example**:
```
Sales = b0 + b1*Discount + b2*Age + b3*Income + b4*Region + error
```
b1 estimates treatment effect after controlling for confounders.

### Method 4: Propensity Score Methods

Estimate probability of treatment, then use to adjust.

**L'Oreal Example**:
1. Predict P(discount) from customer features
2. Weight/match based on propensity scores
3. Compare outcomes

### Method 5: Instrumental Variables

Use an instrument that affects treatment but not outcome directly.

**L'Oreal Example**:
- Instrument: Random promotion code distribution
- Affects: Who uses discount
- Does not affect: Purchase amount directly

---

## Treatment Effect Decomposition

### Direct vs Indirect Effects

**L'Oreal Example: Beauty Advisor Effect**

```
                    -> Immediate purchase (+Rs 500)
Beauty Advisor -> 
                    -> Product knowledge -> Future purchases (+Rs 200)
```

Total effect: Rs 700
Direct effect: Rs 500 (immediate purchase)
Indirect effect: Rs 200 (through knowledge)

### Short-term vs Long-term Effects

**L'Oreal Example: Discount Effect Over Time**

| Period | With Discount | Without Discount | Effect |
|--------|---------------|------------------|--------|
| Month 1 (discount) | Rs 2,000 | Rs 1,000 | +Rs 1,000 |
| Month 2 | Rs 800 | Rs 1,100 | -Rs 300 |
| Month 3 | Rs 900 | Rs 1,000 | -Rs 100 |
| Cumulative | Rs 3,700 | Rs 3,100 | +Rs 600 |

**Insight**: 
- Short-term effect: +Rs 1,000
- Long-term cumulative effect: +Rs 600
- Some purchase was pulled forward, not incremental

---

## Key Metrics Derived from Treatment Effects

### 1. Incremental Sales
```
Incremental Sales = Treatment Effect * Number Treated
```

**L'Oreal Example**:
- ATT = Rs 500/customer
- Customers treated = 100,000
- Incremental sales = Rs 5 Crores

### 2. Return on Investment (ROI)
```
ROI = Incremental Revenue / Treatment Cost
```

**L'Oreal Example**:
- Incremental sales: Rs 5 Cr
- Discount cost: Rs 2 Cr
- ROI = 5/2 = 2.5x

### 3. Number Needed to Treat (NNT)
```
NNT = 1 / Treatment Effect Rate
```

**L'Oreal Example**:
- Conversion rate with discount: 15%
- Conversion rate without: 10%
- Treatment effect: 5 percentage points
- NNT = 1/0.05 = 20

We need to discount 20 customers to get 1 incremental purchase.

---

## Key Takeaways

1. **Treatment effect = Treated outcome - Counterfactual** - requires estimating what would have happened
2. **ATE** is average effect on everyone; **ATT** is effect on those actually treated
3. **Treatment effects are heterogeneous** - different segments respond differently
4. **CATE** allows targeting interventions to segments with highest effect
5. **ATT often exceeds ATU** because treatments are given to high-potential units first
6. **Long-term effects may differ from short-term** due to pull-forward and habit formation
7. **Randomization is the gold standard** for unbiased treatment effect estimation

---

## Summary Table

| Term | Definition | L'Oreal Example |
|------|------------|-----------------|
| ITE | Individual effect | Effect on one customer |
| ATE | Average effect on all | Effect if all customers got discount |
| ATT | Effect on treated | Effect on customers who got discount |
| ATU | Effect on untreated | Effect if non-discounted customers got discount |
| CATE | Effect by segment | Effect varies by age, region, income |

Understanding treatment effects is fundamental to measuring intervention success and optimizing business decisions.
