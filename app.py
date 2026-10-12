

# import streamlit as st
# import pandas as pd

# from data_loader import DataLoader
# from Report_generator import ReportGenerator


# # ==================================================
# # PAGE CONFIGURATION
# # ==================================================

# st.set_page_config(
#     page_title="AI Data Analyst Agent",
#     page_icon="🤖",
#     layout="wide"
# )


# # ==================================================
# # TITLE
# # ==================================================

# st.title("🤖 AI Data Analyst Agent")

# st.write(
#     "Upload your CSV/Excel file and analyze, "
#     "clean and visualize your data."
# )


# # ==================================================
# # SESSION STATE
# # ==================================================

# if "cleaned_data" not in st.session_state:
#     st.session_state.cleaned_data = None

# if "file_key" not in st.session_state:
#     st.session_state.file_key = None


# # ==================================================
# # SIDEBAR
# # ==================================================

# st.sidebar.title("📂 Data Analyst")


# # ==================================================
# # FILE UPLOAD
# # ==================================================

# uploaded_file = st.sidebar.file_uploader(
#     "Upload CSV / Excel",
#     type=[
#         "csv",
#         "xlsx",
#         "xls"
#     ]
# )


# # ==================================================
# # COMMAND INPUT
# # ==================================================

# st.sidebar.subheader("💬 Enter Command")

# command = st.sidebar.text_input(
#     "Type your command:",
#     placeholder="/productsales"
# )


# # ==================================================
# # AVAILABLE COMMANDS
# # ==================================================

# st.sidebar.subheader("📋 Available Commands")


# # ------------------------------
# # Sales Metrics
# # ------------------------------

# st.sidebar.markdown("**Sales Metrics**")

# st.sidebar.code("/totalsales")
# st.sidebar.code("/averagesales")
# st.sidebar.code("/maxsales")
# st.sidebar.code("/minsales")


# # ------------------------------
# # Product Analysis
# # ------------------------------

# st.sidebar.markdown("**Product Analysis**")

# st.sidebar.code("/productsales")
# st.sidebar.code("/productavg")
# st.sidebar.code("/productmin")
# st.sidebar.code("/productmax")

# st.sidebar.code("/topproducts")
# st.sidebar.code("/lowestproducts")


# # ------------------------------
# # Profit Analysis
# # ------------------------------

# st.sidebar.markdown("**Profit Metrics**")

# st.sidebar.code("/totalprofit")
# st.sidebar.code("/averageprofit")


# # ------------------------------
# # Region Analysis
# # ------------------------------

# st.sidebar.markdown("**Region Analysis**")

# st.sidebar.code("/regionsales")


# # ------------------------------
# # Help
# # ------------------------------

# st.sidebar.markdown("**Help**")

# st.sidebar.code("/commands")


# # ==================================================
# # CHECK FILE
# # ==================================================

# if uploaded_file is None:

#     st.info(
#         "👈 First upload a CSV or Excel file "
#         "from the left sidebar."
#     )


# else:

#     # ==================================================
#     # CREATE FILE KEY
#     # ==================================================

#     current_file_key = (
#         uploaded_file.name,
#         uploaded_file.size
#     )


#     # ==================================================
#     # LOAD NEW FILE
#     # ==================================================

#     if st.session_state.file_key != current_file_key:

#         loader = DataLoader()

#         loaded_data = loader.load_uploaded_file(
#             uploaded_file
#         )

#         if loaded_data is not None:

#             st.session_state.cleaned_data = (
#                 loaded_data.copy()
#             )

#             st.session_state.file_key = (
#                 current_file_key
#             )


#     # ==================================================
#     # GET CURRENT DATA
#     # ==================================================

#     data = st.session_state.cleaned_data


#     # ==================================================
#     # CHECK DATA
#     # ==================================================

#     if data is None:

#         st.error(
#             "❌ Could not load data."
#         )


#     else:

#         # ==================================================
#         # SUCCESS MESSAGE
#         # ==================================================

#         st.success(
#             f"✅ File loaded successfully: "
#             f"{uploaded_file.name}"
#         )


#         # ==================================================
#         # DATA INFORMATION
#         # ==================================================

#         total_rows = data.shape[0]
#         total_columns = data.shape[1]
#         total_missing = data.isnull().sum().sum()


#         col1, col2, col3 = st.columns(3)


