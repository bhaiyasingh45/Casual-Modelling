# Causation

## Definition

Causation means that one event (the cause) directly produces or influences another event (the effect). Unlike correlation, causation implies a directional, mechanistic relationship where changing the cause will change the effect.

---

## The Core Difference

| Aspect | Correlation | Causation |
|--------|-------------|-----------|
| Direction | Symmetric (A~B = B~A) | Directional (A->B != B->A) |
| Manipulation | Observing together | Changing one affects other |
| Inference | "A and B move together" | "A makes B happen" |
| Evidence needed | Data association | Intervention or experiment |

---

## Criteria for Establishing Causation

### Bradford Hill Criteria (Adapted for Business)

1. **Strength of Association**: Strong correlation is suggestive (but not proof)
2. **Consistency**: Effect is reproducible across different settings
3. **Specificity**: Cause leads to specific effect
4. **Temporality**: Cause precedes effect
5. **Biological/Logical Gradient**: More cause leads to more effect (dose-response)
6. **Plausibility**: Mechanism makes logical sense
7. **Coherence**: Fits with existing knowledge
8. **Experiment**: Manipulation of cause changes effect
9. **Analogy**: Similar causes have similar effects

---

## L'Oreal India Example

### Scenario: TV Advertisement Impact

**Question**: Does TV advertising CAUSE sales to increase?

### Testing Causation

**1. Temporality**
- Ad runs in Week 1
- Sales increase measured in Weeks 2-4
- Check: Cause (ad) precedes effect (sales) ✓

**2. Mechanism**
- Customer sees ad -> becomes aware of product -> visits store -> purchases
- Check: Logical pathway exists ✓

**3. Dose-Response**
- 10% more ad spend -> 5% more sales
- 20% more ad spend -> 9% more sales
- Check: More cause leads to more effect ✓

**4. Consistency**
- Effect observed in North India
- Effect observed in South India
- Effect observed across multiple years
- Check: Reproducible ✓

**5. Experiment**
- Run ad in Maharashtra, not in Gujarat (similar markets)
- Compare sales difference
- Check: Controlled test ✓

---

## Types of Causal Relationships

### 1. Direct Causation
X directly causes Y with no intermediate steps.

**L'Oreal Example**: 
Price reduction -> Immediate sales increase
(Direct effect on purchase decision)

### 2. Indirect Causation
X causes Y through intermediate variable Z.

**L'Oreal Example**:
TV Ad -> Brand Awareness -> Store Visit -> Purchase
(Ad doesn't directly cause purchase, but initiates a chain)

### 3. Bidirectional Causation
X causes Y and Y causes X (feedback loop).

**L'Oreal Example**:
High Sales -> More Shelf Space -> Even Higher Sales
(Success breeds more success)

### 4. Common Cause (Confounding)
Z causes both X and Y, creating false appearance of X->Y.

**L'Oreal Example**:
Diwali Season -> More Ad Spend AND More Sales
(Season drives both, ads don't necessarily cause sales)

---

## The Intervention Test

The gold standard for causation is: **If we change X, does Y change?**

### L'Oreal Intervention Example

**Hypothesis**: Beauty advisor recommendations cause higher sales.

**Observational Data**:
- Stores with beauty advisors: Rs 50 lakh/month sales
- Stores without beauty advisors: Rs 30 lakh/month sales
- Correlation suggests advisors help

**Problem**: Maybe high-traffic stores get both more advisors AND more sales.

**Intervention Test**:
- Take 20 similar stores (same traffic, same location type)
- Randomly assign 10 to get beauty advisors
- Keep 10 without advisors
- Compare sales after 3 months

**Result**:
- Stores with advisors: Rs 42 lakh/month
- Stores without: Rs 35 lakh/month
- Causal effect of advisor: Rs 7 lakh/month

This is the true causal impact, not the Rs 20 lakh difference we saw in observational data.

---

## Why Causal Thinking Matters

### Business Decision Example

**Scenario**: L'Oreal observes that customers who use the mobile app spend 40% more.

**Correlation-based Decision**: "Push everyone to use the app to increase spending"

**Causal Thinking**: Wait, do they spend more BECAUSE of the app, or do big spenders just prefer the app?

**Investigation Reveals**:
- App users were already premium customers
- App adoption did not cause spending increase
- Pushing casual buyers to app had no effect on their spending

**Causal Effect of App**: Only 8% increase (not 40%)

**Better Decision**: Focus app promotion on segments where it actually changes behavior.

---

## The Ladder of Causation (Judea Pearl)

### Level 1: Association (Seeing)
"What is?" - Observing correlations

**L'Oreal Example**: "Customers who bought shampoo also bought conditioner"

### Level 2: Intervention (Doing)
"What if?" - Predicting effects of actions

**L'Oreal Example**: "If we bundle shampoo with conditioner, will basket size increase?"

### Level 3: Counterfactual (Imagining)
"What would have been?" - Reasoning about alternatives

**L'Oreal Example**: "Would this customer have bought without the discount?"

---

## Challenges in Establishing Causation

### 1. Confounding Variables

**Problem**: Hidden factors affect both cause and effect.

**L'Oreal Example**: 
- Observed: Influencer posts correlate with sales
- Hidden confounder: Both happen during product launches
- Reality: Launch drives both, not influencer causing sales

### 2. Reverse Causation

**Problem**: Effect actually causes the cause.

**L'Oreal Example**:
- Observed: High ratings correlate with high sales
- Assumed: Ratings cause sales
- Reality: High sales lead to more reviews, improving ratings

### 3. Selection Bias

**Problem**: The groups being compared are fundamentally different.

**L'Oreal Example**:
- Observed: Loyalty program members buy 3x more
- Assumed: Program causes more buying
- Reality: Frequent buyers self-select into program

---

## Framework for Causal Reasoning

When someone claims X causes Y, ask:

1. **Is there correlation?** (Necessary but not sufficient)
2. **Does X precede Y?** (Temporal order)
3. **Is there a mechanism?** (How would it work?)
4. **Are there confounders?** (What else could explain this?)
5. **Is there experimental evidence?** (Has it been tested?)
6. **Is it consistent?** (Does it replicate?)

---

## Key Takeaways

1. Causation requires more than correlation - it needs mechanism and intervention
2. The intervention test is the gold standard: change X, observe Y
3. Confounders create false causal appearances
4. Reverse causation is a common trap
5. Selection bias makes groups incomparable
6. Causal thinking prevents costly business mistakes
7. Always ask "What else could explain this relationship?"

---

## Practical Applications at L'Oreal India

| Question | Correlational Answer | Causal Investigation |
|----------|---------------------|---------------------|
| Do ads work? | Ad spend ~ sales | A/B test in similar markets |
| Do discounts help? | Promo sales are higher | Would they buy anyway? |
| Do advisors matter? | Advised customers buy more | Random advisor assignment |
| Does delivery speed matter? | Fast delivery ~ repeat purchase | Test speed in similar areas |

Moving forward, we will learn techniques to establish causation from observational data when experiments are not possible.
