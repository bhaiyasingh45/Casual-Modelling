# Selection Bias

## Definition

Selection bias occurs when the groups being compared are systematically different in ways that affect the outcome. This makes it impossible to attribute differences in outcomes to the treatment alone.

**Core Problem**: The treated and untreated groups are not comparable.

---

## Why Selection Bias Matters

```
Observed Difference = True Treatment Effect + Selection Bias

If selection bias != 0, observed difference is misleading.
```

---

## L'Oreal India Example: The Loyalty Program Trap

### Observation
L'Oreal's loyalty program members spend 3x more than non-members.

| Group | Annual Spend |
|-------|--------------|
| Loyalty Members | Rs 9,000 |
| Non-Members | Rs 3,000 |

**Naive Conclusion**: "The loyalty program causes 3x increase in spending!"

### The Selection Bias Problem

Who joins the loyalty program?
- Customers who ALREADY buy frequently
- Customers who ALREADY spend more
- Customers who ALREADY prefer L'Oreal

```
Selection Mechanism:
High Spenders -> More Likely to Join -> Appear in "Members" group
Low Spenders -> Less Likely to Join -> Appear in "Non-Members" group
```

### The Reality

| Customer Segment | Joined Loyalty? | Spending |
|-----------------|-----------------|----------|
| High-value (would spend Rs 8,500 anyway) | 90% join | Rs 9,000 |
| Medium-value (would spend Rs 4,000 anyway) | 40% join | Rs 4,500 |
| Low-value (would spend Rs 2,000 anyway) | 5% join | Rs 2,200 |

**True loyalty program effect**: ~Rs 500-1,000 increase
**Observed difference**: Rs 6,000 (mostly selection bias!)

---

## Types of Selection Bias

### 1. Self-Selection Bias

People choose whether to receive treatment.

**L'Oreal Examples**:

| Treatment | Who Self-Selects | Bias Direction |
|-----------|------------------|----------------|
| Loyalty program | High spenders | Overestimate effect |
| Beauty advisor consultation | Interested customers | Overestimate effect |
| Premium products | Wealthy customers | Overestimate premium impact |
| Email newsletter | Engaged customers | Overestimate email effect |

### 2. Administrative Selection

Business decides who gets treatment.

**L'Oreal Examples**:

| Treatment | Selection Criteria | Bias Direction |
|-----------|-------------------|----------------|
| Discount offers | Price-sensitive customers | Underestimate discount impact |
| VIP service | High-value customers | Overestimate service effect |
| Store promotions | High-potential stores | Overestimate promotion effect |
| Influencer seeding | Trendsetter customers | Overestimate influencer effect |

### 3. Survivor Bias

Only successful cases are observed.

**L'Oreal Examples**:
- "Our product development process works - look at all successful launches!"
  - (Ignores products that failed testing and were never launched)
  
- "Stores that adopted new layout have higher sales!"
  - (Weak stores that tried and failed may have closed)

### 4. Attrition Bias

Different groups have different dropout rates.

**L'Oreal Example**:
Testing new skincare routine over 3 months:
- Customers who see results continue (treatment appears to work)
- Customers who don't see results quit (failures not counted)
- Result: Biased positive effect

---

## Detecting Selection Bias

### Method 1: Compare Baseline Characteristics

If treated and control groups differ on pre-treatment variables, selection bias exists.

**L'Oreal Example: Beauty Advisor Study**

| Characteristic | Stores with Advisors | Stores without |
|---------------|---------------------|----------------|
| Avg Monthly Footfall | 800 | 400 |
| Mall Location | 70% | 30% |
| Store Size (sqft) | 1,200 | 600 |
| City Tier | 85% Tier-1 | 45% Tier-1 |

Groups are clearly different. Selection bias is present.

### Method 2: Check Propensity for Treatment

If you can predict who gets treatment, there's selection.

**L'Oreal Example**:
Build model to predict "Which customers join loyalty program?"
- Model achieves 85% accuracy
- Means treatment assignment is predictable, not random
- Selection bias is present

### Method 3: Time Series Check

Did the outcome differ BEFORE treatment?

**L'Oreal Example: Loyalty Program**

| Month | Future Members | Future Non-Members |
|-------|---------------|-------------------|
| Jan (pre-launch) | Rs 700 | Rs 250 |
| Feb (pre-launch) | Rs 720 | Rs 240 |
| Mar (launch) | Rs 750 | Rs 250 |
| Apr (post-launch) | Rs 780 | Rs 260 |

Future members already spent more BEFORE the program launched!

---

## Handling Selection Bias

### 1. Randomized Experiments

Eliminate selection by randomly assigning treatment.

**L'Oreal Application**:
- Randomly invite customers to loyalty program
- Compare invitees who joined vs random control
- But: Can't force enrollment, still some self-selection

