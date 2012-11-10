#!/usr/bin/env python
''' Search for a file name in the specified dir (default current one) '''
import os
import sys
import argparse
import re

# Define colors
RED_CHARACTER = '\x1b[31m'
GREEN_CHARACTER = '\x1b[32m'
YELLOW_CHARACTER = '\x1b[33m'
BLUE_CHARACTER = '\x1b[36m'
PURPLE_CHARACTER = '\x1b[35m'
NO_COLOR = '\x1b[0m'


def search(directory, file_pattern, path_match,
           follow_symlinks=True, output=True, colored=True):
    ''' Search the files matching the pattern.
        The files will be returned, and can be optionally printed '''

    pattern = re.compile(file_pattern)

    results = []

    for root, sub_folders, files in os.walk(directory,
                                            followlinks=follow_symlinks):
        # Ignore hidden directories
        if '/.' in root:
            continue

        # Search in files and subfolders
        for filename in files + sub_folders:
            full_filename = os.path.join(root, filename)
            to_match = full_filename if path_match else filename
            match = re.search(pattern, to_match)
            if match:
                # Split the match to be able to colorize it
                # prefix, matched_pattern, sufix
                smatch = [to_match[:match.start()],
                          to_match[match.start(): match.end()],
                          to_match[match.end():]]
                if not path_match:
                    # Add the fullpath to the prefix
                    smatch[0] = os.path.join(root, smatch[0])

                if output:
                    print_match(smatch, colored)

                results.append(full_filename)

    return results


def print_match(splitted_match, colored, color=RED_CHARACTER):
    ''' Output a match on the console '''
    if colored:
        a, b, c = splitted_match
        colored_output = (a, color, b, NO_COLOR, c)
    else:
        colored_output = splitted_match

    print (''.join(colored_output))


def parse_params_and_search():
    parser = argparse.ArgumentParser(
        description='Search file name in directory tree'
    )
    parser.add_argument('-p',
                        action='store_true',
                        help='match whole path, not only name of files',
                        dest='path_match',
                        default=False)
    parser.add_argument('--nocolor',
                        action='store_false',
                        dest='colored',
                        help='Do not display color',
                        default=True)
    parser.add_argument('--nosymlinks',
                        action='store_false',
                        dest='follow_symlinks',
                        help='Do not follow symlinks'
                             ' (following symlinks can lead to '
                             'infinite recursion)',
                        default=True)

    parser.add_argument('dir', nargs='?',
                        help='Directory to search', default='.')
    parser.add_argument('filepattern')
    args = parser.parse_args()

    # If output is redirected, deactivate color
    if not sys.stdout.isatty():
        args.colored = False

    search(directory=args.dir,
           file_pattern=args.filepattern,
           path_match=args.path_match,
           colored=args.colored,
           follow_symlinks=args.follow_symlinks)


def run():
    try:
        parse_params_and_search()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
