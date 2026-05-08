# Directed Acyclic Graphs (DAGs)

## Definition

A Directed Acyclic Graph (DAG) is a visual and mathematical tool for representing causal relationships between variables. It consists of:

- **Nodes**: Variables (circles)
- **Edges**: Directed arrows showing causal influence
- **Acyclic**: No variable can cause itself through any path

DAGs are the foundation of modern causal inference.

---

## Basic DAG Notation

```
A -> B      : A causes B
A -> B -> C : A causes B, B causes C (causal chain)
A <- C -> B : C causes both A and B (common cause/fork)
A -> C <- B : Both A and B cause C (collider)
```

---

## L'Oreal India: A Complete DAG

### Sales Drivers DAG

```
                    Season
                   /      \
                  v        v
    Marketing Budget -> Awareness -> Purchase Intent
           |              ^                |
           v              |                v
    Price Promotion   Competition      Actual Sales
           |              ^                ^
           v              |                |
    Perceived Value ------+           Distribution
                                          ^
                                          |
                                     Store Count
```

### Reading the DAG

1. **Season** affects both Marketing Budget and Awareness directly
2. **Marketing Budget** affects Awareness and Price Promotions
3. **Awareness** is affected by Marketing, Season, and Competition
4. **Actual Sales** depends on Purchase Intent and Distribution
5. **Distribution** depends on Store Count

---

## DAG Building Blocks

### 1. Chain (Mediation)

```
X -> M -> Y
```

**L'Oreal Example**:
```
TV Ad -> Brand Awareness -> Purchase
```

- TV Ad affects Purchase THROUGH Brand Awareness
- Awareness is the MEDIATOR
- Controlling for Awareness blocks the effect of TV Ad

### 2. Fork (Common Cause / Confounder)

```
    Z
   / \
  v   v
  X   Y
```

**L'Oreal Example**:
```
      Diwali Season
         /    \
        v      v
   Ad Spend   Sales
```

- Diwali causes BOTH higher ad spend AND higher sales
- Creates spurious correlation between Ad Spend and Sales
- Must control for Season to see true ad effect

### 3. Collider

```
  X   Y
   \ /
    v
    Z
```

**L'Oreal Example**:
```
  Quality   Marketing
      \       /
       v     v
     Popular Products
```

- Both Quality and Marketing cause product popularity
- Controlling for Popularity creates spurious association between Quality and Marketing
- Don't control for colliders!

### 4. Descendant

A variable caused by another (directly or indirectly).

```
X -> Y -> Z
```

Z is a descendant of X and Y.

**L'Oreal Example**:
Customer Satisfaction is a descendant of Product Quality, Delivery Time, and Price.

---

## Paths in DAGs

### Types of Paths

1. **Causal Path**: Follows arrow directions from cause to effect
2. **Backdoor Path**: Goes against arrow direction at some point
3. **Blocked Path**: Contains a collider or conditioned variable
4. **Open Path**: All arrows flow, no colliders, nothing conditioned

### L'Oreal Example: Paths Between Ad Spend and Sales

```
         Season
        /      \
       v        v
  Ad Spend --> Awareness --> Sales
                              ^
                              |
                          Price
```

**Path 1 (Causal)**: Ad Spend -> Awareness -> Sales
This is the DIRECT causal effect we want to measure.

**Path 2 (Backdoor)**: Ad Spend <- Season -> Awareness -> Sales
This is a CONFOUNDING path through Season.

To estimate causal effect, we must block Path 2 by controlling for Season.

---

## D-Separation: When Variables are Independent

Two variables are d-separated (conditionally independent) if all paths between them are blocked.

### Blocking Rules

1. **Chain is blocked** by conditioning on middle variable
   - X -> M -> Y: Conditioning on M blocks path

2. **Fork is blocked** by conditioning on common cause
   - X <- Z -> Y: Conditioning on Z blocks path

3. **Collider blocks path by default**
   - X -> Z <- Y: Path is blocked unless we condition on Z

### L'Oreal Example: Is Ad Spend Independent of Customer Income?

```
         Season
        /      \
       v        v
  Ad Spend    Awareness
                 |
                 v
              Sales <- Income
```

Paths from Ad Spend to Income:
1. Ad Spend <- Season -> Awareness -> Sales <- Income

This path has a collider at Sales. Path is BLOCKED.

Without conditioning on anything, Ad Spend and Income are d-separated (independent).

If we condition on Sales, we OPEN the path (collider bias).

---

## The Backdoor Criterion

To estimate causal effect of X on Y:

1. Identify all backdoor paths from X to Y
2. Find a set of variables that blocks all backdoor paths
3. Do NOT condition on:
   - Descendants of X
   - Colliders on any path

### L'Oreal Example: Effect of Promotion on Sales

```
                Customer Segment
               /        |        \
              v         v         v
        Promotion -> Purchase <- Price Sensitivity
              |                        |
              v                        |
         Sales <-----------------------+
```

**Question**: What is causal effect of Promotion on Sales?

