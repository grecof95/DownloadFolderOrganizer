#Download Folder Organizer
#Frank Greco 5/7/26
#Python3.13
 
import pathlib #path(), .iterdir(), .suffix, .exists(), .mkdir(), is_file(), .is_dir()
import shutil #move()
import datetime #datetime.now(), strftime()
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
 
#Locate download folder
 
download_folder = pathlib.Path.home() / "Downloads" #path to download folder 
dl = download_folder / "DownloadOrganizerLogs" #Log folder
dl.mkdir(parents=True, exist_ok=True) #make a download and logs subfolder folder if either doesn't exist
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #get date time
month_year = datetime.datetime.now().strftime("%B%Y") #get month and year for subdirectory (e.g., May2026)
month_year_folder = dl / month_year #create path for month/year subfolder
month_year_folder.mkdir(exist_ok=True) #create the month/year subfolder if it doesn't exist
process_log = month_year_folder / f"log_{timestamp}.txt" #the log placed inside month/year subfolder
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

#set up nested dictionary structure
#Main Category > Subcategory > File Extensions
file_categories = {
    "Documents": {
        "WordFiles": [".docx", ".doc"],
        "PDFs": [".pdf"],
        "TextFiles": [".txt", ".rtf"]
    },
    "Excel": {
        "Spreadsheets": [".xlsx", ".xls"],
        "CSVFiles": [".csv"]
    },
    "Images": {
        "Photos": [".jpg", ".jpeg", ".png", ".svg"],
        "GIFs": [".gif"], 
        "Paint": [".paint"]
    },
    "Archives": {
        "ZipFiles": [".zip"],
        "RarFiles": [".rar"],
        "SevenZip": [".7z"]
    },
    "Executables": {
        "Installers": [".exe", ".msi"]
    },
    "Programming": {
        "Python": [".py"],
        "C#": [".cs"],
        "Java": [".java", ".class"],
        "C and C++": [".cpp", ".c", ".h", ".cxx"],
        "Ruby": [".rb"],
        "Swift": [".swift"],
        "Go": [".go"],
        "Rust": [".rs"],
        "PHP": [".php", ".phtml"]
    },
    "Web Dev and Markup": {
        "Javascript": [".js", ".mjs"],
        "HTML": [".html"],
        "CSS": [".css"],
        "JSON": [".json", ".jsonId"],
        "XML": [".xml"],
        "Markdown": [".md"],
        "Sass": [".scss", ".sass"]
    },
    "ScriptsAndConfig":{
        "Shell": [".sh"],
        "Windows Batch file": [".bat", ".cmd"],
        "Database": [".sql"],
        "Initialization Config": [".ini"],
        "YAML Config": [".yaml", ".yml"]
    },
    "Media": {
        "Audio": [".mp3", ".wav"],
        "Video": [".mp4", ".avi", ".mov"]
    }
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
    if item.name in {"DownloadOrganizerLogs", "Folders", "Documents", "Excel", "Images", "Archives", "Executables", "Code", "Other", "Programming", "Web Dev and Markup", "ScriptsAndConfig", "Media"}: #if the folder is named one of these, ignore it
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
 
#Recursive function to process files in all subdirectories
def organize_files(search_folder):
    global file_success_counter, file_failure_counter
    
    for item in search_folder.iterdir():
        # Skip only the main category folders and system folders (allow searching in subcategories)
        if item.name in {"DownloadOrganizerLogs", "Folders"}:
            continue
        
        # If it's a directory, recursively search it
        if item.is_dir():
            organize_files(item)
            continue
        
        # If it's a file, process it
        if item.is_file():
            fl = item
            ext = item.suffix.lower()
 
            with open(process_log, "a") as f:
                f.write(f"{timestamp}: {fl} is file type {ext} \n")
 
            # Find the main category and subcategory
            main_category = "Other"
            sub_category = "Other"
            
            for category, subcategories in file_categories.items():
                for subcat, extensions in subcategories.items():
                    if ext in extensions:
                        main_category = category
                        sub_category = subcat
                        break
                if main_category != "Other":
                    break
 
            with open(process_log, "a") as f:
                f.write(f"{timestamp}: File {fl} with type {ext} move to {main_category}/{sub_category} \n")
 
            # Create main category folder
            main_folder_path = download_folder / main_category
            if not main_folder_path.exists():
                main_folder_path.mkdir()
                with open(process_log, "a") as f:
                    f.write(f"{timestamp}: Creating main folder directory {main_folder_path}\n")
 
            # For "Other" category, skip subcategory creation and move directly
            if main_category == "Other":
                destination = main_folder_path / item.name
            else:
                # Create subcategory folder for other categories
                sub_folder_path = main_folder_path / sub_category
                if not sub_folder_path.exists():
                    sub_folder_path.mkdir()
                    with open(process_log, "a") as f:
                        f.write(f"{timestamp}: Creating subfolder directory {sub_folder_path}\n")
                destination = sub_folder_path / item.name
            
            # Check if file is already in the correct location
            if item == destination:
                with open(process_log, "a") as f:
                    f.write(f"{timestamp}: File {item} already in correct location {destination}\n")
                continue
            
            try:
                shutil.move(item, destination)
                with open(process_log, "a") as f:
                    f.write(f"{timestamp}: Moving {item} to {destination}\n")
                file_success_counter += 1
 
            except Exception as e:
                with open(process_log, "a") as f:
                    f.write(f"{timestamp}: Unable to move {item} to {destination} \nError: {str(e)} \n")
                file_failure_counter += 1
 
#Read files for file type (not folders) - searches in all subdirectories recursively
organize_files(download_folder)
 
with open(process_log, "a") as f: #write final log
     f.write(f"{timestamp}: File movement job complete. Download folder organized.\nTotal folders moved: {folder_success_counter}.\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}.\nTotal files failed to move: {file_failure_counter}")
 
# Close progress window and show completion message
progress_root.destroy()
 
#display on screen job complete
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Complete", f"File movement job complete. Download folder organized.\n\nTotal folders moved: {folder_success_counter}\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}\nTotal files failed to move: {file_failure_counter}\n\nLog location: {process_log}")
root.destroy()