# Root Cause Analysis vs Causal Modeling

## Overview

These two approaches are often confused but serve different purposes:

| Aspect | Root Cause Analysis (RCA) | Causal Modeling |
|--------|--------------------------|-----------------|
| Question | "Why did this specific problem happen?" | "What is the effect of X on Y in general?" |
| Direction | Backward-looking (diagnose past) | Forward-looking (predict interventions) |
| Scope | Single incident or anomaly | Population-level relationships |
| Output | Specific cause of specific problem | Quantified causal effect |
| Use case | Troubleshooting, incident response | Decision making, optimization |

---

## Root Cause Analysis (RCA)

### Definition
A systematic process to identify the underlying cause of a specific problem or incident. The goal is to find what went wrong and prevent recurrence.

### When to Use RCA
- Sales dropped suddenly in a region
- A campaign performed worse than expected
- Product returns spiked
- Customer complaints increased
- A specific metric deviated from normal

### RCA Methodology

**The 5 Whys Technique**

Start with the problem and ask "why" repeatedly until you reach the root cause.

**L'Oreal Example: Sales Drop in Tamil Nadu**

**Problem**: Tamil Nadu sales dropped 30% in March 2025.

- **Why 1**: Why did sales drop?
  - Because fewer units were sold in modern trade channel.

- **Why 2**: Why were fewer units sold in modern trade?
  - Because products were out of stock at major retailers.

- **Why 3**: Why were products out of stock?
  - Because replenishment orders were not fulfilled.

- **Why 4**: Why were orders not fulfilled?
  - Because the regional warehouse had inventory shortage.

- **Why 5**: Why did the warehouse have shortage?
  - Because demand forecast underestimated March sales due to early Tamil New Year.

**Root Cause**: Forecasting model did not account for shifting festival dates.

**Solution**: Update forecast model to include variable festival calendar.

### Fishbone Diagram (Ishikawa)

Categorizes potential causes into groups.

**L'Oreal Example: Low Campaign Performance**

```
                    People              Process
                      |                    |
        Inexperienced team    Late launch timing
              |                        |
              +------------------------+
                         |
                    [Low Campaign ROI]
                         |
              +------------------------+
              |                        |
    Wrong audience targeting    Budget cuts mid-campaign
              |                    |
                    Product              External
```

**Categories to explore**:
- People: Team capabilities, training
- Process: Workflow, timing, approvals
- Product: Quality, relevance, pricing
- External: Competition, economy, weather

---

## Causal Modeling

### Definition
A framework for quantifying the causal effect of one variable on another across a population. The goal is to understand "if we change X, what happens to Y?"

### When to Use Causal Modeling
- Should we increase ad spend?
- What is the ROI of promotions?
- Does fast delivery improve retention?
- Which channel drives the most incremental sales?
- How much would sales change if we cut price?

### Causal Modeling Methodology

**L'Oreal Example: Effect of Beauty Advisors on Sales**

**Question**: What is the causal effect of having a beauty advisor on store sales?

**Approach**:

1. **Define Treatment**: Presence of beauty advisor (yes/no)
2. **Define Outcome**: Monthly store sales
3. **Identify Confounders**: Store size, location, footfall, product assortment
4. **Build DAG**:
```
    Store Location
         |
         v
    Store Footfall -> Beauty Advisor Assignment
         |                    |
         v                    v
    Baseline Potential -> Actual Sales
```

5. **Choose Method**: Propensity score matching
6. **Estimate Effect**: Compare matched stores with/without advisors
7. **Result**: Beauty advisors increase sales by Rs 5 Lakhs/month (95% CI: 3-7 Lakhs)

---

## Key Differences

### 1. Specificity of Question

**RCA**: "Why did Store #127 in Chennai have 40% sales drop in March?"
- Specific store, specific time, specific problem

**Causal Modeling**: "What is the effect of stockouts on sales across all stores?"
- General relationship, population-level

### 2. Direction of Analysis

**RCA**: Works backward from effect to cause
```
Effect (Sales drop) <- Cause (Stockout) <- Cause (Forecast error)
```

**Causal Modeling**: Works forward from cause to effect
```
Cause (Ad Spend) -> Effect (Awareness) -> Effect (Sales)
```

### 3. Data Requirements

**RCA**: 
- Detailed investigation of single incident
- Qualitative data (interviews, logs, observations)
- Timeline of events

**Causal Modeling**:
- Large dataset with many observations
- Variation in treatment (some exposed, some not)
- Measured confounders

### 4. Output Format

**RCA**: 
- Narrative explanation
- Specific corrective action
- Prevention measures

**Causal Modeling**:
- Quantified effect size with uncertainty
- Statistical confidence
- Actionable coefficient (e.g., "each Rs 1 Lakh ad spend -> Rs 5 Lakh sales")

---

## L'Oreal India: Side-by-Side Comparison

### Scenario: Promotion Effectiveness

**RCA Approach**:
"The Buy-2-Get-1 promotion in February underperformed. Why?"

