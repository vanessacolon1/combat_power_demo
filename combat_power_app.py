import streamlit as st
import pandas as pd
import os

DATA_FILE = "combat_power.csv"
# Mapping for readability
col_map = {
    "uic": "Unit ID",
    "uic_hierarchy": "Hierarchy",
    "uic_name": "Unit Name",
    "oh_gcss": "On-Hand Equipment",
    "total_fmc_gcss": "Fully Mission Capable",
    "total_nmc_supply": "NMC Supply",
    "total_nmc_maintenance": "NMC Maintenance",
    "equipment_description": "Equipment Description",
    "model": "Model"
}

# Load dataset with caching
@st.cache_data
def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, sep="\t")
        df.rename(columns=col_map, inplace=True)  # adjust if tab-delimited
        return df
    else:
        st.warning(f"{DATA_FILE} not found. Please upload your dataset.")
        return None

# Save dataset back to CSV
def save_data(df):
    df.to_csv(DATA_FILE, sep="\t", index=False)
    st.success("Changes saved to combat_power.csv!")

# Streamlit app
def main():
    st.sidebar.title("Combat Power Dashboard")
    page = st.sidebar.radio(
        "Navigation",
        ["Home", "Search UIC", "Update Combat Power", "Analysis"]
    )

    df = load_data()
    if df is None:
        uploaded_file = st.file_uploader("Upload combat_power.csv", type=["csv", "tsv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file, sep="\t")
            st.success("Dataset loaded successfully.")

    if df is not None:
        if page == "Home":
            st.title("Combat Power Dashboard")
            st.write("This dashboard allows commanders to view and update combat power data across units.")
            st.dataframe(df.head())

        elif page == "Search UIC":
            st.title("Search Unit by UIC")
            uic = st.text_input("Enter your UIC")
            if uic:
                unit = df[df['Unit ID'] == uic]
                if not unit.empty:
                    st.write(f"### {unit.iloc[0]['Unit Name']}")
                    st.dataframe(unit[['On-Hand Equipment', 'Fully Mission Capable', 'NMC Supply', 'NMC Maintenance']])
                else:
                    st.warning("UIC not found.")

        elif page == "Update Combat Power":
            st.title("Update Combat Power for UIC")
            uic = st.text_input("Enter your UIC to update")
            if uic:
                idx = df[df['uic'] == uic].index
                if not idx.empty:
                    idx = idx[0]
                    st.write(f"### Current values for {df.loc[idx,'Unit Name']}")
                    st.dataframe(df.loc[idx, ['Fully Mission Capable','NMC Supply','NMC Maintenance']])
                    
                    # Inputs for updating values
                    total_fmc = st.number_input("Total FMC GCSS", value=int(df.loc[idx,'Fully Mission Capable']))
                    total_nmc_supply = st.number_input("Total NMC Supply", value=int(df.loc[idx,'NMC Supply']))
                    total_nmc_maintenance = st.number_input("Total NMC Maintenance", value=int(df.loc[idx,'NMC Maintenance']))

                    if st.button("Update Combat Power"):
                        df.loc[idx,'Fully Mission Capable'] = total_fmc
                        df.loc[idx,'NMC Supply'] = total_nmc_supply
                        df.loc[idx,'NMC Maintenance'] = total_nmc_maintenance
                        save_data(df)
                        st.write("### Updated Values")
                        st.dataframe(df.loc[idx, ['Fully Mission Capable','NMC Supply','NMC Maintenance']])
                else:
                    st.warning("UIC not found.")

        elif page == "Analysis":
            st.title("Combat Power Analysis")

            st.write("### Aggregate by UIC")
            hierarchy = st.selectbox("Select Unit", df['Unit ID'].unique())
            hierarchy_df = df[df['Unit ID'] == hierarchy]

            st.write("#### Total FMC, NMC by Unit")
            agg_df = hierarchy_df.groupby('Unit Name')[['Fully Mission Capable','NMC Supply','NMC Maintenance']].sum()
            st.dataframe(agg_df)

            st.bar_chart(agg_df)

            st.write("### Overall Summary")
            st.dataframe(df[['On-Hand Equipment','Fully Mission Capable','NMC Supply','NMC Maintenance']].describe())

if __name__ == "__main__":
    main()
