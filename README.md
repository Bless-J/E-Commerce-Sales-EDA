# E-Commerce Sales EDA

Exploratory analysis of a public synthetic e-commerce transaction dataset. The notebook examines transaction value, category-level quantity, monthly sales, shipping status, and return patterns.

## Project files

- [`notebooks/ecommerce_sales_eda.ipynb`](notebooks/ecommerce_sales_eda.ipynb): cleaned, reproducible analysis.
- `requirements.txt`: Python dependencies.

## Dataset

Download `realistic_e_commerce_sales_data.csv` from the [Kaggle source](https://www.kaggle.com/datasets/brsahan/e-commerce-dataset/data?select=realistic_e_commerce_sales_data.csv). Place it in `data/` or upload it to `/content/` in Google Colab. The dataset is not stored in this repository; follow its license and terms.

The notebook expects these columns: Customer ID, Gender, Region, Age, Product Name, Category, Unit Price, Quantity, Total Price, Shipping Fee, Shipping Status, and Order Date. Each row is treated as a transaction record because no order identifier is present.

## Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Download the CSV from the source above.
3. Open the notebook in Jupyter or upload it to Google Colab.
4. Run all cells and review the caveats beside each question.

## Analysis questions

- Which age group contributes the most item sales in this sample?
- Which product categories have the highest mean quantity per transaction row?
- How do category price and unit volume compare descriptively?
- How do sales, shipping fees, and return-row rates vary by region and shipping status?
- Which months have the highest observed item sales?

## Limitations

This dataset contains 1,000 rows and appears synthetic. It has no order ID, profit, or verified customer-level identifiers. Results are descriptive and should not be interpreted as causal or generalized to real retailers. Current results should be populated only after a clean run of the revised notebook.

## LinkedIn project description

**E-Commerce Sales Exploratory Analysis** — Analyzed a synthetic retail transaction dataset with Python, pandas, Matplotlib, and Seaborn. Investigated sales by age group and region, category quantity patterns, monthly trends, shipping status, and return rates, while documenting denominator and data-quality limitations. Add verified findings after rerunning the notebook.
