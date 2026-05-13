# Causal Modeling

A practical learning repository for understanding and implementing causal modeling, causal inference, and causal AI concepts from fundamentals to advanced applications.

## Repository Purpose

This repository documents my learning journey exploring causal modeling concepts and techniques. It serves as both a personal learning log and a reference guide built progressively as new concepts are learned.

---

## Why Causal Modeling?

Traditional analytics answers: What happened?
Machine Learning answers: What will happen?
**Causal Modeling answers: What will happen IF we intentionally change something?**

This repository focuses on:
- Cause vs correlation
- Business interventions
- Decision intelligence
- Counterfactual reasoning
- Treatment effects
- Real-world applications in retail and supply chain

---

## Repository Structure

```
Casual-Modelling/
├── README.md                 # This file
├── notes/                    # Learning notes and concepts
│   ├── 01_fundamentals/
│   ├── 02_causal_inference/
│   ├── 03_statistical_methods/
│   ├── 04_advanced_techniques/
│   └── 05_applications/
├── notebooks/                # Jupyter notebooks with hands-on examples
│   ├── 01_intro_to_causal_graphs.ipynb
│   ├── 02_causal_inference_basics.ipynb
│   └── ...
├── code/                     # Implementation code and reusable functions
│   ├── causal_graphs.py
│   ├── inference.py
│   └── utils.py
├── data/                     # Sample datasets for experimentation
│   ├── sample_retail_data.csv
│   └── ...
└── resources/                # External references, papers, links
    └── references.md
```

---

## Learning Path

### Phase 1: Fundamentals (Start Here)
- Understanding causality vs correlation
- Why causal modeling matters
- Key concepts and terminology
- Causal graphs and DAGs (Directed Acyclic Graphs)

### Phase 2: Causal Inference Basics
- Do-calculus and causal calculus
- Backdoor criterion
- Front-door criterion
- Confounder identification

### Phase 3: Statistical Methods
- Matching techniques
- Stratification and adjustment
- Propensity score methods
- Instrumental variables

### Phase 4: Advanced Techniques
- Difference-in-differences
- Synthetic control methods
- Heterogeneous treatment effects
- Double machine learning

### Phase 5: Real-World Applications
- Retail use cases
- Supply chain optimization
- A/B testing with causal inference
- Uplift modeling

### Phase 6: Production & Scale
- Implementation best practices
- Performance considerations
- Integration with ML pipelines

---

## Getting Started

1. Start with the [Use Case Context](notes/00_use_case_context.md) - L'Oreal India
2. Read the [Fundamentals Index](notes/01_fundamentals/00_index.md) for learning path
3. Follow along with Jupyter notebooks in `notebooks/`
4. Implement concepts with code in `code/`
5. Reference external materials in `resources/references.md`

---

## Fundamentals Notes (Complete)

All foundational concepts with L'Oreal India examples:

| # | Topic | Description |
|---|-------|-------------|
| 1 | [Correlation](notes/01_fundamentals/01_correlation.md) | How variables move together |
| 2 | [Causation](notes/01_fundamentals/02_causation.md) | Does one variable cause another? |
| 3 | [Correlation vs Causation](notes/01_fundamentals/03_correlation_vs_causation.md) | Key differences and traps |
| 4 | [Confounders](notes/01_fundamentals/04_confounders.md) | Hidden variables creating false relationships |
| 5 | [Counterfactuals](notes/01_fundamentals/05_counterfactuals.md) | What would have happened otherwise? |
| 6 | [Treatment Effect](notes/01_fundamentals/06_treatment_effect.md) | ATE, ATT, CATE explained |
| 7 | [Hypothesis Testing](notes/01_fundamentals/07_hypothesis_testing.md) | Statistical significance |
| 8 | [A/B Testing](notes/01_fundamentals/08_ab_testing.md) | Experimentation gold standard |
| 9 | [Bayesian Statistics](notes/01_fundamentals/09_bayesian_statistics.md) | Updating beliefs with evidence |
| 10 | [DAGs](notes/01_fundamentals/10_dag.md) | Directed Acyclic Graphs |
| 11 | [Root Cause vs Causal Modeling](notes/01_fundamentals/11_root_cause_vs_causal_modeling.md) | When to use which |
| 12 | [Uplift Modeling](notes/01_fundamentals/12_uplift_modeling.md) | Incremental effect prediction |
| 13 | [Selection Bias](notes/01_fundamentals/13_selection_bias.md) | Why groups differ systematically |
| 14 | [Propensity Scores](notes/01_fundamentals/14_propensity_score.md) | Creating comparable groups |
| 15 | [Structural Causal Models](notes/01_fundamentals/15_structural_causal_models.md) | Complete SCM framework |

