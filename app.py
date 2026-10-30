"""Interactive Streamlit dashboard for the E-Commerce Sales EDA project."""

from __future__ import annotations

from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="E-Commerce Sales Explorer",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

NAVY = "#14283F"
TEAL = "#168C8C"
GOLD = "#E3A23B"
MUTED = "#687789"


def load_data(file_bytes: bytes) -> pd.DataFrame:
    """Read CSV bytes and standardize the fields used by the dashboard."""
    df = pd.read_csv(BytesIO(file_bytes))
    required = {"Order Date", "Product Name", "Category", "Region", "Total Price", "Quantity", "Shipping Status"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Total Price"] = pd.to_numeric(df["Total Price"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    if "Shipping Fee" in df.columns:
        df["Shipping Fee"] = pd.to_numeric(df["Shipping Fee"], errors="coerce")
    if "Age" in df.columns:
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    for column in ("Product Name", "Category", "Region", "Shipping Status"):
        df[column] = df[column].fillna("Unknown").astype(str).str.strip().replace("", "Unknown")

    df = df.dropna(subset=["Order Date", "Total Price", "Quantity"]).copy()
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    if "Age" in df.columns:
        df["Age Group"] = pd.cut(
            df["Age"],
            bins=[0, 18, 35, 50, 65, float("inf")],
            labels=["0–18", "19–35", "36–50", "51–65", "66+"],
            include_lowest=True,
        ).astype("object").fillna("Unknown")
    else:
        df["Age Group"] = "Not provided"
    return df


def money(value: float) -> str:
    return f"${value:,.0f}"


st.markdown(
    f"""
    <style>
      .block-container {{max-width: 1440px; padding-top: 2rem; padding-bottom: 3rem;}}
      h1, h2, h3 {{color: {NAVY};}}
      [data-testid="stMetric"] {{background:#F4F7FA; border:1px solid #E3EAF0;
        padding:16px 18px; border-radius:12px;}}
      [data-testid="stMetricLabel"] {{color:{MUTED};}}
      .eyebrow {{color:{TEAL}; font-weight:700; letter-spacing:.12em; text-transform:uppercase;}}
      .note {{color:{MUTED}; font-size:.92rem;}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">Portfolio data project</div>', unsafe_allow_html=True)
st.title("E-Commerce Sales Explorer")
st.markdown(
    "Explore sales patterns, customer segments, and shipping outcomes in a synthetic "
    "retail dataset. Use the filters to focus the analysis."
)

with st.sidebar:
    st.header("Load the data")
    upload = st.file_uploader("Upload the source CSV", type=["csv"])
    st.caption("Expected file: `realistic_e_commerce_sales_data.csv`.")
    st.link_button(
        "Open dataset source",
        "https://www.kaggle.com/datasets/brsahan/e-commerce-dataset/data?select=realistic_e_commerce_sales_data.csv",
        use_container_width=True,
    )
    st.divider()
    if upload is None:
        st.caption("No CSV is bundled with this app. Upload the source file to explore the dashboard, and check its terms before reuse.")
    else:
        st.caption(f"Loaded `{upload.name}` for this session. The CSV is not stored in this GitHub repository.")

if upload is None:
    st.info("Upload the CSV in the sidebar to explore the dashboard.")
    st.subheader("What you can explore")
    intro_cols = st.columns(3)
    intro_cols[0].markdown("**Sales over time**\n\nCompare monthly item-sales totals and categories.")
    intro_cols[1].markdown("**Customer and region views**\n\nFilter age groups and regions while keeping missing values visible.")
    intro_cols[2].markdown("**Shipping outcomes**\n\nReview shipping statuses and descriptive return-row rates.")
    st.markdown(
        '<p class="note">This project uses synthetic data. Results are descriptive and should not be interpreted as evidence about a real retailer.</p>',
        unsafe_allow_html=True,
    )
    st.stop()

try:
    data = load_data(upload.getvalue())
except Exception as exc:  # Show actionable input feedback in the app.
    st.error(f"Could not read this file: {exc}")
    st.stop()

if data.empty:
    st.error("No rows with valid dates, sales values, and quantities were found.")
    st.stop()

with st.sidebar:
    st.header("Explore")
    date_range = st.date_input(
        "Order date range",
        value=(data["Order Date"].min().date(), data["Order Date"].max().date()),
        min_value=data["Order Date"].min().date(),
        max_value=data["Order Date"].max().date(),
    )
    selected_regions = st.multiselect("Region", sorted(data["Region"].unique()), default=sorted(data["Region"].unique()))
    selected_categories = st.multiselect("Category", sorted(data["Category"].unique()), default=sorted(data["Category"].unique()))
    selected_age = st.multiselect("Age group", sorted(data["Age Group"].astype(str).unique()), default=sorted(data["Age Group"].astype(str).unique()))

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range

filtered = data[
    data["Order Date"].dt.date.between(start_date, end_date)
    & data["Region"].isin(selected_regions)
    & data["Category"].isin(selected_categories)
    & data["Age Group"].astype(str).isin(selected_age)
].copy()

if filtered.empty:
    st.warning("No rows match these filters. Widen the date range or select more filter values.")
    st.stop()

known_shipping = filtered[filtered["Shipping Status"] != "Unknown"]
return_rows = int(known_shipping["Shipping Status"].str.casefold().eq("returned").sum())
return_rate = return_rows / len(known_shipping) * 100 if len(known_shipping) else 0
shipping_total = filtered["Shipping Fee"].sum(min_count=1) if "Shipping Fee" in filtered else None

kpis = st.columns(4)
kpis[0].metric("Item sales", money(filtered["Total Price"].sum()))
kpis[1].metric("Transaction rows", f"{len(filtered):,}")
kpis[2].metric("Units", f"{filtered['Quantity'].sum():,.0f}")
kpis[3].metric("Returned row rate", f"{return_rate:.1f}%", help=f"{return_rows:,} returned rows / {len(known_shipping):,} rows with known shipping status")

st.markdown(
    '<p class="note">Sales use the supplied <code>Total Price</code>. Rows are not necessarily unique orders. Return rate excludes unknown shipping statuses and is a row-level descriptive measure.</p>',
    unsafe_allow_html=True,
)

monthly = filtered.groupby("Month", as_index=False)["Total Price"].sum()
category = filtered.groupby("Category", as_index=False).agg(Sales=("Total Price", "sum"), Units=("Quantity", "sum"))
region = filtered.groupby("Region", as_index=False)["Total Price"].sum().sort_values("Total Price", ascending=True)

left, right = st.columns([1.55, 1])
with left:
    st.subheader("Monthly item sales")
    fig = px.line(monthly, x="Month", y="Total Price", markers=True, color_discrete_sequence=[TEAL])
    fig.update_traces(line=dict(width=3), marker=dict(size=7))
    fig.update_layout(height=350, margin=dict(l=0, r=10, t=10, b=0), xaxis_title=None, yaxis_title="Sales ($)", hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Sales by category")
    fig = px.pie(category, values="Sales", names="Category", hole=.58, color_discrete_sequence=[TEAL, GOLD, "#547A9B", "#91B5B5", "#AAB6C2"])
    fig.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=0), legend_title=None)
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Item sales by region")
    fig = px.bar(region, x="Total Price", y="Region", orientation="h", text_auto="$,.0f", color_discrete_sequence=[TEAL])
    fig.update_layout(height=320, margin=dict(l=0, r=10, t=10, b=0), xaxis_title="Sales ($)", yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Shipping status")
    shipping = filtered["Shipping Status"].value_counts().rename_axis("Shipping Status").reset_index(name="Rows")
    fig = px.bar(shipping.sort_values("Rows"), x="Rows", y="Shipping Status", orientation="h", text="Rows", color_discrete_sequence=[GOLD])
    fig.update_layout(height=320, margin=dict(l=0, r=10, t=10, b=0), xaxis_title="Transaction rows", yaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Explore the filtered records")
display_columns = [c for c in ["Order Date", "Product Name", "Category", "Region", "Age Group", "Quantity", "Total Price", "Shipping Fee", "Shipping Status"] if c in filtered]
st.dataframe(filtered[display_columns].sort_values("Order Date", ascending=False), use_container_width=True, hide_index=True)

with st.expander("Data notes and limitations"):
    st.markdown(
        "- The source dataset is synthetic and the results describe this file only.\n"
        "- The file has no order ID, so counts and return rates are calculated per row, not per order.\n"
        "- Missing age, region, and shipping status values are retained as `Unknown`.\n"
        "- Unknown shipping statuses are excluded from the returned-row-rate denominator.\n"
        "- The analysis uses the supplied `Total Price`; 20 rows in the supplied file differ from `Unit Price × Quantity`."
    )
    if shipping_total is not None:
        st.caption(f"Shipping fees in the filtered rows total {money(shipping_total)}; item sales do not include shipping fees.")

st.caption("Built with Streamlit, pandas, and Plotly · E-Commerce Sales EDA portfolio project")
