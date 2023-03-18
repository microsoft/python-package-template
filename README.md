# Python Project Template

This project is a template for creating Python projects that follows the Python Standards declared in PEP 621. It uses a pyproject.yaml file to configure the project and Flit to simplify the build process and publish to PyPI. One advantage of using Flit is that you do not need a setup.py or setup.cfg file. Instead, you only need to include the relevant information in your pyproject.toml file.

## Project Organization

- `.github/workflows`: Contains GitHub Actions used for building, testing, and publishing.
- `.devcontainer/Dockerfile`: Contains Dockerfile to build a development container for VSCode with all the necessary extensions for Python development installed.
- `.devcontainer/devcontainer.json`: Contains the configuration for the development container for VSCode, including the Docker image to use, any additional VSCode extensions to install, and whether or not to mount the project directory into the container.
- `.vscode/settings.json`: Contains VSCode settings specific to the project, such as the Python interpreter to use and the maximum line length for auto-formatting.
- `src`: Place new source code here.
- `tests`: Contains Python-based test cases to validate source code.
- `pyproject.toml`: Contains metadata about the project and configurations for additional tools used to format, lint, type-check, and analyze Python code.

### `pyproject.toml`

The pyproject.toml file is used in modern Python projects as an alternative to the setup.py file. It contains metadata about the project, including the project name, version, description, authors, and dependencies. It also includes configuration for various tools used in the project, such as linters, formatters, and test runners.

In this particular pyproject.toml file, the [build-system] section specifies that the flit package should be used to build the project. The [project] section contains metadata about the project, including the name, description, authors, and classifiers. The [project.optional-dependencies] section lists optional dependencies, such as pyspark, and the [project.urls] section lists URLs for the project documentation, source code, and issue tracker.

The file also contains various configuration sections for different tools, including bandit, black, coverage, flake8, pyright, pytest, tox, and pylint. These sections specify settings for each tool, such as the maximum line length for flake8 and the minimum code coverage percentage for coverage.

#### Tool Sections

##### black

Black is a Python code formatter that automatically reformats Python code to conform to the PEP 8 style guide. It is used to maintain a consistent code style throughout the project.

The pyproject.toml file specifies the maximum line length and whether or not to use a "fast" mode for formatting. Black also allows for a pyproject.toml configuration file to be included in the project directory to customize its behavior.

##### coverage

Coverage is a tool for measuring code coverage during testing. It generates a report of which lines of code were executed during testing and which were not.

The pyproject.toml file specifies that branch coverage should be measured and that the tests should fail if the coverage falls below 100%. Coverage can be integrated with a variety of test frameworks, including pytest.

##### pytest

Pytest is a testing framework for Python that allows you to write test cases in a simple and intuitive way. It is capable of running both pytest-style tests and unittest-style tests, making it a flexible and versatile option for testing Python code.

In addition to its support for both pytest and unittest, pytest also offers a number of useful features for testing, such as fixtures, which allow you to set up test data and other resources before running tests; parameterized tests, which allow you to run the same test with different input values; and plugins, which allow you to extend pytest's functionality in various ways.

The pyproject.toml file configures various test markers used during testing, such as integration, notebooks, gpu, spark, slow, and unit. It also specifies options for generating test coverage reports, setting the Python path, and outputting test results in the xunit2 format. This makes it easy to customize pytest to fit the specific needs of your project.

##### pylint
Pylint is a Python code linter and static analysis tool that checks your code for errors and style issues. It provides a comprehensive report of all errors, warnings, and conventions in your code.

The pyproject.toml file contains a variety of configurations for Pylint, such as which extensions are allowed, which warnings to ignore, and how to format the output. It also contains various settings for code style, including the maximum number of arguments and the maximum number of attributes allowed for a class. Pylint provides a score for your code's quality, which can help you maintain a high standard of code readability and maintainability.

##### pyright
Pyright is a static type checker for Python that uses type annotations to analyze your code and catch type-related errors. It is capable of analyzing Python code that uses type annotations as well as code that uses docstrings to specify types.

The pyproject.toml file contains configurations for Pyright, such as the directories to include or exclude from analysis, the virtual environment to use, and various settings for reporting missing imports and type stubs. By using Pyright, you can catch errors related to type mismatches before they even occur, which can save you time and improve the quality of your code.

##### flake8
Flake8 is a code linter for Python that checks your code for style and syntax issues. It checks your code for PEP 8 style guide violations, syntax errors, and more.

The pyproject.toml file contains configurations for Flake8, such as the maximum line length, which errors to ignore, and which style guide to follow. By using Flake8, you can ensure that your code follows the recommended style guide and catch syntax errors before they cause problems.

##### tox
Tox is a tool for automating Python package testing and building. It can be used to run tests in multiple environments and versions of Python, ensuring that your package is compatible with a wide range of environments.

The pyproject.toml file contains configurations for Tox, such as which environments to test and which commands to run. By using Tox, you can automate the testing and building process, making it easier to ensure that your package works in a wide range of environments.

