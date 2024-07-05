# Python 3 Installation Guide

This course is taught in Python, using Python 3. You will need to have Python 3 installed on your computer and bring it to class each session. Here are the detailed instructions for installing Python 3 on your machine.

## For Windows Users

1. **Install Sublime Text**: Download and install Sublime Text from the [official Sublime Text website](https://www.sublimetext.com).
2. **Install Git Bash**: Download and install Git Bash to use Git and Unix-style command-line tools from [Git for Windows](https://gitforwindows.org).
3. **Uninstall Python 3** if you installed it already
4. **Install Python 3**:
   - Visit the [Python Downloads page for Windows](https://www.python.org/downloads/windows/).
   - Click on "Latest Python 3 Release".
   - Click "Download Windows installer (64-bit)
   - Run Executable Installer.
      1. The first installation window shows two checkboxes. Make sure both are checked:
          - "Use admin privileges when installing py.exe"
          - "Add python.exe to PATH"
      ![](figures/python_1_.png)
      2. Click custom installation. Check all boxes. Press Continue.
      ![](figures/python_2_.png)
      3. Make sure all these boxes are selected:
      ![](figures/python_3_.png)
          - "Install Python 3.12 for all users"
          - "Associate files with Python (requires the 'py' launcher)"
          - "Create shortcuts for installed applications"
          - "Add Python to environment variables"
          - "Precompile standard library"
      4. Click Install.
      5. Click disable path length limit.
      ![](figures/python_3_.png)
      6. Click CLose
5. **Verify Python Installation**:
   - Open Git Bash.
   - Type `python --version` to check if Python 3 is accessible. If this command doesn't work, try `python3 --version`.
6. **If Git Bash does not recognize Python:** we need to edit our PATH file to ensure that it does.

   1. **打开控制面板 (Open Control Panel)**
      - Press `Win + S` to open the search bar.
      - Type `控制面板` and press Enter to open Control Panel.

   2. **系统和安全 (System and Security)**
      - Click on `系统和安全` (System and Security). In some views, you might need to click `系统` (System) directly.

   3. **系统 (System)**
      - Click on `系统` (System) which might appear under System and Security, depending on your view settings.

   4. **高级系统设置 (Advanced system settings)**
      - On the left sidebar, you'll find `高级系统设置` (Advanced system settings). Click on it.
   5. **环境变量 (Environment Variables)**
      - In the System Properties window that opens, go to the `高级` (Advanced) tab.
      ![](figures/path_1_.png)
      - Click on the `环境变量` (Environment Variables) button near the bottom of the tab.
      ![](figures/path_2_.png)
   6. Double click on `Path` and click `新建` (New). Paste the path to your `python.exe` file. It should be somewhere like `C:\Program Files\Python312\python.exe`. Move the position of the path to the top with `上移` (Up). Click `确定` (Confirm).
      ![](figures/path_3_.png)
7. Close Git Bash and reopen it. Type `python --version` to check if Python 3 is accessible. If this command doesn't work, try `python3 --version`.

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
