# Structural Causal Models (SCM)

## Definition

A Structural Causal Model (SCM) is a mathematical framework that combines:
1. A set of variables
2. A set of structural equations defining causal relationships
3. A probability distribution over exogenous (external) factors

SCMs provide a complete description of the data generating process and allow us to reason about interventions and counterfactuals.

---

## Components of an SCM

### 1. Endogenous Variables (V)
Variables determined within the system.

**L'Oreal Example**: Sales, Awareness, Price, Marketing Spend

### 2. Exogenous Variables (U)
External factors not explained by the model.

**L'Oreal Example**: Consumer trends, economic conditions, competitor actions

### 3. Structural Equations (F)
Functions that determine each endogenous variable.

```
V_i = f_i(Parents(V_i), U_i)
```

### 4. Probability Distribution P(U)
Distribution over exogenous variables.

---

## L'Oreal India: A Complete SCM

### Scenario: Sales Driver Model

**Endogenous Variables**:
- M = Marketing Spend
- A = Brand Awareness
- P = Price
- S = Sales

**Exogenous Variables**:
- U_M = Budget decisions, corporate strategy
- U_A = Organic word-of-mouth, PR
- U_P = Cost fluctuations, competition
- U_S = Unobserved demand factors

### Structural Equations

```
M = f_M(U_M)
    Marketing spend determined by corporate budget

A = f_A(M, U_A)
    Awareness depends on marketing and organic factors

P = f_P(U_P)
    Price determined by costs and competition

S = f_S(A, P, U_S)
    Sales depend on awareness, price, and unobserved demand
```

### Specific Functional Forms

```
M = U_M                           (exogenous)
A = 0.3 * M + U_A                 (awareness increases with marketing)
P = U_P                           (exogenous)
S = 50 * A - 10 * P + U_S         (sales increase with awareness, decrease with price)
```

### Graphical Representation (DAG)

```
U_M -> M -> A -> S <- P <- U_P
             ^         
             |         
            U_A       U_S
```

---

## SCM Operations

### 1. Observation (Conditioning)

What is the probability of an outcome given observed data?

```
P(S | M = 100)
```

**L'Oreal Question**: "What are typical sales when we observe marketing spend of Rs 100L?"

### 2. Intervention (do-operator)

What happens if we SET a variable to a specific value?

```
P(S | do(M = 100))
```

**L'Oreal Question**: "What would sales be if we SET marketing spend to Rs 100L?"

### 3. Counterfactual

What would have happened in a specific case if conditions were different?

```
P(S_x | M = 50, S = 200)

"Given that marketing was 50 and sales were 200, 
what would sales have been if marketing had been 100?"
```

**L'Oreal Question**: "Given that we spent Rs 50L on marketing and got Rs 200Cr sales last quarter, what would sales have been if we had spent Rs 100L?"

---

## Observation vs Intervention

### Why They Differ

**Observation**: P(S | M = 100)
- Includes cases where high marketing was chosen BECAUSE conditions favored high sales
- Confounded by U_M

**Intervention**: P(S | do(M = 100))
- Removes the natural selection mechanism
- Isolates pure causal effect

### L'Oreal Example

**Observation**: 
When we observe M = Rs 100L:
- Often during peak seasons (Diwali)
- Often in high-potential regions
- Often when demand signals are strong

**Average sales when M = 100L observed**: Rs 250 Cr
(But this includes favorable conditions)

**Intervention**:
If we SET M = Rs 100L regardless of conditions:
- Includes off-peak seasons
- Includes all regions equally
- Includes weak demand periods

**Average sales when M = 100L is set**: Rs 180 Cr
(Pure causal effect of marketing)

---

## Graphical Surgery for Intervention

To compute P(Y | do(X = x)):

1. Remove all arrows INTO X
2. Set X = x
3. Compute P(Y) in modified graph

### L'Oreal Example: Effect of Marketing on Sales

**Original Graph**:
```
U_M -> M -> A -> S
```

**After do(M = 100)**:
```
U_M    M=100 -> A -> S
```

U_M no longer affects M. M is fixed at 100.

**Calculation**:
```
P(S | do(M = 100))
= P(S | A) * P(A | M = 100)
= P(S | A) * P(A | M = 100)  (A follows from M = 100)
```

---

## Counterfactual Computation

### Three Steps for Counterfactuals

1. **Abduction**: Given observed data, infer exogenous variables
2. **Action**: Modify the model per the intervention
3. **Prediction**: Compute outcome in modified model

### L'Oreal Example: Counterfactual Analysis

**Observed**: In Q1, M = 50, A = 30, S = 200

**Question**: What would S have been if M = 100?

**Step 1: Abduction**
Given M = 50, A = 30, S = 200, infer U values:
```
A = 0.3 * M + U_A
30 = 0.3 * 50 + U_A
U_A = 30 - 15 = 15

S = 50 * A - 10 * P + U_S
200 = 50 * 30 - 10 * P + U_S
(Need to know P to solve)

Assume P = 100:
200 = 1500 - 1000 + U_S
U_S = -300
```

