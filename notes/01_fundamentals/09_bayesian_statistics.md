# Bayesian Statistics

## Definition

Bayesian statistics is a framework for updating beliefs based on evidence. Unlike frequentist statistics (which focuses on long-run frequencies), Bayesian statistics treats probability as a degree of belief that can be updated as new data arrives.

---

## The Core Formula: Bayes' Theorem

```
P(Hypothesis | Data) = P(Data | Hypothesis) * P(Hypothesis) / P(Data)
```

In plain terms:
```
Posterior = Likelihood * Prior / Evidence
```

| Term | Meaning | L'Oreal Example |
|------|---------|-----------------|
| Prior | Initial belief before seeing data | "We think 30% of customers respond to discounts" |
| Likelihood | Probability of data given hypothesis | "If 30% respond, what's chance of seeing this data?" |
| Posterior | Updated belief after seeing data | "After experiment, 35% likely respond to discounts" |
| Evidence | Total probability of the data | Normalizing constant |

---

## L'Oreal India Example: Updating Beliefs

### Scenario: New Product Launch Success Rate

L'Oreal India is launching a new serum. Based on historical data:
- 40% of new serums succeed (>10,000 units/month)
- 60% fail (<10,000 units/month)

### Prior Belief
```
P(Success) = 0.40
P(Failure) = 0.60
```

### New Evidence
After 2 weeks, early sales data shows strong performance.
- If product will succeed: 80% chance of strong early sales
- If product will fail: 20% chance of strong early sales (lucky start)

```
P(Strong Early Sales | Success) = 0.80
P(Strong Early Sales | Failure) = 0.20
```

### Applying Bayes' Theorem

Step 1: Calculate total probability of strong early sales
```
P(Strong Sales) = P(Strong | Success) * P(Success) + P(Strong | Failure) * P(Failure)
                = 0.80 * 0.40 + 0.20 * 0.60
                = 0.32 + 0.12
                = 0.44
```

Step 2: Calculate posterior probability
```
P(Success | Strong Sales) = P(Strong | Success) * P(Success) / P(Strong Sales)
                          = 0.80 * 0.40 / 0.44
                          = 0.32 / 0.44
                          = 0.727
```

### Updated Belief
After seeing strong early sales:
- P(Success) updated from 40% to 72.7%
- This is a rational update based on evidence

---

## Bayesian vs Frequentist

| Aspect | Frequentist | Bayesian |
|--------|-------------|----------|
| Probability | Long-run frequency | Degree of belief |
| Parameters | Fixed but unknown | Random variables with distributions |
| Prior information | Not used | Incorporated explicitly |
| Result | P(data given hypothesis) | P(hypothesis given data) |
| Interpretation | "If we repeated this, 5% would be false positives" | "There's 95% chance the effect is positive" |
| Sample size | Fixed in advance | Can update continuously |

---

## Key Bayesian Concepts

### 1. Prior Distribution
Your belief about a parameter before seeing data.

**L'Oreal Example: Conversion Rate**
- Past campaigns had conversion rates between 2-5%
- Prior: Conversion ~ Beta(20, 480) (centered at 4%)

**Types of Priors**:
- **Informative**: Strong belief based on past data
- **Weakly informative**: Some constraints but flexible
- **Uninformative/Flat**: No prior preference

### 2. Likelihood Function
The probability of observing the data given parameter values.

**L'Oreal Example**:
- If true conversion rate is 4%, what's the chance of seeing 45 conversions in 1000 visitors?
- Likelihood = Binomial(45 | n=1000, p=0.04)

### 3. Posterior Distribution
Updated belief after combining prior with data.

**L'Oreal Example**:
- Prior: Conversion ~ 4% (uncertainty: 2-5%)
- Data: 45 conversions in 1000 visitors (4.5%)
- Posterior: Conversion ~ 4.3% (uncertainty: 3.2-5.5%)

The posterior is narrower (less uncertain) because we have more information.

---

## L'Oreal India: Bayesian A/B Testing

### Traditional (Frequentist) A/B Test Result
```
Control: 2.0% conversion
Treatment: 2.4% conversion
P-value: 0.03
```
Interpretation: "Statistically significant at 5% level"

### Bayesian A/B Test Result
```
Control posterior: 2.0% (95% CI: 1.8% - 2.2%)
Treatment posterior: 2.4% (95% CI: 2.1% - 2.7%)
P(Treatment > Control): 97%
Expected lift: 0.4 percentage points
95% CI of lift: 0.1pp - 0.7pp
```

### Why Bayesian is More Intuitive

**Frequentist says**: "If there's no effect, there's 3% chance of seeing this data"
**Bayesian says**: "There's 97% chance treatment is better than control"

The Bayesian statement directly answers what we want to know.

---

## Bayesian Advantages for Business

### 1. Intuitive Probability Statements

**Frequentist**: "We reject the null at 5% significance"
**Bayesian**: "There's 95% probability the campaign increased sales"

Business stakeholders understand the Bayesian statement.

### 2. Incorporate Prior Knowledge

**L'Oreal Example**: 
"We know from 50 past campaigns that conversion lifts are usually 10-30%. This new campaign claims 200% lift - let's be skeptical."

The prior acts as regularization against extreme claims.

### 3. No Need for Fixed Sample Size

**Frequentist**: Must determine sample size before test; peeking inflates error
**Bayesian**: Can update beliefs continuously; decision based on posterior probability

**L'Oreal Example**:
- Day 3: P(Treatment better) = 75%... keep testing
- Day 7: P(Treatment better) = 90%... keep testing
- Day 10: P(Treatment better) = 97%... ship it

