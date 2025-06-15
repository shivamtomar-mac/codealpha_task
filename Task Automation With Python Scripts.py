import os
import shutil

def organize_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for f in files:
        ext = f.split('.')[-1].lower()
        folder = ''
        if ext in ['jpg', 'png', 'gif', 'jpeg']:
            folder = 'images'
        elif ext in ['txt']:
            folder = 'texts'
        elif ext in ['pdf']:
            folder = 'pdfs'
        else:
            folder = 'others'

        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        src = os.path.join(path, f)
        dst = os.path.join(folder_path, f)
        shutil.move(src, dst)

def main():
    directory = "Replace It With Directory"
    if(directory == "Replace It With Directory" or directory == ""):
        directory = input("Enter directory path to organize: ")
    
    if os.path.exists(directory):
        organize_files(directory)
        print("Files successfully organized.")
    else:
        print("Directory not found.")
    

if __name__ == '__main__':
    main()
