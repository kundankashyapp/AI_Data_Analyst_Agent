

import pandas as pd


class DataLoader:

    def __init__(self):

        self.data = None


    # ---------------------------------------------
    # LOAD NORMAL FILE
    # ---------------------------------------------

    def load_file(self, file_path):

        try:

            if file_path.endswith(".csv"):

                self.data = pd.read_csv(file_path)

            elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):

                self.data = pd.read_excel(file_path)

            else:

                print("Unsupported file format.")

                return None

            print("File loaded successfully.")

            return self.data

        except Exception as e:

            print(f"Error loading file: {e}")

            return None


    # ---------------------------------------------
    # LOAD STREAMLIT UPLOADED FILE
    # ---------------------------------------------

    def load_uploaded_file(self, uploaded_file):

        try:

            file_name = uploaded_file.name.lower()

            if file_name.endswith(".csv"):

                self.data = pd.read_csv(uploaded_file)

            elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):

                self.data = pd.read_excel(uploaded_file)

            else:

                return None

                self.data.columns = self.data.columns.str.strip()

            return self.data

        except Exception as e:

            st_error = f"Error loading uploaded file: {e}"

            print(st_error)

            return None


    # ---------------------------------------------
    # GET SUMMARY
    # ---------------------------------------------

    def get_summary(self):

        if self.data is None:

            print("No data loaded.")

            return

        print("\nDataset Summary")
        print("=" * 50)

        print("Rows:", self.data.shape[0])
        print("Columns:", self.data.shape[1])

        print("\nColumn Names:")
        print(self.data.columns.tolist())

        print("\nData Types:")
        print(self.data.dtypes)


    # ---------------------------------------------
    # SHOW PREVIEW
    # ---------------------------------------------

    def show_preview(self):

        if self.data is None:

            print("No data loaded.")

            return

        print("\nData Preview")
        print("=" * 50)

        print(self.data.head())
