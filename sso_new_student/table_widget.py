from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
import pandas as pd


class DataFrameViewer(QTableWidget):
    def __init__(self, df: pd.DataFrame, parent=None) -> None:
        super().__init__(parent)
        self.df = df
        self._setup_table()

    def _setup_table(self) -> None:
        # Set dimensions
        self.setRowCount(len(self.df))
        self.setColumnCount(len(self.df.columns))

        # Set headers
        self.setHorizontalHeaderLabels(list(self.df.columns))

        # Populate data
        for row in range(len(self.df)):
            for col in range(len(self.df.columns)):
                value = str(self.df.iloc[row, col])
                item = QTableWidgetItem(value)
                self.setItem(row, col, item)
