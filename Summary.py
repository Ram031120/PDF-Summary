import streamlit as st
import pandas as pd
from io import BytesIO

def save_to_excel(dataframe, filename):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(label="Download Processed File", data=processed_data, file_name=filename, mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

def main():
    st.title("Excel Data Extractor & Transfer Tool")
    
    uploaded_file = st.file_uploader("Upload your source Excel file", type=["xls", "xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
        
        st.write("### Select Columns to Transfer")
        selected_columns = st.multiselect("Choose columns", df.columns.tolist())
        
        if selected_columns:
            filtered_df = df[selected_columns]
            st.write("Preview of Selected Data:")
            st.dataframe(filtered_df)
            
            save_to_excel(filtered_df, "transferred_data.xlsx")

if __name__ == "__main__":
    main()