### Development
#### Codespaces
GitHub Codespaces is a cloud-based tool that provides a fully functional development environment that you can access from anywhere. To get started, you can create a Codespace from a template repository and explore some of the essential features available to you within the Codespace.

You'll work in the browser version of Visual Studio Code, which is initially the default editor for GitHub Codespaces. After creating your Codespace, you may prefer to work in the desktop version of Visual Studio Code instead of the browser version. To do this, 
you can go to your GitHub account settings, click on "Codespaces," and then select "Default editor" under the "Advanced" section. From here, you can choose to set your default editor to the desktop version of Visual Studio Code.

Once you have set your default editor, you can connect to your Codespace from within the desktop version of Visual Studio Code. Simply click on the "Connect to a Codespace" button in the bottom-left corner of the window and select your Codespace from the list of available options. After creating your Codespace, you can use it to develop, test, and deploy your code without having to install any software on your local machine.

In addition to these features, you can enable Settings Sync to synchronize extensions and other settings across devices and instances of VS Code. Whether Settings Sync is enabled by default in a Codespace depends on your existing settings and on whether you open the Codespace in the browser or in the VS Code desktop application.

#### Devcontainer
Dev Containers in Visual Studio Code allows you to use a Docker container as a complete development environment, opening any folder or repository inside a container and taking advantage of all of VS Code's features. A devcontainer.json file in your project describes how VS Code should access or create a development container with a well-defined tool and runtime stack. You can use an image as a starting point for your devcontainer.json. An image is like a mini-disk drive with various tools and an operating system pre-installed. You can pull images from a container registry, which is a collection of repositories that store images.

To create a dev container in VS Code, you need to create a devcontainer.json file, which describes how VS Code should start the container and what to do after it connects. You can make and persist changes to the dev container, such as installation of new software, through use of a Dockerfile. Additional dev container configuration is also possible, including installing additional tools, automatically installing extensions, forwarding or publishing additional ports, setting runtime arguments, reusing or extending your existing Docker Compose setup, and adding more advanced container configuration.

After any changes are made, you must build your dev container to ensure changes take effect. Once your dev container is functional, you can connect to and start developing within it. If the predefined container configuration does not meet your needs, you can also attach to an already running container instead. If you want to install additional software in your dev container, you can use the integrated terminal in VS Code and execute any command against the OS inside the container.

When editing the contents of the .devcontainer folder, you'll need to rebuild for changes to take effect. You can use the Dev Containers: Rebuild Container command for your container to update. However, if you rebuild the container, you will have to reinstall anything you've installed manually. To avoid this problem, you can use the postCreateCommand property in devcontainer.json. There is also a postStartCommand that executes every time the container starts.

You can also use a Dockerfile to automate dev container creation. In your Dockerfile, use FROM to designate the image, and the RUN instruction to install any software. You can use && to string together multiple commands. If you don't want to create a devcontainer.json by hand, you can select the Dev Containers: Add Dev Container Configuration Files... command from the Command Palette (F1) to add the needed files to your project as a starting point, which you can further customize for your needs.

#### Setup
This project includes three files in the .devcontainer and .vscode directories that enable you to use GitHub Codespaces or Docker and VSCode locally to set up an environment that includes all the necessary extensions and tools for Python development.

The Dockerfile specifies the base image and dependencies needed for the development container. The Dockerfile installs the necessary dependencies for the development container, including Python 3 and flit, a tool used to build and publish Python packages. It sets an environment variable to indicate that flit should be installed globally. It then copies the pyproject.toml file into the container and creates an empty README.md file. It creates a directory src/python_package and installs only the development dependencies using flit. Finally, it removes unnecessary files, including the pyproject.toml, README.md, and src directory.

The devcontainer.json file defines the configuration for the development container, including the Docker image to use, any additional VSCode extensions to install, and whether or not to mount the project directory into the container. It is based on the format details provided by Microsoft, which can be found at https://aka.ms/devcontainer.json, and uses the python-3-miniconda container as its base, which can be found at https://github.com/microsoft/vscode-dev-containers/tree/v0.222.0/containers/python-3-miniconda. The file also contains customizations for VSCode, such as a list of recommended extensions for Python development and specific settings for those extensions. Additionally, it includes a command to install pre-commit hooks when the container is created, which ensures that code is properly formatted and validated before it is committed to the repository.

The settings.json file contains various project-specific settings that can be configured in VSCode, such as auto-formatting options, auto-trimming of trailing whitespace, Git auto-fetching, and more. It also contains specific settings for Python, such as the default interpreter to use, the formatting provider, and whether to enable unittest or pytest. Additionally, it includes arguments for various tools such as Pylint, Black, Flake8, and Isort, which are specified in the pyproject.toml file.

## Getting Started

To get started with this template, simply clone this repository and start building your project within the `src` directory.

## Contributing

This project welcomes contributions and suggestions. For details, visit the repository's [Contributor License Agreement (CLA)](https://cla.opensource.microsoft.com) and [Code of Conduct](https://opensource.microsoft.com/codeofconduct/) pages.
