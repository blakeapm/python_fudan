# Launching Sublime Text from Terminal on Mac

## Step 1: Check Your Shell Version in Terminal

Open your terminal and type the following command:
```sh
echo $SHELL
```
This command displays the path of the shell executable, indicating which shell you are using in Terminal:
- `/bin/zsh` for zsh
- `/bin/bash` for bash

## Step 2: Create a Symlink for Sublime Text

Run this command in your Terminal:
```sh
sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
```
Enter your password when prompted.

## Step 3: Edit the Shell Configuration File

Open your shell configuration file based on your shell type from Step 1:

For zsh users:
```sh
open ~/.zshrc
```

For bash users:
```sh
open ~/.bash_profile
```

If the file does not exist, create it and open it again:

For zsh:
```sh
touch ~/.zshrc
open ~/.zshrc
```

For bash:
```sh
touch ~/.bash_profile
open ~/.bash_profile
```

## Step 4: Add Sublime Text Alias and Path

In your shell configuration file, add:
```sh
alias subl="open -a /Applications/Sublime\ Text.app"
export PATH="/usr/local/bin:$PATH"
```
Save the file and close the editor.

## Step 5: Reload the Configuration File

Apply the changes by sourcing your configuration file:

For zsh:
```sh
source ~/.zshrc
```

For bash:
```sh
source ~/.bash_profile
```

## Step 6: Test Sublime Text Command

You should now be able to open folders or files in Sublime Text using the `subl` command:
```sh
subl .
subl new_file.txt
```

# Launching Sublime Text from Git Bash on Windows

## Introduction
Learn how to configure Git Bash to open files in Sublime Text using the command `subl`. This allows for quick editing of files directly from the command line.

## Step 1: Add Sublime Text to the PATH
1. Find the installation path of Sublime Text (usually `C:\Program Files\Sublime Text 4`).
2. Add this path to your system's PATH environment variable:
    - Open the Start Search, type in "env", and select "Edit the system environment variables".
    - Click on "Environment Variables".
    - Under "System variables", find the PATH variable, select it, and click "Edit".
    - Click "New" and add the path to Sublime Text's installation directory from step 1.
    - Click "OK" to close all windows.

## Step 2: Verify PATH Configuration
1. Open Git Bash.
2. Type `subl` and press Enter.
3. Sublime Text should open.

## Step 3: Launch Sublime Text Using the Alias
1. Now you can open files in Sublime Text from Git Bash using the alias.
2. Example: `subl myfile.txt`
