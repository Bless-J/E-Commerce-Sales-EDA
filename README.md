# E-Commerce Sales Exploratory Analysis

A reproducible exploratory analysis of a 1,000-row synthetic e-commerce transaction dataset. The notebook examines sales value, category quantities, regional differences, monthly patterns, shipping status, and returned transaction rows.

## Project files

- [`notebooks/ecommerce_sales_eda.ipynb`](notebooks/ecommerce_sales_eda.ipynb): cleaned analysis and visualizations.
- `requirements.txt`: Python dependencies.

## Dataset

The source is the [Kaggle e-commerce dataset](https://www.kaggle.com/datasets/brsahan/e-commerce-dataset/data?select=realistic_e_commerce_sales_data.csv). Download `realistic_e_commerce_sales_data.csv` and place it in `data/` or `/content/` in Google Colab. The data is not committed to this repository; review the source license and terms before reuse.

The supplied file contains 1,000 rows and 12 columns, covers 2023-01-01 through 2024-01-03, and has no order identifier. It has 100 missing ages, 50 missing regions, 50 missing shipping statuses, and 20 rows where `Total Price` differs from `Unit Price × Quantity`. All 1,000 rows have valid dates, prices, and quantities. The notebook keeps missing age and region values visible as `Unknown` instead of imputing them into demographic or regional groups.

## Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Download the CSV from the source above.
3. Open the notebook in Jupyter or Google Colab and run all cells.

## Findings from the supplied data

The notebook you supplied completed all 11 code cells without recorded errors. That run imputed missing ages with the median and missing regions with the most common region, which changes subgroup summaries. The clean version now keeps those records in an `Unknown` group and excludes unknown shipping statuses from return-rate denominators. Findings below are recalculated from your CSV using these revised rules; rerun the updated notebook to regenerate matching notebook outputs.

- Accessories have the highest mean quantity per transaction row (3.06). Without an order ID this is not a verified multi-item basket measure.
- Among records with a known age, ages 51–65 contribute the largest total item sales ($428,490). The 100 rows with missing age account for $165,440 and are shown separately as `Unknown`.
- Among named regions, East has the largest item-sales total ($329,950), followed by North ($324,990), West ($323,390), and South ($301,040). The 50 missing-region rows account for $67,230 and are kept as `Unknown` rather than assigned to a region.
- November 2023 has the largest monthly item-sales total ($147,150), followed by January ($141,360) and June ($129,450). The file covers only about one year, so this does not establish a recurring seasonal pattern.
- Among rows with known shipping status, West has the highest observed return-row rate among named regions (39.9%, 95 of 238 rows). This is descriptive; rows with unknown shipping status are excluded from the denominator, and there is no unique order ID.

These subgroup findings use explicit unknown categories so missing data is not silently attributed to the median age group or most common region. The underlying dataset is synthetic, so treat the results as a portfolio analysis exercise rather than real retailer evidence.

## Limitations

The dataset has 1,000 rows and appears synthetic. It contains no order ID, profit, or verified customer-level identifier. A row should not be described as a complete shopping basket without evidence. Twenty rows have an arithmetic mismatch between `Total Price` and `Unit Price × Quantity`; the analysis uses the supplied `Total Price` as item sales and reports the mismatch rather than silently changing it. Shipping-status comparisons are descriptive rather than causal.

## LinkedIn project description

**E-Commerce Sales Exploratory Analysis** — Analyzed a synthetic retail transaction dataset using Python, pandas, Matplotlib, and Seaborn. Investigated sales by age group and region, category-level quantities, monthly trends, shipping charges, and returned-row rates while documenting missing values, price-total inconsistencies, and limits on interpreting basket size and seasonality.
