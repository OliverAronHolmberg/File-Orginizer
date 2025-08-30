📂 File Organizer Script

A Python script that automatically organizes files in a specified directory into their respective folders based on file type. Designed for personal use to tidy up files like pictures, videos, documents, and music.

🚀 Features

Moves image files (.png, .webp, .jpeg, .jpg, .gif) to the Pictures folder.

Moves video files (.mp4, .mov, .mkv) to the Videos folder.

Moves document files (.pdf, .docx) to the Documents folder.

Moves audio files (.mp3, .wav) to the Music folder.

Automatically scans all subfolders in the specified root directory.

Prints the names of files being moved.

Handles errors gracefully and continues processing other files.

⚙️ Requirements

Python 3.x

Standard libraries only: os, shutil

No additional installation required

📝 Usage

Update the file paths in the script according to your system for Pictures, Videos, Documents, Music, and the root folder.

Optionally, change the root folder to any folder you want to organize.

Run the script.

The script will move files to the corresponding folders and print the moved files’ names.

⚠️ Notes

Only files with the specified extensions will be moved.

Files with unsupported extensions will be ignored.

The script will not overwrite files with the same name in the destination folder; duplicates need to be handled manually.

Make sure the destination folders exist before running the script.
