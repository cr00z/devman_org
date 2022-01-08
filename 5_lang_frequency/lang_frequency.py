import argparse
import collections
import os
import re


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='script for frequency analysis of words in any text')
    parser.add_argument('text_filename', metavar='text_filename', type=str,
                        help='text filename')
    parser.add_argument('-t', '--top_of_words', action='store', default=10,
                        type=int, help='top of words')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, encoding='utf-8') as text_file_object:
        return text_file_object.read()


def get_most_frequent_words(input_text, num_of_words):
    input_text = re.split(r'[\W\d]+', input_text)
    word_counter = collections.Counter(input_text)
    return word_counter.most_common(num_of_words)


if __name__ == '__main__':
    args = get_cmdline_args()
    loaded_text = load_data(args.text_filename)
    if loaded_text is None:
        exit("we're really looking for your file to open, but didn't find it")
    most_frequent_words = get_most_frequent_words(loaded_text, args.top_of_words)
    if args.verbose:
        print("FREQUENCY    WORD")
        for word, frequency in most_frequent_words:
            print("{:<13}{}".format(frequency, word))
    else:
        print(' '.join([word for word, _ in most_frequent_words]))
