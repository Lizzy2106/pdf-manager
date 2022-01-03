from PyPDF2 import PdfFileReader

def extract_info(pdf_file):
	with open(pdf_file, 'rb') as file:
		pdf = PdfFileReader(file)
		information = pdf.getDocumentInfo()
		number_of_pages = pdf.getNumPages()

	txt = f"""
	Information about {pdf_file}:

	Author: {information.author}
	Creator: {information.creator}
	Producer: {information.producer}
	Subject: {information.subject}
	Title: {information.title}
	Number of pages: {number_of_pages}
	"""

	print(txt)
	return information

if __name__ == '__main__':
	path = 't1.pdf'
	extract_info(path)