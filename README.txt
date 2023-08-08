### Global variables
    file - constants.py

    -Tokens-
    **${DATA_ENGINEER_TOKEN}** - required for running tests with the Data Engineer role.
    **${PROJECT_MANAGER_TOKEN}** - required for running tests with the Project Manager role.
    **${SITE_IM_PERSON_TOKEN}** - required for running tests with the Site Incident Management Person role.

    -Environments-
    **${DEV_ENV}** -  boolean value
    **${STAGE_ENV}** - boolean value

### Pre-commit hooks for Python Code Quality

The "pre-commit-config.yaml" file in this repository configures pre-commit hooks to maintain code quality and consistency for Python projects. Below is a brief description of each hook included in the file:

1.  **trailing-whitespace:**
    This hook checks for and removes any trailing whitespace at the end of lines, ensuring cleaner code formatting.

2.  **end-of-file-fixer:**
    The end-of-file-fixer hook ensures that the files end with a newline character, promoting consistency in line endings.

3.  **check-yaml:**
    This hook validates YAML files for syntax errors, helping to maintain properly structured configuration files.

4.  **debug-statements:**
    The debug-statements hook detects and flags any leftover debug statements like "print" statements, promoting cleaner code in the repository.

5.  **double-quote-string-fixer:**
    This hook automatically converts single-quoted strings to double-quoted strings, promoting consistent string formatting.

6.  **reorder-python-imports:**
    The reorder-python-imports hook automatically sorts and organizes Python import statements to adhere to best practices.

7.  **add-trailing-comma:**
    This hook automatically adds trailing commas to Python dictionaries and lists, making version control changes cleaner and more readable.

8.  **pyupgrade (with --py38-plus):**
    The pyupgrade hook applies various Python code upgrades, and with the --py38-plus argument, it performs Python 3.8+ upgrade-related changes.

9.  **autopep8:**
    The autopep8 hook automatically formats Python code according to the PEP 8 style guide.

10. **flake8 (with --max-line-length '120'):**
    The flake8 hook checks Python code against coding standards and style rules, with a custom maximum line length of 120 characters.

11. **mypy (with additional_dependency types-all):**
    The mypy hook performs static type checking on Python code, ensuring type safety. It uses the additional dependency "types-all" to support type hinting.

12. **pydocstyle:**
    The pydocstyle hook checks Python docstrings against PEP 257 standards, promoting clean and consistent documentation.

### How to use "pre-commit-config.yaml"
1. Run it manually with command ***pre-commit run --all-files***
2. Install file with config to hooks using command ***pre-commit install***
