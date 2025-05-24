# streamlit_app.py

import streamlit as st

# Page title
st.title("Indian Apparel Brand Portfolio")
st.markdown("Discover and explore homegrown Indian fashion brands.")

# Sample list of brands
brands = [
    {
        "name": "Fabindia",
        "description": "Handcrafted ethnic apparel from across India.",
        "website": "https://www.fabindia.com",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Fabindia_logo.svg/1280px-Fabindia_logo.svg.png"
    },
    {
        "name": "Raw Mango",
        "description": "Handwoven saris and contemporary textiles.",
        "website": "https://www.rawmango.com",
        "image": "https://www.rawmango.com/logo.png"
    },
    {
        "name": "Suta",
        "description": "Comfortable and conscious clothing.",
        "website": "https://suta.in",
        "image": "https://suta.in/cdn/shop/files/Suta-Logo.png"
    },
    # Add more brands...
]

# Show brand cards
for brand in brands:
    with st.container():
        st.image(brand["image"], width=1500)
        st.subheader(brand["name"])
        st.write(brand["description"])
        st.markdown(f"[Visit Website]({brand['website']})")
        st.markdown("---")