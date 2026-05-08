# Fundamentals of Causal Modeling - Index

This section covers all foundational concepts you need to understand before diving into practical causal modeling techniques.

---

## Use Case Context

- [00_use_case_context.md](../00_use_case_context.md) - L'Oreal India business context used throughout all examples

---

## Core Concepts

| # | Topic | File | Key Question |
|---|-------|------|--------------|
| 1 | Correlation | [01_correlation.md](01_correlation.md) | How do two variables move together? |
| 2 | Causation | [02_causation.md](02_causation.md) | Does one variable actually cause another? |
| 3 | Correlation vs Causation | [03_correlation_vs_causation.md](03_correlation_vs_causation.md) | How to distinguish the two? |
| 4 | Confounders | [04_confounders.md](04_confounders.md) | What hidden variables create false relationships? |
| 5 | Counterfactuals | [05_counterfactuals.md](05_counterfactuals.md) | What would have happened otherwise? |
| 6 | Treatment Effect | [06_treatment_effect.md](06_treatment_effect.md) | How much does an intervention change outcomes? |

---

## Statistical Foundations

| # | Topic | File | Key Question |
|---|-------|------|--------------|
| 7 | Hypothesis Testing | [07_hypothesis_testing.md](07_hypothesis_testing.md) | Is the observed effect real or random chance? |
| 8 | A/B Testing | [08_ab_testing.md](08_ab_testing.md) | How to run experiments for causal proof? |
| 9 | Bayesian Statistics | [09_bayesian_statistics.md](09_bayesian_statistics.md) | How to update beliefs with evidence? |

---

## Causal Modeling Frameworks

| # | Topic | File | Key Question |
|---|-------|------|--------------|
| 10 | DAGs | [10_dag.md](10_dag.md) | How to represent causal relationships visually? |
| 11 | Root Cause vs Causal Modeling | [11_root_cause_vs_causal_modeling.md](11_root_cause_vs_causal_modeling.md) | When to use which approach? |
| 12 | Uplift Modeling | [12_uplift_modeling.md](12_uplift_modeling.md) | Who will change behavior because of treatment? |
| 13 | Selection Bias | [13_selection_bias.md](13_selection_bias.md) | Why are treated and control groups different? |
| 14 | Propensity Scores | [14_propensity_score.md](14_propensity_score.md) | How to create comparable groups? |
| 15 | Structural Causal Models | [15_structural_causal_models.md](15_structural_causal_models.md) | How to build complete causal models? |

---

## Recommended Reading Order

### For Complete Beginners
1. Correlation
2. Causation
3. Correlation vs Causation
4. Confounders
5. DAGs
6. Hypothesis Testing
7. A/B Testing

### For Those with Statistics Background
1. Correlation vs Causation (review)
2. Confounders
3. Counterfactuals
4. Treatment Effect
5. DAGs
6. Selection Bias
7. Propensity Scores
8. Structural Causal Models

### For Quick Business Understanding
1. Use Case Context
2. Correlation vs Causation
3. Root Cause vs Causal Modeling
4. Treatment Effect
5. Uplift Modeling

---

## Concept Relationships

```
Correlation
    |
    v
Causation <---- Confounders
    |               |
    v               v
Counterfactuals  Selection Bias
    |               |
    v               v
Treatment Effect  Propensity Scores
    |               |
    +-------+-------+
            |
            v
    Structural Causal Models
            |
            v
    Uplift Modeling
```

---

## Key L'Oreal India Examples by Concept

| Concept | Primary Example |
|---------|-----------------|
| Correlation | Ad spend and sales correlation |
| Causation | TV advertising impact |
| Confounders | Diwali season affecting both marketing and sales |
| Counterfactuals | What sales would be without campaign |
| Treatment Effect | Beauty advisor impact on store sales |
| Hypothesis Testing | Instagram campaign significance |
| A/B Testing | Product reviews on e-commerce conversion |
| Bayesian | Updating new product success probability |
| DAGs | Sales drivers network |
| Root Cause | Tamil Nadu sales drop investigation |
| Uplift | Discount targeting optimization |
| Selection Bias | Loyalty program member comparison |
| Propensity Scores | Email marketing effect estimation |
| SCM | Complete marketing-sales model |

---

## Prerequisites Check

Before moving to advanced topics, ensure you can answer:

- [ ] What is the difference between correlation and causation?
- [ ] What is a confounder and why does it matter?
- [ ] What is a counterfactual?
- [ ] What is ATE, ATT, and CATE?
- [ ] What is a p-value?
- [ ] What makes A/B testing the gold standard?
- [ ] What is a DAG and what are its building blocks?
- [ ] When to use RCA vs causal modeling?
- [ ] What is uplift and why is it different from response?
- [ ] What is selection bias and how to address it?
- [ ] What is a propensity score?
- [ ] What are the three levels of causal reasoning (observe, do, imagine)?

If you can answer all these, you are ready for the next sections on Causal Inference Methods and Statistical Techniques.
