from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_file):
	pdf_writer = PdfFileWriter()
	pdf_reader = PdfFileReader(pdf_file)

	#Rotate page 90 degrees to the right
	page_1 = pdf_reader.getPage(0).rotateClockwise(90)
	pdf_writer.addPage(page_1)

	#Rotate page 90 degrees to the left
	page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
	pdf_writer.addPage(page_2)

	#Add a page in normal orientation
	pdf_writer.addPage(pdf_reader.getPage(2))

	with open('rotate_pages.pdf', 'wb') as fw:
		pdf_writer.write(fw)

if __name__ == '__main__':
	path = 't1.pdf'
	rotate_pages(path)