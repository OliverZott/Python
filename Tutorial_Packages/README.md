# Example - Calculator Package

Simple example on creating pthon packages.

# Resources
## Sample Project!
https://github.com/pypa/sampleproject/blob/main/setup.py

## General
- https://packaging.python.org/
- https://www.youtube.com/watch?v=GIF3LaRqgXo   (Best Practices!!)
- https://www.youtube.com/watch?v=zhpI6Yhz9_4

## Licenses
- https://choosealicense.com/

## Manifest file
- https://packaging.python.org/guides/using-manifest-in/


# Steps
## Structure 
- __init__.py
- LICENSE.txt
- README.md
- MANIFEST.in
- CHANGELOG.txt
- setup.py
## Upload/Dist
- PyPI account
- `pip install setuptools twine`
- cd project_folder
- `python setup.py sdist` ... create distributable version
- `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`  ...upload to pypi repo