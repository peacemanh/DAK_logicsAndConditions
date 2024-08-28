#!/bin/bash

# Repository Management Guide

# To clone the repository for the first time, use the following command:
git clone https://github.com/peacemanh/DAK_logicsAndConditions.git
# This will create a local copy of the repository on your machine.

# Navigate to a local copy of the repository on your machine
cd DAK_logicsAndConditions

# Keeping Your Local Code Up-to-Date
git pull origin main

# Pushing Changes to the Remote Repository

# 1. Using Git Command Line

# Stage Your Changes:
git add <filename>

# Commit Your Changes:
git commit -m "Your commit message"

# Push Your Changes:
git push origin main

# 2. Using Visual Studio Code (VS Code) UI

# To push changes using the VS Code UI, follow these steps:

# Open the Source Control Panel:
# Click on the Source Control icon in the Activity Bar on the side of the VS Code window.

# Stage Your Changes:
# You will see a list of changed files. Click the + icon next to each file to stage it,
# or click the + icon at the top of the panel to stage all changes.

# Commit Your Changes:
# In the Source Control panel, enter a commit message in the input box at the top.
# Click the checkmark icon (✔) or press Ctrl+Enter (or Cmd+Enter on macOS) to commit your changes.

# Push Your Changes:
# After committing, click on the ... (More Actions) icon in the Source Control panel.
# Select Push from the dropdown menu.
# Alternatively, you can use the Sync Changes button (🔄) if it is available in the status bar to both push and pull changes.