**Backdoor paths**:
1. Promotion <- Customer Segment -> Purchase -> ... (blocked at Purchase, it's a collider for Segment)
2. Promotion <- Customer Segment -> Price Sensitivity -> Sales

**To block**: Condition on Customer Segment

**Adjustment set**: {Customer Segment}

Regression: Sales = b0 + b1*Promotion + b2*Customer_Segment + error

b1 is the causal effect of Promotion on Sales.

---

## Building a DAG: Step-by-Step

### Step 1: List All Relevant Variables

**L'Oreal Sales Analysis**:
- Outcome: Monthly Sales
- Treatment: Marketing Spend
- Potential confounders: Season, Region, Price, Competition, Distribution, Economy

### Step 2: Determine Causal Relationships

For each pair, ask: "Does X cause Y, does Y cause X, or neither?"

| Variable 1 | Variable 2 | Relationship |
|------------|------------|--------------|
| Marketing | Sales | Marketing -> Sales |
| Season | Marketing | Season -> Marketing |
| Season | Sales | Season -> Sales |
| Price | Sales | Price -> Sales |
| Competition | Sales | Competition -> Sales |
| Competition | Marketing | Competition -> Marketing |
| Region | Sales | Region -> Sales |
| Region | Marketing | Region -> Marketing |

### Step 3: Draw the DAG

```
          Season           Competition
         /   |  \            /     \
        v    v   v          v       v
    Marketing -> Awareness -> Sales <- Price
        ^                      ^
        |                      |
      Region -----------------+
```

### Step 4: Identify Confounders and Adjustment Sets

For Marketing -> Sales effect:
- Backdoor paths through Season, Competition, Region
- Adjustment set: {Season, Competition, Region}

---

## Common DAG Patterns in Retail

### 1. Price-Demand Relationship

```
          Cost
         /    \
        v      v
     Price -> Demand <- Income
        |              /
        v             v
     Revenue <-------+
```

To estimate price effect on demand: Control for Cost and Income

### 2. Marketing Attribution

```
    Budget Allocation
         |
         v
     TV Ad -> Awareness
         |        |
         v        v
    Digital Ad -> Conversion -> Sales
         ^              ^
         |              |
    Customer Segment ---+
```

Multiple paths from each ad type to sales.

### 3. Store Performance

```
        Location Quality
           /      \
          v        v
    Store Size -> Footfall -> Sales
          |                    ^
          v                    |
    Inventory ----------------+
```

---

## Causal Effects from DAGs

### Total Effect
All causal paths from X to Y.

### Direct Effect
Only the direct arrow X -> Y, blocking mediators.

### Indirect Effect
Through mediators only.

**L'Oreal Example**:

```
TV Ad -> Awareness -> Sales
   |                   ^
   +-------------------+
```

- **Total effect** of TV Ad: All paths
- **Direct effect**: TV Ad -> Sales (immediate brand recognition)
- **Indirect effect**: TV Ad -> Awareness -> Sales (through awareness building)

Total = Direct + Indirect

---

## Do-Calculus and Interventions

### Seeing vs Doing

**Seeing** (Conditioning): P(Sales | Marketing = High)
"What are sales when we observe high marketing?"

**Doing** (Intervention): P(Sales | do(Marketing = High))
"What are sales when we SET marketing to high?"

### Why They Differ

```
    Season
   /      \
  v        v
Marketing  Sales
```

P(Sales | Marketing = High) includes cases where Season caused high marketing.
P(Sales | do(Marketing = High)) removes Season's influence on Marketing.

### Graphical Intervention

do(X = x) is represented by removing all arrows INTO X.

Original:
```
Season -> Marketing -> Sales
            ^
            |
```

After do(Marketing):
```
Season    Marketing -> Sales
```

Now Marketing is no longer affected by Season.

---

## Common DAG Mistakes

### Mistake 1: Forgetting Confounders

```
Wrong: Marketing -> Sales

Right: 
    Season
   /      \
  v        v
Marketing  Sales
```

### Mistake 2: Conditioning on Collider

```
Quality    Marketing
    \       /
     v     v
    Success

Wrong: Analyze only successful products (conditions on collider)
Creates spurious negative correlation between Quality and Marketing
```

### Mistake 3: Conditioning on Mediator

```
Price -> Perceived Value -> Purchase

Wrong: Control for Perceived Value when estimating Price effect
Blocks the causal pathway!
```

### Mistake 4: Ignoring Time

```
Wrong: 
Sales -> Marketing (treating as contemporaneous)

Right:
Sales(t-1) -> Marketing(t) -> Sales(t)
```

---

## DAG Software Tools

### Python
- **DoWhy**: Causal inference with DAGs
- **pgmpy**: Probabilistic graphical models
- **CausalNex**: Bayesian networks for causal reasoning

### R
- **dagitty**: DAG drawing and analysis
- **ggdag**: DAG visualization

### Online
- **DAGitty.net**: Web-based DAG builder

---

## Key Takeaways

1. **DAGs represent causal assumptions visually** - makes assumptions explicit
2. **Three building blocks**: Chains, Forks, Colliders
3. **Confounders create backdoor paths** - must be blocked for causal inference
4. **Never condition on colliders** - creates spurious associations
5. **Backdoor criterion** identifies what to control for
6. **Seeing vs Doing** - observational data vs intervention
7. **DAGs don't prove causation** - they represent assumptions to be tested
8. **Time matters** - causes precede effects

---

## DAG Checklist for L'Oreal Analysis

Before estimating a causal effect:

- [ ] Listed all relevant variables
- [ ] Drew DAG with all causal relationships
- [ ] Identified the treatment (cause) variable
- [ ] Identified the outcome (effect) variable
- [ ] Found all backdoor paths
- [ ] Determined adjustment set (what to control for)
- [ ] Verified not conditioning on colliders
- [ ] Verified not conditioning on descendants of treatment
- [ ] Checked if adjustment set is measurable in data
- [ ] Documented causal assumptions for review
