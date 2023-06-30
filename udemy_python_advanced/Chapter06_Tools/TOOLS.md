# Tools

linter: tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs
formatter: tool that automatically formats source code to follow a particular style guide
import optimizer: tool that automatically sorts and formats import statements

## Flake 8

- <https://flake8.pycqa.org/en/latest/>
- config: .flake8
- `flake8 .\test.py`

## Pylint

- <https://pylint.readthedocs.io/en/stable/>
- config: .pylintrc
- `pylint .\test.py`
- `pylint --generate-rcfile > .pylintrc`

## Isort

- <https://pycqa.github.io/isort/>
- pyproject.toml
- `isort .\test.py --diff`

## Autppep8

- vs code extension

## Black

- vs code extension
- standard ("better" then autopep8?)

## Ruff

- <https://beta.ruff.rs/docs/configuration/>
- `ruff .` ...testing all files in current directory
- `ruff . --fix` ...fixing all files in current directory
- to test: `Measure-Command {isort .}` vs `Measure-Command {ruff .}`

## Autodocstring

- install vs code extension
- configure in settings.json
- usage: `"""<tab>` or `"""<enter>`

## Mypy
