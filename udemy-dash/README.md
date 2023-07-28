# Plotly - Dash

<https://www.udemy.com/course/interaktive-python-visualisierungen-mit-plotly-und-dash/learn/lecture/14723266#overview>

**Resources**  

- <https://plotly.com/python/>
- <https://plotly.com/python/reference/>

**Dev Mode**

- <https://dash.plotly.com/devtools#configuring-dash-dev-tools-&-app.run-reference>

## Prerequisites

```bash
# Create/activate/deactivate venv
python -m venv venv
.\venv\Scripts\activate
source venv/bin/activate
.\venv\Scripts\deactivate

# Install packages with activated env and check
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt 
pip list

# Freeze and Upgrade current packages  
pip freeze > pip_list.txt   
pip install --upgrade --force-reinstall -r requirements.txt
```

## Run

## TOC

## Remarks

- **plotly.graph_objs** vs **plotly.express**:
  - plotly.graph_objs provides a more low-level and flexible way to create figures while plotly.express provides a more concise and consistent way to create common figures.
  - plotly.express is a high-level wrapper for plotly.graph_objs which itself is a low-level library for drawing figures. plotly.express is to plotly.graph_objs what seaborn is to matplotlib.

- Static export
  - <https://plotly.com/python/static-image-export/>

## Usefull in VS Code

- install Autopep8 extension
- create settings file
- format on save enable
- format notebook enable

## Useful tools and packages

### Formatter-Linter-Type checker

- Formatter
  - black
  - `black --check .`
  - isort
  - `isort --check .`
  - `isort . --diff` (check diff)
  - `isort --skip venv .` (apply)
- Linter
  - flake8 (check only)
  - flake8-comprehensions
  - `flake8 .`
  - flake8 only checks the code by default and does not apply any changes.
- Type checker
  - mypy (check only)
  - `mypy --exclude venv .`
  - mypy only checks the code by default and does not apply any changes

### Pre-Commit

Running all tools on commit or manually. Every time you make a commit, pre-commit will automatically run black, flake8, isort, and mypy on the code.

- <https://pre-commit.com/>
- `pip install pre-commit`
- **.pre-commit-config.yaml** for configuration (in root dir)
- `pre-commit install` to set up the pre-commit hook
- `pre-commit install-hooks`
- `pre-commit run --all-files`

### Logging

- loguru

### Testing

- pytest

## Autodocstring (doc tool)

- install vs code extension
- configure in settings.json
- usage: `"""<tab>` or `"""<enter>`
