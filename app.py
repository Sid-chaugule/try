# Sidebar
st.sidebar.title("📉 Customer Churn Predictor")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Introduction",
        "📊 Predict",
        "ℹ️ About"
    ]
)

# INTRO PAGE
if page == "🏠 Introduction":

    st.title("Customer Churn Prediction")

    st.info("""
Predict whether a telecom customer is likely to leave.
Use customer profile and subscription details.
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model","Logistic Regression")

    with col2:
        st.metric("Features","9")

    with col3:
        st.metric("Goal","Reduce Churn")

# PREDICT PAGE
elif page == "📊 Predict":

    st.title("Customer Prediction")

    with st.container():

        st.subheader("Customer Information")

        col1,col2=st.columns(2)

        with col1:
            age=st.number_input("Age",18,100,35)
            tenure=st.number_input("Tenure",0,120,24)

        with col2:
            gender=st.selectbox(
                "Gender",
                ["Male","Female"]
            )

            contract=st.selectbox(
                "Contract",
                [
                    "Month-to-Month",
                    "One-Year",
                    "Two-Year"
                ]
            )

    if st.button(
        "🔍 Predict",
        use_container_width=True
    ):

        # KEEP YOUR EXISTING MODEL CODE

        if prediction == 1:
            st.error(
                f"⚠ Likely to Churn ({churn_prob:.1f}%)"
            )

        else:
            st.success(
                f"✅ Likely to Stay ({no_churn_prob:.1f}%)"
            )

        tab1,tab2=st.tabs(
            [
                "Result",
                "Feature Values"
            ]
        )

        with tab1:
            st.metric(
                "Churn Probability",
                f"{churn_prob:.1f}%"
            )

            st.progress(
                int(churn_prob)
            )

        with tab2:
            st.dataframe(input_df)

# ABOUT PAGE
else:

    st.title("About")

    st.markdown("""
### Model Pipeline

- Data Cleaning
- Feature Engineering
- Standard Scaling
- SMOTE
- Logistic Regression

### Tech Stack

- Streamlit
- Scikit-learn
- Pandas
- Joblib
""")
