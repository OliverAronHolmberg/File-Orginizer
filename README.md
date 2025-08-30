# File Organizer Script

A Python script that automatically organizes files in a specified directory into their respective folders based on file type. Designed for personal use to tidy up files like pictures, videos, documents, and music.

## Features

- Image Files: Moves .png, .webp, .jpeg, .jpg, .gif to the Pictures folder.

- Video Files: Moves .mp4, .mov, .mkv to the Videos folder.

- Document Files: Moves .pdf, .docx to the Documents folder.

- Audio Files: Moves .mp3, .wav to the Music folder.

- Error Handling: Continues processing other files even if some files encounter errors.

## Requirements

- Python 3

- Standard libraries only: os, shutil

## Usage

- Update File Paths: Modify the script to set your desired directories for Pictures, Videos, Documents, Music, and the root folder.

- Run the Script: Execute the script in your terminal or command prompt.

- File Organization: The script will move files to the corresponding folders and print the names of moved files.

## Notes

- Only files with the specified extensions will be moved.

- Files with unsupported extensions will be ignored.

- Ensure the destination folders exist before running the script.

