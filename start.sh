#!/bin/bash

find . -maxdepth 1 -type f -name '[0-9]*.last' -exec rm {} \;
rename 's/([0-9]+)/$1.last/' *

source Venv/bin/activate
python3 main.py &> temp_outut.txt &
pid=$(pgrep -f "python3 main.py")
touch "${pid}"

