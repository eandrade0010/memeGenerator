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
- `meme.py`: The main script that the user interacts with at the command line. Optional flags `--body` and `--author` are used to generate the meme with the given arguments

# Running the program
Clone the following repo using 