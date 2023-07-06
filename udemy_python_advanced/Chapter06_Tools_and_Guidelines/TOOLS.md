# Tools

linter: tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs
formatter: tool that automatically formats source code to follow a particular style guide
import optimizer: tool that automatically sorts and formats import statements

## Flake 8 (linter)

- <https://flake8.pycqa.org/en/latest/>
- config: .flake8
- `flake8 .\test.py`

## Pylint (linter)

- <https://pylint.readthedocs.io/en/stable/>
- config: .pylintrc
- `pylint .\test.py`
- `pylint --generate-rcfile > .pylintrc`

## Isort (import optimizer)

- <https://pycqa.github.io/isort/>
- pyproject.toml
- `isort .\test.py --diff`

## Autppep8 (formatter)

- vs code extension

## Black (formatter)

- vs code extension
- standard ("better" then autopep8?)

## Ruff (linter)

- comnining linters
- <https://beta.ruff.rs/docs/configuration/>
- `ruff .` ...testing all files in current directory
- `ruff . --fix` ...fixing all files in current directory
- to test: `Measure-Command {isort .}` vs `Measure-Command {ruff .}`

## Autodocstring (doc tool)

- install vs code extension
- configure in settings.json
- usage: `"""<tab>` or `"""<enter>`

## Mypy (type annotation tool)

- <https://mypy.readthedocs.io/en/latest/config_file.html>
- typing in gerneal : <https://docs.python.org/3/library/typing.html>
- **settings.json**: `"python.linting.mypyEnabled": true,`
- **console**: `mypy .\type_annotations.py`
