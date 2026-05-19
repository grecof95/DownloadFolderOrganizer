#Download Folder Organizer v2.0
#Frank Greco 5/7/26
#Python3.13
 
#import libraries
import pathlib
import shutil
import datetime
import sys
import tkinter as tk #application gui library
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import re

# ============================================================
# MAIN LOOP - Allows navigation between menu, organize, and undo
# ============================================================

while True:
    
    #Main menu screen - Choose Organize or Undo
    main_menu_root = tk.Tk()
    main_menu_root.title("Download Folder Organizer")
    main_menu_root.geometry("550x350")
    main_menu_root.resizable(False, False)

    # Title
    title_label = tk.Label(main_menu_root, text="Download Folder Organizer", font=("Arial", 18, "bold"))
    title_label.pack(pady=20)

    # Description
    description_text = """Choose an operation:

ORGANIZE: Automatically sorts your Downloads folder into categories and subcategories
(Documents/WordFiles, Images/Photos, Programming/Python, etc.)

UNDO: Reverses the last organization operation by reading the log file
and moving files back to their original location"""

    description_label = tk.Label(main_menu_root, text=description_text, font=("Arial", 10), justify=tk.LEFT, wraplength=500)
    description_label.pack(pady=15, padx=20)

    # Button frame
    button_frame = tk.Frame(main_menu_root)
    button_frame.pack(pady=25)

    selected_operation = None

    #function for when user selects organize to go the organize section of the script
    def on_organize():
        global selected_operation
        selected_operation = "organize" #use selected option to navigate to organize portion of code
        main_menu_root.destroy() #close the GUI box

    #function for when user selects organize to go the organize section of the script
    def on_undo():
        global selected_operation
        selected_operation = "undo" #use selected option to navigate to undo portion of code
        main_menu_root.destroy() #close the GUI box

    #organize button
    organize_btn = tk.Button(button_frame, text="Organize Downloads", font=("Arial", 12, "bold"), command=on_organize, width=20, bg="#4CAF50", fg="white", padx=10, pady=10)
    organize_btn.pack(side=tk.LEFT, padx=10)

    #undo button
    undo_btn = tk.Button(button_frame, text="Undo Organization", font=("Arial", 12, "bold"), command=on_undo, width=20, bg="#FF9800", fg="white", padx=10, pady=10)
    undo_btn.pack(side=tk.LEFT, padx=10)

    main_menu_root.mainloop()

    # Exit if user didn't select anything (closed the window)
    if selected_operation is None:
        sys.exit()

    # ============================================================
    # ORGANIZE MODE
    # ============================================================

    if selected_operation == "organize":
        
        #Locate download folder
        download_folder = pathlib.Path.home() / "Downloads"
        dl = download_folder / "DownloadOrganizerLogs"
        dl.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        month_year = datetime.datetime.now().strftime("%B%Y")
        month_year_folder = dl / month_year
        month_year_folder.mkdir(exist_ok=True)
        process_log = month_year_folder / f"log_{timestamp}.txt"
        folders_dir = download_folder / "Folders"
        folders_dir.mkdir(exist_ok=True)
        
        #Counters
        file_success_counter = 0
        file_failure_counter = 0
        folder_success_counter = 0
        folder_failure_counter = 0
        
        #does download folder exist? No> error and exit. Yes> continue
        if download_folder.exists():
            with open(process_log, "w") as f:
                f.write(f"{timestamp}: Downloads folder found, continuing.\n")
        else:     
            with open(process_log, "w") as f:
                f.write(f"{timestamp}: Downloads folder not accessible. Fix program.")
         
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", f"Downloads folder not accessible.\n\nCheck error log in {process_log}")
            root.destroy()
            sys.exit()
         
        #does log folder exist? No> error and exit. Yes> continue
        if dl.exists():
            with open(process_log, "w") as f:
                f.write(f"{timestamp}: Logs folder found, continuing.\n")
        else:     
            with open(process_log, "w") as f:
                f.write(f"{timestamp}: Logs folder not accessible. Fix program.\n")
         
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", f"Logs folder not accessible.\n\nCheck error log in {process_log}")
            root.destroy()
            sys.exit()

        #assigning false value to cancel organize clicked for use below   
        cancel_organize_clicked = False

        #Welcome screen before organizing
        welcome_root = tk.Tk()
        welcome_root.title("Download Folder Organizer")
        welcome_root.geometry("550x300")
        welcome_root.resizable(False, False)

        # Title for organizer
        welcome_title = tk.Label(welcome_root, text="Download Folder Organizer", font=("Arial", 18, "bold"))
        welcome_title.pack(pady=15)

        # Description
        welcome_description_text = """This program will organize your Downloads folder into categories and subcategories:

Examples: Documents/WordFiles, Images/Photos, Programming/Python, etc.

Files will be automatically sorted by type and moved to appropriate folders.

Do you wish to organize your Downloads folder now?"""

        #gui for the organizer 
        welcome_description_label = tk.Label(welcome_root, text=welcome_description_text, font=("Arial", 10), justify=tk.LEFT, wraplength=500)
        welcome_description_label.pack(pady=15, padx=20)

        # Button frame
        welcome_button_frame = tk.Frame(welcome_root)
        welcome_button_frame.pack(pady=20)

        organize_confirmed = False

        #creating function for organizer confirmation
        def on_confirm_organize():
            global organize_confirmed
            organize_confirmed = True
            welcome_root.destroy() #close gui

        #creating function for organizer cancellation - goes back to main menu
        def on_cancel_organize():
            global cancel_organize_clicked
            cancel_organize_clicked = True
            welcome_root.destroy()

        confirm_btn = tk.Button(welcome_button_frame, text="Organize!", font=("Arial", 12, "bold"), command=on_confirm_organize, width=18, bg="#4CAF50", fg="white", padx=10, pady=8)
        confirm_btn.pack(side=tk.LEFT, padx=10)

        cancel_btn = tk.Button(welcome_button_frame, text="Cancel", font=("Arial", 12), command=on_cancel_organize, width=18, padx=10, pady=8)
        cancel_btn.pack(side=tk.LEFT, padx=10)

        welcome_root.mainloop()

        # If cancel clicked, go back to main menu (continue the while loop)
        if cancel_organize_clicked:
            continue

        # Exit if user clicked cancel
        if not organize_confirmed:
            sys.exit()

        #set up nested dictionary structure
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
        for item in download_folder.iterdir():
         
            # skip system/output folders
            if item.name in {"DownloadOrganizerLogs", "Folders", "Documents", "Excel", "Images", "Archives", "Executables", "Code", "Other", "Programming", "Web Dev and Markup", "ScriptsAndConfig", "Media"}:
                continue
         
            # Move folders (no internal inspection)
            if item.is_dir():
                try:
                    shutil.move(item, folders_dir)
                    with open(process_log, "a") as f:
                        f.write(f"{timestamp}: Moved folder named {item} to {folders_dir} \n")
                    folder_success_counter += 1
                except Exception as e:
                    with open(process_log, "a") as f:
                        f.write(f"{timestamp}: Folder named {item} could not be moved to {folders_dir} \nError: {str(e)} \n")
                    folder_failure_counter += 1
                continue
         
        #Recursive function to process files in all subdirectories
            #Recursive function to process files in all subdirectories
            def organize_files(search_folder):
                global file_success_counter, file_failure_counter
                
                for item in search_folder.iterdir():
                    # Skip only the main category folders and system folders
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
                        
                        # Check if file is already in the correct location - SKIP IT, DON'T LOG IT
                        if item.resolve() == destination.resolve():
                            continue
                        
                        # Only log and move if file needs to be moved
                        try:
                            shutil.move(str(item), str(destination))
                            with open(process_log, "a") as f:
                                f.write(f"{timestamp}: Successfully moved {item.name} to {main_category}/{sub_category}\n")
                            file_success_counter += 1

                        except Exception as e:
                            with open(process_log, "a") as f:
                                f.write(f"{timestamp}: FAILED to move {item.name} to {main_category}/{sub_category} - Error: {str(e)}\n")
                            file_failure_counter += 1
         
        #Read files for file type - searches in all subdirectories recursively
        organize_files(download_folder)
         
        with open(process_log, "a") as f:
             f.write(f"{timestamp}: File movement job complete. Download folder organized.\nTotal folders moved: {folder_success_counter}.\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}.\nTotal files failed to move: {file_failure_counter}")
         
        # Close progress window and show completion message
        progress_root.destroy()
         
        #display on screen job complete
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Complete", f"File movement job complete. Download folder organized.\n\nTotal folders moved: {folder_success_counter}\nTotal folders failed to move: {folder_failure_counter}\nTotal files moved: {file_success_counter}\nTotal files failed to move: {file_failure_counter}\n\nLog location: {process_log}")
        root.destroy()
        
        # END ORGANIZE MODE - Go back to main menu
        continue

