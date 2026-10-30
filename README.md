# E-Commerce Sales Exploratory Analysis

A reproducible exploratory analysis of a 1,000-row synthetic e-commerce transaction dataset. The notebook examines sales value, category quantities, regional differences, monthly patterns, shipping status, and returned transaction rows.

## Project files

- [`notebooks/ecommerce_sales_eda.ipynb`](notebooks/ecommerce_sales_eda.ipynb): cleaned analysis and visualizations.
- `requirements.txt`: Python dependencies.

## Dataset

The source is the [Kaggle e-commerce dataset](https://www.kaggle.com/datasets/brsahan/e-commerce-dataset/data?select=realistic_e_commerce_sales_data.csv). Download `realistic_e_commerce_sales_data.csv` and place it in `data/` or `/content/` in Google Colab. The data is not committed to this repository; review the source license and terms before reuse.

The supplied file contains 1,000 rows and 12 columns, covers 2023-01-01 through 2024-01-03, and has no order identifier. It has 100 missing ages, 50 missing regions, 50 missing shipping statuses, and 20 rows where `Total Price` differs from `Unit Price × Quantity`. The notebook reports these data quality issues and does not silently remove high-value rows.

## Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Download the CSV from the source above.
3. Open the notebook in Jupyter or Google Colab and run all cells.

## Verified findings from the supplied CSV

- `Total Price` is used as item sales; shipping fee is added only for the separately named customer charge measure.
- In the supplied data, age group 36–50 has the largest total item sales after the notebook's documented median imputation for missing ages. This is a descriptive result from a synthetic sample, not evidence that age causes spending.
- Accessories have the highest mean quantity per transaction row (about 3.06); without an order ID this is not a verified basket-size measure.
- The highest item-sales months include November 2023, January 2023, and June 2023. The file spans only about one year, so this does not establish a recurring seasonal pattern.
- Regional sales totals are close, and observed return rates vary by region. Counts use transaction rows because no unique order ID is supplied.

Run the notebook for exact tables and charts. These findings are based on the CSV you provided; the older HTML report's claims should not be reused without checking the corresponding definitions and data-cleaning steps.

## Limitations

The dataset appears synthetic and has 1,000 rows. It contains no order ID, profit, or verified customer-level identifier. A row should not be described as a complete shopping basket without evidence. Imputation can affect subgroup summaries, and shipping-status comparisons are descriptive rather than causal.

## LinkedIn project description

**E-Commerce Sales Exploratory Analysis** — Analyzed a synthetic retail transaction dataset using Python and pandas. Investigated sales by age group and region, category-level quantities, monthly trends, shipping charges, and returned-row rates; documented missing values, price-total inconsistencies, and limits on interpreting basket size and seasonality.
