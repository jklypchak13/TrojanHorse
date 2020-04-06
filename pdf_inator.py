#!/usr/bin/env python3
"""
Pdf-Inator

Creates a pdf copy of all files inside of src/ directory

Make sure to run

```sh
pipenv install --dev
# or pip install fpdf
```
"""
from pathlib import Path
import sys
import os

from fpdf import FPDF

# Add Crawler to Sys Path
CRAWLER_PATH: str = f"{Path(__file__).parent.absolute()}{os.sep}src"
sys.path.append(CRAWLER_PATH)

from src.trojan.crawler import Crawler


def calculate_path(path: Path) -> str:
    """
    Creates pdfs path

    Parameters
    ----------

    path: Path
      Path to a python file

    Returns
    -------

    str
      Sub-path starting with pdfs/src/**/something.pdf
    """
    src_index: int = path.parts.index("src")
    return f"pdfs{os.sep}{f'{os.sep}'.join(path.parts[src_index:])}"


def create_pdf(file_path: Path) -> None:
    """
    Creates the PDF copy of a python or JSON file

    something.(py|json).pdf

    Parameters
    ----------

    file_path: Path
      Path to python or json file
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    with open(file_path, "r") as file:
        for line in file:
            pdf.cell(200, 10, txt=line, ln=1)
    pdf_dir_path: Path = Path(calculate_path(file_path))
    Path(pdf_dir_path.parent).mkdir(parents=True, exist_ok=True)
    pdf_path: str = f"{str(pdf_dir_path)}.pdf"
    pdf.output(pdf_path)


# Construct pdfs directory
Path("pdfs").mkdir(parents=True, exist_ok=True)

# Only select python or json files
crawler: Crawler = Crawler("src", [".py", ".json"], True)
crawler.walk_tree()

for file in crawler.get_files():
    create_pdf(Path(file))
