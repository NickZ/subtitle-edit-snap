#!/bin/bash

# This script runs strace for debugging
# use '-e' option to select which calls you want or don't want.

sudo strace -u $USER -e 'open,openat,open_by_handle_at,execve,stat,access,fstat,newfstatat' -f -s 255 -D -vv -o ./baresubedit.trace.log mono ./subtitleedit/SubtitleEdit.exe
#sudo strace -u $USER -e '!select,pselect6,_newselect,clock_gettime,sigaltstack,gettid,gettimeofday,nanosleep' -f -D -vv -o ./subedit.trace.log  /snap/bin/subtitle-edit $@
