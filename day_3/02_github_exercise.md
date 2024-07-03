#### Step 1: Clone the Repository

1. **Clone the repository** to your local machine. This will download the repository, allowing you to work on it locally.
   ```bash
   git clone git@github.com:blakeapm/github_example.git
   ```

2. **Navigate into the repository directory** on your machine.
   ```bash
   cd github_example
   ```

3. **Translate** your assigned stanza in the `i_rise.txt` file. It doesn't have to be perfect! Make sure to save your changes.

#### Step 2: Commit Changes Locally

1. **Stage your changes** for committing. This prepares your changes for a commit.
   ```bash
   git add i_rise.txt
   ```

2. **Commit** your changes locally with a descriptive message. This records your changes in your local repository.
   ```bash
   git commit -m "Add Chinese translation for stanza <number>"
   ```

#### Step 3: Push Changes to GitHub

1. **Push** your local commits to the main branch on GitHub. This uploads your changes to the remote repository.
   ```bash
   git push origin main
   ```

#### Step 4: Verify Changes on GitHub

1. **Open your web browser** and go to the GitHub repository page: `https://github.com/blakeapm/github_example`
2. **Navigate to the `i_rise.txt` file** within the repository to see your changes reflected there.
3. **Review the commit history** by clicking on "Commits" near the top of the repository page to see a log of all the changes that have been made.

#### Step 5: Pull Changes from GitHub

1. **Pull** the latest changes from the main branch. This is especially useful if multiple people are working on the project and you want to make sure your local repository is up to date.
   ```bash
   git pull origin main
   ```

#### Step 6: View Changes Locally

1. **Check the status** of your local repository to see which files have changed.
   ```bash
   git status
   ```

2. **View the commit history** locally to see the changes made over time.
   ```bash
   git log
   ```