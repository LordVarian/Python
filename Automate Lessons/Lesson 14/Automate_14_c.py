import pypdf, os

os.chdir(r'C:\Users\David Huang\Downloads\Python')
pdfFile = open('meetingminutes1.pdf', 'rb')
# pdfs are in read binary mode
reader = pypdf.PdfReader(pdfFile)
len(reader.pages)

page = reader.pages[0]
print(page.extract_text())

for pageNum in range(1, len(reader.pages) + 1):
    print(reader.pages[pageNum - 1].extract_text())

