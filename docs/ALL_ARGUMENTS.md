All arguments
---

Call `ffind --help` to display all the options.


    usage: ffind.py [-h] [-p] [--nocolor] [--nosymlinks] [--hidden] [-c]  [-i]
                [--delete | --exec "command" | --module "module_name args" | --command "program"]
                [--ignore-vcs] [-f] [--version]
                [dir] filepattern

    Search file name in directory tree

    positional arguments:
      dir                   Directory to search
      filepattern

    optional arguments:
      -h, --help            show this help message and exit
      -p                    Match whole path, not only name of files. Set env
                            variable FFIND_SEARCH_PATH to set this automatically
      --nocolor             Do not display color. Set env variable FFIND_NO_COLOR
                            to set this automatically
      --nosymlinks          Do not follow symlinks (following symlinks can lead to
                            infinite recursion) Set env variable FFIND_NO_SYMLINK
                            to set this automatically
      --hidden              Do not ignore hidden directories and files. Set env
                            variable FFIND_SEARCH_HIDDEN to set this automatically
      -c                    Force case sensitive. By default, all lowercase
                            patterns are case insensitive. Set env variable
                            FFIND_CASE_SENSITIVE to set this automatically
      -i                    Force case insensitive. This allows case insensitive
                            for patterns with uppercase. If both -i and -c are
                            set, the search will be case sensitive.Set env
                            variable FFIND_CASE_INSENSITIVE to set this
                            automatically
      --delete              Delete files found
      --exec "command"      Execute the given command with the file found as
                            argument. The string '{}' will be replaced with the
                            current file name being processed. If this option is
                            used, ffind will return a status code of 0 if all the
                            executions return 0, and 1 otherwise
      --module "module_name args"
                            Execute the given module with the file found as
                            argument. The string '{}' will be replaced with the
                            current file name being processed. If this option is
                            used, ffind will return a status code of 0 if all the
                            executions return 0, and 1 otherwise. Only SystemExit
                            is caught
      --command "program"   Execute the given python program with the file found
                            placed in local variable 'filename'. If this option is
                            used, ffind will return a status code of 1 if any
                            exceptions occur, and 0 otherwise. SystemExit is not
                            caught
      --ignore-vcs          Ignore version control system files and directories.
                            Set env variable FFIND_IGNORE_VCS to set this
                            automatically
      -f                    Experimental fuzzy search. Increases the matches, use
                            with care. Combining it with regex may give crazy
                            results
      --return-results      For testing purposes only. Please ignore
      --version             show program's version number and exit

