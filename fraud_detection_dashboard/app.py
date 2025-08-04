import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 Financial Fraud Detection Dashboard")
st.markdown("Upload your transaction file and view fraud predictions, performance metrics, and insights.")

# Upload CSV
uploaded_file = st.file_uploader("Upload prediction CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Show raw data
    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # Fraud count summary
    st.subheader("🔍 Fraud vs Non-Fraud Count")
    fraud_counts = df['isFraud'].value_counts().rename({0: "Not Fraud", 1: "Fraud"})
    st.bar_chart(fraud_counts)

    # Prediction Accuracy
    st.subheader("📊 Prediction Accuracy")
    correct = (df['isFraud'] == df['prediction']).sum()
    total = len(df)
    accuracy = correct / total
    st.metric("Model Accuracy", f"{accuracy * 100:.2f}%")

    # Feature Importance - Use hardcoded importance from previous step
    st.subheader("🧠 Feature Importance (Random Forest)")
    importance_data = {
        "Feature": ["oldbalanceOrg", "newbalanceDest", "amount", "newbalanceOrig", "oldbalanceDest", "type_index"],
        "Importance": [0.5028, 0.1565, 0.1474, 0.0974, 0.0643, 0.0316]
    }
    importance_df = pd.DataFrame(importance_data).sort_values(by="Importance", ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="Importance", y="Feature", data=importance_df, ax=ax)
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    # Optional: Show prediction probabilities
    st.subheader("🧪 Sample Prediction Probabilities")
    st.dataframe(df[["isFraud", "prediction", "probability"]].head())

else:
    st.info("⬆️ Upload the `rf_predictions_output.csv` file to begin.")
