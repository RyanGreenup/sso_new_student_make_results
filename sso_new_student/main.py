import typer

app = typer.Typer(pretty_exceptions_enable=False)

@app.command()
def main() -> None:
    print("Hello")

if __name__ == "__main__":
    app()
