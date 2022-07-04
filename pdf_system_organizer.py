import os
import sys
import time

#Implementar via sys.argv

#1. Getting the current files and directory:
cur_dir = os.getcwd()
files = os.listdir(cur_dir)
file_names = []

#Mudança 04/07: 
#1. Programa ir numa pasta desejada.
#2. Ver se deseja mudar como o programa já o faz.
#3. Listas mudanças em um .txt

#1.1 Filtering the PDF files:
for file in files:
    if ".pdf" in file:
        file_names.append(file)

#2. Making a renaming automatic function:
def pdf_model(pdf_name):
    author_name = input(f"What's the Author's name? Write the full name, if possible.\n")
    splited_name = author_name.split()
    
    if len(splited_name) > 1:
        last_name = splited_name[-1]
        first_name = splited_name[0]
        name = last_name + ", " + first_name[0].title() + "."
    else:
        name = author_name.capitalize()
        
    book_title = input("What is the name of the book?\n")
    
    book_name = name + ' - ' + book_title.title() + ".pdf"
    
    try:
        os.rename(pdf_name, book_name)
        print(f"The new name of your pdf is: {book_name}")
    except Exception as e:
        print(f"Not possible due to {e}")
    return book_name

#3. Looping through the PDF files:
for pdf in file_names:
    print(f"\nthis is your pdf: {pdf}")
    time.sleep(1)
    print(f"\n --- processing ----\n")
    renaming_choice = input("Do you want to rename this pdf? (y/n): ")
    
    if renaming_choice == "n":
        sys.exit(1)
    
    print(f"\n")
    manual_renaming = input("Do you want to rename it manually? (y/n): ")
    if manual_renaming != "y":
        print(f"\nThe automatic renaming is made through: Author's last name + author's first name's letter + book's name.")
        print(f"\n...")
        pdf_model(pdf)
        

    while renaming_choice == "y" and manual_renaming == "y":
        print(f"\n...")
        new_name = input("What is the new name of your pdf? ")
        os.rename(pdf, new_name)
        print(f"\n...")
        print(f"The new name of your pdf is: ' {new_name} '.")
        print(f"\n...")
        renaming_choice = input("Do you still want to rename this pdf? (y/n): ")
        sys.exit(1)

