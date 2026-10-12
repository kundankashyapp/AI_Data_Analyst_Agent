

import pandas as pd
import plotly.express as px


class ReportGenerator:

    def __init__(self, data):

        self.data = data.copy()

        # ==================================================
        # CLEAN COLUMN NAMES
        # ==================================================

        self.data.columns = (
            self.data.columns
            .astype(str)
            .str.strip()
        )

        # ==================================================
        # COLUMN MAPPING
        # ==================================================

        self.column_map = {
            column.lower(): column
            for column in self.data.columns
        }

    # ==================================================
    # FIND COLUMN
    # ==================================================

    def get_column(self, column_name):

        return self.column_map.get(
            column_name.lower()
        )

    # ==================================================
    # CHECK DATA
    # ==================================================

    def check_data(self):

        if self.data is None:
            return False

        if self.data.empty:
            return False

        return True

    # ==================================================
    # TOTAL SALES
    # ==================================================

    def total_sales(self):

        if not self.check_data():
            return "No data available."

        sales_column = self.get_column("Sales")

        if sales_column is None:
            return "Sales column not found."

        total = self.data[sales_column].sum()

        return f"Total Sales: {total:,.2f}"

    # ==================================================
    # AVERAGE SALES
    # ==================================================

    def average_sales(self):

        if not self.check_data():
            return "No data available."

        sales_column = self.get_column("Sales")

        if sales_column is None:
            return "Sales column not found."

        average = self.data[sales_column].mean()

        return f"Average Sales: {average:,.2f}"

    # ==================================================
    # MAXIMUM SALES
    # ==================================================

    def maximum_sales(self):

        if not self.check_data():
            return "No data available."

        sales_column = self.get_column("Sales")

        if sales_column is None:
            return "Sales column not found."

        maximum = self.data[sales_column].max()

        return f"Maximum Sales: {maximum:,.2f}"

    # ==================================================
    # MINIMUM SALES
    # ==================================================

    def minimum_sales(self):

        if not self.check_data():
            return "No data available."

        sales_column = self.get_column("Sales")

        if sales_column is None:
            return "Sales column not found."

        minimum = self.data[sales_column].min()

        return f"Minimum Sales: {minimum:,.2f}"

    # ==================================================
    # PRODUCT-WISE TOTAL SALES
    # ==================================================

    def product_sales(self):

        if not self.check_data():
            return None

        product_column = self.get_column("Product")
        sales_column = self.get_column("Sales")

        if product_column is None:
            return "Product column not found."

        if sales_column is None:
            return "Sales column not found."

        result = (
            self.data
            .groupby(product_column)[sales_column]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        result.columns = [
            "Product",
            "Total Sales"
        ]

        return result

    # ==================================================
    # PRODUCT-WISE AVERAGE SALES
    # ==================================================

    def product_average_sales(self):

        if not self.check_data():
            return None

        product_column = self.get_column("Product")
        sales_column = self.get_column("Sales")

        if product_column is None:
            return "Product column not found."

        if sales_column is None:
            return "Sales column not found."

        result = (
            self.data
            .groupby(product_column)[sales_column]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        result.columns = [
            "Product",
            "Average Sales"
        ]

        return result

    # ==================================================
    # PRODUCT-WISE MINIMUM SALES
    # ==================================================

    def product_min_sales(self):

        if not self.check_data():
            return None

        product_column = self.get_column("Product")
        sales_column = self.get_column("Sales")

        if product_column is None:
            return "Product column not found."

        if sales_column is None:
            return "Sales column not found."

        result = (
            self.data
            .groupby(product_column)[sales_column]
            .min()
            .sort_values(ascending=True)
            .reset_index()
        )

        result.columns = [
            "Product",
            "Minimum Sales"
        ]

        return result

    # ==================================================
    # PRODUCT-WISE MAXIMUM SALES
    # ==================================================

    def product_max_sales(self):

        if not self.check_data():
            return None

        product_column = self.get_column("Product")
        sales_column = self.get_column("Sales")

        if product_column is None:
            return "Product column not found."

        if sales_column is None:
            return "Sales column not found."

        result = (
            self.data
            .groupby(product_column)[sales_column]
            .max()
            .sort_values(ascending=False)
            .reset_index()
        )

        result.columns = [
            "Product",
            "Maximum Sales"
        ]

        return result

    # ==================================================
    # TOP PRODUCTS
    # ==================================================

    def top_products(self, n=10):

        result = self.product_sales()

        if isinstance(result, str):
            return result

        return result.head(n)

    # ==================================================
    # LOWEST PRODUCTS
    # ==================================================

    def lowest_products(self, n=10):

        result = self.product_sales()

        if isinstance(result, str):
            return result

        return (
            result
            .sort_values(
                "Total Sales",
                ascending=True
            )
            .head(n)
        )

    # ==================================================
    # TOTAL PROFIT
    # ==================================================

    def total_profit(self):

        if not self.check_data():
            return "No data available."

        profit_column = self.get_column("Profit")

        if profit_column is None:
            return "Profit column not found."

        total = self.data[profit_column].sum()

        return f"Total Profit: {total:,.2f}"

    # ==================================================
    # AVERAGE PROFIT
    # ==================================================

    def average_profit(self):

        if not self.check_data():
            return "No data available."

        profit_column = self.get_column("Profit")

        if profit_column is None:
            return "Profit column not found."

        average = self.data[profit_column].mean()

        return f"Average Profit: {average:,.2f}"

    # ==================================================
    # REGION-WISE SALES
    # ==================================================

    def region_sales(self):

        if not self.check_data():
            return None

        region_column = self.get_column("Region")
        sales_column = self.get_column("Sales")

        if region_column is None:
            return "Region column not found."

        if sales_column is None:
            return "Sales column not found."

        result = (
            self.data
            .groupby(region_column)[sales_column]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        result.columns = [
            "Region",
            "Total Sales"
        ]

        return result

    # ==================================================
    # PRODUCT TOTAL SALES CHART
    # ==================================================

    def product_sales_chart(self):

        result = self.product_sales()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Total Sales",
            title="Product-wise Total Sales",
            text="Total Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Total Sales"
        )

        return fig

    # ==================================================
    # PRODUCT AVERAGE SALES CHART
    # ==================================================

    def product_average_sales_chart(self):

        result = self.product_average_sales()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Average Sales",
            title="Product-wise Average Sales",
            text="Average Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Average Sales"
        )

        return fig

    # ==================================================
    # PRODUCT MINIMUM SALES CHART
    # ==================================================

    def product_min_sales_chart(self):

        result = self.product_min_sales()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Minimum Sales",
            title="Product-wise Minimum Sales",
            text="Minimum Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Minimum Sales"
        )

        return fig

    # ==================================================
    # PRODUCT MAXIMUM SALES CHART
    # ==================================================

    def product_max_sales_chart(self):

        result = self.product_max_sales()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Maximum Sales",
            title="Product-wise Maximum Sales",
            text="Maximum Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Maximum Sales"
        )

        return fig

    # ==================================================
    # TOP PRODUCTS CHART
    # ==================================================

    def top_products_chart(self):

        result = self.top_products()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Total Sales",
            title="Top 10 Products by Sales",
            text="Total Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Total Sales"
        )

        return fig

    # ==================================================
    # LOWEST PRODUCTS CHART
    # ==================================================

    def lowest_products_chart(self):

        result = self.lowest_products()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Product",
            y="Total Sales",
            title="Lowest 10 Products by Sales",
            text="Total Sales"
        )

        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Total Sales"
        )

        return fig

    # ==================================================
    # REGION SALES CHART
    # ==================================================

    def region_sales_chart(self):

        result = self.region_sales()

        if isinstance(result, str):
            return None

        fig = px.bar(
            result,
            x="Region",
            y="Total Sales",
            title="Region-wise Total Sales",
            text="Total Sales"
        )

        fig.update_layout(
            xaxis_title="Region",
            yaxis_title="Total Sales"
        )

        return fig

    # ==================================================
    # AVAILABLE COMMANDS
    # ==================================================

    def available_commands(self):

        return {
            "/totalsales":
                "Calculate total sales",

            "/averagesales":
                "Calculate average sales",

            "/maxsales":
                "Find maximum sales",

            "/minsales":
                "Find minimum sales",

            "/productsales":
                "Show product-wise total sales + chart",

            "/productavg":
                "Show product-wise average sales + chart",

            "/productmin":
                "Show product-wise minimum sales + chart",

            "/productmax":
                "Show product-wise maximum sales + chart",

            "/topproducts":
                "Show top 10 products + chart",

            "/lowestproducts":
                "Show lowest 10 products + chart",

            "/totalprofit":
                "Calculate total profit",

            "/averageprofit":
                "Calculate average profit",

            "/regionsales":
                "Show region-wise sales + chart",

            "/commands":
                "Show all available commands"
        }

    # ==================================================
    # EXECUTE COMMAND
    # ==================================================

    def execute_command(self, command):

        command = command.strip().lower()

        if command == "/totalsales":

            result = self.total_sales()
            chart = None

        elif command == "/averagesales":

            result = self.average_sales()
            chart = None

        elif command == "/maxsales":

            result = self.maximum_sales()
            chart = None

        elif command == "/minsales":

            result = self.minimum_sales()
            chart = None

        elif command == "/productsales":

            result = self.product_sales()
            chart = self.product_sales_chart()

        elif command == "/productavg":

            result = self.product_average_sales()
            chart = self.product_average_sales_chart()

        elif command == "/productmin":

            result = self.product_min_sales()
            chart = self.product_min_sales_chart()

        elif command == "/productmax":

            result = self.product_max_sales()
            chart = self.product_max_sales_chart()

        elif command == "/topproducts":

            result = self.top_products()
            chart = self.top_products_chart()

        elif command == "/lowestproducts":

            result = self.lowest_products()
            chart = self.lowest_products_chart()

        elif command == "/totalprofit":

            result = self.total_profit()
            chart = None

        elif command == "/averageprofit":

            result = self.average_profit()
            chart = None

        elif command == "/regionsales":

            result = self.region_sales()
            chart = self.region_sales_chart()

        elif command == "/commands":

            result = self.available_commands()
            chart = None

        else:

            result = (
                "Unknown command.\n\n"
                "Type /commands to see available commands."
            )

            chart = None

        return result, chart


