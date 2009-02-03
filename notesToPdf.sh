#!/bin/bash
python ntt.py "$1"
pdflatex "$1.tex"
rm "$1.tex" "$1.log" "$1.aux"
