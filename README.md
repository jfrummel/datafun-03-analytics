# datafun-03-analytics
Create a New Project with a Local Project Virtual Environment

1. Project Creation in GitHub

Steps to Create a New Repository in GitHub
Log in to GitHub. Open your browser and log in to your GitHub account.

Go to the "Create Repository" Page

In the top-right corner of GitHub, click the + dropdown menu.
Select New repository.
Name Your Repository

Enter a name for your new repository.
Naming Guidelines for Python Projects:
Use all lowercase.
Use dashes between words.
Avoid spaces or special characters.
Example: my-python-project
Provide a brief description of your project. This is optional but recommended.

Select the Public option so others can view your repository.

Add a Default README File

Check the box for Add a README file.
This file is essential for cloning and initializing your project.
Create the Repository

Click the Create repository button to finalize the process.
Important
If you forget to add a README file, delete the repository and start over with a default README.
The following steps will NOT work the same if the new repository does not have a file in the repo already.

2. Clone Repo to local machine



Run the following command from the project root directory. Type git clone and paste your URL. The following is only an example. The command works in PowerShell, bash, zsh, Git Bash, and more.

git clone https://github.com/youraccount/yourrepo

3. add-gitignore-and-requirements.md


.gitignore is used to keep things out of GitHub like .venv and secrets
requirements.txt is a good way to list and install external dependencies
Before Starting
Open your project repository in VS Code.

Create a new file in your root project folder named exactly: .gitignore If the name or location is not exact, it will not work.

Create requirements.txt
Create a new file in your root project folder named exactly: requirements.txt. If the name or location is not exact, it will not work.


Experience
Read and understand the purpose of these files. Know how and why we vary the contents. Experience comes from working with these files and understanding how to manage them for a project.

4. git-add-commit-push.md
This page provides instructions to add files to version control, commit changes, and push them to your remote repository.

git add - stages changes, adds files to source control
git commit - creates a labeled snapshot of staged changes.
git push - updates the remote repository
Before Starting
Ensure your project repository is open in VS Code, and you have made changes (e.g. created the .gitignore and requirements.txt files).

Task 1. Git add-commit-push
Using a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT: Replace the commit message with a clear and descriptive note about what you added or changed. Wrap the commit message in double quotes.

git add .
git commit -m "Add .gitignore and requirements.txt files"
git push -u origin main
After subsequent changes, you may be able to use a simpler version of the last command:

git push
Experience
Experience comes from executing these commands frequently after making useful changes to a project.

5.  create-virtual-environment.md
This page provides instructions to create a place in your project repository folder that will hold the Python virtual environment for the project. It provides an isolated Python environment for the project, so we don't mess up the global Python used by our machine.

This is typically just done once at the beginning of a project. If it gets messed up, we can delete .venv and recreate it at any time.

Before Starting
Open your project repository in VS Code.

We'll open a new terminal in VS Code and run a single command to create a new .venv folder for the local project virtual environment.

Windows Users - Task 1. Create .venv
Run the following command from the project root directory.

On Windows, Use PowerShell (not cmd):

py -m venv .venv

Accept VS Code Suggestions
If VS Code asks: We noticed a new environment has been created. Do you want to select it for the workspace folder? Click Yes.

ADVANCED OPTION (Only Use When Required)
Python versions matter. In many projects we can use the most recent version of Python 3. However, using tools like Apache Kafka or Apache Spark may require an earlier version of Python (it takes a while to get all the code updated).

To use those tools in a project, we may need to install a specific earlier version of Python and specify the required version when we create the virtual environment. For example:

On Windows, Use PowerShell (not cmd): py -3.11 -m venv .venv

6. git-pull-before-changes.md
Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub. Keep both locations up-to-date and in sync.

Pulling ensures that:

You work with the latest code.
Merge conflicts are minimized.
Collaboration stays smooth.
Before Starting
Open your project repository in VS Code.

