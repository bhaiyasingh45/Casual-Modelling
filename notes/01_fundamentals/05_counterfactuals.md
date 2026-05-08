# Counterfactuals

## Definition

A counterfactual is an answer to the question: "What would have happened if things had been different?" It describes an alternative reality where a specific action or event did NOT occur (or occurred differently).

Counterfactual thinking is the highest level of causal reasoning - it requires imagining what would have happened in a parallel universe.

---

## The Fundamental Question

For any treatment/intervention:

**Factual**: What actually happened after the treatment?
**Counterfactual**: What would have happened WITHOUT the treatment?

The difference between these two is the TRUE causal effect.

```
Causal Effect = Factual Outcome - Counterfactual Outcome
```

---

## L'Oreal India Example: The Diwali Campaign

### Scenario

L'Oreal India ran a massive Diwali campaign in 2025:
- TV ads across all channels
- Influencer partnerships
- Heavy discounts
- In-store promotions

**October 2025 Sales**: Rs 150 Crores

### The Counterfactual Question

"What would October 2025 sales have been if we had NOT run the Diwali campaign?"

### Why This is Hard

We cannot observe the counterfactual. We cannot go back in time and NOT run the campaign. We only see ONE version of reality.

```
Reality (Factual):    Campaign -> Rs 150 Cr sales
Counterfactual:       No Campaign -> ??? 
```

### Possible Counterfactual Estimates

**Method 1: Last Year's Diwali**
October 2024 sales: Rs 120 Cr
Campaign effect estimate: 150 - 120 = Rs 30 Cr

**Problem**: Market grew. Maybe sales would have been Rs 130 Cr even without campaign.

**Method 2: Pre-Campaign Trend**
August sales: Rs 80 Cr
September sales: Rs 90 Cr
Projected October (no campaign): Rs 100 Cr
Campaign effect estimate: 150 - 100 = Rs 50 Cr

**Problem**: Diwali always increases sales. Would have been higher even without campaign.

**Method 3: Control Region**
Suppose we didn't run campaign in Northeast India:
- Northeast October sales: Rs 8 Cr (no campaign)
- Northeast October 2024: Rs 6 Cr
- Growth without campaign: 33%

Apply 33% growth to rest of India:
- Expected (no campaign): Rs 120 Cr x 1.33 = Rs 160 Cr
- Wait, that's MORE than actual... something is wrong.

**Problem**: Northeast is not comparable to rest of India.

**Method 4: Synthetic Control**
Build a "synthetic" India using weighted combination of:
- L'Oreal sales in other countries
- Competitor sales in India
- Historical patterns

Estimated counterfactual: Rs 115 Cr
Campaign effect: 150 - 115 = Rs 35 Cr

This is more sophisticated but still an estimate.

---

## The Fundamental Problem of Causal Inference

We can NEVER directly observe the counterfactual. This is called the "Fundamental Problem of Causal Inference."

For any individual unit (customer, store, product):
- If treated: We observe treated outcome, cannot observe untreated outcome
- If not treated: We observe untreated outcome, cannot observe treated outcome

```
Customer A received discount -> Bought (What if no discount?)
Customer B received no discount -> Didn't buy (What if discount?)
```

---

## Approaches to Estimate Counterfactuals

### 1. Randomized Experiments (A/B Tests)

Create two equivalent groups:
- Treatment group: Gets the intervention
- Control group: Does not get intervention

The control group serves as the counterfactual for the treatment group.

**L'Oreal Example**: 
- 10,000 customers get discount email (treatment)
- 10,000 similar customers get regular email (control)
- Control group outcome = counterfactual for treatment group

### 2. Before-After Comparison

Use the same unit's past as the counterfactual.

**L'Oreal Example**:
- Store sales before beauty advisor: Rs 30L/month
- Store sales after beauty advisor: Rs 40L/month
- Counterfactual (no advisor) = Rs 30L/month

**Problem**: Other things change over time (seasonality, trends).

### 3. Difference-in-Differences

Combine treatment/control with before/after.

**L'Oreal Example**:
| | Before | After | Change |
|---|--------|-------|--------|
| Treatment stores (got advisors) | 30L | 40L | +10L |
| Control stores (no advisors) | 25L | 30L | +5L |

- Treatment group change: +10L
- Control group change: +5L (this is the counterfactual trend)
- Advisor effect: 10L - 5L = 5L

### 4. Matching