### 4. Direct Probability of Business Questions

**L'Oreal Question**: "What's the probability that ROI is positive?"

**Bayesian Answer**: Calculate from posterior distribution
- P(ROI > 0) = 92%
- P(ROI > 50%) = 78%
- P(ROI > 100%) = 45%

---

## Bayesian Inference in Practice

### Example: Estimating Campaign ROI

**Prior Information**:
- Past campaigns: Average ROI = 100%, SD = 50%
- Prior: ROI ~ Normal(100%, 50%)

**Campaign Data**:
- This campaign: Observed ROI = 150%
- Measurement uncertainty: SE = 30%

**Posterior Calculation**:
Combining prior and likelihood (weighted by precision):

```
Posterior mean = (Prior precision * Prior mean + Data precision * Data mean) / (Prior + Data precision)

Precision = 1/Variance

Prior precision = 1/(50^2) = 0.0004
Data precision = 1/(30^2) = 0.0011

Posterior mean = (0.0004 * 100 + 0.0011 * 150) / (0.0004 + 0.0011)
               = (0.04 + 0.165) / 0.0015
               = 137%

Posterior SD = sqrt(1/(0.0004 + 0.0011)) = 26%
```

**Result**: ROI is likely around 137% (95% CI: 86% - 188%)

The Bayesian estimate (137%) is between the prior (100%) and the data (150%), pulled toward prior due to uncertainty.

---

## Bayesian Networks for Causal Modeling

Bayesian networks combine:
- Directed graph showing causal relationships
- Probability distributions at each node
- Ability to update beliefs when observing data

### L'Oreal Example: Sales Drivers Network

```
                    Season
                      |
                      v
Ad Spend --------> Awareness --------> Sales
                      ^                  ^
                      |                  |
               Competitor Activity   Price
```

**Probability Tables**:
- P(Awareness | Ad Spend, Season, Competitor)
- P(Sales | Awareness, Price)

**Inference**:
- Observe: Sales are low
- Query: What's the probability Ad Spend is insufficient?
- Answer: P(Low Ad Spend | Low Sales) = Update using Bayes

---

## Prior Selection for L'Oreal Contexts

### For Conversion Rates
```
Prior: Beta(alpha, beta)
- Beta(1, 1): Uniform, no prior knowledge
- Beta(2, 50): Weak prior centered at ~4%
- Beta(20, 480): Strong prior centered at ~4% (based on historical)
```

### For Sales Lifts
```
Prior: Normal(mu, sigma)
- Normal(0, 10): Weakly skeptical of large effects
- Normal(0.15, 0.05): Informative, based on past campaigns
```

### For Binary Outcomes (Success/Failure)
```
Prior: Bernoulli(p)
- Based on historical success rates
```

---

## Bayesian Decision Making

### Expected Value Calculation

**L'Oreal Example**: Should we launch this campaign?

| Outcome | Probability | Value | Expected Value |
|---------|-------------|-------|----------------|
| Success (ROI > 100%) | 70% | +Rs 50L | +Rs 35L |
| Moderate (ROI 0-100%) | 20% | +Rs 10L | +Rs 2L |
| Failure (ROI < 0) | 10% | -Rs 20L | -Rs 2L |
| **Total Expected Value** | | | **+Rs 35L** |

Decision: Expected value is positive, launch campaign.

### Value of Information

**Question**: Should we run a pilot before full launch?

Pilot cost: Rs 5L
If pilot reveals failure probability:
- Can avoid Rs 20L loss with 10% probability
- Value of pilot = 0.10 * 20L = Rs 2L

Since pilot cost (5L) > value of information (2L), skip pilot and launch directly.

---

## Bayesian Updating in Real-Time

### L'Oreal Dashboard Concept

**Week 0 (Prior)**:
- Campaign success probability: 60%
- Expected ROI: 80%

**Week 1 (Update 1)**:
- Early engagement high
- Campaign success probability: 72%
- Expected ROI: 95%

**Week 2 (Update 2)**:
- Conversion picking up
- Campaign success probability: 85%
- Expected ROI: 110%

**Week 3 (Update 3)**:
- Full results in
- Campaign success probability: 95%
- Expected ROI: 120% (95% CI: 90%-150%)

---

## Key Takeaways

1. **Bayes' theorem** updates prior beliefs with new evidence
2. **Prior** captures existing knowledge before data
3. **Posterior** is the updated belief after seeing data
4. **Bayesian gives direct probability statements** ("95% chance effect is positive")
5. **Can incorporate business knowledge** as informative priors
6. **No fixed sample size needed** - can update continuously
7. **Bayesian networks** combine causal structure with probabilistic inference
8. **Supports decision making** through expected value calculations

---

## When to Use Bayesian vs Frequentist

| Use Bayesian When | Use Frequentist When |
|-------------------|---------------------|
| Strong prior knowledge exists | Little prior information |
| Stakeholders want probability statements | Traditional reporting required |
| Continuous monitoring needed | Fixed sample size acceptable |
| Small sample sizes | Large sample sizes |
| Decision-making under uncertainty | Regulatory/compliance context |
| Combining multiple data sources | Simple, standard tests |

---

## Resources for Learning More

**Books**:
- Statistical Rethinking by Richard McElreath
- Bayesian Data Analysis by Gelman et al.

**Python Libraries**:
- PyMC: Probabilistic programming
- ArviZ: Bayesian visualization
- Bambi: Bayesian regression

**Online**:
- Bayesian Methods for Hackers (free online book)
- Statistical Rethinking lectures (YouTube)
