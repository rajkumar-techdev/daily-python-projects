import os #operating system

import shutil#used to move files from one place to another

#main function pass the path of the folder you want to organize

def organize_folder(folder_path):
    file_types={
        "Images":[".png",".jpg","jpeg",".gif"],
        "Documents":[".pdf",".docx",".txt",".pptx"],
        "Videos":[".mp4","mkv",".avi"],
        "Audio":[".mp3","wav"],
    }

#loop though every file and folder inside the path you provided

    for filename in os.listdir(folder_path):
       file_ext=os.path.splitext(filename)[1]
       file_moved=False

       for folder,extensions in file_types.items():
           if file_ext.lower() in extensions:
               folder_name=os.path.join(folder_path,folder)
               os.makedirs(folder_name,exist_ok=True)
               shutil.move(os.path.join(folder_path,filename),os.path.join(folder_name,filename))
               file_moved=True
               break

       if not file_moved and os.path.isfile(os.path.join(folder_path,filename)):
           others_folder=os.path.join(folder_path,"Others")
           os.makedirs(others_folder,exist_ok=True)
           shutil.move(os.path.join(folder_path,filename),os.path.join(others_folder,filename))

    print("Files Organized Successfully")

organize_folder("C:/Users/DTLP07/Desktop/Organizer")

