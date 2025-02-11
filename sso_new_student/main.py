import typer
from .set_data import make_dataframe
from pathlib import Path
import pandas as pd
import sys
import seaborn as sns
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
import pandas as pd

app = typer.Typer(pretty_exceptions_enable=False)

@app.command()
def main() -> None:
    dfs: dict[str, pd.DataFrame] = make_dataframe('EMC', '38000', '10', 'N5', Path("/tmp/"))
    # Pull out the first df:
    keys = list(dfs.keys())
    if len(keys) <= 0:
        print("No Dataframes returned", file = sys.stderr)
    if (df := dfs.get(keys[0])) is None:
        print("No Dataframe available, this is a bug")

    for campus, df in dfs.items():
        df = df
        print(campus)
        print(df.to_markdown())

    df = pd.read_csv("/home/ryan/Downloads/working/newresultsEMC.csv")

    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow(df)
    window.resize(800, 600)
    window.show()

    # Run the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    app()
