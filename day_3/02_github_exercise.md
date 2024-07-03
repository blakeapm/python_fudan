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

#### Step 3: Pull Changes from GitHub

1. **Pull** edits from other students that are in the main branch on GitHub. This ensures all changes from the remote repository are on your local machine.
   ```bash
   git pull origin main
   ```

#### Step 4: Push Changes to GitHub

1. **Push** your local commits to the main branch on GitHub. This uploads your changes to the remote repository.
   ```bash
   git push origin main
   ```

If you see an error that looks like the example below, this is because you do not have changes that other students have made in your local repo since you last pulled (in step 3). Repeat step 3 and try again!

Error example:

```
To github.com:blakeapm/github_example.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:blakeapm/github_example.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

#### Step 5: Verify Changes on GitHub

1. **Open your web browser** and go to the GitHub repository page: `https://github.com/blakeapm/github_example`
2. **Navigate to the `i_rise.txt` file** within the repository to see your changes reflected there.
3. **Review the commit history** by clicking on "Commits" near the top of the repository page to see a log of all the changes that have been made.

#### Step 6: Pull Changes from GitHub

1. **Pull** the latest changes from the main branch. This is especially useful if multiple people are working on the project and you want to make sure your local repository is up to date.
   ```bash
   git pull origin main
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