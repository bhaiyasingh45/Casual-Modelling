# Confounders (Confounding Variables)

## Definition

A confounder is a variable that influences BOTH the treatment (cause) and the outcome (effect), creating a spurious association between them. Confounders are the primary reason why correlation does not imply causation.

---

## Visual Representation

```
        Confounder (Z)
           /    \
          /      \
         v        v
    Treatment    Outcome
       (X)         (Y)
```

The confounder Z affects both X and Y, making it appear that X causes Y even when there is no direct relationship.

---

## L'Oreal India Example: The Classic Confounder

### Scenario: Promotion and Sales

**Observation**: Products on promotion have 50% higher sales than products not on promotion.

**Naive Conclusion**: Promotions cause 50% sales lift.

**The Hidden Confounder: Product Popularity**

```
        Product Popularity
           /         \
          /           \
         v             v
    Put on Promotion   High Sales
```

**Reality**:
- Marketing team promotes products that are ALREADY selling well
- Popular products would have high sales even without promotion
- The promotion effect is much smaller than 50%

### Data Breakdown

| Product Type | On Promotion | Not on Promotion | Difference |
|--------------|--------------|------------------|------------|
| Popular SKUs | 100 units | 80 units | +25% |
| Average SKUs | 50 units | 40 units | +25% |
| Slow SKUs | 20 units | 15 units | +33% |

**Overall (confounded)**: Promoted products sell 100 vs 30 (unpromoted average) = +233%

**True promotion effect**: ~25-33% (after accounting for baseline popularity)

---

## Types of Confounders

### 1. Observed Confounders
Variables we can measure and account for.

**L'Oreal Example**: 
- Region (different regions have different baseline demand)
- Season (Diwali affects both ad spend and sales)
- Store size (larger stores get more promotions AND more sales)

### 2. Unobserved Confounders
Variables we cannot measure but affect the relationship.

