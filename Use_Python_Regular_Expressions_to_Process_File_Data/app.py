import sys
import os
import regex

if len(sys.argv) != 3:
    raise ValueError('Please enter an input and output filename')

fname = sys.argv[1]

if not os.path.isfile(fname):
    raise ValueError('File does not exist')

with open(fname, mode='r', encoding='utf-8') as f:
    contacts = f.readlines()

clist = []

for str in contacts:
    cstr = regex.regex_email(str)
    if cstr[0:6] == 'email:':
        clist.append(cstr + '\n')

    with open(sys.argv[2], mode='w', encoding='utf-8') as f:
        f.writelines(clist)

