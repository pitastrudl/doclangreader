#!/usr/bin/env python
import PyPDF2
import os

with os.scandir('W:\OpendirFiles\Bash') as dirr:
    for fajl in dirr:
            if fajl.name.endswith('pdf') and fajl.is_file():
                 print(fajl.name)

#W:\OpendirFiles\Bash


pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
bufferedtext = ""

stoppage=0
for x in range(pdfReader.getNumPages()):

    pageObj = pdfReader.getPage(x)
    bufferedtext += pageObj.extractText()
    if stoppage == 10:
        break
    else:
        stoppage += 1
    print('\n', x)
    print('\n', stoppage)

print(bufferedtext)

#getdir
#list files
#list only pdf
#itearete trough list