**Step 2: Action**
Set M = 100 (intervention)

**Step 3: Prediction**
With M = 100 and same U values:
```
A' = 0.3 * 100 + 15 = 45
S' = 50 * 45 - 10 * 100 + (-300)
S' = 2250 - 1000 - 300 = 950
```

**Counterfactual**: Sales would have been Rs 950 Cr instead of Rs 200 Cr.

---

## SCM for Common L'Oreal Questions

### Question 1: Marketing ROI

**Model**:
```
M -> A -> S
```

**Equation**: S = f(A) = f(g(M)) = f(g(M))

**Causal Effect**: dS/dM = (dS/dA) * (dA/dM)

**Interpretation**: Rs 1 additional marketing spend -> Rs X additional sales

### Question 2: Price Elasticity

**Model**:
```
P -> S
```

**Equation**: S = alpha - beta * P

**Causal Effect**: dS/dP = -beta

**Interpretation**: Rs 1 price increase -> beta units decrease in sales

### Question 3: Channel Cannibalization

**Model**:
```
Online_Presence -> Online_Sales
       |
       v
Offline_Sales
```

**Equation**: 
```
Online_Sales = f(Online_Presence)
Offline_Sales = g(Online_Sales) + h(Other_Factors)
```

**Causal Questions**:
- Direct effect of online on online sales
- Indirect (spillover) effect on offline sales
- Net effect (cannibalization or growth?)

---

## Identifiability

A causal effect is **identifiable** if it can be computed from observational data alone.

### When Effects are Identifiable

1. **No confounders**: Direct effect is identifiable
2. **Confounders observed**: Adjustment identifies effect
3. **Valid instrument exists**: IV methods identify effect
4. **Backdoor criterion satisfied**: Adjustment set exists

### When Effects are NOT Identifiable

1. **Unmeasured confounders** with no instruments
2. **Feedback loops** without time information
3. **Complete mediation** without variation in mediator

### L'Oreal Example: Identifiability Check

**Question**: Effect of beauty advisor on sales

**DAG**:
```
Store_Quality -> Has_Advisor -> Sales
      |                          ^
      +--------------------------+
```

**Confounder**: Store Quality (affects both advisor assignment and sales)

**Identifiable?** Yes, if Store_Quality is measured.

**Adjustment**: Control for Store_Quality

---

## SCM vs Other Frameworks

| Framework | What it provides | Limitations |
|-----------|------------------|-------------|
| Correlation | Association strength | No causal direction |
| Regression | Conditional expectations | Correlation, not causation |
| DAG | Causal structure | No equations, no counterfactuals |
| **SCM** | Full causal model | Requires correct specification |

SCM is the most complete framework, combining:
- DAG (causal structure)
- Equations (functional relationships)
- Probability (uncertainty)
- Counterfactuals (what-if reasoning)

---

## Building an SCM for L'Oreal

### Step 1: Define Scope
What is the causal question?
"Effect of marketing on sales across India"

### Step 2: List Variables
Endogenous: Marketing, Awareness, Consideration, Purchase, Sales
Exogenous: Economy, Competition, Weather, Trends

### Step 3: Determine Structure (DAG)
Based on domain knowledge:
```
Marketing -> Awareness -> Consideration -> Purchase -> Sales
                ^                            ^
                |                            |
            Competition                    Price
```

### Step 4: Specify Functional Forms
Linear, log-linear, or nonparametric?

```
Awareness = beta_1 * Marketing + beta_2 * Competition + U_A
Sales = beta_3 * Purchase - beta_4 * Price + U_S
```

### Step 5: Estimate Parameters
From data, estimate beta values.

### Step 6: Validate
- Does the model fit observed data?
- Are causal effects plausible?
- Do counterfactuals make sense?

### Step 7: Use for Decision Making
- Predict effect of interventions
- Compare alternative strategies
- Optimize marketing mix

---

## Key Takeaways

1. **SCM = DAG + Equations + Probability** - complete causal model
2. **Structural equations** define how variables are determined
3. **Observation != Intervention** - conditioning vs do-operator
4. **Counterfactuals** require abduction-action-prediction process
5. **Graphical surgery** removes arrows to compute interventions
6. **Identifiability** determines if effects can be computed from data
7. **SCMs enable** prediction, intervention, and counterfactual reasoning
8. **Correct specification** is crucial - wrong model gives wrong answers

---

## SCM Checklist

Building an SCM:
- [ ] Clearly defined causal question
- [ ] All relevant variables identified
- [ ] Causal structure (DAG) specified
- [ ] Functional forms chosen
- [ ] Exogenous variables defined
- [ ] Parameters estimated from data
- [ ] Model validated against observations
- [ ] Identifiability checked for target effects

Using an SCM:
- [ ] Correct operation used (observe vs intervene vs counterfactual)
- [ ] Graphical surgery applied correctly for interventions
- [ ] Counterfactuals computed via abduction-action-prediction
- [ ] Uncertainty quantified in estimates
- [ ] Sensitivity analysis for model assumptions
