from PyPDF2 import PdfMerger, PdfReader
import os

os.chdir(r'C:\Users\David Huang\Downloads\Solo Leveling')
merger = PdfMerger()

for filename in os.listdir():
    with open(filename, 'rb') as source:
        tmp = PdfReader(source)
        merger.append(tmp)

pdfname = input("Please enter combined pdf file name:")
merger.write(pdfname + ".pdf")