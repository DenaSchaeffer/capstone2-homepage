#!/usr/bin/python3
#
# we can break this file

# Usage: python3 keyword_generator.py <Directory Containing Files>
from collections import Counter
from io import StringIO
from json import dump
from os import scandir
from pdfminer3.high_level import extract_text_to_fp
from string import punctuation
from sys import argv, exit
from bs4 import BeautifulSoup

soup = BeautifulSoup('HTML-files', 'html')


if (len(argv) < 2):
    print(
        'Usage: python3 keygen.py <Directory Containing Files>\nNo input directory specified. Quitting...\n'
    )
    exit(1)
c = Counter()
for f in scandir(argv[1]):
    with open(f.path, 'rb') as i:
        # s = StringIO()
        # extract_text_to_fp(i, s)
        # c.update(word.lower().strip(punctuation)
        #          for word in s.getvalue().split())
        # ================ for HTML =====================
        




with open('assets/htmloutput.json', 'w', encoding='utf-8') as o:
    dump(dict(c.most_common()), o)
