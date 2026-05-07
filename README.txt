================================================================================
DOWNLOAD FOLDER ORGANIZER v2.0
================================================================================

DESCRIPTION:
Download Folder Organizer is a Python application that automatically organizes 
files in your Downloads folder by file type into a two-level folder structure. 
It creates category folders (Documents, Images, Excel, Archives, Code, etc.) 
and then further organizes files into subcategories (WordFiles, PDFs, Photos, 
etc.) for even better organization.

Any folders that are not recognized system folders are moved to a "Folders" 
subfolder for safekeeping.

================================================================================
WHAT'S NEW IN v2.0:
================================================================================

 Two-Level Organization:
   - Files are now organized into main categories AND subcategories
   - Example: Documents/WordFiles/, Documents/PDFs/, Documents/TextFiles/
   - Much cleaner and more intuitive file discovery

 Expanded File Type Support:
   - Added support for 40+ file types (up from ~20)
   - New categories: Programming, Web Dev and Markup, ScriptsAndConfig, Media
   - Supports languages: Python, C#, Java, C/C++, Ruby, Swift, Go, Rust, PHP
   - Supports web dev: JavaScript, HTML, CSS, JSON, XML, Markdown, Sass
   - Supports scripts: Shell, Windows Batch, SQL, YAML, INI configs
   - Supports media: MP3, WAV, MP4, AVI, MOV

 Improved Logging:
   - Logs now organized by month/year in subfolders
   - Downloads/DownloadOrganizerLogs/May2026/log_2026-05-07_17-59-15.txt
   - Easier to find and archive old logs

 Smart File Detection:
   - Recursively searches all subdirectories for misplaced files
   - Corrects files that were manually placed in wrong folders
   - Skips files that are already in correct location (accurate counters)

 Robust Error Handling:
   - Detailed error messages for failed file movements
   - Shows exact reason why a file couldn't be moved (e.g., file is open)
   - Complete logs for troubleshooting

================================================================================
FEATURES:
================================================================================

- Two-level file categorization (Main Category / Subcategory)
- Recursively searches and organizes files in all subdirectories
- Detects and corrects misplaced files
- Creates detailed logs organized by month and year
- User-friendly progress window during organization
- Detailed error messages for troubleshooting
- Accurate success/failure counters
- Support for 40+ file types across 9 main categories

File Categories and Subcategories:

Documents:
  - WordFiles (.docx, .doc)
  - PDFs (.pdf)
  - TextFiles (.txt, .rtf)
  - DataFiles (.json, .xml)

Excel:
  - Spreadsheets (.xlsx, .xls)
  - CSVFiles (.csv)

Images:
  - Photos (.jpg, .jpeg, .png, .svg)
  - GIFs (.gif)
  - Paint (.paint)

Archives:
  - ZipFiles (.zip)
  - RarFiles (.rar)
  - SevenZip (.7z)

Executables:
  - Installers (.exe, .msi)

Programming:
  - Python (.py)
  - C# (.cs)
  - Java (.java, .class)
  - C and C++ (.cpp, .c, .h, .cxx)
  - Ruby (.rb)
  - Swift (.swift)
  - Go (.go)
  - Rust (.rs)
  - PHP (.php, .phtml)

Web Dev and Markup:
  - Javascript (.js, .mjs)
  - HTML (.html)
  - CSS (.css)
  - JSON (.json, .jsonId)
  - XML (.xml)
  - Markdown (.md)
  - Sass (.scss, .sass)

ScriptsAndConfig:
  - Shell (.sh)
  - Windows Batch file (.bat, .cmd)
  - Database (.sql)
  - Initialization Config (.ini)
  - YAML Config (.yaml, .yml)

Media:
  - Audio (.mp3, .wav)
  - Video (.mp4, .avi, .mov)

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
  Downloads/DownloadOrganizerLogs/[MonthYear]/log_[DATE_TIME].txt

Examples:
  - Downloads/DownloadOrganizerLogs/May2026/log_2026-05-07_17-59-15.txt
  - Downloads/DownloadOrganizerLogs/June2026/log_2026-06-03_10-15-22.txt

These logs contain information about:
- Files that were successfully moved
- Files that failed to move (with error reasons)
- Folders that were moved
- Creation of new category/subcategory folders
- Files already in correct location (detected on re-runs)

You can use these logs to troubleshoot issues or verify what the program did.

================================================================================
FILE ORGANIZATION STRUCTURE:
================================================================================

After running the organizer, your Downloads folder will look like:

