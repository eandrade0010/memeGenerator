# Meme Generator

MemeGenerator uses a command-line interface as well as a Flask deployable program to generate memes using a collection of dog photos and quotes provided in a variety of file types; while also allowing the user to either submit a form or provide optional command-line arguments to generate a meme of their own creation.

This project utilizes the skills developed in the Large Python Codebases course of Udacity's Intermediate Python nanodegree, namely:
- Building modules using more advanced OOP design and strategy objects
- Using libraries in a virtual environment to facilitate deployment of project 
- Command-line interfaces with the argparser library to receive optional arguments from the user
- The Flask framework to deploy the project ot the web

# Project Scaffolding
```zsh
├── README.md                 # This file
├── requirements.txt          # Dependencies
└── src
    ├── MemeEngine.py
    ├── QuoteEngine
    │   ├── CSVIngestor.py
    │   ├── DOCXIngestor.py
    │   ├── Ingestor.py
    │   ├── IngestorInterface.py
    │   ├── PDFIngestor.py
    │   ├── QuoteModel.py
    │   ├── TXTIngestor.py
    │   └── __init__.py
    ├── _data
    │   ├── DogQuotes
    │   │   ├── DogQuotesCSV.csv
    │   │   ├── DogQuotesDOCX.docx
    │   │   ├── DogQuotesPDF.pdf
    │   │   └── DogQuotesTXT.txt
    │   ├── SimpleLines
    │   │   ├── SimpleLines.csv
    │   │   ├── SimpleLines.docx
    │   │   ├── SimpleLines.pdf
    │   │   └── SimpleLines.txt
    │   └── photos
    │       └── dog
    │           ├── xander_1.jpg
    │           ├── xander_2.jpg
    │           ├── xander_3.jpg
    │           └── xander_4.jpg
    ├── app.py
    ├── assets
    │   └── impact.ttf
    ├── meme.py
    ├── static
    ├── templates
    │   ├── base.html
    │   ├── meme.html
    │   └── meme_form.html
    └── tmp
```

Taking a closer look at each of the files and folders
- `meme.py`: The main script that the user interacts with at the command line. Optional flags `--body` and `--author` are used to generate the meme with the given arguments. Does this by interacting with the `QuoteEnginge` module and `MemeEngine` package.
  - The `QuoteEngine` package consists of modules with strategy objects designed to "ingest" the quotation and attributed author from various types of provided files (i.e. pdf, docx, txt, csv). Each quotation is encapsulated in a `QuoteModel` object
  - The `MemeEngine` module handles the resizing and drawing of text onto a given image which is subsequently saved to the directory the `MemeEngine` object was initialized with
- `app.py`: is a minimal Flask application which allows the user to generate memes at random much like the `meme.py` program. Additionally, the user is able to provide an image url and post the quote and author of their liking. Each meme is created much like before, with the `MemeEngine` module

Supplementary files/folders
- `assets` dir: Houses the font of the text being used for the memes in the `MemeEngine` module
- `static` dir: Folder for the Flask application
- `templates` dir: Contains the html templates for the Flask application
- `tmp` dir: Stores the images generated from the `meme.py` program
- `_data` dir: Holds the quotation files and dog photos used in both programs
- `requirements.txt`: Dependencies for running the application

### Dependencies
    - `PIL`: Handling images and drawing text onto images
    - `os`: Interacting with operating system to search directory for images and files as well as saving and removing files after processing
    - `docx`: Parsing word documents
    - `subprocess`: Interacting with command-line to launch the `pdftotext` tool
    - `argparse`: Handler for optional command-line arguments
    - `flask`: Used for deployment of Flask app
    - `requests`: Interacts with the internet to request images provided as URLs

# Running the program
Clone the following repo using 
```commandline
git clone https://github.com/eandrade0010/memeGenerator.git
```

Navigate to the repo and create a virtual environment by using the command `venv`:
```
python3 -m venv .venv     # Unix/macOS
py -m venv .venv          # Windows
```

Activate the virtual environment by running the following command
```
source .venv/bin/activate   # Unix/macOS
.venv\Scripts\activate      # Windows
```

Finally, install the dependencies by running the following command
```commandline
pip install -r requirements.txt
```

Running the program is done as follows
```python
python3 meme.py [OPTIONS]     # CLI interface
python3 app.py                # Web interface
```

| Options | Description  |
| :--: |:------------:|
| `-body [QUOTE]` | Allows the user to input quotation of their liking |
| `-author [AUTHOR]` | User inputs the author name |




