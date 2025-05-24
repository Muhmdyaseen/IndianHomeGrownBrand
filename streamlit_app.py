import streamlit as st
import pandas as pd

# --- Load Data from Google Sheets ---
url = 'https://docs.google.com/spreadsheets/d/16qDWOLojEEMYQlKG33e0E0gxBPLc50BVlexxBFn9vPc/export?format=csv'
brands = pd.read_csv(url, on_bad_lines='warn')

# --- Page Title ---
st.title("Indian Apparel Brand Portfolio")
st.markdown("Discover and explore homegrown Indian fashion brands.")

# --- Sidebar: Custom Category Click List ---
st.sidebar.title("Filter by Category")

categories = ["All"] + sorted(brands["category"].dropna().unique().tolist())

# --- Sidebar: Category Filter ---
st.sidebar.title("Filter by Category")
categories = ["All"] + sorted(brands["category"].dropna().unique().tolist())
selected_category = st.sidebar.radio("Select category", categories)


# --- Search Bar (Right Aligned) ---
col1, col2, col3 = st.columns([5, 1, 3])
with col3:
    search_query = st.text_input("Search", placeholder="Type a brand name", label_visibility="collapsed")

# --- Clean Search Input ---
search_query = search_query.strip().lower()

# --- Filter Logic ---
filtered_brands = brands.copy()

if selected_category != "All":
    filtered_brands = filtered_brands[filtered_brands["category"] == selected_category]

if search_query:
    filtered_brands = filtered_brands[filtered_brands["name"].str.lower().str.contains(search_query, na=False)]


# --- Display Results ---
if not filtered_brands.empty:
    for _, brand in filtered_brands.iterrows():
        with st.container():
            # if pd.notna(brand.get("image", None)):
            #     st.image(brand["image"], width=150)
            st.subheader(brand["name"])
            st.write(brand["description"])
            st.markdown(f"[Visit Website]({brand['website']})")
            st.markdown("---")
else:
    st.warning("No brands match your search or filter.")