Downloads/
├── Documents/
│   ├── WordFiles/          (contains .docx, .doc files)
│   ├── PDFs/               (contains .pdf files)
│   ├── TextFiles/          (contains .txt, .rtf files)
│   └── DataFiles/          (contains .json, .xml files)
├── Excel/
│   ├── Spreadsheets/       (contains .xlsx, .xls files)
│   └── CSVFiles/           (contains .csv files)
├── Images/
│   ├── Photos/             (contains .jpg, .jpeg, .png, .svg files)
│   ├── GIFs/               (contains .gif files)
│   └── Paint/              (contains .paint files)
├── Archives/
│   ├── ZipFiles/           (contains .zip files)
│   ├── RarFiles/           (contains .rar files)
│   └── SevenZip/           (contains .7z files)
├── Executables/
│   └── Installers/         (contains .exe, .msi files)
├── Programming/
│   ├── Python/             (contains .py files)
│   ├── C#/                 (contains .cs files)
│   ├── Java/               (contains .java, .class files)
│   ├── C and C++/          (contains .cpp, .c, .h, .cxx files)
│   ├── Ruby/               (contains .rb files)
│   ├── Swift/              (contains .swift files)
│   ├── Go/                 (contains .go files)
│   ├── Rust/               (contains .rs files)
│   └── PHP/                (contains .php, .phtml files)
├── Web Dev and Markup/
│   ├── Javascript/         (contains .js, .mjs files)
│   ├── HTML/               (contains .html files)
│   ├── CSS/                (contains .css files)
│   ├── JSON/               (contains .json, .jsonId files)
│   ├── XML/                (contains .xml files)
│   ├── Markdown/           (contains .md files)
│   └── Sass/               (contains .scss, .sass files)
├── ScriptsAndConfig/
│   ├── Shell/              (contains .sh files)
│   ├── Windows Batch file/ (contains .bat, .cmd files)
│   ├── Database/           (contains .sql files)
│   ├── Initialization Config/ (contains .ini files)
│   └── YAML Config/        (contains .yaml, .yml files)
├── Media/
│   ├── Audio/              (contains .mp3, .wav files)
│   └── Video/              (contains .mp4, .avi, .mov files)
├── Other/                  (contains files with unknown extensions)
├── Folders/                (contains any subdirectories from Downloads)
└── DownloadOrganizerLogs/  (contains organization logs)
    ├── May2026/
    ├── June2026/
    └── [MonthYear]/

================================================================================
COMMON ISSUES:
================================================================================

Q: A file says it failed to move. Why?
A: Check the log file in Downloads/DownloadOrganizerLogs/. Common reasons include:
   - File is currently open in another program
   - File is locked by Windows or another process
   - Permission issues
   
Solution: Close the file or program using it and run the organizer again.

Q: I ran it twice and it shows files moved again. Why?
A: In v2.0, the program now detects when files are already in the correct 
   location and skips them. Check the log for "already in correct location" 
   messages. The file count should be 0 on subsequent runs if nothing changed.

Q: Can I undo the organization?
A: The program doesn't have an undo feature, but all files are simply moved 
   to organized folders - nothing is deleted. You can manually move files back 
   if needed.

Q: Will this delete my files?
A: No. The program only moves files to different folders. No files are deleted.
   See the LICENSE file for liability information.

Q: Can I customize the file categories?
A: Currently, the categories are built into the program. To customize them, 
   you would need to modify the source code available on GitHub.

Q: How do I know what the program did?
A: Check the log file in Downloads/DownloadOrganizerLogs/[MonthYear]/
   Each run creates a new log with a timestamp.

================================================================================
SYSTEM REQUIREMENTS:
================================================================================

- Windows 7, 8, 10, or 11
- Approximately 50-100 MB of disk space for the application
- Read/write access to your Downloads folder

================================================================================
CHANGELOG:
================================================================================

v2.0 (May 7, 2026):
  - Added two-level folder organization (Category/Subcategory)
  - Expanded file type support from ~20 to 40+ types
  - Added Programming category (Python, C#, Java, C/C++, Ruby, Swift, Go, Rust, PHP)
  - Added Web Dev and Markup category (JS, HTML, CSS, JSON, XML, Markdown, Sass)
  - Added ScriptsAndConfig category (Shell, Batch, SQL, YAML, INI)
  - Added Media category (Audio, Video)
  - Reorganized logs into month/year subfolders
  - Added recursive directory searching for misplaced files
  - Added detection for files already in correct location
  - Improved accuracy of success/failure counters
  - Enhanced error messages with specific failure reasons
  - Renamed logs folder to "DownloadOrganizerLogs"

v1.0 (May 7, 2026):
  - Initial release
  - Single-level file categorization
  - Support for ~20 file types
  - Basic logging functionality

================================================================================
SUPPORT:
================================================================================

This is a free, open-source project. For issues, suggestions, or to view 
the source code, visit the GitHub repository.

================================================================================
VERSION:
================================================================================

Version: 2.0
Last Updated: May 7, 2026
Python Version: 3.13
License: MIT

================================================================================