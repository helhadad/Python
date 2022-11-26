<#
Author  : Hesham Elhadad 
ID      : L00177542
Purpose : This script demonstrates a solution of assignment 1 
          Where a script is required to create an application folder structure
Date    : 04-Nov-2022 
Rev     : 0
#>

Clear-Host
# Get the working directory
$Current_Dir = Get-Location
Write-Host "`nCurrent Direcorty is $Current_Dir"
# Preparing the user message
$Header_Message = "`nThis Script will create the following folders under the current dirctory if they do not exist:
                    ---------------------------------------------------------------------------------------------
                                                - Documentation
                                                - Input
                                                - Output
                                                - Lib
                                                - Logs
                                                - Tests
                    ---------------------------------------------------------------------------------------------
                    Please press any <key> to continue or <Esc> to cancel        "

Write-host $Header_Message
Write-host ""
                    

# Reading a key from keyboard by the user
$key = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown').VirtualKeyCode

# Check if the Key is the 'Esc' Key which is equal to 27.
# If the 'Esc' key was pressed, the script will exit with a message.
if ($key -eq 27){
    Write-Host "`nScript was canceled by the user" -ForegroundColor DarkBlue -BackgroundColor Yellow
    Write-Host ""
    Exit
}

# Adding all project folders in a collection so future folders can be added smoothly if required.
$Project_Folders = "Documentation", "Output","Input","Lib","Tests","Logs"
#Test if folder is exists before creating
foreach ($Folder in $Project_Folders) {
 
    $Folder_Path = Join-Path -Path $Current_Dir -ChildPath $Folder
#   Check if folders already exist or not, and creare them if do not exist 
    if (!(Test-Path -Path $Folder_Path)){
        # The following 3 Write-Host cdmlet will output to the same line due to '-NoNewLine' flag, this is done to isolate coloured words
        Write-Host "Folder " -NoNewline
        Write-Host "$Folder" -NoNewline -ForegroundColor Yellow -BackgroundColor Red 
        Write-Host " not exist and will be created"
        # mkdir will creat the folder if does not exist
        mkdir $Folder_Path
    }
    else{
        # Reporting to the user what was created and what was already exist
        # The following 3 Write-Host cdmlet will output to the same line due to '-NoNewLine' flag, this is done to isolate coloured words
        Write-Host "Folder " -NoNewline
        Write-Host "$Folder" -NoNewline -ForegroundColor Blue -BackgroundColor Green
        Write-Host " already exists"
    }
}
