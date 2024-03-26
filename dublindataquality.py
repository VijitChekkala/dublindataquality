import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to calculate data quality score
def calculate_data_quality_score(df):
    # Calculate metrics
    usability_score = (count_meaningful_columns(df) + count_constant_columns(df) + count_valid_features(df)) / 3 * 100
    metadata_score = count_filled_metadata(df) * 100
    freshness_score = calculate_freshness(df) * 100
    completeness_score = calculate_completeness(df) * 100
    accessibility_score = check_accessibility(df) * 100

    # Calculate overall score
    overall_score = (usability_score * 0.38) + (metadata_score * 0.25) + (freshness_score * 0.18) + (completeness_score * 0.12) + (accessibility_score * 0.07)
    overall_score_percentage = overall_score / 100  # Convert overall score back to percentage
    return {
        "Usability": usability_score,
        "Metadata": metadata_score,
        "Freshness": freshness_score,
        "Completeness": completeness_score,
        "Accessibility": accessibility_score,
        "Overall Score": overall_score_percentage
    }

# Calculate proportion of columns with meaningful names
def count_meaningful_columns(df):
    meaningful_columns = sum([1 for col in df.columns if len(col.strip()) > 0])
    return meaningful_columns / len(df.columns)

# Calculate proportion of columns with a constant value
def count_constant_columns(df):
    constant_columns = sum([1 for col in df.columns if df[col].nunique() == 1])
    return constant_columns / len(df.columns)

# Calculate proportion of valid features
def count_valid_features(df):
    # Placeholder function, you should implement this according to your specific criteria
    # For geospatial datasets, you might check if certain columns are within expected ranges or have valid formats
    # This is just a dummy implementation
    return 0.5

# Calculate percent of metadata fields that have been filled out
def count_filled_metadata(df):
    # Placeholder function, you should implement this according to your specific criteria
    # For example, you might check if certain metadata columns are not null
    # This is just a dummy implementation
    return 0.7

# Calculate freshness
def calculate_freshness(df):
    # Placeholder function, you should implement this according to your specific criteria
    # For example, you might compare the publication date with the current date
    # This is just a dummy implementation
    return 0.8

# Calculate completeness
def calculate_completeness(df):
    # Calculate proportion of empty cells
    total_cells = df.size
    empty_cells = df.isnull().sum().sum()
    return (total_cells - empty_cells) / total_cells

# Check accessibility
def check_accessibility(df):
    # Placeholder function, you should implement this according to your specific criteria
    # For example, you might check if the data can be accessed via a specific API
    # This is just a dummy implementation
    return 1.0

# Main function
def main():
    st.title("Data Quality Score Calculator")

    # Upload file
    uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["xls", "xlsx", "csv"])

    if uploaded_file is not None:
        # Read data
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Display data
        st.write("Uploaded Dataset:")
        st.write(df)

        # Calculate data quality score
        data_quality_score = calculate_data_quality_score(df)

        # Display scores
        st.subheader("Data Quality Scores:")
        for metric, score in data_quality_score.items():
            if metric == "Overall Score":
                st.write(f"{metric}: {score * 100:.2f}%")  # Display overall score as percentage
            else:
                st.write(f"{metric}: {score:.2f}%")

        # Display definitions
        st.subheader("Feature Definitions:")
        st.write("**Usability:** Measures how easy it is to work with the data. It includes the proportion of columns with meaningful names, constant values, and valid features.")
        st.write("**Metadata:** Indicates how well the data is described. It's measured by the percent of metadata fields that have been filled out by the publisher.")
        st.write("**Freshness:** Reflects how close the data is to its creation date. It considers the time gap between the expected refresh rate and the actual refresh, and the gap between the last refresh and today.")
        st.write("**Completeness:** Measures how much data is missing. It's calculated as the proportion of empty cells in the dataset.")
        st.write("**Accessibility:** Assesses how easy it is to access the data. For this MVP, it checks whether the data can be accessed via the DataStore API.")

if __name__ == "__main__":
    main()
