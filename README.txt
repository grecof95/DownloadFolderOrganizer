================================================================================
DOWNLOAD FOLDER ORGANIZER
================================================================================
 
DESCRIPTION:
Download Folder Organizer is a Python application that automatically organizes 
files in your Downloads folder by file type. It creates category folders 
(Documents, Images, Excel, Archives, Code, Executables) and moves files into 
the appropriate folder based on their file extension.
 
Any folders that are not recognized system folders are moved to a "Folders" 
subfolder for safekeeping.
 
================================================================================
FEATURES:
================================================================================
 
- Automatically categorizes files by type
- Moves unrecognized folders to a dedicated "Folders" directory
- Creates detailed logs of all file movements and errors
- User-friendly progress window during organization
- Detailed error messages if files cannot be moved
- Supports the following file types:
 
  Documents:  .txt, .docx, .pdf, .json, .xml
  Excel:      .xlsx, .xls, .csv
  Images:     .jpg, .jpeg, .png, .gif, .paint
  Archives:   .zip, .rar, .7z
  Executables: .exe, .msi
  Code:       .py, .cs, .js, .html, .sql
 
================================================================================
REQUIREMENTS:
================================================================================
 
- Windows operating system
- No additional software required (Python not needed)
 
================================================================================
INSTALLATION & USAGE:
================================================================================
 
1. Download the DownloadFolderOrganizer.exe file
2. Double-click the .exe file to run
3. A progress window will appear showing the organization is in progress
4. Once complete, a summary window will display the results
5. Check your Downloads folder to see the organized files
 
================================================================================
LOGS:
================================================================================
 
Each time you run the program, a detailed log is created in:
  Downloads/Logs/log_[DATE_TIME].txt
 
These logs contain information about:
- Files that were successfully moved
- Files that failed to move (with error reasons)
- Folders that were moved
- Creation of new category folders
 
You can use these logs to troubleshoot issues or verify what the program did.
 
================================================================================
FILE ORGANIZATION STRUCTURE:
================================================================================
 
After running the organizer, your Downloads folder will look like:
 
Downloads/
├── Documents/          (contains .txt, .docx, .pdf, etc.)
├── Excel/              (contains .xlsx, .xls, .csv)
├── Images/             (contains .jpg, .png, .gif, etc.)
├── Archives/           (contains .zip, .rar, .7z)
├── Executables/        (contains .exe, .msi)
├── Code/               (contains .py, .js, .html, etc.)
├── Other/              (contains files with unknown extensions)
├── Folders/            (contains any subdirectories from Downloads)
└── Logs/               (contains organization logs)
 
================================================================================
COMMON ISSUES:
================================================================================
 
Q: A file says it failed to move. Why?
A: Check the log file in Downloads/Logs/. Common reasons include:
   - File is currently open in another program
   - File is locked by Windows or another process
   - Permission issues
   
Solution: Close the file or program using it and run the organizer again.
 
Q: Can I undo the organization?
A: The program doesn't have an undo feature, but all files are simply moved 
   to organized folders - nothing is deleted. You can manually move files back 
   if needed.
 
Q: Will this delete my files?
A: No. The program only moves files to different folders. No files are deleted.
   See the LICENSE file for liability information.
 
Q: Can I customize the file categories?
A: Currently, the categories are built into the program. To customize them, 
   you would need to modify the source code.
 
================================================================================
SYSTEM REQUIREMENTS:
================================================================================
 
- Windows 7, 8, 10, or 11
- Approximately 50-100 MB of disk space for the application
- Read/write access to your Downloads folder
 
================================================================================
SUPPORT:
================================================================================
 
This is a free, open-source project. For issues, suggestions, or to view 
the source code, visit the GitHub repository.
 
================================================================================
VERSION:
================================================================================
 
Version: 1.0
Created: May 7, 2026
Python Version: 3.13
 
================================================================================