Environment variables
---

Setting these environment variables on your command line shell, you'll set options by default. For example:

    export FFIND_CASE_SENSITIVE=1
    # equivalent to ffind -c something
    ffind something 
    FFIND_CASE_SENSITIVE=1 ffind something

- FFIND_SORT: Return the results sorted. This is slower, and is mainly to ensure
              consistency on the tests, as some filesystems may order files differently
- FFIND_CASE_SENSITIVE: Search is case sensitive. Equivalent to `-c` flag
- FFIND_CASE_INSENSITIVE: Search is case insensitive. Equivalent to `-i` flag.
- FFIND_SEARCH_HIDDEN: Search in hidden directories and files. Equivalent to `--hidden` flag.
- FFIND_SEARCH_PATH: Search in the whole path. Equivalent to `-p` flag.
- FFIND_IGNORE_VCS: Ignore paths in version control. Equivalent to `--ignore-vcs`
- FFIND_NO_SYMLINK: Do not follow symlinks. Equivalent to `--nosymlinks` flag.
- FFIND_NO_COLOR: Do not show colors. Equivalent to `--nocolor` flag.
- FFIND_FUZZY_SEARCH: Enable fuzzy search. Equivalent to `-f` flag.

If an environment variable is present, when calling `ffind -h`, the option will display [SET] at the end.
