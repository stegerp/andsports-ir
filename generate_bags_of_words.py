import glob
import os
import pickle
import sys

COLLECTION_BAG_OF_WORDS_FILE_NAME = "collection.bow"


def generate_document_bag_of_words(document):
    bag_of_words = {}
    with open(document, 'r', encoding='utf-8') as file:
        content = file.read()
        tokens = content.split()
        for token in tokens:
            if token in bag_of_words:
                continue
            bag_of_words[token] = tokens.count(token)
    with open(document[:-4] + '.bow', 'wb') as bag_of_words_file:
        pickle.dump(bag_of_words, bag_of_words_file)
    return bag_of_words


def generate_bags_of_words(documents_directory):
    collection_bag_of_words = {}
    for document in glob.glob(documents_directory + '/*.txt'):
        document_bag_of_words = generate_document_bag_of_words(document)
        for token in document_bag_of_words:
            if token in collection_bag_of_words:
                # Total the numbers
                collection_bag_of_words[token] = collection_bag_of_words[token] + document_bag_of_words[token]
            else:
                collection_bag_of_words[token] = document_bag_of_words[token]
    with open(os.path.join(documents_directory, COLLECTION_BAG_OF_WORDS_FILE_NAME),
              'wb') as collection_bag_of_words_file:
        pickle.dump(collection_bag_of_words, collection_bag_of_words_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python <script file>.py <path/to/documents directory>")
        exit()
    generate_bags_of_words(sys.argv[1])
