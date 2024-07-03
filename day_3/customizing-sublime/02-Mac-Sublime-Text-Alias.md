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