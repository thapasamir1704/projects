import PyPDF2
import sys

pdffile=sys.argv[1]
template = PyPDF2.PdfFileReader(open(pdffile, 'rb')) #superpdf is the name of pdf you want to  watermark
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)