Find similar untreated units to serve as counterfactuals.

**L'Oreal Example**:
For each customer who got a discount:
- Find a similar customer (same age, income, purchase history) who didn't
- The non-discounted customer's behavior = counterfactual

### 5. Synthetic Control

Create a weighted combination of control units to match treatment unit.

**L'Oreal Example**:
To estimate "What would Maharashtra sales be without the campaign?":
- Use Gujarat (40%), Rajasthan (30%), MP (30%)
- Weight them to match Maharashtra's pre-campaign trends
- The synthetic control's post-campaign sales = counterfactual

---

## L'Oreal India: Customer-Level Counterfactuals

### The Individual Customer Problem

**Customer Profile**:
- Priya, 28, Mumbai
- Bought L'Oreal serum after seeing Instagram ad
- Paid Rs 1,500

**Counterfactual Questions**:

1. "Would Priya have bought WITHOUT the Instagram ad?"
   - Maybe she was already planning to buy
   - Maybe she would have discovered it in store
   
2. "Would Priya have bought without the discount?"
   - Maybe she would have paid full price
   - Maybe she would have bought competitor product

3. "Would Priya have bought ANYTHING if she hadn't bought the serum?"
   - Maybe her budget was fixed
   - Maybe she would have bought a competitor serum

### Why Individual Counterfactuals Matter

**Attribution**: If Priya would have bought anyway, the ad gets NO credit.
**Incrementality**: Only the customers who would NOT have bought are incremental.
**ROI**: True ROI = Revenue from incremental customers / Ad spend

---

## Counterfactual Reasoning Framework

### Step 1: Define the Intervention
What specific action are we evaluating?

**L'Oreal Example**: "15% discount on Revitalift range in September"

### Step 2: Define the Counterfactual
What is the alternative scenario?

**L'Oreal Example**: "No discount on Revitalift range in September"

### Step 3: Identify the Outcome
What metric are we measuring?

**L'Oreal Example**: "Revitalift unit sales in September"

### Step 4: Estimate the Counterfactual
What would the outcome have been in the alternative scenario?

**L'Oreal Example**: "Based on August sales trend and similar products without discount, estimated 8,000 units"

### Step 5: Calculate Causal Effect
Factual - Counterfactual = Effect

**L'Oreal Example**: "Actual: 12,000 units. Counterfactual: 8,000 units. Discount effect: 4,000 incremental units"

---

## Common Counterfactual Mistakes

### Mistake 1: Assuming Zero Counterfactual

**Wrong**: "Campaign generated Rs 150 Cr sales"
**Reality**: Sales would not be zero without campaign

**Correct**: "Campaign generated Rs 35 Cr INCREMENTAL sales (150 - 115 counterfactual)"

### Mistake 2: Using Wrong Comparison Period

**Wrong**: "Sales in campaign month vs non-campaign month"
**Reality**: Months differ in many ways beyond campaign

**Correct**: Use control group or synthetic control for same time period

### Mistake 3: Ignoring Cannibalization

**Wrong**: "Promotion drove 10,000 units"
**Reality**: Some customers pulled forward purchases from next month

**Correct**: Look at cumulative sales over longer period

### Mistake 4: Ignoring Spillovers

**Wrong**: "Maharashtra campaign impact = Maharashtra sales increase"
**Reality**: Campaign may have increased sales in neighboring Gujarat too

**Correct**: Account for geographic spillover effects

---

## Key Takeaways

1. **Counterfactuals are unobservable** - we can only estimate them
2. **Causal effect = Factual - Counterfactual** - both are needed
3. **The fundamental problem of causal inference** prevents direct observation
4. **Randomized experiments** create valid counterfactuals through control groups
5. **Observational methods** (DiD, matching, synthetic control) estimate counterfactuals
6. **Never assume zero counterfactual** - something would have happened anyway
7. **Individual counterfactuals determine incrementality** - would this person have bought anyway?

---

## Summary Table

| Question Type | Counterfactual Form |
|--------------|---------------------|
| Did the campaign work? | What would sales be without campaign? |
| Did the discount help? | Would customer buy at full price? |
| Did the advisor matter? | Would customer buy without advice? |
| Did fast delivery help retention? | Would customer return with slow delivery? |
| Did the new channel help? | Would these sales happen in existing channels? |

Counterfactual thinking is essential for all causal inference and forms the foundation of methods we will learn next.