# import pandas as pd
# import plotly.express as px


# class ReportGenerator:

#     def __init__(self, data):

#         self.data = data

#         # ==================================================
#         # CLEAN COLUMN NAMES
#         # ==================================================

#         self.data.columns = (
#             self.data.columns
#             .astype(str)
#             .str.strip()
#         )

#         # ==================================================
#         # COLUMN MAPPING
#         # ==================================================
#         # This allows:
#         # Product
#         # product
#         # PRODUCT
#         # Product
#         # to work correctly.
#         # ==================================================

#         self.column_map = {
#             column.lower(): column
#             for column in self.data.columns
#         }

#     # ==================================================
#     # FIND COLUMN
#     # ==================================================

#     def get_column(self, column_name):

#         return self.column_map.get(
#             column_name.lower()
#         )

#     # ==================================================
#     # CHECK DATA
#     # ==================================================

#     def check_data(self):

#         if self.data is None:
#             return False

#         if self.data.empty:
#             return False

#         return True

#     # ==================================================
#     # TOTAL SALES
#     # ==================================================

#     def total_sales(self):

#         if not self.check_data():
#             return "No data available."

#         sales_column = self.get_column("Sales")

#         if sales_column is None:
#             return "Sales column not found."

#         total = self.data[sales_column].sum()

