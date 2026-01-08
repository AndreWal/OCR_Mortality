import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests
    import polars as pl
    from pathlib import Path
    return Path, mo, pl, requests


@app.cell
def _(base, requests):
    def get_assets(params):
        r = requests.get(f"{base}/assets", params=params, timeout=60)
        r.raise_for_status()
        data = r.json()

        # Be defensive: APIs sometimes return {"items":[...]} or just [...]
        if isinstance(data, list):
            return data
        for k in ("items", "assets", "content", "results", "data"):
            if k in data and isinstance(data[k], list):
                return data[k]
        raise ValueError(f"Unexpected response shape: {type(data)} keys={list(getattr(data,'keys',lambda:[])())}")
    return (get_assets,)


@app.cell
def _():
    base = "https://dam-api.bfs.admin.ch/hub/api/dam"

    sterm1 = "Die Bewegung der Bevölkerung in der Schweiz im Jahre"

    sterm2 = "Bevölkerungsbewegung in der Schweiz"

    params1 = {
        "extendedSearch": sterm1,
        "language": "de",
        # Prefer using year filters if the API offers them (Swagger will show the exact names):
        "publishingYearStart": 1800,
        "publishingYearEnd": 1930,
        "limit": 1000,
    }

    params2 = {
        "extendedSearch": sterm2,
        "language": "de",
        # Prefer using year filters if the API offers them (Swagger will show the exact names):
        "publishingYearStart": 1929,
        "publishingYearEnd": 1980,
        "limit": 1000,
    }
    return base, params1, params2


@app.cell
def _(get_assets, params1, params2):
    assets1 = get_assets(params1)

    assets2 = get_assets(params2)
    return assets1, assets2


@app.cell
def _(assets1, assets2):
    sel = []

    for i in range(len(assets1)):
        tmp = {
            "id": assets1[i]["ids"]["damId"],
            "title": assets1[i]["description"]["titles"]["main"]
        }
        sel.append(tmp)

    for i in range(len(assets2)):
        tmp = {
            "id": assets2[i]["ids"]["damId"],
            "title": assets2[i]["description"]["titles"]["main"]
        }
        sel.append(tmp)
    return (sel,)


@app.cell
def _(pl, sel):
    results = pl.DataFrame(sel)
    title = pl.col("title").str.strip_chars()

    final = (
        results
        .filter(
            (
                title.str.starts_with("Bevölkerungsbewegung")
                | title.str.starts_with("Die Bewegung der Bevölkerung")
            )
            & ~title.str.ends_with("Text")
        )
        .with_columns(
            year=title
                .str.extract(r"(\d{4})\s*(?:\.\s*\w+)?\s*$", 1)
                .cast(pl.Int32)
        )
    )
    return (final,)


@app.cell
def _(final, mo):
    mo.ui.dataframe(final)
    return


@app.cell
def _(Path):
    pdf_dir = Path("data/pdfs")
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir
    return (pdf_dir,)


@app.cell
def _(requests):
    def download_assets(base, id, path):
        res = requests.get(f"{base}/assets/{id}/master")
        if res.status_code != 200:
           raise RuntimeError(f"Failed to download asset {id}: {res.status_code}")
        with open(path, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Saved {path}")
    return (download_assets,)


@app.cell
def _(base, download_assets, final, pdf_dir):
    for k in range(final.shape[0]):
        download_assets(base, final[k,0], f"{pdf_dir}/{final[k,2]}.pdf")
    return


if __name__ == "__main__":
    app.run()
