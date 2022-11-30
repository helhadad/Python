<#
Script  : Add_To_Git.ps1
Author  : Hesham Elhadad
ID      : L00177542
Date    : 29-Nov-22
Purpose : This script adds all files to the Python Repo and Push them to GIT
Rev     : 0
#>
#Clear the Powershell Command Prompt
Clear-Host
git status
Write-Host "*********************************************************"
Write-Host" Performing an add for all files in tis directoy"
git add .
git status
Write-Host "*********************************************************"
$CommitMessage = Read-Host "Please enter your commit message"
git commit -m "$CommitMessage"
git status
Write-Host "*********************************************************"
Write-Host" Pushing to GitHub repository"
git push -u origin main
Write-Host "*********************************************************"
Write-Host "********************      D O N E      ******************"