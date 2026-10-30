# E-Commerce Sales Exploratory Analysis

A reproducible exploratory analysis and interactive dashboard for a 1,000-row synthetic e-commerce transaction dataset. Explore sales value, category quantities, regional differences, monthly patterns, shipping status, and returned transaction rows.

## Project files

- [`notebooks/ecommerce_sales_eda.ipynb`](notebooks/ecommerce_sales_eda.ipynb): cleaned analysis and visualizations.
- [`app.py`](app.py): interactive Streamlit dashboard.
- `requirements.txt`: notebook and dashboard dependencies.

## Dataset

The source is the [Kaggle e-commerce dataset](https://www.kaggle.com/datasets/brsahan/e-commerce-dataset/data?select=realistic_e_commerce_sales_data.csv). Download `realistic_e_commerce_sales_data.csv` and place it in `data/` or `/content/` in Google Colab. The data is not committed to this repository; review the source license and terms before reuse.

The supplied file contains 1,000 rows and 12 columns, covers 2023-01-01 through 2024-01-03, and has no order identifier. It has 100 missing ages, 50 missing regions, 50 missing shipping statuses, and 20 rows where `Total Price` differs from `Unit Price × Quantity`. All 1,000 rows have valid dates, prices, and quantities. The notebook keeps missing age and region values visible as `Unknown` instead of imputing them into demographic or regional groups.

## Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Download the CSV from the source above.
3. Open the notebook in Jupyter or Google Colab and run all cells.

## Findings from the supplied data

The validated notebook run completed all 11 code cells with saved outputs and no recorded errors. It uses the corrected handling: missing ages and regions remain `Unknown`, and rows with unknown shipping status are excluded from return-rate denominators. The findings below match its outputs. The repository notebook also checks `/content/sample_data/`, the path used in the Colab run.

- Accessories have the highest mean quantity per transaction row (3.06). Without an order ID this is not a verified multi-item basket measure.
- Among records with a known age, ages 51–65 contribute the largest total item sales ($428,490). The 100 rows with missing age account for $165,440 and are shown separately as `Unknown`.
- Among named regions, East has the largest item-sales total ($329,950), followed by North ($324,990), West ($323,390), and South ($301,040). The 50 missing-region rows account for $67,230 and are kept as `Unknown` rather than assigned to a region.
- November 2023 has the largest monthly item-sales total ($147,150), followed by January ($141,360) and June ($129,450). The file covers only about one year, so this does not establish a recurring seasonal pattern.
- Among rows with known shipping status, West has the highest observed return-row rate among named regions (39.9%, 95 of 238 rows). This is descriptive; rows with unknown shipping status are excluded from the denominator, and there is no unique order ID.

These subgroup findings use explicit unknown categories so missing data is not silently attributed to the median age group or most common region. The underlying dataset is synthetic, so treat the results as a portfolio analysis exercise rather than real retailer evidence.

## Limitations

The dataset has 1,000 rows and appears synthetic. It contains no order ID, profit, or verified customer-level identifier. A row should not be described as a complete shopping basket without evidence. Twenty rows have an arithmetic mismatch between `Total Price` and `Unit Price × Quantity`; the analysis uses the supplied `Total Price` as item sales and reports the mismatch rather than silently changing it. Shipping-status comparisons are descriptive rather than causal.

## Interactive dashboard

Run the dashboard locally with `streamlit run app.py`, then upload the source CSV in the sidebar. The dashboard includes date, region, category, and age-group filters; sales summary metrics; interactive monthly, category, region, and shipping charts; and a filtered record table. The CSV is not included in this repository, so users need to obtain it from the linked source and check its current reuse terms.

To publish it with [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud), connect your GitHub account, create an app from this repository's `main` branch, and set the app file path to `app.py`. Once deployed, add the resulting public app URL to this README and your LinkedIn project entry. The deployed app prompts each visitor to upload the CSV because the dataset is not bundled with the code.

## LinkedIn project description

**E-Commerce Sales Exploratory Analysis & Dashboard** — Analyzed a synthetic retail transaction dataset using Python, pandas, Matplotlib, Seaborn, Streamlit, and Plotly. Built an interactive dashboard to explore sales by month, region, category, and age group, with transparent handling of missing data and descriptive shipping outcomes. Documented price-total inconsistencies and limits on interpreting basket size and seasonality.