#         with col1:

#             st.metric(
#                 "Total Rows",
#                 total_rows
#             )


#         with col2:

#             st.metric(
#                 "Total Columns",
#                 total_columns
#             )


#         with col3:

#             st.metric(
#                 "Total Missing Values",
#                 total_missing
#             )


#         # ==================================================
#         # COLUMN NAMES
#         # ==================================================

#         st.subheader("📋 Columns in Dataset")


#         column_names = list(data.columns)


#         column_text = " | ".join(
#             [
#                 f"**{column}**"
#                 for column in column_names
#             ]
#         )


#         st.markdown(column_text)


#         # ==================================================
#         # COLUMN DETAILS
#         # ==================================================

#         with st.expander(
#             "🔍 View Column Details"
#         ):

#             for index, column in enumerate(
#                 data.columns,
#                 start=1
#             ):

#                 st.write(
#                     f"{index}. `{column}`"
#                 )


#         # ==================================================
#         # MISSING VALUE ANALYSIS
#         # ==================================================

#         st.subheader(
#             "🔎 Missing Value Analysis"
#         )


#         # --------------------------------------------------
#         # Calculate missing values
#         # --------------------------------------------------

#         missing_count = data.isnull().sum()

#         missing_percentage = (
#             data.isnull().mean() * 100
#         )


#         # --------------------------------------------------
#         # Create summary
#         # --------------------------------------------------

#         missing_summary = pd.DataFrame({

#             "Column":
#                 data.columns,

#             "Missing Values":
#                 missing_count.values,

#             "Missing %":
#                 missing_percentage.values
#         })


#         # --------------------------------------------------
#         # Only columns with missing values
#         # --------------------------------------------------

#         missing_columns = (
#             missing_summary[
#                 missing_summary["Missing Values"] > 0
#             ]
#         )


#         # ==================================================
#         # NO MISSING VALUES
#         # ==================================================

#         if missing_columns.empty:

#             st.success(
#                 "✅ Great! No missing values found "
#                 "in your dataset."
#             )


#         # ==================================================
#         # MISSING VALUES FOUND
#         # ==================================================

#         else:

#             st.warning(
#                 f"⚠️ Missing values found in "
#                 f"{len(missing_columns)} column(s)."
#             )


#             # --------------------------------------------------
#             # Missing values by column
#             # --------------------------------------------------

#             st.markdown(
#                 "### 📋 Missing Values by Column"
#             )


#             st.dataframe(
#                 missing_columns,
#                 use_container_width=True,
#                 hide_index=True
#             )


#             # --------------------------------------------------
#             # Missing value chart
#             # --------------------------------------------------

#             st.markdown(
#                 "### 📊 Missing Values Chart"
#             )


#             chart_data = (
#                 missing_columns[
#                     ["Column", "Missing Values"]
#                 ]
#                 .set_index("Column")
#             )


#             st.bar_chart(
#                 chart_data
#             )


#             # ==================================================
#             # ROWS WITH MISSING VALUES
#             # ==================================================

#             st.markdown(
#                 "### 🔍 Rows Containing Missing Values"
#             )


#             rows_with_missing = data[
#                 data.isnull().any(axis=1)
#             ]


#             rows_with_missing_display = (
#                 rows_with_missing.copy()
#             )


#             rows_with_missing_display.insert(
#                 0,
#                 "Row Number",
#                 rows_with_missing_display.index + 1
#             )


#             st.dataframe(
#                 rows_with_missing_display,
#                 use_container_width=True,
#                 hide_index=True
#             )


#             # ==================================================
#             # MISSING COLUMNS BY ROW
#             # ==================================================

#             st.markdown(
#                 "### 🧭 Missing Columns by Row"
#             )


#             missing_details = []


#             for index, row in data.iterrows():

#                 missing_columns_in_row = [
#                     column
#                     for column in data.columns
#                     if pd.isna(row[column])
#                 ]


#                 if missing_columns_in_row:

#                     missing_details.append({

#                         "Row Number":
#                             index + 1,

#                         "Missing Columns":
#                             ", ".join(
#                                 missing_columns_in_row
#                             )
#                     })


#             missing_details_df = pd.DataFrame(
#                 missing_details
#             )


#             st.dataframe(
#                 missing_details_df,
#                 use_container_width=True,
#                 hide_index=True
#             )


