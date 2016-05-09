#!/usr/bin/env python
''' Search for a file name in the specified dir (default current one) '''
from __future__ import print_function
import os
import sys
import re
import runpy
import itertools

# Try to load argparse and if it doesn't exist load the backported version
# from ffind package
try:
    import argparse
except ImportError:
    from backports import argparse

import pkg_resources  # part of setuptools
try:
    VERSION = pkg_resources.require('ffind')[0].version
except:
    # Default if not installed yet
    VERSION = '1.0.2'

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


class WrongPattern(Exception):
    pass


def create_comparison(file_pattern, ignore_case, fuzzy):
    ''' Return the adequate comparison (regex or simple) '''
    if fuzzy:
        # Generate a pattern to fuzzy match
        file_pattern = '.*?'.join(f for f in file_pattern)

    try:
        if ignore_case:
            pattern = re.compile(file_pattern, re.IGNORECASE)
        else:
            pattern = re.compile(file_pattern)
    except re.error:
        msg = (
        '{red}Sorry, the expression {pattern} is incorrect.{no_color}\n'
        'Remember that this should be a regular expression.\n'
        '(https://docs.python.org/howto/regex.html)\n'
        'If you are trying something "*py" for "Everyfile that ends with py"\n'
        'you can use just "py"(if you can tolerate .pyc) or "py$"\n'
        )
        raise WrongPattern(msg.format(pattern=file_pattern,
                                      red=RED_CHARACTER,
                                      no_color=NO_COLOR))

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
           ignore_case=False, ignore_vcs=False, return_results=True,
           fuzzy=False, return_exec_result=False, run_module_command=False,
           program=False):
    '''
        Search the files matching the pattern.
        The files will be returned as a list, and can be optionally printed

        if return_exec_result is True in no return_results are specified,
        the function will return 1 if any execution has been wrong
    '''

    # Create the compare function
    compare = create_comparison(file_pattern, ignore_case, fuzzy)

    if return_results:
        results = []

    exec_result = 0

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

                full_filename = os.path.join(root, filename)

                if delete:
                    delete_file(full_filename)

                elif exec_command:
                    if execute_command(exec_command[0], full_filename):
                        exec_result = 1

                elif run_module_command:
                    if run_module(run_module_command, full_filename):
                        exec_result = 1

                elif program:
                    if execute_python_string(program, full_filename):
                        exec_result = 1

                elif output:
                    print_match(smatch, colored)

                if return_results:
                    results.append(full_filename)

    if return_results:
        return results
    elif return_exec_result:
        return exec_result


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

    result = os.system(command)
    if result:
        return 1
    return 0


def execute_python_string(program, full_filename):
    try:
        exec(program, {}, {'filename': full_filename})
        result = 0
    except Exception as e:
        print(e)
        result = 1

    return result


def run_module(module_invocation, full_filename):
    old_argv = sys.argv
    result = 0

    args = module_invocation.split()
    module_name, args = args[0], args[1:]

    if args:
        args = [arg.replace('{}', full_filename) for arg in args]
    else:
        args = [full_filename]

    sys.argv = [module_name] + args

    try:
        runpy.run_module(module_name, run_name='__main__')
    except SystemExit as e:
        result = e.code
    except Exception as e:
        print(e)
        result = 1

    sys.argv = old_argv

    return result


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

    action = parser.add_mutually_exclusive_group()

    action.add_argument('--delete',
                        action='store_true',
                        dest='delete',
                        help='Delete files found',
                        default=False)

    action.add_argument('--exec',
                        dest='exec_command',
                        nargs=1,
                        metavar=('"command"'),
                        help='Execute the given command with the file found '
                             "as argument. The string '{}' will be replaced "
                             'with the current file name being processed. '
                             'If this option is used, ffind will return a '
                             'status code of 0 if all the executions return '
                             '0, and 1 otherwise',
                        default=False)

    action.add_argument('--module',
                        dest='run_module',
                        metavar=('"module_name args"'),
                        help='Execute the given module with the file found '
                             "as argument. The string '{}' will be replaced "
                             'with the current file name being processed. '
                             'If this option is used, ffind will return a '
                             'status code of 0 if all the executions return '
                             '0, and 1 otherwise.  Only SystemExit is caught',
                        default=False)

    action.add_argument('--command',
                        dest='program',
                        metavar=('"program"'),
                        help='Execute the given python program with the file '
                             "found placed in local variable 'filename'. "
                             'If this option is used, ffind will return a '
                             'status code of 1 if any exceptions occur, '
                             'and 0 otherwise.  SystemExit is not caught',
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

    exec_result = search(directory=args.dir,
                         file_pattern=args.filepattern,
                         path_match=args.path_match,
                         colored=args.colored,
                         follow_symlinks=args.follow_symlinks,
                         ignore_hidden=args.ignore_hidden,
                         delete=args.delete,
                         ignore_case=ignore_case,
                         exec_command=args.exec_command,
                         return_exec_result=True,
                         ignore_vcs=args.ignore_vcs,
                         fuzzy=args.fuzzy,
                         return_results=False,
                         run_module_command=args.run_module,
                         program=args.program,
                         )
    exit(exec_result)


def run():
    try:
        parse_params_and_search()
    except KeyboardInterrupt:
        pass
    except WrongPattern as err:
        print(err)
        exit(1)


if __name__ == '__main__':
    run()
