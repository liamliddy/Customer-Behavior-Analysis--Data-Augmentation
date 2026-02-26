# Customer Behavior Analysis & Data Augmentation

## **Objective**
Analyze key drivers of customer engagement and spending patterns using a foundational dataset of customer interactions. This project explores how demographic factors (Age, Gender) relate to behavioral metrics such as Income, Spending Score, and Visit Frequency.  
The goal is to identify high‑value customer segments and support smarter marketing strategies, to increase profits and accelerate customer engagement. 

---

## **Pipeline Overview**

 **1. Data Source**
- Imported the **Muhammad Hussnain Customer Behaviour Dataset** as the baseline dataset.
- https://www.kaggle.com/datasets/muhammadhussnain09/customer-behaviour-dataset

### **2. Data Augmentation**
- Built a custom Python script to generate synthetic customer records.
  - Increased the sample size of dataset to simulate more customer data.
- Applied a **stochastic noise algorithm** (±5–10%) to:
  - Age  
  - Income  
  - Spending Score  
  - Visit Frequency  
- Ensured the augmented dataset preserved the statistical integrity of the original distribution.

### **3. Visualization & Analytics**
- Loaded the expanded dataset into **Power BI**.
- Performed demographic segmentation, trend analysis, and behavioral clustering.

---

# **Tech Stack**

## **Data Engineering**
- 🐍 **Python**  
  - pandas  
  - os  
  - csv
    
## **Analytics & Visualization**
- 📊 **Power BI**
  - **Power Query** for data profiling, type enforcement, and column creation 
  - **DAX** for calculated measures such as:
    - R² correlation matrices to evaluate relationships between demographic and behavioral variables.
    - Average Spending per Visit  
    - Income‑to‑Score Correlation  
  - Multi‑page interactive dashboards for segmentation & trend insights

---

# Dashboard & Insights Preview

![Dashboard Preview](https://github.com/liamliddy/Customer-Behavior-Analysis--Data-Augmentation/blob/main/DASHBOARD/DASHBOARD_1.png)
## **Demographic Segments**

### **The High-Income "Savers" (Ages 30–49)**
Despite having the highest median incomes (peaking at $95,000 for males in the 30–39 bracket), this group shows a dip in spending scores.
Key Insight: "Home" and "Electronics" are the preferred categories, but they are likely infrequent purchases rather than impulse buys.
Behavioral Gap: High income does not equal high frequency.

### **The Lifecycle Shoppers (Ages 20–29 & 50–70)**
Early Career (20–29): This group has the highest visit frequency. While their income is lower for Electronics ($45k), their spending score for the category is high. They are "aspirational" shoppers.
Legacy Loyalists (60–70): Driven heavily by females preferring Sports and Groceries. This segment represents the "Loyal" and "Frequent" visitor types who provide the baseline revenue stability.

---

![Dashboard Preview](https://github.com/liamliddy/Customer-Behavior-Analysis--Data-Augmentation/blob/main/DASHBOARD/DASHBOARD_2.png)
## **The "Affluence vs. Engagement" Paradox**

The most striking finding in this dataset is the inverse relationship between Median Annual Income and Spending Score. High-income segments (particularly males 30-39) are the most "conservative" spenders, while lower-to-middle income segments (21-29 and 50+) drive the highest spending intensity. This suggests that "loyalty" and "spending" are driven by lifestyle necessity and aspirational buying rather than raw purchasing power.

---

![Dashboard Preview](https://github.com/liamliddy/Customer-Behavior-Analysis--Data-Augmentation/blob/main/DASHBOARD/DASHBOARD_6.png)

![Dashboard Preview](https://github.com/liamliddy/Customer-Behavior-Analysis--Data-Augmentation/blob/main/DASHBOARD/DASHBOARD_3.png)
## **Strategic Recommendations**

### **The "Affluence Conversion" Program**
Target the 30–49 high-income males ($95k/Home) and 40–49 females ($90k/Electronics).
Recommendation: Implement a "Premium Tiers" loyalty program that rewards high-value single transactions rather than just frequency. Move them from "Occasional" to "Frequent" by bundling Home/Electronic purchases with Grocery incentives.

### **Segment-Specific Marketing Shifts**
For 20–24 Cohort: Capitalize on high visit frequency and sports preference. Use "limited drop" sports apparel to maintain the high spending score despite their lower median income ($45k).
For 60–70 Females: They are your most consistent visitors. Expand the "Sports" category to include wellness and community-based activities to solidify their "Loyal" status.

### **Category Re-Positioning**
Groceries as a "Gateway": Since "Rare" visitors prefer Groceries, use grocery coupons to cross-sell "Electronics" to the younger crowd and "Home" to the older crowd.
Electronics for Women 40–49: Data shows a high income ($90k) but low current spending score. There is a marketing gap here; shift electronics advertising from "gaming/utility" to "smart home/productivity" for this segment.

---

![Dashboard Preview](https://github.com/liamliddy/Customer-Behavior-Analysis--Data-Augmentation/blob/main/DASHBOARD/DASHBOARD_FIN.png)
## **Correlation Analysis**

### **Electronics (Ages 25–34)**
High Predictability. With R² values of 0.45 and 0.39, these groups are highly income-sensitive. For these young adults, the ability to buy electronics is strictly tied to their earning power.

### **Groceries (Ages 40–49)**
Mid-Life Necessity. The R² values of 0.38 and 0.31 suggest that income moderately influences grocery spending in these prime earning years.
Sports & Clothing (Ages 50–70): Low Predictability. The extremely low R² values (near 0.00) confirm your observation that older women buy sports and clothing regardless of income. These are "lifestyle" categories driven by habit and interest, not budget.
