🛒 Shopper Spectrum: Customer Segmentation and Product Recommendations in E-Commerce
📌 Project Overview

Shopper Spectrum is an E-Commerce Analytics project that focuses on understanding customer purchasing behavior through Customer Segmentation and Product Recommendation techniques. The project uses transaction data from an online retail store to identify different customer groups using RFM (Recency, Frequency, Monetary) analysis and recommend products using Item-Based Collaborative Filtering.

The solution helps businesses improve customer retention, personalize marketing campaigns, and enhance customer experience through data-driven insights.

🎯 Problem Statement

E-commerce businesses generate massive amounts of transaction data every day. Understanding customer behavior and providing personalized recommendations is essential for increasing customer satisfaction and sales. This project aims to segment customers based on their purchasing patterns and recommend relevant products using machine learning techniques.

🚀 Features
📊 Customer Segmentation
RFM Analysis (Recency, Frequency, Monetary)
Customer Clustering using KMeans
Customer Categories:
🏆 High-Value Customers
⭐ Regular Customers
🛒 Occasional Shoppers
⚠️ At-Risk Customers
🛍️ Product Recommendation System
Item-Based Collaborative Filtering
Cosine Similarity
Top 5 Product Recommendations
Personalized Product Suggestions
📈 Exploratory Data Analysis
Country-wise Transaction Analysis
Revenue Analysis
Top Selling Products
Monthly Sales Trends
Customer Purchase Behavior
Cluster Visualizations
🌐 Streamlit Dashboard
Interactive User Interface
Customer Segmentation Prediction
Product Recommendation Module
Business Insights Dashboard
📂 Dataset Information

Dataset Columns:

Column	Description
InvoiceNo	Transaction Number
StockCode	Product Code
Description	Product Name
Quantity	Quantity Purchased
InvoiceDate	Transaction Date
UnitPrice	Price Per Unit
CustomerID	Customer Identifier
Country	Customer Country

Dataset Size:

541,909 Records
8 Features
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Scikit-Learn
KMeans Clustering
DBSCAN
Hierarchical Clustering
Collaborative Filtering
Cosine Similarity
Joblib
Streamlit
🔄 Project Workflow
1. Data Collection & Understanding
Load Online Retail Dataset
Explore Dataset Structure
Analyze Missing Values
Identify Duplicate Records
2. Data Preprocessing
Remove Missing Customer IDs
Remove Cancelled Transactions
Remove Invalid Quantities and Prices
Handle Duplicates
Create TotalAmount Feature
3. Exploratory Data Analysis
Country Analysis
Product Analysis
Sales Trend Analysis
Customer Analysis
Revenue Analysis
4. Feature Engineering

Generate RFM Features:

Recency
Frequency
Monetary
5. Customer Segmentation
Feature Scaling
KMeans Clustering
Elbow Method
Silhouette Score Analysis
Customer Segment Creation
6. Product Recommendation System
Customer-Product Matrix
Cosine Similarity Matrix
Product Recommendation Function
7. Deployment
Save Models using Joblib
Streamlit Application Development
🤖 Machine Learning Models Used
Model 1: KMeans Clustering

Used for customer segmentation based on RFM features.

Model 2: DBSCAN

Used for density-based customer clustering.

Model 3: Hierarchical Clustering

Used for hierarchical customer grouping.

Final Selected Model

✅ KMeans Clustering

Reason:

Better Cluster Separation
Higher Silhouette Score
Easy Interpretation
Fast Execution
📊 Evaluation Metrics

The following metrics were used:

Silhouette Score
Inertia (Elbow Method)

These metrics help evaluate cluster quality and customer segment separation.

🖥️ Streamlit Application
Home Page
Project Overview
Business Benefits
KPI Cards
Customer Segmentation Module

Input:

Recency
Frequency
Monetary

Output:

Customer Segment
Segment Interpretation
Product Recommendation Module

Input:

Product Name

Output:

Top 5 Recommended Products
About Page
Problem Statement
Business Use Cases
Methodologies Used
📦 Installation
Clone Repository
git clone https://github.com/yourusername/shopper-spectrum.git
cd shopper-spectrum
Install Dependencies
pip install -r requirements.txt
Run Streamlit App
streamlit run app.py
📁 Project Structure
Shopper-Spectrum/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── online_retail.csv
│
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   └── product_similarity.pkl
│
└── notebooks/
    └── Shopper_Spectrum.ipynb
📈 Business Benefits
Improved Customer Retention
Personalized Marketing Campaigns
Better Customer Understanding
Enhanced Shopping Experience
Increased Revenue Opportunities
Data-Driven Decision Making
🔮 Future Enhancements
Real-Time Recommendation Engine
Deep Learning-Based Recommendation System
Cloud Deployment
Advanced Customer Lifetime Value Prediction
Real-Time Customer Segmentation
Interactive Business Intelligence Dashboard

📜 Conclusion

This project successfully analyzed customer purchasing behavior using RFM analysis and clustering techniques. Customers were segmented into meaningful groups, and a product recommendation system was developed using collaborative filtering. The generated insights can help businesses improve customer engagement, optimize marketing strategies, and deliver personalized shopping experiences.

<img width="1135" height="412" alt="image" src="https://github.com/user-attachments/assets/a8537de7-d71b-4b13-8c46-b5e07cba6022" />

<img width="1365" height="515" alt="image" src="https://github.com/user-attachments/assets/5c96a31b-4632-4b2a-bd04-65ebfc931136" />

<img width="859" height="604" alt="image" src="https://github.com/user-attachments/assets/1455eb4c-71fb-488d-9e90-67156ffcb2db" />

