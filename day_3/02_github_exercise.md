### Git Collaboration Exercise (update)

#### Step 1: Clone the Repository
1. **Clone the repository** to your local machine. This action downloads the repository, allowing you to work on it locally.
   ```bash
   git clone git@github.com:blakeapm/github_example.git
   ```
2. **Navigate into the repository directory** on your machine.
   ```bash
   cd github_example
   ```

#### Step 2: Translate Your Assigned Stanza
1. **Open your assigned file** (e.g., `i_rise_1.txt` for stanza 1-2, `i_rise_3.txt` for stanza 3-4, etc.) and translate the stanza. It doesn't have to be perfect! Make sure to save your changes.

#### Step 3: Commit Changes Locally
1. **Stage your changes** for committing. This action prepares your changes for a commit.
   ```bash
   git add filename  # Replace filename with your assigned file, e.g., i_rise_1.txt
   ```
2. **Commit** your changes locally with a descriptive message. This command records your changes in your local repository.
   ```bash
   git commit -m "Add Chinese translation for stanzas 1-2"
   ```

#### Step 4: Push Changes to GitHub
1. **Push** your local commits to the main branch on GitHub. This action uploads your changes to the remote repository.
   ```bash
   git push origin main
   ```

#### Step 5: Verify Changes on GitHub
1. **Open your web browser** and go to the GitHub repository page (e.g., `https://github.com/blakeapm/github_example`).
2. **Navigate to your assigned file** within the repository to see your changes reflected there.
3. **Review the commit history** by clicking on "Commits" near the top of the repository page to see a log of all the changes that have been made.

#### Step 6: Pull Changes from GitHub
1. **Pull** the latest changes from the main branch. This step is especially useful if multiple people are working on the project and you want to make sure your local repository is up to date.
   ```bash
   git pull origin main
   ```
   If you run into an error, run:
   ```bash
   git pull --rebase origin main
   ```

#### Step 7: View Changes Locally
1. **Check the status** of your local repository to see which files have changed.
   ```bash
   git status
   ```
2. **View the commit history** locally to see the changes made over time.
   ```bash
   git log
   ```
