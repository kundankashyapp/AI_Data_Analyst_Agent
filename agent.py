import pandas as pd


class DataAnalystAgent:

    def __init__(self):
        self.name = "AI Data Analyst Agent"
        self.status = "Ready"
        self.data = None

    def welcome(self):
        print("=" * 60)
        print("             AI DATA ANALYST AGENT")
        print("=" * 60)
        print("Agent Name :", self.name)
        print("Status     :", self.status)
        print("=" * 60)

    def load_data(self, file_path):
        try:
            self.data = pd.read_excel(file_path)

            print("\nData loaded successfully!")
            print("Rows    :", self.data.shape[0])
            print("Columns :", self.data.shape[1])

            print("\nColumn Names:")
            print(list(self.data.columns))

        except Exception as e:
            print("\nError while loading data:")
            print(e)

    def show_data(self):
        if self.data is None:
            print("Please load data first.")
            return

        print("\nFirst 5 Rows:")
        print(self.data.head())

    def analyze(self, question):
        print("\nYour Question:")
        print(question)

        print("\nAgent Response:")
        print("I will analyze your data based on your question.")

    def run(self):

        self.welcome()

        # Load Excel file
        self.load_data("data/sales_data.xlsx")

        # Show sample data
        self.show_data()

        # Ask user question
        question = input("\nAsk your data question: ")

        # Analyze question
        self.analyze(question)


# Create Agent
agent = DataAnalystAgent()

# Run Agent
agent.run()