# Use Case Context: L'Oreal India

## Company Overview

L'Oreal is a global beauty and cosmetics company. In India, L'Oreal operates across multiple regions with diverse consumer segments, distribution channels, and product categories.

---

## India Market Structure

### Regions
- North India (Delhi NCR, Punjab, Haryana, UP)
- South India (Tamil Nadu, Karnataka, Kerala, Andhra Pradesh, Telangana)
- West India (Maharashtra, Gujarat, Rajasthan)
- East India (West Bengal, Odisha, Bihar, Jharkhand)
- Central India (Madhya Pradesh, Chhattisgarh)
- Northeast India (Assam, Meghalaya, etc.)

### Tier Classification
- Tier 1: Metro cities (Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad)
- Tier 2: Large cities (Pune, Ahmedabad, Jaipur, Lucknow, Chandigarh)
- Tier 3: Smaller cities and towns
- Rural: Villages and semi-urban areas

---

## Product Categories

| Category | Examples | Target Segment |
|----------|----------|----------------|
| Skincare | Moisturizers, serums, sunscreens | Women 18-45 |
| Haircare | Shampoos, conditioners, hair color | All demographics |
| Makeup | Lipsticks, foundations, mascaras | Women 16-40 |
| Fragrances | Perfumes, deodorants | Premium segment |
| Men's Grooming | Face wash, beard care | Men 18-45 |

---

## Distribution Channels

1. **E-commerce**: Amazon, Flipkart, Nykaa, own website
2. **Modern Trade**: Big Bazaar, Reliance Retail, DMart
3. **General Trade**: Local kirana stores, chemists
4. **Exclusive Brand Outlets (EBOs)**: L'Oreal branded stores
5. **Salons**: Professional products for salons
6. **Quick Commerce**: Blinkit, Zepto, Instamart

---

## Seasonal Factors in India

| Season/Event | Impact on Sales |
|--------------|-----------------|
| Diwali (Oct-Nov) | Peak sales, gifting season |
| Wedding Season (Nov-Feb) | High makeup and skincare demand |
| Summer (Mar-Jun) | Sunscreen, light moisturizers |
| Monsoon (Jul-Sep) | Haircare issues, anti-fungal products |
| Holi (Mar) | Post-Holi skincare surge |

---

## Business Questions We Will Explore

Throughout this learning journey, we will use L'Oreal India to answer causal questions such as:

1. **Sales Impact**: If we increase TV advertising spend in South India, will sales actually increase?

2. **Promotion Effectiveness**: Did the "Buy 2 Get 1 Free" promotion cause incremental sales, or would customers have bought anyway?

3. **Channel Attribution**: Does launching on quick commerce cannibalize e-commerce sales or create new demand?

4. **Regional Variations**: Why did the same campaign work in Maharashtra but fail in Tamil Nadu?

5. **Price Sensitivity**: If we reduce prices by 10%, how much will demand increase?

6. **Inventory Impact**: Does stockout in one SKU cause customers to switch brands or wait?

7. **Customer Retention**: Does faster delivery actually improve repeat purchase rates?

8. **Marketing Attribution**: Which touchpoint (Instagram ad, influencer, TV) actually caused the purchase?

---

## Sample Data Elements

For our causal modeling exercises, we will work with data like:

**Sales Data**
- Daily/weekly sales by SKU, region, channel
- Revenue, units sold, average selling price
- Returns and cancellations

**Marketing Data**
- Ad spend by channel (TV, digital, print)
- Impressions, clicks, conversions
- Influencer campaigns

**Customer Data**
- Demographics (age, gender, location)
- Purchase history
- Loyalty program membership

**Operational Data**
- Inventory levels
- Delivery times
- Stockout incidents

**External Data**
- Competitor pricing
- Weather data
- Festival calendars
- Economic indicators

---

## Why L'Oreal India for Causal Modeling?

This use case is ideal for learning causal modeling because:

1. **Multiple Confounders**: Region, season, competition, and economic factors all affect sales
2. **Natural Experiments**: Different regions receive different treatments (campaigns, pricing)
3. **Rich Data**: Multiple channels and touchpoints create complex attribution problems
4. **Business Relevance**: Decisions worth millions depend on understanding true causal effects
5. **Counterfactual Questions**: "What would sales be if we hadn't run that promotion?"

---

## Learning Approach

We will use this context to understand:

| Concept | L'Oreal India Example |
|---------|----------------------|
| Correlation vs Causation | Ad spend and sales move together, but does spending cause sales? |
| Confounders | Diwali affects both ad spend and sales |
| Counterfactuals | What would sales be without the campaign? |
| Treatment Effect | Impact of launching in quick commerce |
| DAGs | Mapping all factors affecting sales |
| A/B Testing | Testing two pricing strategies in similar regions |
| Uplift Modeling | Which customers respond to discounts? |

This practical context will make abstract concepts concrete and applicable.
