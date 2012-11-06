ffind
=====

Info: An utility to search files recursivelly on a dir. 
Author: Jaime Buelta

About
=====

Basically, replaces `find . -name '*FILE_PATTERN*'` with 'ffind.py FILE_PATTERN'

- Input filename is a regex, in case is needed.
- Search recursively on current directory by default.
- Regex can affect only the filename (default) or the full path.
- Will print colorized output in glamorous red (default), except on redirected output.
- Ignores hidden directories (directories starting with .)
- Follow symlinks by default, but that can be deactivated if necesary to avoid
  recursion problems

Just check ffind.py -h to see all the options
