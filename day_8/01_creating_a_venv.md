# Creating a Python Virtual Environment on macOS

This guide will show you how to create and manage a Python virtual environment using the Terminal on a macOS system.

## Step 1: Check Python Installation

First, confirm that Python is installed and accessible from your Terminal.

1. Open the Terminal app.
2. Check your Python version by running:
   ```bash
   python3 --version
   ```
   This should display the Python version if it's correctly installed.

## Step 2: Creating a Virtual Environment

Choose or create a directory where you want to set up your virtual environment.

1. Navigate to your project directory or where you want to create the virtual environment:
   ```bash
   cd /path/to/your/folder
   ```
2. Create a new virtual environment using the following command:
   ```bash
   python3 -m venv fudan_venv
   ```
   - `fudan_venv` is the name of the virtual environment directory. You can use any name you prefer.

## Step 3: Activating the Virtual Environment

Activate the virtual environment by running:

```bash
source fudan_venv/bin/activate
```

- You should see `(venv)` appear at the beginning of your Terminal prompt, indicating that the virtual environment is active.

## Step 4: Deactivating the Virtual Environment

When you are finished working within the virtual environment, deactivate it to return to your global Python settings:

```bash
deactivate
```

# Creating a Python Virtual Environment in Windows on Git Bash

This guide will walk you through the steps to create and manage a Python virtual environment using Git Bash on a Windows system.

## Step 1: Check Python Installation

Ensure Python is installed and correctly added to your system's PATH.

1. Open Git Bash.
2. Execute the command:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```
   This command should return the version of Python installed.

## Step 2: Creating a Virtual Environment

Choose a directory where you want to place your virtual environment.

1. Navigate to your project directory or where you want to create the virtual environment:
   ```bash
   cd /path/to/your/folder
   ```
2. Create a new virtual environment by running:
   ```bash
   python -m venv fudan_venv
   ```
   or
   ```bash
   python3 -m venv fudan_venv
   ```
   - `fudan_venv` is the name of the virtual environment folder. You can name it anything you prefer.

## Step 4: Activating the Virtual Environment

To activate the virtual environment in Git Bash, use the following command:

```bash
source fudan_venv/Scripts/activate
```

- Your command prompt should now reflect the activated environment, showing something like `(fudan_venv)` before the prompt.

## Step 4: Deactivating the Virtual Environment

When you are done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```