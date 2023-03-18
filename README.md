# Python Project Template

This project is a template for creating Python projects that follows the Python Standards declared in [PEP 621](https://peps.python.org/pep-0621/).
It uses a `pyproject.yaml` file to configure the project and [Flit](https://pypi.org/project/flit/) to simplify the build process and publish to PyPI.
One advantage of using Flit is that you do not need a `setup.py` or `setup.cfg` file. Instead, you only need to include the relevant information in your `pyproject.toml` file.

## Project Organization

- `.github/workflows`: Contains GitHub Actions used for building, testing, and publishing.
- `src`: Place new source code here.
- `tests`: Contains Python-based test cases to validate source code.
- `pyproject.toml`: Python Project Declaration.

### `pyproject.toml`

The `pyproject.toml` file contains the following sections:

- `project`: Defines the project metadata, which may have been previously contained in a `setup.py` file.
- `tool`: Defines the configurations for additional tools used to format, lint, type-check, and analyze Python code.

#### `tool` sections

- `black`: Auto-formats code.
- `coverage`: Configures code coverage reports generated during testing.
- `pytest`: Configures various test markers used during testing.
- `pylint`: Performs linting and static analysis. Any modifications made by the auto-formatter (`black`) are always considered correct.

## Getting Started

To get started with this template, simply clone this repository and start building your project within the `src` directory.

## Contributing

This project welcomes contributions and suggestions.
For details, visit the repository's [Contributor License Agreement (CLA)](https://cla.opensource.microsoft.com) and [Code of Conduct](https://opensource.microsoft.com/codeofconduct/) pages.
