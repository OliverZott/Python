# Python Advanced

<https://www.udemy.com/course/fortgeschrittene-python-programmierung/learn/lecture/18919946#overview>
<https://github.com/franneck94/UdemyPythonPro/blob/master/Chapter02_Basics/Memory/Inplace.ipynb>
<https://github.com/franneck94/Python-Project-Template>

## Prerequisites

Create/activate/deactivate venv

```bash
python -m venv venv
.\venv\Scripts\activate
source venv/bin/activate
.\venv\Scripts\deactivate
```

Install packages with activated env and check

````bash
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list
````

Freeze and Upgrade current packages  

```bash
pip freeze > pip_list.txt   
pip install --upgrade --force-reinstall -r requirements.txt
```

## Tools

black, ruff, (isort), autodocstring, mypy

- **black** (formatter)
  - [autopep8, black, yapf]
  - `black --check .`
  - use trailing comma in last line to keep multi-line code
- **flake8** (linter)
  - [flake8, pylint, ruff]
  - `flake8 .`
  - config in **.flake8**
- **isort** (import formatter)
  - `pip install isort`
  - `isort .\test.py --diff`
  - `isort --check .`
  - `isort . --diff` (check diff)
  - `isort --skip venv .` (apply)
  - <https://pycqa.github.io/isort/>
  - (install vs code extension ???)
  - pyproject.toml
- documentation: **autodocstring**
  - install vs code extension
  - settings.json: `"autoDocstring.docstringFormat": "numpy"`
- type linter: **mypy**
  - `pip install mypy`
  - **settings.json**: `"python.linting.mypyEnabled": true,`
  - **console**: `mypy .\type_annotations.py`

### Pre-Commit

- running all tools on commit or manually
- <https://pre-commit.com/>
- `pipo install pre-commit`
- `pre-commit install`
- `pre-commit install-hooks`
- `pre-commit run --all-files`

### pyproject.toml

- this config file is used in build tools like poetry, flit, pipenv
- it's not used for configuration of vs code / python interpreter

## Run

## TOC
