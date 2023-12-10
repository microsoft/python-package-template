# pre-commit-config.yaml

Pre-commit is a Python package which can be used to create 'git' hooks which scan can prior to checkins.
The included configuration focuses on python actions which will help to prevent users from committing code which will fail during builds.
In general, only formatting actions are automatically performed. These include auto-formatting with 'black', or sorting dependencies with 'isort'.
Linting actions are left to the discretion of the user.
