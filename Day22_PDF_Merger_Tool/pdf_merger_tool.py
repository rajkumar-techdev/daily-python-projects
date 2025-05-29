import PyPDF2
import os

def merge_pdf(pdf_list,output_filename):
    merger=PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()
    print(f"\n Mergerd PDF Saved as : {output_filename}")


def main():
    print("PDF Merger Tool")

    num_files=int(input("How many PDF Files do you want to merge?:  "))

    pdf_list=[]

    for i in range(num_files):
        file=input(f"Enter path for PDF {i+1}: ")
        if os.path.exists(file):
            pdf_list.append(file)
        else:
            print("File not found,Skipping")

    if pdf_list:
        output_name=input("Enter output file name: ")
        merge_pdf(pdf_list,output_name)
    else:
        print("No Valid PDF File found")

main()


