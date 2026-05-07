#Download Folder Organizer
#Frank Greco 5/7/2026
#Python 3.13

import pathlib #path(), .iterdir(), .suffix, .exists(), .mkdir(), is_file(), .is_dir()
import shutil #move()
import datetime #datetime.now(), strftime()
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#commands needed
download_folder = pathlib.Path.home() / "Downloads" #path to download folder 
dl = download_folder / "Logs" #Log folder
dl.mkdir(parents=True, exist_ok=True) #make a download and logs subfolder folder if either doesn't exist
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #get date time
process_log = dl / f"log_{timestamp}.txt" #the log
folders_dir = download_folder / "Folders" #downloaded folders folder
folders_dir.mkdir(exist_ok=True) #make a downloaded folders folder subfolder folder if it doesn't exist
 
#Counters
file_success_counter = 0
file_failure_counter = 0
folder_success_counter = 0
folder_failure_counter = 0
 
#does download folder exist? No> error and exit. Yes> continue
if download_folder.exists():
    with open(process_log, "w") as f: #open up the error log file
        f.write(f"{timestamp}: Downloads folder found, continuing.\n") #Write log. 
else:     
    with open(process_log, "w") as f: #open up the error log file
        f.write(f"{timestamp}: Downloads folder not accessible. Fix program.") #Write error. 
 
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Error", f"Downloads folder not accessible.\n\nCheck error log in {process_log}")
    root.destroy()
    sys.exit() #exit program for this error
 
#does download folder exist? No> error and exit. Yes> continue
if dl.exists():
    with open(process_log, "w") as f: #open up the error log file
        f.write(f"{timestamp}: Logs folder found, continuing.\n") #Write log. 
else:     
    with open(process_log, "w") as f: #open up the error log file
        f.write(f"{timestamp}: Logs folder not accessible. Fix program.\n") #Write error. 
 
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Error", f"Logs folder not accessible.\n\nCheck error log in {process_log}")
    root.destroy()
    sys.exit() #exit program for this error
 
#set up dictionary
#documents> pdf, docx, txt | Excel>xlsx, xls, csv | Images |jpg, png, gif | Archives > zip, rar | Executables exe>msi | Code > py, js, html, etc
file_categories = {
    ".txt": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".json": "Documents",
    ".xml": "Documents",
    ".xlsx": "Excel",
    ".xls": "Excel",
    ".csv": "Excel",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".paint": "Images",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".exe": "Executables",
    ".msi": "Executables",
    ".py": "Code",
    ".cs": "Code",
    ".js": "Code",
    ".html": "Code",
    ".sql": "Code"
}
 
# Create progress window
progress_root = tk.Tk()
progress_root.title("Download Folder Organizer")
progress_root.geometry("400x120")
progress_root.resizable(False, False)
 
progress_label = tk.Label(progress_root, text="Organizing downloads folder...", font=("Arial", 12))
progress_label.pack(pady=10)
 
progress_bar = ttk.Progressbar(progress_root, mode='indeterminate', length=350)
progress_bar.pack(pady=10)
progress_bar.start()
 
progress_root.update()
 
#folder logic
for item in download_folder.iterdir(): #for every folder in the download folder
 
    # skip system/output folders
    if item.name in {"Logs", "Folders", "Documents", "Excel", "Images", "Archives", "Executables", "Code", "Other"}: #if the folder is named one of these, ignore it
        continue
 
    # Move folders (no internal inspection)
    if item.is_dir():
        try:
            shutil.move(item, folders_dir)
            with open(process_log, "a") as f:
                f.write(f"{timestamp}: Moved folder named {item} to {folders_dir} \n") #log the file to to the file type. 
            folder_success_counter += 1
        except Exception as e:
            with open(process_log, "a") as f:
                f.write(f"{timestamp}: Folder named {item} could not be moved to {folders_dir} \nError: {str(e)} \n") #log the file to to the file type. 
            folder_failure_counter += 1
        continue
 
#Read files for file type (not folders) For each file: detemine file extension 
for file in download_folder.iterdir(): #for every file in the download folder, go through each one through iteration function interdir()
    
    # Skip system folders
    if file.name in {"Logs", "Folders", "Documents", "Excel", "Images", "Archives", "Executables", "Code", "Other"}:
        continue
    
    if file.is_file(): #If the file is a file
 
        fl = file #the files themselves
        ext = file.suffix.lower() #get the file suffix aka the file type and make sure it's transposed to all lower case
 
        with open(process_log, "a") as f: #open up the log
            f.write(f"{timestamp}: {fl} is file type {ext} \n") #log the file to to the file type. 
 
        category = file_categories.get(ext, "Other") #Match extension to category - No match assign to "other"
 
        with open(process_log, "a") as f: #open up the log
                    f.write(f"{timestamp}: File {fl} with type {ext} move to {category} \n") #log the file to to the file type. 
 
        folder_path = download_folder / category #make a destination folder based in download folder and category like downloads/images etc
 
        if not folder_path.exists(): #If the folder path doesn't exist, 
            folder_path.mkdir() #make a folder path
 
        with open(process_log, "a") as f: #open up the log
            f.write(f"{timestamp}: Creating folder directory {folder_path}") #log the new folder being created
 
 
        destination = folder_path / file.name #make a final destination after the creation is done. Then we can move the file to this destination
        try:
            shutil.move(file, destination) #moving file
            with open(process_log, "a") as f: #open up the log
                f.write(f"{timestamp}: Moving {file} to {destination}") #log the file being moved
            file_success_counter +=1 #add one to the success counter
 
        except Exception as e: 
            with open(process_log, "a") as f: #open up the error log file
                f.write(f"{timestamp}: Unable to move {file} to {destination} \nError: {str(e)} \n") #write error to the log
            file_failure_counter +=1 #add one to the fail counter
 
with open(process_log, "a") as f: #write final log
     f.write(f"{timestamp}: File movement job complete. Download folder organized.\nTotal folders moved: {folder_success_counter}.\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}.\nTotal files failed to move: {file_failure_counter}")
 
# Close progress window and show completion message
progress_root.destroy()
 
#display on screen job complete
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Complete", f"File movement job complete. Download folder organized.\n\nTotal folders moved: {folder_success_counter}\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}\nTotal files failed to move: {file_failure_counter}\n\nLog location: {process_log}")
root.destroy()