**L'Oreal Example**:
- Customer intent (customers already planning to buy visit promoted aisles)
- Word of mouth (cannot measure but affects both awareness and sales)
- Competitor stockouts (drives customers to L'Oreal without our knowledge)

---

## Common Confounders in Retail/Beauty Industry

### 1. Seasonality

**How it confounds**:
- Diwali: Both marketing spend and sales increase
- Summer: Both sunscreen ads and sunscreen sales increase
- Wedding season: Both makeup campaigns and makeup sales increase

**L'Oreal Example**:
```
        Diwali Season
           /       \
          /         \
         v           v
    High Ad Spend    High Sales
```

Without controlling for season, we overestimate ad effectiveness.

### 2. Customer Segment

**How it confounds**:
- Premium customers: Get personalized service AND spend more
- Young customers: Use digital channels AND have different product preferences
- Urban customers: Have access to EBOs AND higher purchasing power

**L'Oreal Example**:
```
        Customer Income
           /         \
          /           \
         v             v
    Uses Premium      Buys More
    Salon Channel     Products
```

Premium channels appear more effective, but it is the customer, not the channel.

### 3. Geography

**How it confounds**:
- Metro cities: Have more stores AND more customers
- Coastal regions: Have humidity (hair issues) AND beauty-conscious population
- South India: Higher education AND higher beauty product usage

**L'Oreal Example**:
```
        Metro City
          /     \
         /       \
        v         v
    More Stores   More Sales
```

Store count correlates with sales, but causation is limited.

### 4. Time Trends

**How it confounds**:
- E-commerce growing: Both digital ads and online sales trending up
- Beauty awareness increasing: Both marketing effectiveness and demand rising
- Economic growth: Both disposable income and beauty spending rising

**L'Oreal Example**:
```
        Post-COVID Digital Shift
              /         \
             /           \
            v             v
    Digital Ad Spend     E-comm Sales
       Increase          Increase
```

Both grew due to the shift, not because ads caused sales.

---

## How to Handle Confounders

### Method 1: Stratification
Analyze within subgroups where confounder is constant.

**L'Oreal Application**:
Instead of: "Do promotions increase sales?"
Do: "Do promotions increase sales within Tier-1 cities during non-festive months?"

| Stratum | Promoted Sales | Non-Promoted Sales | Lift |
|---------|---------------|-------------------|------|
| Tier-1, Non-festive | 80 | 65 | 23% |
| Tier-1, Festive | 150 | 120 | 25% |
| Tier-2, Non-festive | 45 | 38 | 18% |
| Tier-2, Festive | 90 | 72 | 25% |

True promotion effect: ~20-25% (not the confounded 50%)

### Method 2: Statistical Adjustment
Include confounders as control variables in regression.

**L'Oreal Application**:
```
Sales = b0 + b1*Promotion + b2*Region + b3*Season + b4*StoreSize + error
```

The coefficient b1 now represents promotion effect AFTER controlling for confounders.

### Method 3: Matching
Compare promoted products only to similar non-promoted products.

**L'Oreal Application**:
For each promoted SKU, find a non-promoted SKU with:
- Same category
- Same price range
- Same region
- Same baseline sales velocity

Compare only these matched pairs.

### Method 4: Randomization
Randomly assign treatment to eliminate confounding.

**L'Oreal Application**:
- Randomly select 50 similar stores for promotion
- Keep 50 similar stores as control
- Confounders are balanced by randomization

---

## Identifying Confounders: The Framework

Ask these questions for any X -> Y relationship:

### Question 1: What affects X (the treatment)?
List all factors that determine who/what gets the treatment.

**For promotions at L'Oreal**:
- Product popularity (popular items get promoted)
- Margin (high-margin items get promoted)
- Inventory (overstocked items get promoted)
- Season (festive times have more promotions)
- Competitor activity (responding to competitor deals)

### Question 2: Which of these also affect Y (the outcome)?
Of the factors above, which also affect sales?

- Product popularity -> affects sales (CONFOUNDER)
- Margin -> may not directly affect unit sales
- Inventory -> if stockout prevented, affects sales (CONFOUNDER)
- Season -> affects sales (CONFOUNDER)
- Competitor activity -> affects sales (CONFOUNDER)

### Question 3: Can we measure these confounders?
- Product popularity: Yes (past sales data)
- Season: Yes (calendar)
- Competitor activity: Partially (visible promotions)
- Customer intent: No (unobserved)

---

## Real L'Oreal India Confounder Analysis

### Case: Beauty Advisor Effectiveness

**Question**: Do beauty advisors increase sales?

**Naive Analysis**:
- Stores with beauty advisors: Rs 50L/month
- Stores without: Rs 30L/month
- Apparent effect: +67%

**Confounder Identification**:

| Factor | Affects Advisor Assignment? | Affects Sales? | Confounder? |
|--------|---------------------------|----------------|-------------|
| Store footfall | Yes (high traffic stores get advisors) | Yes | Yes |
| Store location (mall vs standalone) | Yes | Yes | Yes |
| City tier | Yes | Yes | Yes |
| Store age | Yes | Yes | Yes |
| Product assortment | Possibly | Yes | Maybe |

**Adjusted Analysis** (controlling for store footfall):

| Footfall Bucket | With Advisor | Without Advisor | Effect |
|-----------------|--------------|-----------------|--------|
| High (>500/day) | Rs 55L | Rs 48L | +15% |
| Medium (200-500) | Rs 35L | Rs 30L | +17% |
| Low (<200) | Rs 18L | Rs 15L | +20% |

**True Effect**: ~15-20% (not 67%)

---

## The Danger of Unobserved Confounders

Even after controlling for observed confounders, unobserved ones remain.

### L'Oreal Example: Marketing Mix Modeling

**Observed confounders controlled**:
- Season
- Price
- Distribution
- Competitor activity

**Unobserved confounders still present**:
- Consumer trends (K-beauty trend affecting demand)
- Social media virality (not captured in paid media data)
- Product quality improvements
- Regulatory changes (ingredient bans affecting competitors)

**Implication**: Causal estimates from observational data are always uncertain due to potential unobserved confounders.

---

## Key Takeaways

1. **Confounders create false correlations** between treatment and outcome
2. **Identify confounders by asking**: "What affects both the treatment AND the outcome?"
3. **Observed confounders** can be controlled through stratification, regression, or matching
4. **Unobserved confounders** require randomized experiments or advanced methods
5. **Business decisions based on confounded analysis** often fail when implemented
6. **The true causal effect is usually smaller** than the naive correlation suggests
7. **Randomization is the gold standard** for eliminating confounding

---

## Summary: Confounder Checklist

Before claiming X causes Y, verify:

- [ ] Listed all factors that affect X (treatment assignment)
- [ ] Identified which of these also affect Y (confounders)
- [ ] Separated observed vs unobserved confounders
- [ ] Controlled for observed confounders in analysis
- [ ] Acknowledged limitations from unobserved confounders
- [ ] Compared adjusted effect to naive effect
- [ ] Considered whether randomized experiment is needed for confident conclusion
