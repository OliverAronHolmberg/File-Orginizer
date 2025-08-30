import os
import shutil

pictures = r"C:\Users\Olive\Pictures"
videos = r"C:\Users\Olive\Videos"
documents = r"C:\Users\Olive\Documents"
music = r"C:\Users\Olive\Music"

root = r"C:\Users\Olive"
# root = r"folder"

folders = os.listdir(root)
for folder in folders:
    try:
        files = os.listdir(f"{root}/{folder}")
        for file in files:
            source = os.path.join(root, folder, file)
            if file.endswith(".png") or file.endswith(".webp") or file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".gif"):
                shutil.move(source, os.path.join(pictures, file))
                print(file)
            if file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mkv"):
                shutil.move(source, os.path.join(videos, file))
                print(file)
            if file.endswith(".pdf") or file.endswith(".docx"):
                shutil.move(source, os.path.join(documents, file))
                print(file)
            if file.endswith(".mp3") or file.endswith(".wav"):
                shutil.move(source, os.path.join(music, file))
                print(file)
            else:
                continue
    except:
        print("Error")
        continue
        


    