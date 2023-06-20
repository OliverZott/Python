# Python Advanced

<https://www.udemy.com/course/interaktive-python-visualisierungen-mit-plotly-und-dash/learn/lecture/14723266#overview>

Resources:
<https://plotly.com/python/>
<https://plotly.com/python/reference/>

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
