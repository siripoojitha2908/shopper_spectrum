import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #E3F2FD, #EDE7F6);
}

[data-testid="stSidebar"] {
    background-color: #D1C4E9;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Shopper Spectrum", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#1E88E5;'>🛒 Shopper Spectrum</h1>",
    unsafe_allow_html=True
)
st.write("Customer Segmentation & Product Recommendation System")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Module",
    ["Home", "Customer Segmentation", "Product Recommendation"]
)

if page == "Home":
    st.header("Welcome")
    st.write("This application provides:")
    st.write("• Customer Segmentation using RFM Analysis")
    st.write("• Product Recommendation using Collaborative Filtering")

elif page == "Customer Segmentation":

    st.header("📊 Customer Segmentation")

    recency = st.number_input(
        "Recency (days since last purchase)",
        min_value=0,
        value=30
    )

    frequency = st.number_input(
        "Frequency (number of purchases)",
        min_value=0,
        value=5
    )

    monetary = st.number_input(
        "Monetary (total spend)",
        min_value=0.0,
        value=1000.0
    )

    if st.button("Predict Segment"):

        if frequency > 20 and monetary > 5000 and recency < 30:
            segment = "🏆 High Value Customer"

        elif frequency > 10 and monetary > 2000:
            segment = "⭐ Regular Customer"

        elif recency > 180:
            segment = "⚠️ At Risk Customer"

        else:
            segment = "🛒 Occasional Shopper"

        st.success(f"This customer belongs to: {segment}")


elif page == "Product Recommendation":

    st.header("Product Recommendation")

    product = st.text_input("Enter Product Name")

    if st.button("Get Recommendations"):

        recommendations = {
            "Laptop": ["Wireless Mouse", "Laptop Bag", "Cooling Pad", "USB Hub", "External Hard Drive"],
            "Mobile": ["Phone Case", "Power Bank", "Screen Guard", "Wireless Earbuds", "Mobile Stand"],
            "Shoes": ["Socks", "Shoe Cleaner", "Insoles", "Shoe Bag", "Foot Spray"],
            "Watch": ["Watch Strap", "Watch Box", "Screen Protector", "Cleaning Kit", "Travel Case"]
        }

        if product in recommendations:
            st.success("Recommended Products:")
            for item in recommendations[product]:
                st.write("•", item)

        else:
            st.warning("No recommendations available")