import os
import shutil

f = os.listdir("C:/Users/Saipa/OneDrive/Desktop/Dummy_Downloads")

file_types = {
    ".pdf":"PDF_files",
    ".jpeg":"Images",
    ".jpg":"Images",
    ".png":"Images",
    ".docx":"Documents",
    ".doc":"Documents"
    }


for file in f:
    item_full_path = os.path.join('C:/Users/Saipa/OneDrive/Desktop/Dummy_Downloads',file)
    if not os.path.isfile(item_full_path):
        continue
    matched = False
    for ext in file_types:

        if file.lower().endswith(ext):
            matched = True
            folder_name = file_types[ext]
            source_path = os.path.join('C:/Users/Saipa/OneDrive/Desktop/Dummy_Downloads/',file)
            target_folder_path = os.path.join('C:/Users/Saipa/OneDrive/Desktop/Test_download',folder_name)
            destination_file_path = os.path.join(target_folder_path,file)   
            if not os.path.exists(target_folder_path):
                os.mkdir(target_folder_path)
                print(f"Created folder: {target_folder_path}")
            if os.path.exists(destination_file_path):
                name, extension =os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_file_path):
                    newfile_name = name + "_" + str(counter) + extension
                    destination_file_path = os.path.join(target_folder_path, newfile_name)
                    counter += 1
            shutil.move(source_path,destination_file_path)
            print(f"Moved '{file}' from '{source_path}' to '{destination_file_path}'")
            break
    if not matched:
        folder_name = "Others"
        target_folder_path = os.path.join('C:/Users/Saipa/OneDrive/Desktop/Test_download',folder_name)
        destination_file_path = os.path.join(target_folder_path,file)
        source_path = os.path.join('C:/Users/Saipa/OneDrive/Desktop/Dummy_Downloads/',file)
        if not os.path.exists(target_folder_path):
            os.mkdir(target_folder_path)
            print(f"Created folder: {target_folder_path}")
        if os.path.exists(destination_file_path):
            name, extension =os.path.splitext(file)
            counter = 1
            while os.path.exists(destination_file_path):
                newfile_name = name + "_" + str(counter) + extension
                destination_file_path = os.path.join(target_folder_path, newfile_name)
                counter += 1
        shutil.move(source_path,destination_file_path)
        print(f"Moved '{file}' from '{source_path}' to '{destination_file_path}'")
    
                
            
                
