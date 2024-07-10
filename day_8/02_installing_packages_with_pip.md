# Installing Python Packages with pip

This guide provides instructions on how to install Python packages using `pip`, the Python package installer, in Git Bash on Windows and the Terminal on macOS.

## Installing Packages with pip

`pip` is a powerful tool that helps you install and manage Python packages. It connects to the Python Package Index (PyPI), downloads the package, and installs it on your system.

### Check pip Version

To confirm that `pip` is installed and check its version, run the following command in your terminal:

```bash
pip --version
```

If `pip` is not installed, or you need to upgrade, you can install or upgrade `pip` by downloading `get-pip.py` from the official site and running it.

### Installing a Package

To install a package using `pip`, use the following command:

```bash
pip install package_name
```

Replace `package_name` with the name of the package you want to install.

### Example: Installing the Requests Library

```bash
pip install requests
```

This command will download and install the `requests` library and its dependencies.

## Upgrading Packages

To upgrade an existing package to the latest version, use the following command:

```bash
pip install --upgrade package_name
```

## Uninstalling Packages

To remove a package installed with pip, use the command:

```bash
pip uninstall package_name
```

## List Installed Packages

To see a list of all installed packages:

```bash
pip list
```