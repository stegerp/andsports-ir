import glob
import math
import os
import pickle
import sys
import collections
import itertools

from nltk.corpus import stopwords
from nltk.downloader import download
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

LANGUAGE = "spanish"
STEMMER = SnowballStemmer(LANGUAGE)
COLLECTION_BAG_OF_WORDS_FILE_NAME = "collection.bow"


def generate_query_document(query_text):
    # tokenize
    query_document = query_text.lower()
    tokens = word_tokenize(query_document, language=LANGUAGE)
    query_document = [w for w in tokens if w.isalpha()]
    # remove stopwords
    query_document = [w for w in query_document if w not in stopwords.words(LANGUAGE)]
    # stem
    query_document = [STEMMER.stem(w) for w in query_document]
    return query_document


# \sum_{i = 1}^{n}log((\lambda - 1) \frac {tf_{i, C}} {|C|} + \lambda \frac {tf_{i, D}}{|D|})
# tfc = raw term count in the collection
# C = length of the collection
# tfd = term frequency in document
# D = length of the document
# lam = smoothing factor to avoid non-zero probabilities (document level)
def calculate_query_term_likelihood(tfc, C, tfd, D, lam=0.65):
    exp1 = ((1 - lam) * (float(tfc) / float(C)))
    exp2 = lam * (float(tfd) / float(D))
    exp3 = exp1 + exp2
    if exp3 != 0:
        log = math.log(exp3)
    else:
        log = 0  # set number for non-existing words in collection
    return log


def get_best(scores, limit=10):
    scores = collections.OrderedDict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    return dict(itertools.islice(scores.items(), 0, limit))


def calculate_query_likelihood(query_document, collection_bag_of_words, document_bags_of_words):
    scores = {}
    C = sum(collection_bag_of_words.values())
    for document_name, document_bag_of_words in document_bags_of_words.items():
        score = 0
        for term in query_document:
            tfc = 0
            if term in collection_bag_of_words:
                tfc = collection_bag_of_words[term]
            D = sum(document_bag_of_words.values())
            tfd = 0
            if term in document_bag_of_words:
                tfd = document_bag_of_words[term]
            score += calculate_query_term_likelihood(tfc, C, tfd, D)
        scores[document_name] = math.exp(score / len(document_bags_of_words))
    return get_best(scores, 10)


def load_collection_bag_of_words(documents_directory):
    with open(os.path.join(documents_directory, COLLECTION_BAG_OF_WORDS_FILE_NAME),
              'rb') as collection_bag_of_words_file:
        collection_bag_of_words = pickle.loads(collection_bag_of_words_file.read())
    return collection_bag_of_words


def load_document_bags_of_words(documents_directory):
    document_bags_of_words = {}
    for document_bag_of_words_path in glob.glob(documents_directory + '/*.bow'):
        if not os.path.basename(document_bag_of_words_path) == COLLECTION_BAG_OF_WORDS_FILE_NAME:
            with open(document_bag_of_words_path, 'rb') as document_bag_of_words_file:
                document_bag_of_words = pickle.loads(document_bag_of_words_file.read())
                document_bags_of_words[os.path.basename(document_bag_of_words_path)[:-4]] = document_bag_of_words
    return document_bags_of_words


def get_query_likelihood_score(documents_directory, query_text):
    download('punkt', download_dir="nltk_data")
    download('stopwords', download_dir="nltk_data")
    query_document = generate_query_document(query_text)
    if len(query_document) == 0:
        print("Query not precise enough. Please refine your query")
        return

    collection_bag_of_words = load_collection_bag_of_words(documents_directory)
    document_bags_of_words = load_document_bags_of_words(documents_directory)

    scores = calculate_query_likelihood(query_document, collection_bag_of_words, document_bags_of_words)
    for document_name, score in scores.items():
        print(document_name + "\t" + str(score))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python <script file>.py <path/to/documents directory> <query text>")
        exit()
    get_query_likelihood_score(sys.argv[1], " ".join(sys.argv[2:]))