# ============================================================
    # UNDO MODE
    # ============================================================

    elif selected_operation == "undo":
        
        #assigning value of false to cancel undo clicked which can then be reassigned to true later
        cancel_undo_clicked = False

        #Welcome screen for undo
        undo_welcome_root = tk.Tk()
        undo_welcome_root.title("Download Folder Organizer - UNDO")
        undo_welcome_root.geometry("550x350")
        undo_welcome_root.resizable(False, False)

        # Title
        undo_title = tk.Label(undo_welcome_root, text="Download Folder Organizer - UNDO", font=("Arial", 18, "bold"))
        undo_title.pack(pady=15)

        # Description
        undo_description_text = """This utility will UNDO a file organization operation.

It works by reading a log file and moving files back to their original location (Downloads folder).

IMPORTANT:
- Select the log file you wish to undo
- Folders created during organization will NOT be removed
- Only files will be moved back
- This action cannot be undone after completion

Do you wish to proceed?"""

        undo_description_label = tk.Label(undo_welcome_root, text=undo_description_text, font=("Arial", 10), justify=tk.LEFT, wraplength=500)
        undo_description_label.pack(pady=10, padx=20)

        # Button frame
        undo_button_frame = tk.Frame(undo_welcome_root)
        undo_button_frame.pack(pady=20)

        undo_proceed_clicked = False
        undo_selected_log_file = None

        def on_select_undo_log():
            global undo_selected_log_file, undo_proceed_clicked
            download_folder = pathlib.Path.home() / "Downloads"
            logs_folder = download_folder / "DownloadOrganizerLogs"
            
            undo_selected_log_file = filedialog.askopenfilename(
                initialdir=logs_folder,
                title="Select Log File to Undo",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if undo_selected_log_file:
                undo_proceed_clicked = True
                undo_welcome_root.destroy()

        def on_cancel_undo():
            global cancel_undo_clicked
            cancel_undo_clicked = True
            undo_welcome_root.destroy()

        select_log_btn = tk.Button(undo_button_frame, text="Select Log File", font=("Arial", 12, "bold"), command=on_select_undo_log, width=18, bg="#2196F3", fg="white", padx=10, pady=8)
        select_log_btn.pack(side=tk.LEFT, padx=10)

        cancel_undo_btn = tk.Button(undo_button_frame, text="Cancel", font=("Arial", 12), command=on_cancel_undo, width=18, padx=10, pady=8)
        cancel_undo_btn.pack(side=tk.LEFT, padx=10)

        undo_welcome_root.mainloop()

        # If cancel clicked, go back to main menu (continue the while loop)
        if cancel_undo_clicked:
            continue

        # Exit if user clicked cancel
        if not undo_proceed_clicked or not undo_selected_log_file:
            sys.exit()

        #Setup undo
        download_folder = pathlib.Path.home() / "Downloads"
        log_file = pathlib.Path(undo_selected_log_file)

        if not log_file.exists():
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", f"Log file not found: {log_file}")
            root.destroy()
            sys.exit()

        # Create undo log file
        dl = download_folder / "DownloadOrganizerLogs"
        undo_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        month_year = datetime.datetime.now().strftime("%B%Y")
        month_year_folder = dl / month_year
        month_year_folder.mkdir(exist_ok=True, parents=True)
        undo_log = month_year_folder / f"Undo_{undo_timestamp}.txt"

        #Counters
        files_moved_back = 0
        files_failed = 0
        files_skipped = 0
        folder_moved_counter = 0
        folder_failed_counter = 0

        # Create progress window
        undo_progress_root = tk.Tk()
        undo_progress_root.title("Download Folder Organizer - UNDO")
        undo_progress_root.geometry("400x120")
        undo_progress_root.resizable(False, False)

        undo_progress_label = tk.Label(undo_progress_root, text="Reading log and undoing organization...", font=("Arial", 12))
        undo_progress_label.pack(pady=10)

        undo_progress_bar = ttk.Progressbar(undo_progress_root, mode='indeterminate', length=350)
        undo_progress_bar.pack(pady=10)
        undo_progress_bar.start()

        undo_progress_root.update()

        # Write initial log entries
        with open(undo_log, "w") as f:
            f.write(f"{undo_timestamp}: Logs folder found, continuing.\n")

        #Parse log file and extract move operations
        move_operations = []

        try:
            with open(log_file, "r") as f:
                for line in f:
                    # Look for lines that contain "Successfully moved" operations
                    if "Successfully moved " in line:
                        # Extract the filename and destination category/subcategory
                        match = re.search(r"Successfully moved (.+) to (.+)$", line)
                        if match:
                            filename = match.group(1).strip()
                            category_subcat = match.group(2).strip()  # e.g., "Documents/PDFs"
                            
                            # Split category and subcategory
                            parts = category_subcat.split("/")
                            if len(parts) == 2:
                                main_category = parts[0]
                                sub_category = parts[1]
                                
                                # Build the full destination path
                                destination_path = download_folder / main_category / sub_category / filename
                                
                                # Original location was in Downloads folder
                                original_location = download_folder / filename
                                
                                # We want to move FROM destination BACK TO original
                                move_operations.append((str(destination_path), str(original_location), main_category, sub_category, filename))
                            elif len(parts) == 1:
                                # "Other" category has no subcategory
                                main_category = parts[0]
                                destination_path = download_folder / main_category / filename
                                original_location = download_folder / filename
                                move_operations.append((str(destination_path), str(original_location), main_category, "Other", filename))
                                
        except Exception as e:
            undo_progress_root.destroy()
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", f"Error reading log file:\n{str(e)}")
            root.destroy()
            sys.exit()

        #Execute undo operations
        for destination, original_location, main_category, sub_category, filename in move_operations:
            dest_path = pathlib.Path(destination)
            source_path = pathlib.Path(original_location)
            
            # Check if file exists at current location
            if not dest_path.exists():
                with open(undo_log, "a") as f:
                    f.write(f"{undo_timestamp}: File {filename} not found at {main_category}/{sub_category} (already moved)\n")
                files_skipped += 1
                continue
            
            # Check if file is a file (not a directory)
            if not dest_path.is_file():
                continue
            
            try:
                # Move file back to original location
                shutil.move(str(dest_path), str(source_path))
                with open(undo_log, "a") as f:
                    f.write(f"{undo_timestamp}: Successfully moved {filename} from {main_category}/{sub_category} back to Downloads.\n")
                files_moved_back += 1
            except Exception as e:
                with open(undo_log, "a") as f:
                    f.write(f"{undo_timestamp}: FAILED to move {filename} from {main_category}/{sub_category} back to Downloads - Error: {str(e)}\n")
                files_failed += 1
                continue

        # Write final summary to log
        with open(undo_log, "a") as f:
            f.write(f"{undo_timestamp}: File movement job complete. Undo action complete.\nTotal files moved: {files_moved_back}.\nTotal files failed to move: {files_failed}\nTotal files not found: {files_skipped}")

        undo_progress_root.destroy()

        # Show completion message
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Undo Complete", f"""Download Folder Organization has been undone.

Files moved back: {files_moved_back}
Files failed to move back: {files_failed}
Files not found (already moved): {files_skipped}

Note: Organized folders were NOT removed to preserve any files you may have manually placed in them.

Undo log created: {undo_log}""")
        root.destroy()
        
        # END UNDO MODE - Go back to main menu
        continue