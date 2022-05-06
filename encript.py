import PyPDF2

#pdf_in_file = open("simple.pdf",'rb')
pdf_filename = 'a.pdf'
pdf_in_file = open(pdf_filename,'rb')

inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages
output = PyPDF2.PdfFileWriter()

for i in range(pages_no):
    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt("555")

    #with open("simple_password_protected.pdf", "wb") as outputStream:
    with open("gre_research_validity_data_password_protected.pdf", "wb") as outputStream:
        output.write(outputStream)
pdf_in_file.close()



