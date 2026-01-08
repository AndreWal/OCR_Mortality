# 📊 Swiss Population Mortality OCR Pipeline

> Transform historical Swiss mortality data from dusty PDFs into modern, analysis-ready datasets 🇨🇭

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 What is this?

This project brings up to **145+ years of Swiss population mortality data** (starting from 1878!) into the modern age. Using state-of-the-art OCR and Large Language Models, I:

1. 📥 **Download** historical PDF documents from the Swiss Federal Statistical Office (BFS) API
2. 🔍 **Extract** complex tables using OCR-LLM technology
3. 🧹 **Transform** messy data into clean CSV/Parquet files
4. 📈 **Visualize** mortality patterns across time

Perfect for researchers, data scientists, and anyone curious about Swiss demographic history! 🏔️

## ✨ Features

- 🤖 **AI-Powered OCR**: Leverages transformer models (dots.ocr) to understand complex table structures
- 🐳 **Docker-First**: Reproducible environment with all dependencies included
- ⚡ **Fast Processing**: Uses Polars and DuckDB for blazing-fast data manipulation
- 📓 **Interactive Notebooks**: Built with Marimo for literate programming
- 🎨 **Rich CLI**: Beautiful terminal UI with progress bars and colored output
- 🔒 **Type-Safe**: Full type hints with mypy checking

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Python 3.12

### Using Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd OCR_Project
   ```

2. **Start the Marimo notebook environment**
   ```bash
   docker compose -f docker/docker-compose.yml up --build
   ```

3. **Open your browser**
   
   Navigate to `http://localhost:3000` and start exploring!

## 📁 Project Structure

```
OCR_Project/
├── 📄 pyproject.toml          # Project dependencies & configuration
├── 🔒 uv.lock                 # Locked dependencies (reproducible builds)
├── 🐳 docker/
│   ├── Dockerfile             # Container definition
│   └── docker-compose.yml     # Orchestration config
├── 📊 data/
│   └── pdfs/                  # Downloaded PDF documents
├── 📓 scripts/
│   ├── 1.Get_Data.py          # Marimo notebook: Download PDFs
│   ├── 2.OCR_Extract.py       # Marimo notebook: OCR extraction (TODO)
│   └── 3.Visualize.py         # Marimo notebook: Data visualization (TODO)
└── 🐍 src/
    └── ocr_pipeline/          # Main package
        ├── __init__.py        # Package marker
        └── cli.py             # Command-line interface
```

## 🎮 Usage

### 1. Download PDFs

Use the Marimo notebook [`scripts/1.Get_Data.py`](scripts/1.Get_Data.py) or the CLI:

```bash
docker run -it --rm -v $(pwd):/app bfs-ocr bfs-download --help
```

### 2. Extract Tables with OCR

```bash
docker run --rm -v $(pwd):/app bfs-ocr bfs-ocr --input data/pdfs/ --output data/tables/
```

### 3. Build Analysis-Ready Datasets

```bash
docker run --rm -v $(pwd):/app bfs-ocr bfs-build --input data/tables/ --output data/final/
```

### 4. Explore Interactively

The Marimo notebooks provide an interactive, reproducible environment:

```bash
docker compose -f docker/docker-compose.yml up
# Open http://localhost:3000
```

## 🛠️ Technology Stack

### Core
- **[uv](https://github.com/astral-sh/uv)** - Lightning-fast Python package installer
- **[Marimo](https://marimo.io/)** - Reactive Python notebooks
- **[Typer](https://typer.tiangolo.com/)** - Modern CLI framework
- **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal output

### Data Processing
- **[Polars](https://pola.rs/)** - Blazing-fast DataFrames
- **[DuckDB](https://duckdb.org/)** - In-process analytical database
- **[Pandas](https://pandas.pydata.org/)** - Classic data manipulation
- **[PyArrow](https://arrow.apache.org/docs/python/)** - Columnar data format

### OCR & ML (Optional)
- **[PyTorch](https://pytorch.org/)** - Deep learning framework
- **[Transformers](https://huggingface.co/docs/transformers)** - State-of-the-art NLP models
- **[Dots.ocr](https://huggingface.co/rednote-hilab/dots.ocr)** - Vision-language model for table understanding

### Document Processing
- **[PyMuPDF](https://pymupdf.readthedocs.io/)** - PDF rendering and extraction
- **[Pillow](https://pillow.readthedocs.io/)** - Image processing

## 🧪 Development

### Local Setup (without Docker)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync

# Install with OCR support (includes PyTorch & transformers)
uv sync --extra ocr

# Run tests
uv run pytest

# Lint code
uv run ruff check .

# Type checking
uv run mypy src/
```

### Pre-commit Hooks

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## 📊 Data Sources

All data comes from the **Swiss Federal Statistical Office (BFS)** / **Office fédéral de la statistique (OFS)**:
- Historical mortality tables (1878-present)
- Population statistics by canton and district

## 🤝 Contributing

Contributions welcome! Whether it's:
- 🐛 Bug reports
- 💡 Feature suggestions
- 📝 Documentation improvements
- 🔧 Code contributions

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Swiss Federal Statistical Office for providing open historical data
- The amazing open-source community behind all the tools used here

---

**Happy analyzing! 📈✨**

*Made with ❤️ for Swiss demographic research*