#             # ==================================================
#             # FILL MISSING VALUES
#             # ==================================================

#             st.divider()

#             st.subheader(
#                 "🧹 Fill / Handle Missing Values"
#             )


#             st.write(
#                 "Select the columns and method you want "
#                 "to use for handling missing values."
#             )


#             # ==================================================
#             # AVAILABLE COLUMNS WITH MISSING VALUES
#             # ==================================================

#             columns_with_missing = (
#                 missing_columns["Column"]
#                 .tolist()
#             )


#             selected_columns = st.multiselect(

#                 "Select columns:",

#                 options=columns_with_missing,

#                 default=columns_with_missing
#             )


#             # ==================================================
#             # SELECT METHOD
#             # ==================================================

#             method = st.selectbox(

#                 "Select method:",

#                 [
#                     "Mean (Average)",
#                     "Median",
#                     "Mode",
#                     "Fill with 0",
#                     "Remove Rows"
#                 ]
#             )


#             # ==================================================
#             # METHOD EXPLANATION
#             # ==================================================

#             if method == "Mean (Average)":

#                 st.info(
#                     "Mean fills missing numeric values "
#                     "using the average of that column."
#                 )

#             elif method == "Median":

#                 st.info(
#                     "Median fills missing numeric values "
#                     "using the middle value of that column."
#                 )

#             elif method == "Mode":

#                 st.info(
#                     "Mode fills missing values using "
#                     "the most frequently occurring value."
#                 )

#             elif method == "Fill with 0":

#                 st.info(
#                     "Missing numeric values will be replaced "
#                     "with 0."
#                 )

#             elif method == "Remove Rows":

#                 st.info(
#                     "Rows containing missing values in "
#                     "the selected columns will be removed."
#                 )


#             # ==================================================
#             # APPLY BUTTON
#             # ==================================================

#             if st.button(
#                 "🔧 Apply Missing Value Treatment",
#                 type="primary"
#             ):

#                 if not selected_columns:

#                     st.error(
#                         "❌ Please select at least one column."
#                     )

#                 else:

#                     # Make a copy
#                     new_data = data.copy()

#                     changed_columns = []

#                     removed_rows = 0


#                     # ==================================================
#                     # MEAN
#                     # ==================================================

#                     if method == "Mean (Average)":

#                         for column in selected_columns:

#                             if pd.api.types.is_numeric_dtype(
#                                 new_data[column]
#                             ):

#                                 missing_before = (
#                                     new_data[column]
#                                     .isnull()
#                                     .sum()
#                                 )

#                                 if missing_before > 0:

#                                     mean_value = (
#                                         new_data[column]
#                                         .mean()
#                                     )

#                                     new_data[column] = (
#                                         new_data[column]
#                                         .fillna(mean_value)
#                                     )

#                                     changed_columns.append(
#                                         column
#                                     )

#                             else:

#                                 st.warning(
#                                     f"⚠️ `{column}` is not "
#                                     f"a numeric column. "
#                                     f"Mean cannot be used."
#                                 )


#                     # ==================================================
#                     # MEDIAN
#                     # ==================================================

#                     elif method == "Median":

#                         for column in selected_columns:

#                             if pd.api.types.is_numeric_dtype(
#                                 new_data[column]
#                             ):

#                                 missing_before = (
#                                     new_data[column]
#                                     .isnull()
#                                     .sum()
#                                 )

#                                 if missing_before > 0:

#                                     median_value = (
#                                         new_data[column]
#                                         .median()
#                                     )

#                                     new_data[column] = (
#                                         new_data[column]
#                                         .fillna(median_value)
#                                     )

#                                     changed_columns.append(
#                                         column
#                                     )

#                             else:

#                                 st.warning(
#                                     f"⚠️ `{column}` is not "
#                                     f"a numeric column. "
#                                     f"Median cannot be used."
#                                 )


#                     # ==================================================
#                     # MODE
#                     # ==================================================

#                     elif method == "Mode":

#                         for column in selected_columns:

#                             missing_before = (
#                                 new_data[column]
#                                 .isnull()
#                                 .sum()
#                             )

#                             if missing_before > 0:

#                                 mode_values = (
#                                     new_data[column]
#                                     .mode()
#                                 )

#                                 if not mode_values.empty:

#                                     mode_value = (
#                                         mode_values.iloc[0]
#                                     )