#         return f"Total Sales: {total:,.2f}"

#     # ==================================================
#     # AVERAGE SALES
#     # ==================================================

#     def average_sales(self):

#         if not self.check_data():
#             return "No data available."

#         sales_column = self.get_column("Sales")

#         if sales_column is None:
#             return "Sales column not found."

#         average = self.data[sales_column].mean()

#         return f"Average Sales: {average:,.2f}"

#     # ==================================================
#     # MAXIMUM SALES
#     # ==================================================

#     def maximum_sales(self):

#         if not self.check_data():
#             return "No data available."

#         sales_column = self.get_column("Sales")

#         if sales_column is None:
#             return "Sales column not found."

#         maximum = self.data[sales_column].max()

#         return f"Maximum Sales: {maximum:,.2f}"

#     # ==================================================
#     # MINIMUM SALES
#     # ==================================================

#     def minimum_sales(self):

#         if not self.check_data():
#             return "No data available."

#         sales_column = self.get_column("Sales")

#         if sales_column is None:
#             return "Sales column not found."

#         minimum = self.data[sales_column].min()

#         return f"Minimum Sales: {minimum:,.2f}"

#     # ==================================================
#     # PRODUCT-WISE TOTAL SALES
#     # ==================================================

#     def product_sales(self):

#         if not self.check_data():
#             return None

#         product_column = self.get_column("Product")
#         sales_column = self.get_column("Sales")

#         if product_column is None:
#             return "Product column not found."

#         if sales_column is None:
#             return "Sales column not found."

#         result = (
#             self.data
#             .groupby(product_column)[sales_column]
#             .sum()
#             .sort_values(ascending=False)
#             .reset_index()
#         )

#         result.columns = [
#             "Product",
#             "Total Sales"
#         ]

#         return result

#     # ==================================================
#     # PRODUCT-WISE AVERAGE SALES
#     # ==================================================

#     def product_average_sales(self):

#         if not self.check_data():
#             return None

#         product_column = self.get_column("Product")
#         sales_column = self.get_column("Sales")