Pull Changes
Run the following command from the project root directory. The command works in PowerShell, bash, zsh, Git Bash, and more.

git pull origin main
Once configured, you might find that a shorter version works as well: git pull

Review the output for updates or conflicts. If there are conflicts, resolve them before proceeding. The best solution to merge conflicts is to AVOID them through a good workflow.

6.  activate-virtual-environment.md
ALWAYS activate the .venv before working on the project.Activate whenever you open a new terminal.

Run the following command from the project root directory. The command works in PowerShell.

.venv\Scripts\activate

07. install-dependencies.md
This page explains how to install external dependencies for a Python project.

Python Standard Library
We do not need to install packages from the Python Standard Library - they are included with our version. The standard library includes helpful packages like pathlib, sqlite3, os, sys, time, and more. See the index.

External Dependencies
External dependencies are libraries, packages, and modules beyond the standard library and include common packages like pandas, numpy, seaborn, and matplotlib.

These must be installed into our local project virtual environment to use them in our code.

Activate/Upgrade/Install
Ensure .venv is active.
Update key packages.
Install dependencies from the requirements.txt file.
Run the following commands from the project root directory. The commands work in PowerShell.

.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt


8.  activate-and-run-python-script.md
This page explains how to run a Python file in VS Code. When we run a Python file directly, we run it as a Python script. Scripts are useful for clear, modular code that we can import into other files and/or schedule to run on a regular basis.


Task 1. Select VS Code Interpreter
VS Code needs our populated .venv to interpret our files correctly.

To set the VS Code Interpreter:

Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux)
Search for "Python: Select Interpreter":
Type Python: Select Interpreter in the Command Palette search bar and select it from the dropdown.
Choose an Interpreter - A list of available Python environments will appear. Look for the local .venv option.
Once selected, check the Python version displayed in the bottom-left corner of the VS Code window in the status bar.
Making Changes / Saving
Now we can get help from the VS Code editor while working on the Python code files.

After making changes, run the file to verify following the steps below. Save your files periodically to avoid losing progress - or make sure the File / Autosave option is on.

Windows Task 2: Activate/Execute
Ensure .venv is active. If active, you don't need to rerun the activate command.
Run the file.
IMPORTANT: Change the name of the file to your actual file. The file must exist in the root project folder for the execute command to work.

Run the following commands from the project root directory. The commands work in PowerShell.

.\.venv\Scripts\activate
py myfile.py

AS-NEEDED: New External Dependencies
If any new external dependencies have been added to any Python scripts, add the external dependencies to requirements.txt and re-run the install dependencies process first.

Experience
Understand why the virtual environment must be activated first. Understand when adding a new external dependency, we must first add it to requirements.txt and re-run the install command. Record your process and steps in your project README.md as you go.
9.  modify-and-test.md
When working on a project always open that project repository folder in VS Code. Remember that in general, terminal commands are intended to be executed in the root project folder.

Use the VS Code menu to turn on autosave (File / Autosave) - or remember to save your changes as you work.

Test your code and ensure it works.

Use git add-commit-push frequently to commit small sets of well-labeled changes to the repository. A good commit history helps identify where things might have gone wrong (or where they got fixed).

In general, do not git add-commit-push if the code doesn't run. Comment out content as needed to get a version that runs without errors before doing git add-commit-push.

06-git-add-commit-push.md
This page provides instructions to add files to version control, commit changes, and push them to your remote repository.

git add - stages changes, adds files to source control
git commit - creates a labeled snapshot of staged changes.
git push - updates the remote repository
Before Starting
Ensure your project repository is open in VS Code, and you have made useful changes.

Task 1. Git add-commit-push
Using a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT: Replace the commit message with a clear and descriptive note about what you added or changed. Wrap the commit message in double quotes.

git add .
git commit -m "Add .gitignore and requirements.txt files"
git push -u origin main
After subsequent changes, you may be able to use a simpler version of the last command:

git push
Experience
Experience comes from executing these commands frequently after making useful changes to a project.