#                                     new_data[column] = (
#                                         new_data[column]
#                                         .fillna(mode_value)
#                                     )

#                                     changed_columns.append(
#                                         column
#                                     )


#                     # ==================================================
#                     # FILL WITH ZERO
#                     # ==================================================

#                     elif method == "Fill with 0":

#                         for column in selected_columns:

#                             if pd.api.types.is_numeric_dtype(
#                                 new_data[column]
#                             ):

#                                 missing_before = (
#                                     new_data[column]
#                                     .isnull()
#                                     .sum()
#                                 )

#                                 if missing_before > 0:

#                                     new_data[column] = (
#                                         new_data[column]
#                                         .fillna(0)
#                                     )

#                                     changed_columns.append(
#                                         column
#                                     )

#                             else:

#                                 st.warning(
#                                     f"⚠️ `{column}` is not "
#                                     f"a numeric column. "
#                                     f"0 cannot be used."
#                                 )


#                     # ==================================================
#                     # REMOVE ROWS
#                     # ==================================================

#                     elif method == "Remove Rows":

#                         rows_before = len(new_data)

#                         new_data = (
#                             new_data
#                             .dropna(
#                                 subset=selected_columns
#                             )
#                             .reset_index(drop=True)
#                         )

#                         removed_rows = (
#                             rows_before
#                             - len(new_data)
#                         )


#                     # ==================================================
#                     # SAVE CLEANED DATA
#                     # ==================================================

#                     st.session_state.cleaned_data = (
#                         new_data
#                     )


#                     # ==================================================
#                     # SUCCESS MESSAGE
#                     # ==================================================

#                     if method == "Remove Rows":

#                         st.success(
#                             f"✅ Missing-value treatment "
#                             f"completed. "
#                             f"{removed_rows} row(s) removed."
#                         )

#                     elif changed_columns:

#                         st.success(
#                             "✅ Missing values filled "
#                             "successfully in: "
#                             + ", ".join(
#                                 changed_columns
#                             )
#                         )

#                     else:

#                         st.warning(
#                             "⚠️ No values were changed."
#                         )


#                     # ==================================================
#                     # SHOW NEW MISSING COUNT
#                     # ==================================================

#                     new_missing = (
#                         new_data
#                         .isnull()
#                         .sum()
#                         .sum()
#                     )


#                     st.metric(
#                         "Remaining Missing Values",
#                         new_missing
#                     )


#                     # ==================================================
#                     # SHOW CLEANED DATA
#                     # ==================================================

#                     st.markdown(
#                         "### 🧹 Cleaned Dataset"
#                     )


#                     st.dataframe(
#                         new_data,
#                         use_container_width=True,
#                         hide_index=True
#                     )


#         # ==================================================
#         # DATA PREVIEW
#         # ==================================================

#         st.subheader(
#             "📊 Data Preview"
#         )


#         st.dataframe(
#             data.head(10),
#             use_container_width=True
#         )


#         # ==================================================
#         # CREATE REPORT GENERATOR
#         # ==================================================

#         report = ReportGenerator(data)


#         # ==================================================
#         # ANALYSIS
#         # ==================================================

#         if command:

#             st.subheader(
#                 "📈 Analysis Result"
#             )


#             # ==================================================
#             # EXECUTE COMMAND
#             # ==================================================

#             result, chart = (
#                 report.execute_command(
#                     command
#                 )
#             )


#             # ==================================================
#             # STRING RESULT
#             # ==================================================

#             if isinstance(result, str):

#                 st.success(result)


#             # ==================================================
#             # DICTIONARY RESULT
#             # ==================================================

#             elif isinstance(result, dict):

#                 st.json(result)


#             # ==================================================
#             # TABLE + CHART RESULT
#             # ==================================================

#             else:

#                 left_column, right_column = (
#                     st.columns(2)
#                 )


#                 # ----------------------------------------------
#                 # TABLE
#                 # ----------------------------------------------

#                 with left_column:

#                     st.markdown(
#                         "### 📋 Calculation"
#                     )


#                     st.dataframe(
#                         result,
#                         use_container_width=True,
#                         hide_index=True
#                     )


#                 # ----------------------------------------------
#                 # CHART
#                 # ----------------------------------------------

#                 with right_column:

#                     if chart is not None:

#                         st.markdown(
#                             "### 📊 Chart"
#                         )