#         if product_column is None:
#             return "Product column not found."

#         if sales_column is None:
#             return "Sales column not found."

#         result = (
#             self.data
#             .groupby(product_column)[sales_column]
#             .mean()
#             .sort_values(ascending=False)
#             .reset_index()
#         )

#         result.columns = [
#             "Product",
#             "Average Sales"
#         ]

#         return result

#     # ==================================================
#     # PRODUCT-WISE MINIMUM SALES
#     # ==================================================

#     def product_min_sales(self):

#         if not self.check_data():
#             return None

#         product_column = self.get_column("Product")
#         sales_column = self.get_column("Sales")

#         if product_column is None:
#             return "Product column not found."

#         if sales_column is None:
#             return "Sales column not found."

#         result = (
#             self.data
#             .groupby(product_column)[sales_column]
#             .min()
#             .sort_values(ascending=True)
#             .reset_index()
#         )

#         result.columns = [
#             "Product",
#             "Minimum Sales"
#         ]

#         return result

#     # ==================================================
#     # PRODUCT-WISE MAXIMUM SALES
#     # ==================================================

#     def product_max_sales(self):

#         if not self.check_data():
#             return None

#         product_column = self.get_column("Product")
#         sales_column = self.get_column("Sales")

#         if product_column is None:
#             return "Product column not found."

#         if sales_column is None:
#             return "Sales column not found."

#         result = (
#             self.data
#             .groupby(product_column)[sales_column]
#             .max()
#             .sort_values(ascending=False)
#             .reset_index()
#         )

#         result.columns = [
#             "Product",
#             "Maximum Sales"
#         ]

#         return result

#     # ==================================================
#     # TOP PRODUCTS
#     # ==================================================

#     def top_products(self, n=10):

#         result = self.product_sales()

#         if isinstance(result, str):
#             return result

#         return result.head(n)

#     # ==================================================
#     # LOWEST PRODUCTS
#     # ==================================================

#     def lowest_products(self, n=10):

#         result = self.product_sales()

#         if isinstance(result, str):
#             return result

#         return (
#             result
#             .sort_values(
#                 "Total Sales",
#                 ascending=True
#             )
#             .head(n)
#         )

#     # ==================================================
#     # TOTAL PROFIT
#     # ==================================================

#     def total_profit(self):

#         if not self.check_data():
#             return "No data available."

#         profit_column = self.get_column("Profit")

#         if profit_column is None:
#             return "Profit column not found."

#         total = self.data[profit_column].sum()

#         return f"Total Profit: {total:,.2f}"

#     # ==================================================
#     # AVERAGE PROFIT
#     # ==================================================

#     def average_profit(self):

#         if not self.check_data():
#             return "No data available."

#         profit_column = self.get_column("Profit")

#         if profit_column is None:
#             return "Profit column not found."

#         average = self.data[profit_column].mean()

#         return f"Average Profit: {average:,.2f}"

#     # ==================================================
#     # REGION-WISE SALES
#     # ==================================================

#     def region_sales(self):

#         if not self.check_data():
#             return None

#         region_column = self.get_column("Region")
#         sales_column = self.get_column("Sales")

#         if region_column is None:
#             return "Region column not found."

#         if sales_column is None:
#             return "Sales column not found."

#         result = (
#             self.data
#             .groupby(region_column)[sales_column]
#             .sum()
#             .sort_values(ascending=False)
#             .reset_index()
#         )

#         result.columns = [
#             "Region",
#             "Total Sales"
#         ]

#         return result

#     # ==================================================
#     # PRODUCT TOTAL SALES CHART
#     # ==================================================

#     def product_sales_chart(self):

#         result = self.product_sales()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Total Sales",
#             title="Product-wise Total Sales",
#             text="Total Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Total Sales"
#         )

#         return fig

#     # ==================================================
#     # PRODUCT AVERAGE SALES CHART
#     # ==================================================

#     def product_average_sales_chart(self):

#         result = self.product_average_sales()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Average Sales",
#             title="Product-wise Average Sales",
#             text="Average Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Average Sales"
#         )

#         return fig

#     # ==================================================
#     # PRODUCT MINIMUM SALES CHART
#     # ==================================================

#     def product_min_sales_chart(self):

#         result = self.product_min_sales()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Minimum Sales",
#             title="Product-wise Minimum Sales",
#             text="Minimum Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Minimum Sales"
#         )

#         return fig

#     # ==================================================
#     # PRODUCT MAXIMUM SALES CHART
#     # ==================================================

#     def product_max_sales_chart(self):

