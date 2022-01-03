from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(path, name_of_spilt):
	pdf = PdfFileReader(path)
	for page in range(pdf.getNumPages()):
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))

		output = f'{name_of_spilt}{page}.pdf'
		with open(output, 'wb') as output_pdf:
			pdf_writer.write(output_pdf)

if __name__ == '__main__':
	path = 'rotate_pages.pdf'
	split_pdf(path, 't1_page')