import PyPDF2

pdf_file_path = 'path_to_pdf.pdf'

with open(pdf_file_path, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)  # get the first page
    text = page.extractText()
modified_text = text.replace("Donecle", "Example")
writer = PyPDF2.PdfFileWriter()
page.setContent(modified_text)  # set the modified content
writer.addPage(page)

with open('modified_pdf.pdf', 'wb') as output_file:
    writer.write(output_file)
