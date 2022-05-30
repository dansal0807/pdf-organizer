#Understading the PDF library

''' Passos do script:

1. Ler os nomes dos pdfs da pasta.
2. Organizar por "Sobrenome" + "-" + "Nome do arquivo";
2.1 Verificar se o arquivo possui essas informações em si.
2.2 Caso tenha ok, Caso não, abrir o arquivo e procurar na primeira e segunda página o nome do arquivo;
2.2.1 Para isso, fazer um print do PDF para buscar o ISBN ou DOI.
3. Diferenciação entre Livros e artigos.
 '''

from PyPDF2 import PdfFileReader
import pdftotext
import string
import requests
import json
import os
import re

cur_dir = os.getcwd()
files = os.listdir(cur_dir)
file_names = []

for file in files:
    if ".pdf" in file:
        file_names.append(file)

def read_pdf(pdf_path):
    #pdf_path = cur_dir + pdf
    with open(pdf_path, 'rb') as file_:
        pdf = PdfFileReader(file_)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        
        txt = f"""
        Information about {pdf_path}: 

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """
        
        for page in range(0,5):
            try:
                pdf_read = pdf.getPage(page)
                print(f"-------- Page {page} --------")
                text = "".join(pdf_read.extractText().split())
                if "DOI" in text:
                    print(f"\n\n\n\n")
                    print("Aqui está o DOI")
                    
                    research_doi = text.split("DOI:")
                    if string.digits not in research_doi[1]:
                        pass
            except Exception as e:
                print(e)
                
        
        return information, pdf_read
    
for file in file_names:
    with open(file, "rb") as file_:
        pdf = pdftotext.PDF(file_)
        print(pdf.read(2))




