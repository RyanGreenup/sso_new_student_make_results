import typer
from .set_data import make_dataframe
from pathlib import Path
import pandas as pd
import sys
import seaborn as sns
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
import pandas as pd
import signal

app = typer.Typer(pretty_exceptions_enable=False)

@app.command()
def main() -> None:

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # Run the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    app()