### 2. Matching

Match treated units with similar untreated units.

**L'Oreal Application**:
For each loyalty member, find a non-member with:
- Same age group
- Same geographic region
- Same spending history (pre-program)
- Same purchase frequency

Compare only matched pairs.

**Result**: Effect estimate drops from Rs 6,000 to Rs 800.

### 3. Propensity Score Methods

Model the probability of treatment and adjust.

**L'Oreal Application**:
1. Build model: P(Join Loyalty | Customer Features)
2. Weight observations by inverse propensity
3. Or match on propensity scores
4. Estimate treatment effect on balanced sample

### 4. Regression Control

Include selection factors as controls in regression.

**L'Oreal Application**:
```
Spending = b0 + b1*Loyalty_Member + b2*Baseline_Spending + b3*Age + b4*Region + error
```

b1 is the loyalty program effect AFTER controlling for selection factors.

### 5. Instrumental Variables

Find a variable that affects treatment but not outcome directly.

**L'Oreal Application**:
- Instrument: Random promotional mailing about loyalty program
- Affects: Likelihood of joining
- Doesn't affect: Spending directly (only through joining)

### 6. Regression Discontinuity

Exploit threshold rules for treatment assignment.

**L'Oreal Application**:
If loyalty program requires Rs 5,000 spending to join:
- Compare customers just above Rs 5,000 (eligible) vs just below (not eligible)
- Customers near threshold are similar
- Difference is causal effect

---

## L'Oreal India: Complete Selection Bias Analysis

### Case Study: Email Marketing Effectiveness

**Question**: Does email marketing increase purchases?

**Naive Analysis**:
- Customers receiving marketing emails: 25% purchase rate
- Customers not receiving emails: 8% purchase rate
- Apparent effect: +17 percentage points

**Selection Bias Investigation**:

**Who receives emails?**
- Customers who opted in (self-selection)
- Active customers (business selection)
- Customers with valid email (technical selection)

**Baseline Comparison**:

| Metric | Email Recipients | Non-Recipients |
|--------|-----------------|----------------|
| Past purchase frequency | 4.2/year | 1.1/year |
| Average order value | Rs 2,100 | Rs 1,200 |
| Website visits/month | 8 | 2 |
| Brand engagement score | High | Low |

Groups are fundamentally different!

**Addressing Selection Bias**:

Method: Propensity Score Matching
1. Model P(Receive Email | Customer Features)
2. Match each email recipient with similar non-recipient
3. Compare purchase rates in matched sample

**Results**:
- Matched email recipients: 22% purchase rate
- Matched non-recipients: 18% purchase rate
- Adjusted effect: +4 percentage points (not 17!)

**Conclusion**: Email marketing increases purchases by ~4 percentage points, not the 17pp naive estimate.

---

## Selection Bias in Common Business Contexts

### 1. Channel Comparison

**Biased**: "Customers from Nykaa have higher lifetime value than Amazon customers"
**Reality**: Beauty enthusiasts shop on Nykaa; general shoppers use Amazon

### 2. Product Performance

**Biased**: "Premium products have higher satisfaction scores"
**Reality**: Customers who buy premium are already brand advocates

### 3. Service Impact

**Biased**: "Customers who call support have higher retention"
**Reality**: Engaged customers call; disengaged just leave quietly

### 4. Training Effectiveness

**Biased**: "Employees who completed training have higher performance"
**Reality**: Motivated employees complete training; they would perform well anyway

---

## Key Takeaways

1. **Selection bias makes groups incomparable** - treated/untreated differ systematically
2. **Self-selection is most common** - people choose treatments that match preferences
3. **Always check baseline differences** - if groups differ pre-treatment, bias exists
4. **Observed differences overstate true effects** - usually by large amounts
5. **Randomization eliminates selection bias** - gold standard solution
6. **Matching and propensity scores help** - but require all confounders measured
7. **Survivor bias hides failures** - only seeing successes distorts picture
8. **Question every comparison** - ask "Why might these groups differ anyway?"

---

## Selection Bias Detection Checklist

Before trusting a treatment effect estimate:

- [ ] Who decides/chooses treatment assignment?
- [ ] Could treated units have been different anyway?
- [ ] Are baseline characteristics balanced?
- [ ] Did outcomes differ before treatment?
- [ ] Is treatment assignment predictable?
- [ ] Are there dropouts/attrition?
- [ ] Are failures visible or hidden?

If any answer raises concern, selection bias likely exists.

---

## Summary: Selection Bias Formula

```
Observed Difference = True Causal Effect + Selection Bias

Example:
Observed: Members spend Rs 6,000 more
Selection Bias: Rs 5,000 (high spenders join)
True Effect: Rs 1,000

Without correcting, we would overestimate by 6x!
```

Always decompose observed differences to isolate true causal effects.
