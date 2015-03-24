#!/usr/bin/env python
''' Search for a file name in the specified dir (default current one) '''
import os
import sys
import re
import itertools
# Try to load argparse and if it doesn't exist load the backported version
# from ffind package
try:
    import argparse
except ImportError:
    from backports import argparse

import pkg_resources  # part of setuptools
VERSION = pkg_resources.require('ffind')[0].version

# Define colors
RED_CHARACTER = '\x1b[31m'
GREEN_CHARACTER = '\x1b[32m'
YELLOW_CHARACTER = '\x1b[33m'
BLUE_CHARACTER = '\x1b[36m'
PURPLE_CHARACTER = '\x1b[35m'
NO_COLOR = '\x1b[0m'

VCS_DIRS = ('CVS',
            'RCS',
            'SCCS',
            '.git',
            '.svn',
            '.arch-ids',
            '{arch}')

VCS_FILES = ('=RELEASE-ID',
             '=meta-update',
             '=update',
             '.bzr',
             '.bzrignore',
             '.bzrtags',
             '.hg',
             '.hgignore',
             '.hgrags',
             '_darcs',
             '.cvsignore',
             '.gitignore',)


def create_comparison(file_pattern, ignore_case, fuzzy):
    ''' Return the adequate comparison (regex or simple) '''
    if fuzzy:
        # Generate a pattern to fuzzy match
        file_pattern = '.*?'.join(f for f in file_pattern)

    if ignore_case:
        pattern = re.compile(file_pattern, re.IGNORECASE)
    else:
        pattern = re.compile(file_pattern)

    def regex_compare(to_match):
        match = re.search(pattern, to_match)
        if match:
            smatch = [to_match[:match.start()],
                      to_match[match.start(): match.end()],
                      to_match[match.end():]]
            return smatch

    # Check if is a proper regex (contains a char different from [a-zA-Z0-9])
    if fuzzy or re.search(r'[^a-zA-Z0-9]', file_pattern):
        return regex_compare

    # We can go with a simplified comparison
    if ignore_case:
        file_pattern = file_pattern.lower()

        def simple_compare_case_insensitive(to_match):
            if file_pattern in to_match.lower():
                return regex_compare(to_match)
        return simple_compare_case_insensitive

    def simple_compare(to_match):
        if file_pattern in to_match:
            return regex_compare(to_match)

    return simple_compare


def filtered_subfolders(sub_folders, ignore_hidden, ignore_vcs):
    '''
    Create a generator to return subfolders to search, removing the
    ones to not search from the original list, to avoid keep
    walking them
    '''

    for folder in sub_folders:
        if ignore_hidden and folder.startswith('.'):
            sub_folders.remove(folder)
        elif ignore_vcs and folder in VCS_DIRS:
            sub_folders.remove(folder)
        else:
            yield folder


def filtered_files(files, ignore_hidden, ignore_vcs):
    '''
    Create a generator to return the filtered files
    '''
    for f in files:
        if ignore_hidden and f.startswith('.'):
            continue
        if ignore_vcs and f in VCS_FILES:
            continue

        yield f


def search(directory, file_pattern, path_match,
           follow_symlinks=True, output=True, colored=True,
           ignore_hidden=True, delete=False, exec_command=False,
           ignore_case=False, ignore_vcs=False, return_results=False,
           fuzzy=False):
    '''
        Search the files matching the pattern.
        The files will be returned as a list, and can be optionally printed
    '''

    # Create the compare function
    compare = create_comparison(file_pattern, ignore_case, fuzzy)

    if return_results:
        results = []

    for root, sub_folders, files in os.walk(directory, topdown=True,
                                            followlinks=follow_symlinks):

        # Ignore hidden and VCS directories.
        fsubfolders = filtered_subfolders(sub_folders, ignore_hidden,
                                          ignore_vcs)
        ffiles = filtered_files(files, ignore_hidden, ignore_vcs)

        # Search in files and subfolders
        for filename in itertools.chain(ffiles, fsubfolders):
            to_match = os.path.join(root, filename) if path_match else filename
            smatch = compare(to_match)
            if smatch:
                if not path_match:
                    # Add the fullpath to the prefix
                    smatch[0] = os.path.join(root, smatch[0])

                if delete:
                    full_filename = os.path.join(root, filename)
                    delete_file(full_filename)

                elif exec_command:
                    full_filename = os.path.join(root, filename)
                    execute_command(exec_command[0], full_filename)

                elif output:
                    print_match(smatch, colored)

                if return_results:
                    full_filename = os.path.join(root, filename)
                    results.append(full_filename)

    if return_results:
        return results


def print_match(splitted_match, colored, color=RED_CHARACTER):
    ''' Output a match on the console '''
    if colored:
        a, b, c = splitted_match
        colored_output = (a, color, b, NO_COLOR, c)
    else:
        colored_output = splitted_match

    print(''.join(colored_output))


def delete_file(full_filename):
    try:
        if os.path.isdir(full_filename):
            os.removedirs(full_filename)
        else:
            os.remove(full_filename)
    except Exception as err:
        print("cannot delete: {error}".format(error=err))


def execute_command(command_template, full_filename):
    if command_template.count('{}') > 0:
        command = command_template.replace('{}', full_filename)
    else:
        command = command_template + " " + full_filename

    os.system(command)


def parse_params_and_search():
    parser = argparse.ArgumentParser(
        description='Search file name in directory tree'
    )
    parser.add_argument('-p',
                        action='store_true',
                        help='Match whole path, not only name of files',
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
    parser.add_argument('--hidden',
                        action='store_false',
                        dest='ignore_hidden',
                        help='Do not ignore hidden directories',
                        default=True)
    parser.add_argument('-c',
                        action='store_true',
                        dest='case_sensitive',
                        help='Force case sensitive. By default, all lowercase '
                             'patterns are case insensitive',
                        default=False)

    parser.add_argument('--delete',
                        action='store_true',
                        dest='delete',
                        help='Delete files found',
                        default=False)

    parser.add_argument('--exec',
                        dest='exec_command',
                        nargs=1,
                        metavar=('"command"'),
                        help='Execute the given command with the file found '
                             "as argument. The string '{}' will be replaced "
                             'with the current file name being processed',
                        default=False)

    parser.add_argument('--ignore-vcs',
                        action='store_true',
                        dest='ignore_vcs',
                        help='Ignore version control system files and '
                             'directories',
                        default=False)

    parser.add_argument('-f',
                        action='store_true',
                        dest='fuzzy',
                        help='Experimental fuzzy search. '
                             'Increases the matches, use with care. '
                             'Combining it with regex may give crazy results',
                        default=False)

    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=VERSION))

    parser.add_argument('dir', nargs='?',
                        help='Directory to search', default='.')
    parser.add_argument('filepattern')
    args = parser.parse_args()

    # If output is redirected, deactivate color
    if not sys.stdout.isatty():
        args.colored = False

    lowercase_pattern = args.filepattern == args.filepattern.lower()
    ignore_case = not args.case_sensitive and lowercase_pattern

    search(directory=args.dir,
           file_pattern=args.filepattern,
           path_match=args.path_match,
           colored=args.colored,
           follow_symlinks=args.follow_symlinks,
           ignore_hidden=args.ignore_hidden,
           delete=args.delete,
           ignore_case=ignore_case,
           exec_command=args.exec_command,
           ignore_vcs=args.ignore_vcs,
           fuzzy=args.fuzzy)


def run():
    try:
        parse_params_and_search()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
