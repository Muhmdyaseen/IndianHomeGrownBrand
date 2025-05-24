# streamlit_app.py

import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/16qDWOLojEEMYQlKG33e0E0gxBPLc50BVlexxBFn9vPc/export?format=csv'
brands = pd.read_csv(url, on_bad_lines='warn')

# Page title
st.title("Indian Apparel Brand Portfolio")
st.markdown("Discover and explore homegrown Indian fashion brands.")

# Layout with columns to align search bar right
col1, col2, col3 = st.columns([5, 1, 3])
with col3:
    search_query = st.text_input("Search", placeholder="Type a brand name", label_visibility="collapsed")

search_query = search_query.strip().lower()
if search_query:
    filtered_brands = brands[brands['name'].str.lower().str.contains(search_query, na=False)]
else:
    filtered_brands = brands

# Show results
if not filtered_brands.empty:
    for _, brand in filtered_brands.iterrows():
        with st.container():
            # st.image(brand["image"], width=150)  # uncomment if image URL is valid
            st.subheader(brand["name"])
            st.write(brand["description"])
            st.markdown(f"[Visit Website]({brand['website']})")
            st.markdown("---")
else:
    st.warning("No brands match your search.")