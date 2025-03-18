"""Brief description of what the script does."""

import sys
import argparse
import string
import csv
from collections import Counter

import utilities as util

SENTENCE_ENDINGS = ['.', '?', '!']


def collection_to_output(collection):
    """Write a collection of items and counts to stdout."""
    collection = collection.most_common()
    for item, count in collection:
        print(f"Number of {item} is {count}")


def count_sentence_endings(reader):
    """
    Count the occurence of full stops, question marks, and
    exclamation points.
    """
    text = reader.read()
    ending_counts = Counter({ending: text.count(ending) for ending in
                             SENTENCE_ENDINGS})
    return ending_counts


def main(args):
    """Run the program."""
    ending_counts = count_sentence_endings(args.infile)
    collection_to_output(ending_counts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    args = parser.parse_args()
    main(args)

