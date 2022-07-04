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
import string
import requests
import json
import os
import re
import doi
import textwrap

cur_dir = os.getcwd()
files = os.listdir(cur_dir)
file_names = []

for file in files:
    if ".pdf" in file:
        file_names.append(file)
        
        
print("Diretório atual: " + cur_dir + f'\n' + "Nome do PDF: " + file_names[0])

def read_pdf(pdf_name):
    pdf_path = cur_dir + "/" + pdf_name
    pdf = open(pdf_path, 'rb')
    pdf_ = PdfFileReader(pdf)   
    
    return pdf_

for file in file_names:
    pdf = read_pdf(file)
    for page in range(0,5):
        try:
            pdf_read = pdf.getPage(page)
            print(f"-------- Page {page} --------")
            text = "".join(pdf_read.extractText().split())
            if "DOI" in text:
                print("Aqui está o DOI")
                research_doi = text.split("DOI:")
                doi_numbers = re.findall(r'\d+', research_doi[1])
                doi_numbers ="".join(doi_numbers)
                doi.validate_doi(doi_numbers)
                
        except Exception as e:
            print(e)