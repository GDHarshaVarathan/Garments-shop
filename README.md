📌Overview:
This project is a simple data analytics tool built using Python. It processes customer, product, and sales datasets to generate useful insights for a retail shop. The idea is to understand customer behavior, track sales trends, and identify top-performing products. Along with that, it also simulates basic customer segmentation and outreach campaigns.

The project is designed as a small-scale example of how businesses can use data to make decisions.

⚙️ Features:
Customer Segmentation – Classifies customers into High-Value, Frequent Buyers, Dormant, and New/Regular based on their purchase history.
Sales Insights – Identifies top products, highlights revenue contribution, and shows purchase trends.
Visual Dashboards – Generates charts for monthly sales, product performance, and customer segments.
Campaign Simulation – Mimics sending email campaigns to different customer groups and tracks basic engagement (opens/clicks).
Forecasting – Uses a simple regression model to predict next month’s sales.
Exports – Creates CSV reports and charts that can be used for further analysis.

🛠️ Tech Stack:
Python
Pandas – for data handling
Matplotlib – for visualizations
Scikit-learn – for basic forecasting
CSV Datasets – input data for customers, products, and sales

📂 Project Structure:
Garments-Shop/
│── Customer1.csv          # Customer details  
│── Product.csv            # Product catalog  
│── Sales1.csv             # Sales transactions  
│── Garments.py            # Main Python script  
│── Customer_Segments.csv  # Exported segmentation results  
│── Campaign_Report_*.csv  # Campaign reports for each segment  
│── Top_Products.png       # Visualization – Top products  
│── Monthly_Sales.png      # Visualization – Monthly sales  
│── Customer_Segments.png  # Visualization – Segment distribution  

🚀 How to Run:
Clone the repository.
Install the required libraries:
pip install pandas matplotlib scikit-learn
Run the script:
python Garments.py
Check the output folder for reports (.csv) and charts (.png).

📊 Example Insights:
Top Product: Saree contributes 30% of total revenue.
Customer Segments: 20% High-Value, 40% Frequent Buyers, 30% Dormant, 10% New.
Forecast: Predicted sales for next month = ₹8,600 (approx).

🎯 Future Improvements:
Add more datasets for better forecasting.
Build an interactive dashboard using Streamlit.
Connect with an external CRM API for campaign automation.
