# Dash tutorial

<https://www.youtube.com/watch?v=XOFrvzWFM7Y&t=217s>

## Prerequisites

create venv

```bash
python -m venv venv
```

activate env

```bash
.\venv\Scripts\activate
. venv/bin/activate
```

deactivate env

```bash
.\venv\Scripts\deactivate
deactivate venv
```

install packages with activated env and check

```bash
pip install --upgrade -r ./environment/requirements.txt
pip list
pip freeze > pip_list.txt   (to freeze current state)
```

or  
`python -m pip install -r ./environment/requirements.txt`

Upgrade:
`pip install --upgrade --force-reinstall -r requirements.txt`

If tkinter error:
`sudo apt install python3-tk`

## Run

```shell
python .\main.py
```

## Remarks

- `pd.read_csv(dtype=..., parse_dates=...)`
  - [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- `pd.DataFrame.pivot_table()`
  - [pandas.pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html)
- `df.loc[]`
  - [pandas.DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)

## Documentation

- [dcc.Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
