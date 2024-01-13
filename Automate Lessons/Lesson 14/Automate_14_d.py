import pypdf, os

os.chdir(r'C:\Users\David Huang\Downloads\Python')

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = pypdf.PdfReader(pdf1File)
reader2 = pypdf.PdfReader(pdf2File)
writer = pypdf.PdfWriter()

for pageNum in range(1, len(reader1.pages) + 1):
    page = reader1.pages[pageNum - 1]
    writer.add_page(page)
    
for pageNum in range(1, len(reader2.pages) + 1):
    page = reader2.pages[pageNum - 1]
    writer.add_page(page)
    
outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()