# How to Copy and Paste and More in Git Bash

This guide explains how to enable and use copy and paste functionality in Git Bash using shortcut keys.

## Enabling Copy and Paste

1. **Open Git Bash Options**:
   - Click the Git Bash icon in the top left corner of the window.
   - Choose "Options" from the dropdown menu.

   ![Open Git Bash Options](figures/gitbash_1.png)

2. **Modify Keyboard Options**:
   - In the Options menu, navigate to the "Keys" tab.
   - Check the option "Copy and Paste (Ctrl+Shift+Ins)" to enable it.

   ![Modify Keyboard Options](figures/gitbash_2.png)

3. **Save and Apply Changes**:
   - Click "Apply" and then "Save" to apply the changes.

## Copying and Pasting

- **To Copy**: Select the text you want to copy in Git Bash, and then use `Ctrl+Shift+Ins` to copy.
- **To Paste**: Click where you want to paste the text and press `Ctrl+Shift+Ins`.

This method allows you to efficiently copy and paste text using Git Bash, facilitating better workflow and data transfer between the terminal and other applications.

## Opening a File or Folder in Windows Explorer

In Git Bash on Windows, the `start` command in Windows can be used to open a folder with the default file manager, which is Windows Explorer.

```bash
start .
```
This will open the current directory in Windows Explorer. You can also specify a path:

```bash
start /path/to/directory
```

This offers the same functionality as `open .` or `open /path/to/directory` in Mac OS:
