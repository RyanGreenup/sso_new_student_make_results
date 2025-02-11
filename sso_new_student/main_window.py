from PySide6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QPushButton,
)
from .table_widget import DataFrameViewer
import pandas as pd
from .set_data import make_dataframe


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Data Viewer")

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create controls layout
        combo_controls_layout = QHBoxLayout()
        button_input_layout = QHBoxLayout()

        # Campus combo
        self.campus_combo = QComboBox()
        self.campus_combo.addItems(["EMC", "MFC", "IDC", "KBC"])
        combo_controls_layout.addWidget(self.campus_combo)

        # Student Number
        self.student_input = QLineEdit("Enter Student ID")
        button_input_layout.addWidget(self.student_input)

        # Year level combo
        self.year_combo = QComboBox()
        self.year_combo.addItems([str(i) for i in range(6, 12)])
        combo_controls_layout.addWidget(self.year_combo)

        # Entrance Score
        self.entrance_score = QComboBox()
        self.entrance_score.addItems([f"N{i}" for i in range(2, 6)])
        combo_controls_layout.addWidget(self.entrance_score)

        # Export button
        self.export_btn = QPushButton("Export CSV")
        button_input_layout.addWidget(self.export_btn)

        # Add controls to main layout
        controls_layout = QVBoxLayout()
        controls_layout.addLayout(combo_controls_layout)
        controls_layout.addLayout(button_input_layout)
        layout.addLayout(controls_layout)


        # Get user inputs and build dataframe
        dfs = make_dataframe(
            campus=self.campus_combo.currentText(),
            stu_id=self.student_input.text(),
            y=self.year_combo.currentText(),
            cg=self.entrance_score.currentText(),
            output_directory=Path.cwd()
        )
        # Add table
        self.table = DataFrameViewer(df)
        layout.addWidget(self.table)
