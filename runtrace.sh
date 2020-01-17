#!/bin/bash
sudo strace -u nick -e 'open,openat,open_by_handle_at,execve' -f -D -vv -o ./subedit.trace.log  /snap/bin/subtitle-edit $@