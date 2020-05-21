import os
import re
import shutil
import sys
import pandas
from nltk.corpus import stopwords
from nltk.downloader import download
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

# Global constants
TEXT_IDENTIFIER_COLUMN = "name"
TEXT_COLUMN = "text"
LANGUAGE = "spanish"
STEMMER = SnowballStemmer(LANGUAGE)
DOCUMENTS_DIRECTORY = "documents"


def tokenize(row):
    text = row[TEXT_COLUMN].lower()
    tokens = word_tokenize(text, language=LANGUAGE)
    row[TEXT_COLUMN] = [w for w in tokens if w.isalpha()]
    return row


def remove_stopwords(row):
    row[TEXT_COLUMN] = [w for w in row[TEXT_COLUMN] if w not in stopwords.words(LANGUAGE)]
    return row


def stem(row):
    row[TEXT_COLUMN] = [STEMMER.stem(w) for w in row[TEXT_COLUMN]]
    return row


def save_to_document(row):
    if not row[TEXT_COLUMN]:
        print("No relevant texts extracted from " + row[TEXT_IDENTIFIER_COLUMN] + ". Document will not be saved.")
        return
    file_name = re.sub(r'[\s\\\/:\?<>|"\']', '_', row[TEXT_IDENTIFIER_COLUMN])  # remove forbidden Windows FS chars
    path = os.path.join(DOCUMENTS_DIRECTORY, file_name)
    with open(path + '.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(row[TEXT_COLUMN]))


def generate_documents(data_file):
    # Read data from csv export file
    data = pandas.read_csv(data_file, sep='\t', header=None,
                           names=[TEXT_IDENTIFIER_COLUMN, TEXT_COLUMN], skiprows=[0])

    download('punkt', download_dir="nltk_data")
    download('stopwords', download_dir="nltk_data")

    if os.path.exists(DOCUMENTS_DIRECTORY):
        shutil.rmtree(DOCUMENTS_DIRECTORY)
    os.makedirs(DOCUMENTS_DIRECTORY)

    data = data.apply(tokenize, axis=1)
    data = data.apply(remove_stopwords, axis=1)
    data = data.apply(stem, axis=1)
    data.apply(save_to_document, axis=1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python <script file>.py <path/to/data file>.csv")
        exit()
    generate_documents(sys.argv[1])
