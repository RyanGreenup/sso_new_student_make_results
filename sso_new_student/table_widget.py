from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
import pandas as pd


class DataFrameViewer(QTableWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.df = pd.DataFrame()  # Empty initial DataFrame
        self._setup_table()

    def _setup_table(self) -> None:
        """Initialize empty table"""
        self.setRowCount(0)
        self.setColumnCount(0)

    def update_data(self, df: pd.DataFrame) -> None:
        """Update table with new DataFrame data"""
        self.df = df
        self.setRowCount(len(self.df))
        self.setColumnCount(len(self.df.columns))
        self.setHorizontalHeaderLabels(list(self.df.columns))

        # Populate data
        for row in range(len(self.df)):
            for col in range(len(self.df.columns)):
                value = str(self.df.iloc[row, col])
                item = QTableWidgetItem(value)
                self.setItem(row, col, item)

    # Ask the user where to save the csv and use the `.to_csv()` method to export it. AI!
    def export_csv(self) -> None:
