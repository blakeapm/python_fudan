# Launching Sublime Text from Git Bash on Windows

## Introduction
Learn how to configure Git Bash to open files in Sublime Text using the command `subl`. This allows for quick editing of files directly from the command line.

## Step 1: Add Sublime Text to the PATH
1. Find the installation path of Sublime Text (usually `C:\Program Files\Sublime Text 4`).
2. Add this path to your system's PATH environment variable:
    - Open the Start Search, type in "env", and select "Edit the system environment variables".
    - Click on "Environment Variables".
    - Under "System variables", find the PATH variable, select it, and click "Edit".
    - Click "New" and add the path to Sublime Text's installation directory.
    - Click "OK" to close all windows.

## Step 3: Verify PATH Configuration
1. Open Git Bash.
2. Type `subl` and press Enter.
3. Sublime Text should open. If it doesn't, verify the PATH configuration and restart your computer if necessary.

## Step 4: Create an Alias in Git Bash
1. Open Git Bash.
2. Edit the `.bashrc` file: `nano ~/.bashrc`
3. Add the following line to create an alias for Sublime Text:
    ```sh
    alias subl='"/c/Program Files/Sublime Text 3/subl.exe"'
    ```
4. Save and exit the editor (Ctrl + X, then Y, then Enter).
5. Reload the `.bashrc` file: `source ~/.bashrc`

## Step 5: Launch Sublime Text Using the Alias
1. Now you can open files in Sublime Text from Git Bash using the alias.
2. Example: `subl myfile.txt`