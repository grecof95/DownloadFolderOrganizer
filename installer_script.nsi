; Download Folder Organizer v2.0 Installer
!include "MUI2.nsh"

Name "Download Folder Organizer"
OutFile "DownloadFolderOrganizer_Installer.exe"
InstallDir "$PROGRAMFILES\DownloadFolderOrganizer"
RequestExecutionLevel admin

; Variables
Var CreateDesktopShortcut

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY

; Custom page for options
Page custom nsDialogsPage nsDialogsPageLeave

!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

;--------------------------------
; Custom Dialog Page for Options
;--------------------------------

Function nsDialogsPage
  nsDialogs::Create 1018
  Pop $0
  
  ${If} $0 == error
    Abort
  ${EndIf}
  
  ; Title
  ${NSD_CreateLabel} 0 0 100% 20u "Installation Options"
  Pop $0
  SendMessage $0 ${WM_SETFONT} -1 0
  
  ; Checkbox for desktop shortcut
  ${NSD_CreateCheckbox} 0 30u 100% 12u "Create shortcut on Desktop"
  Pop $CreateDesktopShortcut
  ${NSD_Check} $CreateDesktopShortcut
  
  ; Description text
  ${NSD_CreateLabel} 20u 50u 90% 40u "If checked, a shortcut to Download Folder Organizer will be placed on your desktop for quick access."
  Pop $0
  
  nsDialogs::Show
FunctionEnd

Function nsDialogsPageLeave
  ; Check if checkbox is selected
  ${NSD_GetState} $CreateDesktopShortcut $CreateDesktopShortcut
FunctionEnd

;--------------------------------
; Installer sections
;--------------------------------

Section "Install"

  SetOutPath "$INSTDIR"
  
  ; Copy application files
  File "DownloadFolderOrganizer.exe"
  File "README.txt"
  File "LICENSE.txt"
  
  ; Create start menu shortcuts
  CreateDirectory "$SMPROGRAMS\DownloadFolderOrganizer"
  CreateShortcut "$SMPROGRAMS\DownloadFolderOrganizer\Download Folder Organizer.lnk" "$INSTDIR\DownloadFolderOrganizer.exe"
  CreateShortcut "$SMPROGRAMS\DownloadFolderOrganizer\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
  
  ; Create desktop shortcut only if checkbox is checked
  ${If} $CreateDesktopShortcut == 1
    CreateShortcut "$DESKTOP\Download Folder Organizer.lnk" "$INSTDIR\DownloadFolderOrganizer.exe"
  ${EndIf}
  
  ; Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  
  ; Registry entries for Add/Remove Programs
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer" "DisplayName" "Download Folder Organizer v2.0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer" "UninstallString" "$INSTDIR\Uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer" "DisplayIcon" "$INSTDIR\DownloadFolderOrganizer.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer" "DisplayVersion" "2.0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer" "Publisher" "Frank Greco"
  
SectionEnd

;--------------------------------
; Uninstaller section
;--------------------------------

Section "Uninstall"

  ; Remove files
  Delete "$INSTDIR\DownloadFolderOrganizer.exe"
  Delete "$INSTDIR\README.txt"
  Delete "$INSTDIR\LICENSE.txt"
  Delete "$INSTDIR\Uninstall.exe"
  
  ; Remove directories
  RMDir "$INSTDIR"
  
  ; Remove start menu shortcuts
  Delete "$SMPROGRAMS\DownloadFolderOrganizer\Download Folder Organizer.lnk"
  Delete "$SMPROGRAMS\DownloadFolderOrganizer\Uninstall.lnk"
  RMDir "$SMPROGRAMS\DownloadFolderOrganizer"
  
  ; Remove desktop shortcut if it exists
  Delete "$DESKTOP\Download Folder Organizer.lnk"
  
  ; Remove registry entries
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DownloadFolderOrganizer"
  
SectionEnd