Investigation:
1. Timing coincided with competitor mega-sale
2. Communication reached customers late
3. Participating stores had limited inventory
4. Promotional display was not prominent

Root cause: Poor execution and timing, not promotion concept itself.

Action: Improve coordination for next promotion.

**Causal Modeling Approach**:
"What is the average effect of Buy-2-Get-1 promotions on sales?"

Analysis:
1. Collect data from 100 promotions across 2 years
2. Control for season, competition, baseline sales
3. Use difference-in-differences methodology
4. Result: B2G1 promotions increase sales by 18% on average (95% CI: 12-24%)

Action: Continue B2G1 promotions, budget for 18% lift.

### When Each is Appropriate

| Situation | Use RCA | Use Causal Modeling |
|-----------|---------|---------------------|
| February promotion failed | Yes | No |
| Should we run more B2G1 promos? | No | Yes |
| Why did Chennai warehouse have stockout? | Yes | No |
| What is effect of stockouts on sales? | No | Yes |
| App crashed during sale event | Yes | No |
| Does app usage increase customer spend? | No | Yes |

---

## Complementary Use

### RCA Informs Causal Modeling

**Example**: RCA reveals that stockouts cause sales drops.
Causal modeling then quantifies: "How much do stockouts reduce sales?"

### Causal Modeling Prioritizes RCA

**Example**: Causal model shows price is biggest sales driver.
RCA then investigates: "Why is our pricing suboptimal in South India?"

### Combined Workflow

```
1. Monitor KPIs
       |
       v
2. Anomaly detected (sales drop)
       |
       v
3. RCA: Why did this happen?
       |
       v
4. Root cause identified (stockout)
       |
       v
5. Causal modeling: What is effect of stockouts generally?
       |
       v
6. Decision: Invest in inventory management
       |
       v
7. Intervention: Improve forecasting system
       |
       v
8. Causal evaluation: Did intervention work?
```

---

## Tools Comparison

### RCA Tools
- 5 Whys
- Fishbone diagram
- Fault tree analysis
- Timeline analysis
- Pareto analysis

### Causal Modeling Tools
- DAGs (Directed Acyclic Graphs)
- Regression with controls
- Propensity score matching
- Difference-in-differences
- Instrumental variables
- DoWhy, EconML, CausalML (Python libraries)

---

## Common Mistakes

### Mistake 1: Using RCA for Causal Inference

**Wrong**: "RCA showed stockout caused sales drop in Store #127, therefore stockouts reduce sales by 40%"

**Problem**: Single incident doesn't establish general effect size.

**Correct**: Use causal modeling across many stores to estimate average effect.

### Mistake 2: Using Causal Modeling for Incident Investigation

**Wrong**: "Our model shows ads increase sales by 15%, so the campaign failure must be due to something else"

**Problem**: Average effects don't explain specific incidents.

**Correct**: Use RCA to investigate why this specific campaign deviated from average.

### Mistake 3: Confusing Correlation with Root Cause

**Wrong RCA**: "Sales dropped when competition launched product. Competition caused our drop."

**Problem**: Assumes correlation = causation without investigation.

**Correct**: Investigate mechanism - did customers actually switch? Check sales by segment.

### Mistake 4: Ignoring Confounders in RCA

**Wrong RCA**: "We added beauty advisor, sales went up. Advisor was the cause."

**Problem**: Maybe sales would have gone up anyway (new product launch, season change).

**Correct**: Consider what else changed during the same period.

---

## L'Oreal Decision Framework

### When a Problem Occurs

```
Is it a one-time incident or recurring pattern?
        |
        +-- One-time: Use RCA
        |     - Why did THIS happen?
        |     - Prevent recurrence
        |
        +-- Recurring: Use Causal Modeling
              - What is the general effect?
              - What intervention would help?
```

### When Planning an Intervention

```
Do we understand the causal mechanism?
        |
        +-- No: Use Causal Modeling first
        |     - Quantify expected effect
        |     - Identify optimal target
        |
        +-- Yes: Implement and monitor
              - Track performance
              - Use RCA if underperforms
```

---

## Key Takeaways

1. **RCA answers "Why did this happen?"** - backward-looking, specific incident
2. **Causal modeling answers "What is the effect of X?"** - forward-looking, general relationship
3. **RCA is qualitative** (narrative), causal modeling is **quantitative** (numbers)
4. **RCA finds root causes** of problems, causal modeling **estimates effect sizes**
5. **Both are complementary** - RCA identifies what to model, models prioritize RCA
6. **Don't use RCA for causal inference** - single incidents don't prove general effects
7. **Don't use causal modeling for incident investigation** - averages don't explain specific cases

---

## Summary Table

| Feature | Root Cause Analysis | Causal Modeling |
|---------|--------------------|-----------------| 
| Question type | Diagnostic | Predictive |
| Time orientation | Past | Future |
| Scope | Single incident | Population |
| Primary output | Explanation | Effect estimate |
| Data type | Qualitative + Quantitative | Quantitative |
| Key tools | 5 Whys, Fishbone | DAGs, Statistical methods |
| Business use | Troubleshooting | Strategy & Optimization |
