# Launching Sublime Text from Terminal on Mac

## Step 1: Create a Symlink for Sublime Text

Open your Terminal app and run the following command to create a symlink for Sublime Text:

```sh
sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
```

Enter your password when prompted.

## Step 2: Check if `.bash_profile` Exists

Check if the `.bash_profile` file exists:

```sh
open ~/.bash_profile
```

If you see an error indicating that the file does not exist, create it using the following command:

```sh
touch ~/.bash_profile
open ~/.bash_profile
```

## Step 3: Edit the `.bash_profile`

Add the following lines to the `.bash_profile` file:

```sh
alias subl="open -a /Applications/Sublime\ Text.app"
export PATH=/usr/local/bin:$PATH
```

Save the file and close the editor.

## Step 4: Reload the `.bash_profile`

Reload your `.bash_profile` to apply the changes:

```sh
source ~/.bash_profile
```

## Step 5: Test Sublime Text Command

Now, you should be able to open folders or files in Sublime Text using the `subl` command. For example:

```sh
subl .
subl ~/.bash_profile
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

## Step 3: Verify PATH Configuration
1. Open Git Bash.
2. Type `subl` and press Enter.
3. Sublime Text should open.

## Step 5: Launch Sublime Text Using the Alias
1. Now you can open files in Sublime Text from Git Bash using the alias.
2. Example: `subl myfile.txt`
