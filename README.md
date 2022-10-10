# Python Project Template

This project follows the Python Standards declared in [PEP 621](https://peps.python.org/pep-0621/).
This uses a pyproject.yaml to configuration the project. In this example, [flit](https://pypi.org/project/flit/) is used to simplify the build process, and publish to pypi.

## Project Organization

- .devcontainer - This directory contains required files for creating a [Codespace](https://github.com/features/codespaces).
- .github
  - workflows - Contains GitHub Actions used for building, testing and publishing.
    - publish-test.yml - Publish wheels to [https://test.pypi.org/](https://test.pypi.org/)
    - publish.yml - Publish wheels to [https://pypi.org/](https://pypi.org/)
    - pull-request.yml - Build and Test pull requests before commiting to main.
    - template-sync.yml - Update GitHub Repo with enhancments to base template
- docs - collect documents (default format .md)
- src - place new source code here
  - python_package - sample package (this can be deleted when creating a new repository)
- tests - contains Python based test cases to validation src code
- .pre-commit-config.yaml - Contains various pre-check fixes for Python
- .templateversionrc - used to track template version usage.
- MANIFEST.in - Declares additional files to include in Python whl
- pyproject.toml - Python Project Declaration
- ws.code-workspace - Recommended configurations for [Visual Studio Code](https://code.visualstudio.com/)

## pyproject.toml

The following sections are defined in the configuration toml.

- build-system
- project
  - optional-dependencies
  - urls
- tool
  - bandit
  - coverage
    - run
    - report
  - pyright
  - pytest
  - tox
  - pylint
    - MESSAGES CONTROL
    - REPORTS
    - REFACTORING
    - BASIC
    - FORMAT
    - LOGGING
    - MISCELLANEOUS
    - SIMILARITIES
    - SPELLING
    - STRING
    - TYPECHECK
    - VARIABLES
    - CLASSES
    - DESIGN
    - IMPORTS
    - EXCEPTIONS

### build-system
TODO: add info on flit configuration

### project
This section defines the project metadata, which may have been previously contained in a setup.py file.

#### optional-dependencies
This are otpimal dependancey groups that can be installed via 'pip install .[tests]'.
One group is included for dependancies required for testing. A second group is included for PySpark based dependancies.

### tool
This section defines the configurations for additional tools used to format, lint, type-check, and analysis Python code.

#### bandit
Performs Security Static Analysis checks on code base.

#### black
Auto-formats code

#### coverage
Configures code coverage reports generatated during testing.

#### pyright
Performs static type checking on Python.

#### pytest
Configures various test markers used during testing.

#### pylint
Performs Linting and Static Analysis. Any modifictions made by the auto-formater (black) are always considered correct.

## Publish to PyPi from GitHub
In order to publish to PyPi, a repostirory secret must be created, "PYPI_PASSWORD". In order to publish to the Test PyPi, a second secret must be added, "TEST_PYPI_PASSWORD". 


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