---

## Topics to Explore

- Root Cause Analysis vs Causal Modeling
- Causal Inference frameworks
- Bayesian statistics and causal models
- A/B Testing and experimentation
- Uplift Modeling
- Treatment Effect Estimation
- Causal Graphs and DAGs
- Retail and Supply Chain Use Cases
- Python libraries: CausalML, DoWhy, EconML, Causalimpact

---


# Real-World Use Cases

Examples explored in this repository:

* SKU sales decline analysis
* Promotion effectiveness
* Inventory stockout impact
* Delivery delay impact on customer retention
* Marketing attribution
* Pricing impact on demand
* Customer uplift modeling
* Supply chain intervention analysis

Example domains:

* Retail
* Beauty & Cosmetics
* E-commerce
* Supply Chain
* Marketing Analytics

---

# Topics Covered

## Foundations

* Statistics Basics
* Probability
* Hypothesis Testing
* Bayesian Statistics
* Experimental Design

## Causal Inference

* Correlation vs Causation
* Confounders
* Counterfactuals
* Treatment Effect
* Selection Bias
* Propensity Score Matching

## Causal Modeling

* Directed Acyclic Graphs (DAGs)
* Structural Causal Models
* Causal Discovery
* Root Cause Analysis vs Causal Modeling

## Experimentation

* A/B Testing
* Incrementality Testing
* Uplift Modeling
* Marketing Experiments

## Retail & Supply Chain

* Inventory Impact Analysis
* Demand Drivers
* Promotion Analysis
* Supply Chain Delays
* Customer Retention Drivers

---

# Tech Stack

## Languages

* Python

## Libraries

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* DoWhy
* EconML
* CausalNex
* PyMC
* pgmpy

## Future Additions

* FastAPI
* Streamlit
* Neo4j
* AWS
* Databricks
* Snowflake

---

# Repository Structure

```text
causal-modeling/
│
├── notebooks/
├── datasets/
├── experiments/
├── causal_graphs/
├── uplift_modeling/
├── bayesian_statistics/
├── retail_supply_chain_usecases/
├── docs/
└── README.md
```

---

# Learning Roadmap

## Phase 1 — Foundations

* Statistics
* Probability
* Regression
* Hypothesis Testing

## Phase 2 — Causal Inference

* DAGs
* Confounders
* Counterfactuals
* Treatment Effect

## Phase 3 — Practical Implementation

* A/B Testing
* Uplift Modeling
* Bayesian Networks
* Causal Graphs

## Phase 4 — Production Systems

* Retail Causal Intelligence Platform
* Intervention Recommendation Engine
* Supply Chain Decision Intelligence

---

# Example Business Questions

Examples of causal questions explored:

* If inventory availability increases, how much sales will improve?
* Does faster delivery improve customer retention?
* Which customers purchase ONLY because of discounts?
* Did marketing campaign actually increase sales?
* Which factor truly caused SKU sales decline?

---

# Key Difference

| Traditional Analytics | Causal Modeling       |
| --------------------- | --------------------- |
| What happened?        | Why did it happen?    |
| Correlation           | Cause-effect          |
| Predictive            | Intervention-focused  |
| Historical analysis   | Decision intelligence |

---

# Goals of This Repository

* Build strong intuition around causal AI
* Learn practical causal inference
* Explore retail & supply chain applications
* Implement real-world causal systems
* Create reusable learning resources
* Build production-grade causal intelligence products

---

# References & Learning Resources

Books:

* Causal Inference in Statistics
* The Book of Why
* Elements of Causal Inference

Libraries:

* DoWhy
* EconML
* CausalNex
* PyMC


