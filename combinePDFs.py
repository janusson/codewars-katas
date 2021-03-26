# CombinePDFs.py / Eric Janusson
# script to combine two pdf files
# sources:
# https://caendkoelsch.wordpress.com/2019/05/10/merging-multiple-pdfs-into-a-single-pdf/
# https://www.programcreek.com/python/example/105483/PyPDF2.PdfFileMerger
import os
import PyPDF2
from pathlib import Path

# << Enter full document paths as loc1 and loc2 and end filename as finalName>>
loc1 = Path('D:/PDF-one.pdf')
loc2 = Path('D:/PDF-two.pdf')
finalName = 'Chemistry Instructor - Eric Janusson'

# open docs
doc1 = open(loc1, 'rb')
doc2 = open(loc2, 'rb')

# Create a new PdfFileWriter object which represents a blank PDF document
writer = PyPDF2.PdfFileWriter()

# create reader objects
reader1 = PyPDF2.PdfFileReader(doc1)
reader2 = PyPDF2.PdfFileReader(doc2)

# loop through pages of doc 1
for pageNum in range(reader1.numPages):
    pageObj = reader1.getPage(pageNum)
    writer.addPage(pageObj)

# loop through pages of doc 2
for pageNum in range(reader2.numPages):
    pageObj = reader2.getPage(pageNum)
    writer.addPage(pageObj)

# make output pdf file and write to it
output = open(finalName, 'wb')
writer.write(output)

# close all files
doc1.close()
doc2.close()
output.close()

print("Output 'Merged PDF File.pdf' location: " + os.getcwd())