#         result = self.product_max_sales()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Maximum Sales",
#             title="Product-wise Maximum Sales",
#             text="Maximum Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Maximum Sales"
#         )

#         return fig

#     # ==================================================
#     # TOP PRODUCTS CHART
#     # ==================================================

#     def top_products_chart(self):

#         result = self.top_products()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Total Sales",
#             title="Top 10 Products by Sales",
#             text="Total Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Total Sales"
#         )

#         return fig

#     # ==================================================
#     # LOWEST PRODUCTS CHART
#     # ==================================================

#     def lowest_products_chart(self):

#         result = self.lowest_products()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Product",
#             y="Total Sales",
#             title="Lowest 10 Products by Sales",
#             text="Total Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Product",
#             yaxis_title="Total Sales"
#         )

#         return fig

#     # ==================================================
#     # REGION SALES CHART
#     # ==================================================

#     def region_sales_chart(self):

#         result = self.region_sales()

#         if isinstance(result, str):
#             return None

#         fig = px.bar(
#             result,
#             x="Region",
#             y="Total Sales",
#             title="Region-wise Total Sales",
#             text="Total Sales"
#         )

#         fig.update_layout(
#             xaxis_title="Region",
#             yaxis_title="Total Sales"
#         )

#         return fig

#     # ==================================================
#     # AVAILABLE COMMANDS
#     # ==================================================

#     def available_commands(self):

#         return {
#             "/totalsales":
#                 "Calculate total sales",

#             "/averagesales":
#                 "Calculate average sales",

#             "/maxsales":
#                 "Find maximum sales",

#             "/minsales":
#                 "Find minimum sales",

#             "/productsales":
#                 "Show product-wise total sales + chart",

#             "/productavg":
#                 "Show product-wise average sales + chart",

#             "/productmin":
#                 "Show product-wise minimum sales + chart",

#             "/productmax":
#                 "Show product-wise maximum sales + chart",

#             "/topproducts":
#                 "Show top 10 products + chart",

#             "/lowestproducts":
#                 "Show lowest 10 products + chart",

#             "/totalprofit":
#                 "Calculate total profit",

#             "/averageprofit":
#                 "Calculate average profit",

#             "/regionsales":
#                 "Show region-wise sales + chart",

#             "/commands":
#                 "Show all available commands"
#         }

#     # ==================================================
#     # GET CHART FOR COMMAND
#     # ==================================================

#     def get_chart_for_command(self, command):

#         command = command.strip().lower()

#         if command == "/productsales":
#             return self.product_sales_chart()

#         elif command == "/productavg":
#             return self.product_average_sales_chart()

#         elif command == "/productmin":
#             return self.product_min_sales_chart()

#         elif command == "/productmax":
#             return self.product_max_sales_chart()

#         elif command == "/topproducts":
#             return self.top_products_chart()

#         elif command == "/lowestproducts":
#             return self.lowest_products_chart()

#         elif command == "/regionsales":
#             return self.region_sales_chart()

#         else:
#             return None

#     # ==================================================
#     # EXECUTE COMMAND
#     # ==================================================

#     def execute_command(self, command):

#         command = command.strip().lower()

#         if command == "/totalsales":

#             result = self.total_sales()
#             chart = None

#         elif command == "/averagesales":

#             result = self.average_sales()
#             chart = None

#         elif command == "/maxsales":

#             result = self.maximum_sales()
#             chart = None

#         elif command == "/minsales":

#             result = self.minimum_sales()
#             chart = None

#         elif command == "/productsales":

#             result = self.product_sales()
#             chart = self.product_sales_chart()

#         elif command == "/productavg":

#             result = self.product_average_sales()
#             chart = self.product_average_sales_chart()

#         elif command == "/productmin":

#             result = self.product_min_sales()
#             chart = self.product_min_sales_chart()

#         elif command == "/productmax":

#             result = self.product_max_sales()
#             chart = self.product_max_sales_chart()

#         elif command == "/topproducts":

#             result = self.top_products()
#             chart = self.top_products_chart()

#         elif command == "/lowestproducts":

#             result = self.lowest_products()
#             chart = self.lowest_products_chart()

#         elif command == "/totalprofit":

#             result = self.total_profit()
#             chart = None

#         elif command == "/averageprofit":

#             result = self.average_profit()
#             chart = None

#         elif command == "/regionsales":

#             result = self.region_sales()
#             chart = self.region_sales_chart()

#         elif command == "/commands":

#             result = self.available_commands()
#             chart = None

#         else:

#             result = (
#                 "Unknown command.\n\n"
#                 "Type /commands to see available commands."
#             )

#             chart = None

#         return result, chart