import streamlit as st
import numpy as np
import pickle


# Load Train Kmeans Model
kmeans = pickle.load(open("kmeans.pkl",'rb'))

# Simple clustering function
def clustering(age, avg_spend, visit_per_week, promotion_interest):
    new_customer = np.array([[age, avg_spend, visit_per_week, promotion_interest]])
    predicted_cluster = kmeans.predict(new_customer)

    if predicted_cluster[0] == 0:
        return "Daily"
    elif predicted_cluster[0] == 1:
        return "Weekend"
    else:
        return "Promotion"


# Streamlit app here==========================================
st.title("Customer Clustering App")
st.write("Enter the customer details:")

# User input (side by side inputs

# row 1 with column 2
col1, col2 = st.columns(2)
with col1:
    st.subheader("Customer Age")
    age = st.number_input("Age", min_value=18, max_value=100, value=40)

with col2:
    st.subheader("Customer Spent Time")
    avg_spend = st.number_input("Average Spend", min_value=0.0, max_value=1000.0, value=30.0)

# row 2 with column 2
col1, col2 = st.columns(2)
with col1:
    st.subheader("Visits per week")
    visit_per_week = st.number_input("Visits per Week", min_value=0, max_value=20, value=4)

with col2:
    st.subheader("Promotion Interest")
    promotion_interest = st.number_input("Promotion Interest", min_value=0, max_value=10, value=7)


# Predict button
if st.button("Predict Cluster"):
    cluster_label = clustering(age, avg_spend, visit_per_week, promotion_interest)
    st.success(f'The customer belongs to the "{cluster_label}" cluster.')