#                         st.plotly_chart(
#                             chart,
#                             use_container_width=True
#                         )


#         # ==================================================
#         # NO COMMAND
#         # ==================================================

#         else:

#             st.info(
#                 "👈 Type a command in the left sidebar.\n\n"
#                 "Example: `/productsales`"
#             )




import streamlit as st
import pandas as pd

from data_loader import DataLoader
from Report_generator import ReportGenerator


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Data Analyst Agent",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("🤖 AI Data Analyst Agent")

st.write(
    "Upload your CSV/Excel file and enter a command "
    "to analyze your data."
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📂 Data Analyst")


# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV / Excel",
    type=[
        "csv",
        "xlsx",
        "xls"
    ]
)


# ==================================================
# COMMAND INPUT
# ==================================================

st.sidebar.subheader("💬 Enter Command")

command = st.sidebar.text_input(
    "Type your command:",
    placeholder="/productsales"
)


# ==================================================
# AVAILABLE COMMANDS
# ==================================================

st.sidebar.subheader("📋 Available Commands")


# ------------------------------
# Sales Metrics
# ------------------------------

st.sidebar.markdown("**Sales Metrics**")

st.sidebar.code("/totalsales")
st.sidebar.code("/averagesales")
st.sidebar.code("/maxsales")
st.sidebar.code("/minsales")


# ------------------------------
# Product Analysis
# ------------------------------

st.sidebar.markdown("**Product Analysis**")

st.sidebar.code("/productsales")
st.sidebar.code("/productavg")
st.sidebar.code("/productmin")
st.sidebar.code("/productmax")

st.sidebar.code("/topproducts")
st.sidebar.code("/lowestproducts")


# ------------------------------
# Profit Analysis
# ------------------------------

st.sidebar.markdown("**Profit Metrics**")

st.sidebar.code("/totalprofit")
st.sidebar.code("/averageprofit")


# ------------------------------
# Region Analysis
# ------------------------------

st.sidebar.markdown("**Region Analysis**")

st.sidebar.code("/regionsales")


# ------------------------------
# Help
# ------------------------------

st.sidebar.markdown("**Help**")

st.sidebar.code("/commands")


# ==================================================
# CHECK FILE
# ==================================================

if uploaded_file is None:

    st.info(
        "👈 First upload a CSV or Excel file "
        "from the left sidebar."
    )


# ==================================================
# PROCESS FILE
# ==================================================

