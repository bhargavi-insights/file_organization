import os
import shutil
import hashlib
import logging

logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s-%(message)s"
)        

UNDO_LOG="undo_log.txt"

categories={1:("Images",[".jpg",".png",".jpeg",".gif"]),
            2:("PDFs",[".pdf"]),
            3:("Videos",[".mp4",".mkv"]),
            4:("WordDoc",[".doc",".docx"])
            }

def create_folder(base,folder):
    folder_path=os.path.join(base,folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        logging.info(f"Created folder:{folder}")

def get_file_hash(filepath):
    hasher=hashlib.md5()
    with open(filepath,"rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()      


path=input("enter the folder you want to organize:")
undo=input("undo last operation? (y/n):").lower()=='y'
delete_duplicates=input("Delete duplicate files? (y/n):").lower()=='y'
dry_run=input("Enable Dry-Run mode? (y/n):").lower()=='y'

if undo:
    if os.path.exists(UNDO_LOG):
        with open(UNDO_LOG,"r") as f:
            for line in f:
                src,dest=line.strip().split("|")
                if os.path.exists(dest):
                    shutil.move(dest,src)
        logging.info("Undo operation completed")
        print("Undo completed succesfully")
    else:
        print("No undo data found")
    exit() 


print("\n Choose the option")
print("1. Organize Images")
print("2. Organize the PDFs")
print("3. Organize the video")
print("4. Organize the word document")
print("5. Organize the All the files")
print("6. Exit")

choice=int(input("Enter your choice:"))


hash_map={}
undo_action=[]
duplicate_file=[]

for file in os.listdir(path):
    src=os.path.join(path,file)

    if os.path.isdir(src):
        continue 
    
    file_hash=get_file_hash(src)
    if file_hash in hash_map:
        duplicate_file.append(file)
    else:
        hash_map[file_hash]=file
    
if delete_duplicates:
    create_folder(path,"Duplicate_Deleted")
    
    for file in duplicate_file:
        src=os.path.join(path,file)
        dest=os.path.join(path,"Duplicate_Deleted",file)
        
        if dry_run:
            print(f"[DRY-RUN] Duplicate → {file}")
        else:
            if os.path.exists(src):
                shutil.move(src,dest)
                undo_action.append(f"{src}|{dest}")
                logging.info(f"Duplicate moved:{file}")    

    print("Duplicate file moved Successfully!")
    exit()

for file in os.listdir(path):
    src=os.path.join(path,file)

    if os.path.isdir(src):
        continue

    ext=os.path.splitext(file)[1].lower()
    moved=False

    if choice==5:    
        for folder,extensions in categories.values():
            if ext in extensions:
                create_folder(path,folder)
                dest=os.path.join(path,folder,file)

                if dry_run:
                    print(f"[DRY-RUN] {file} -> {folder}")
                else:
                    shutil.move(src,dest)
                    undo_action.append(f"{src}|{dest}")
                    logging.info(f"Moved {file} -> {folder}")

                moved=True
                break

        if not moved: 
            create_folder(path,"other")
            dest=os.path.join(path,"other",file)

            if dry_run:
                print(f"[DRY-RUN] {file} -> other")
            else:
                shutil.move(src,dest)
                undo_action.append(f"{src}|{dest}")
                logging.info(f"Moved {file} -> other")
                                           
    else:
        folder,extensions =categories[choice]
        if ext in extensions:
            create_folder(path,folder)
            dest=os.path.join(path,folder,file)

            if dry_run:
                print(f"[DRY-RUN] {file} -> { folder}")
            else:
                shutil.move(src,dest)
                undo_action.append(f"{src}|{dest}")
                logging.info(f"Moveed {file} -> {folder}")

if not dry_run:
    with open(UNDO_LOG,"w") as f:
        for action in undo_action:
            f.write(action+"\n")

print("File organization completed successfully !")                                