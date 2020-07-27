## Documentation

### Technology Stack

- **Python** — Programming language.

- **Pip** — Python package installer.

- **Pipenv** — Python dependency manager.

### Static Files

- **composer.json** — Pipenv configuration. Describe Python dependencies and their versions to download and update through the command line.

- **.editorconfig** — EditorConfig configuration. Keep consistent code editor settings across the project and its files.

## Development

1. Install Python, Pip, and Pipenv to the local machine. Pip is bundled with Python in the latest versions.

   - See the [Environment](#environment) section for the recommended approach to setting up the development environment.

2. Navigate to the project's root directory in the command line.

3. Execute `pipenv install` to automatically download all required dependencies.

## Environment

### macOS

1. Install [Homebrew](https://brew.sh).

2. Execute `brew install python@3.8`.

3. Execute `sudo pip3 install pipenv`.

    - Note that a version of Python is included with macOS for compatibility with legacy software. Each installed version is isolated by default and can be accessed separately:

        - `python` points to the system's pre-installed Python version.

        - `python2` points to Homebrew's Python version 2.x, if installed.

        - `python3` points to Homebrew's Python version 3.x, if installed.

    - The same naming rules apply to other Python-related symlinks, such as `pip3` or `python3-config`.

### Running commands

#### Inside the Pipenv shell

1. Execute `pipenv shell`.

2. Execute `python -m msb`.

#### Outside the Pipenv shell

1. Execute `pipenv run python -m msb`.

## Notes

### Security

MacOS has security measures to prevent scripts from having control over the system. You must open **Security & Privacy** under **System Preferences**, and grant Accessibility access to Terminal (or whichever application you will be running the script from).
