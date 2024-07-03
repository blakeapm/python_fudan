# SendCode Setup Instructions for Sublime Text

Follow these steps to install and configure the SendCode package in Sublime Text, allowing you to send code directly to Terminal or Git-Bash using CTRL (Command on macOS) + Enter.

## Step 1: Install Package Control

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette.
3. Type "Install Package Control" and press enter.

## Step 2: Install SendCode

1. Open the command palette again with `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
2. Type "Install Package" and select "Package Control: Install Package".
3. Search for "SendCode" and install it.

## Step 3: Configure SendCode

1. After installation, navigate to the `SendCode` preferences. For Mac:
	- `Sublime Text` -> `Settings` -> `Package Settings` -> `SendCode` -> `Settings`.
2. In the code on the left, find `python` and edit the string after `"prog": ` to `terminal` for Mac and `git-bash` for Windows

## Step 4: Usage

- Place your cursor on the line or select the block of code you want to execute.
- Press `Ctrl+Enter` (or `Cmd+Enter` on macOS) to send the code to the configured terminal.