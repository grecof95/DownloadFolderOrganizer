================================================================================
DOWNLOAD FOLDER ORGANIZER v3.0
================================================================================

DESCRIPTION:
Download Folder Organizer is a Python application that automatically organizes 
files in your Downloads folder by file type into a two-level folder structure. 
It creates category folders (Documents, Images, Excel, Archives, Code, etc.) 
and then further organizes files into subcategories (WordFiles, PDFs, Photos, 
etc.) for even better organization.

Any folders that are not recognized system folders are moved to a "Folders" 
subfolder for safekeeping.

NEW IN v3.0: Intuitive GUI with menu-driven interface, powerful undo 
functionality, and streamlined installer with desktop shortcut option.

================================================================================
WHAT'S NEW IN v3.0:
================================================================================

 Lightweight GUI Interface:
   - User-friendly graphical interface replaces command-line interaction
   - Simple, intuitive design for easy navigation
   - Progress window shows real-time organization status
   - Summary window displays detailed results after completion

 Main Menu with Feature Selection:
   - Clean button-based menu to choose between operations
   - Organize: Run the file organization process
   - Undo: Reverse a previous organization using saved logs
   - Easy to switch between features without restarting

 Powerful Undo Feature:
   - Reverse any previous organization operation
   - Browse through your organization history in File Explorer
   - Select the specific log file corresponding to the organization you want to undo
   - Automatically restores files to their original locations
   - Complete audit trail of all undo operations in logs

 Professional Installer:
   - Traditional .exe installer with setup wizard
   - Simple step-by-step installation process
   - Option to create desktop shortcut during installation
   - Automatic program registration and configuration
   - Includes uninstaller for clean removal

================================================================================
FEATURES (COMPLETE LIST):
================================================================================

- Two-level file categorization (Main Category / Subcategory)
- Lightweight GUI with main menu interface
- Organize feature: Recursively searches and organizes files in all subdirectories
- Undo feature: Reverses previous organization operations from saved logs
- Detects and corrects misplaced files
- Creates detailed logs organized by month and year
- User-friendly progress window during organization
- Summary window with detailed operation results
- Detailed error messages for troubleshooting
- Accurate success/failure counters
- Support for 40+ file types across 9 main categories
- Professional installer with optional desktop shortcut
- Complete audit trail of all operations

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

- Windows 7, 8, 10, or 11
- Approximately 30-60 MB of disk space for the application
- Read/write access to your Downloads folder

================================================================================
INSTALLATION & USAGE:
================================================================================

INSTALLATION:

1. Download the DownloadFolderOrganizer_Installer.exe file
2. Double-click the installer to launch the setup wizard
3. Follow the on-screen installation instructions
4. Choose installation location (default: Program Files)
5. (Optional) Select "Create Desktop Shortcut" during installation
6. Click "Install" to complete the installation
7. Launch the application from the Start Menu or desktop shortcut

USING THE APPLICATION:

1. Launch Download Folder Organizer from the Start Menu or desktop shortcut
2. The Main Menu window will appear with two options:
   - Organize: Automatically organize your Downloads folder
   - Undo: Reverse a previous organization operation
3. Click the desired button to proceed

ORGANIZE FEATURE:

1. Click "Organize" from the Main Menu
2. A progress window will appear showing the organization is in progress
3. Once complete, a summary window will display:
   - Number of files successfully moved
   - Number of files that failed to move (with error reasons)
   - Number of folders moved to the Folders directory
   - Number of new category/subcategory folders created
   - Number of files already in correct location
4. Review your Downloads folder to see the organized files

UNDO FEATURE:

1. Click "Undo" from the Main Menu
2. File Explorer will open to Downloads/DownloadOrganizerLogs/
3. Navigate to the month/year folder containing the organization you want to undo
4. Select the log file (format: log_YYYY-MM-DD_HH-MM-SS.txt) corresponding to 
   the organization you want to reverse
5. The application will process the undo operation
6. A summary window will display the undo results
7. All files from that organization will be restored to their original locations

Note: The undo feature uses the detailed information saved in each log file to 
precisely reverse file movements. It does not affect files moved by other 
organizations.

================================================================================
LOGS:
================================================================================

Each time you run the program (either Organize or Undo), a detailed log is 
created in:
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
- Undo operations and their results

You can use these logs to:
- Troubleshoot issues or verify what the program did
- Select a specific organization to undo
- Maintain an audit trail of all file operations
- Keep a record of your Downloads folder management history

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
└── DownloadOrganizerLogs/  (contains organization and undo logs)
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

Q: How do I undo an organization?
A: Click "Undo" from the Main Menu, navigate to the appropriate log file in 
   File Explorer, and select the log corresponding to the organization you want 
   to reverse. The application will automatically restore all files to their 
   original locations.

Q: Can I undo multiple organization operations?
A: Yes. Each organization is tracked separately in its own log file. You can 
   undo any specific organization by selecting its log file. However, if you 
   undo an old organization after performing newer ones, some files may have 
   moved again, which could cause conflicts.

Q: I ran it twice and it shows files moved again. Why?
A: In v2.0+, the program detects when files are already in the correct location 
   and skips them. Check the log for "already in correct location" messages. 
   The file count should be 0 on subsequent runs if nothing changed.

Q: Will undoing an organization delete my files?
A: No. The undo feature only moves files back to their original locations. 
   No files are deleted. See the LICENSE file for liability information.

Q: Will this delete my files?
A: No. The program only moves files to different folders. No files are deleted.
   See the LICENSE file for liability information.

Q: Can I customize the file categories?
A: Currently, the categories are built into the program. To customize them, 
   you would need to modify the source code available on GitHub.

Q: How do I know what the program did?
A: Check the log file in Downloads/DownloadOrganizerLogs/[MonthYear]/
   Each run creates a new log with a timestamp. Both organize and undo operations 
   are logged for your reference.

Q: How do I uninstall the program?
A: Use Windows Add/Remove Programs:
   1. Open Settings > Apps > Apps & Features
   2. Find "Download Folder Organizer" in the list
   3. Click it and select "Uninstall"
   4. Follow the uninstall wizard to complete removal

================================================================================
SYSTEM REQUIREMENTS:
================================================================================

- Windows 7, 8, 10, 11, or 12
- Approximately 50-100 MB of disk space for the application
- Read/write access to your Downloads folder
- Administrator privileges may be required for installation

================================================================================
CHANGELOG:
================================================================================

v3.0 (May 8, 2026):
  - Added lightweight GUI interface with main menu
  - Implemented button-based feature selection (Organize/Undo)
  - Added powerful Undo feature to reverse previous organizations
  - Undo feature uses log files to restore original file locations
  - Added professional .exe installer with setup wizard
  - Added option to create desktop shortcut during installation
  - Improved user experience with visual progress and summary windows
  - All previous v2.0 features maintained and working

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

Report bugs or request features through the project's issue tracker.

================================================================================
VERSION:
================================================================================

Version: 3.0
Last Updated: May 8, 2026
Python Version: 3.13
License: MIT

================================================================================