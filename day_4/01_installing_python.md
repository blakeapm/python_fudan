# Python 3 Installation Guide

This course is taught in Python, using Python 3. You will need to have Python 3 installed on your computer and bring it to class each session. Here are the detailed instructions for installing Python 3 on your machine.

## For Windows Users

1. **Install Sublime Text**: Download and install Sublime Text from the [official Sublime Text website](https://www.sublimetext.com).
2. **Uninstall Git Bash** if you have installed it already
3. **Install Git Bash**: Download and install Git Bash to use Git and Unix-style command-line tools from [Git for Windows](https://gitforwindows.org).
4. **Uninstall Python 3** if you installed it already
5. **Install Python 3**:
   - Visit the [Python Downloads page for Windows](https://www.python.org/downloads/windows/).
   - Click on "Latest Python 3 Release".
   - Scroll down to click the link to download the file. Choose either the Windows 32-bit or 64-bit installer.
   - Download and install the executable file for Windows.
   - Run Executable Installer.
      1. The first installation window shows two checkboxes. Make sure both are checked:
          - "Use admin privileges when installing py.exe"
          - "Add python.exe to PATH"
      2. Click custom installation. Check all boxes. Press Continue.
      3. Make sure all these boxes are selected:
          - "Install Python 3.12 for all users"
          - "Associate files with Python (requires the 'py' launcher)"
          - "Create shortcuts for installed applications"
          - "Add Python to environment variables"
          - "Precompile standard library"
      4. Click Install.
      5. Click disable path length limit.
      6. Click CLose
4. **Verify Python Installation**:
   - Open Git Bash.
   - Type `python --version` to check if Python 3 is accessible. If this command doesn't work, try `python3 --version`.

## For Mac Users

1. **Open Terminal**:
   - Navigate to Applications → Utilities → Terminal.
2. **Install Xcode Command Line Tools**:
   - Run `xcode-select --install` in Terminal.
3. **Install Homebrew**:
   - Paste the installation command from the [Homebrew website](https://brew.sh) into Terminal.
   - Follow `Next steps` in the brew installation output. Depending on your Mac OS version, it will be different, but it should look like (**MAKE SURE TO CHANGE your-username to your actual username**):
        - `(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/your-username/.zprofile`
        - `eval "$(/opt/homebrew/bin/brew shellenv)"`
   - Alternatively, download the Homebrew installer [here](https://github.com/Homebrew/brew/releases/tag/4.3.6).
4. **Install Sublime Text**:
   - Download and install Sublime Text from the [official Sublime Text website](https://www.sublimetext.com).
   - Follow the installation instructions.
5. **Install Python 3 Using Homebrew**:
   - In Terminal, run `brew install python`.
6. **Verify Python Installation**:
   - In Terminal, run `python3 --version` to ensure Python 3 is accessible. Make sure you see the folder `homebrew` in the outputted path. If not, come see me.

## Additional Resources

- The [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) is an excellent resource to get started with Python.
- If you encounter any issues, the [Python Docs](https://docs.python.org/3/) provide comprehensive documentation and troubleshooting tips.