else:

    # ==================================================
    # LOAD DATA
    # ==================================================

    loader = DataLoader()

    data = loader.load_uploaded_file(
        uploaded_file
    )


    # ==================================================
    # CHECK DATA
    # ==================================================

    if data is None:

        st.error(
            "❌ Could not load data."
        )


    else:

        # ==================================================
        # SUCCESS MESSAGE
        # ==================================================

        st.success(
            f"✅ File loaded successfully: "
            f"{uploaded_file.name}"
        )


        # ==================================================
        # DATA INFORMATION
        # ==================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Total Rows",
                data.shape[0]
            )


        with col2:

            st.metric(
                "Total Columns",
                data.shape[1]
            )


        with col3:

            total_missing = data.isnull().sum().sum()

            st.metric(
                "Total Missing Values",
                total_missing
            )


        # ==================================================
        # COLUMN NAMES
        # ==================================================

        st.subheader("📋 Columns in Dataset")

        column_names = list(data.columns)

        column_text = " | ".join(
            [f"**{column}**" for column in column_names]
        )

        st.markdown(column_text)


        # ==================================================
        # COLUMN DETAILS
        # ==================================================

        with st.expander("🔍 View Column Details"):

            for index, column in enumerate(
                data.columns,
                start=1
            ):

                st.write(
                    f"{index}. `{column}`"
                )


        # ==================================================
        # MISSING VALUE ANALYSIS
        # ==================================================

        st.subheader("🔎 Missing Value Analysis")


        # --------------------------------------------------
        # Calculate missing values column-wise
        # --------------------------------------------------

        missing_count = data.isnull().sum()

        missing_percentage = (
            data.isnull().mean() * 100
        )


        # --------------------------------------------------
        # Create missing value summary
        # --------------------------------------------------

        missing_summary = pd.DataFrame({
            "Column": data.columns,
            "Missing Values": missing_count.values,
            "Missing %": missing_percentage.values
        })


        # --------------------------------------------------
        # Show only columns having missing values
        # --------------------------------------------------

        missing_columns = missing_summary[
            missing_summary["Missing Values"] > 0
        ]


        # ==================================================
        # NO MISSING VALUES
        # ==================================================

        if missing_columns.empty:

            st.success(
                "✅ Great! No missing values found "
                "in your dataset."
            )


        # ==================================================
        # MISSING VALUES FOUND
        # ==================================================

        else:

            st.warning(
                f"⚠️ Missing values found in "
                f"{len(missing_columns)} column(s)."
            )


            # --------------------------------------------------
            # Missing value table
            # --------------------------------------------------

            st.markdown(
                "### 📋 Missing Values by Column"
            )

            st.dataframe(
                missing_columns,
                use_container_width=True,
                hide_index=True
            )


            # --------------------------------------------------
            # Missing value chart
            # --------------------------------------------------

            st.markdown(
                "### 📊 Missing Values Chart"
            )

            chart_data = missing_columns[
                ["Column", "Missing Values"]
            ].set_index("Column")

            st.bar_chart(
                chart_data
            )


            # ==================================================
            # FIND ROWS WITH MISSING VALUES
            # ==================================================

            st.markdown(
                "### 🔍 Rows Containing Missing Values"
            )


            # --------------------------------------------------
            # Get rows where at least one value is missing
            # --------------------------------------------------

            rows_with_missing = data[
                data.isnull().any(axis=1)
            ]


            # --------------------------------------------------
            # Add original Excel/DataFrame row number
            # --------------------------------------------------

            rows_with_missing_display = (
                rows_with_missing.copy()
            )

            rows_with_missing_display.insert(
                0,
                "Row Number",
                rows_with_missing_display.index + 1
            )


            # --------------------------------------------------
            # Show rows
            # --------------------------------------------------

            st.dataframe(
                rows_with_missing_display,
                use_container_width=True,
                hide_index=True
            )


            # ==================================================
            # SHOW WHICH COLUMN IS MISSING IN EACH ROW
            # ==================================================

            st.markdown(
                "### 🧭 Missing Columns by Row"
            )


            missing_details = []


            for index, row in data.iterrows():

                missing_columns_in_row = [
                    column
                    for column in data.columns
                    if pd.isna(row[column])
                ]


                if missing_columns_in_row:

                    missing_details.append({
                        "Row Number": index + 1,
                        "Missing Columns":
                            ", ".join(
                                missing_columns_in_row
                            )
                    })


            missing_details_df = pd.DataFrame(
                missing_details
            )


            st.dataframe(
                missing_details_df,
                use_container_width=True,
                hide_index=True
            )


        # ==================================================
        # DATA PREVIEW
        # ==================================================

        st.subheader("📊 Data Preview")

        st.dataframe(
            data.head(10),
            use_container_width=True
        )


        # ==================================================
        # CREATE REPORT GENERATOR
        # ==================================================

        report = ReportGenerator(data)


        # ==================================================
        # ANALYSIS
        # ==================================================

        if command:

            st.subheader("📈 Analysis Result")


            # ==================================================
            # EXECUTE COMMAND
            # ==================================================

            result, chart = report.execute_command(
                command
            )


            # ==================================================
            # STRING RESULT
            # ==================================================

            if isinstance(result, str):

                st.success(result)


            # ==================================================
            # DICTIONARY RESULT
            # ==================================================

            elif isinstance(result, dict):

                st.json(result)


            # ==================================================
            # TABLE + CHART RESULT
            # ==================================================

            else:

                left_column, right_column = st.columns(
                    2
                )


                # ----------------------------------------------
                # TABLE
                # ----------------------------------------------

                with left_column:

                    st.markdown(
                        "### 📋 Calculation"
                    )

                    st.dataframe(
                        result,
                        use_container_width=True,
                        hide_index=True
                    )


                # ----------------------------------------------
                # CHART
                # ----------------------------------------------

                with right_column:

                    if chart is not None:

                        st.markdown(
                            "### 📊 Chart"
                        )

                        st.plotly_chart(
                            chart,
                            use_container_width=True
                        )


        # ==================================================
        # NO COMMAND
        # ==================================================

        else:

            st.info(
                "👈 Type a command in the left sidebar.\n\n"
                "Example: `/productsales`"
            )