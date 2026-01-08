import typer

app = typer.Typer()

def download():
    typer.echo("download stub")

def ocr():
    typer.echo("ocr stub")

def build_tables():
    typer.echo("build_tables stub")

if __name__ == "__main__":
    app()