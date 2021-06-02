from setuptools import setup, find_packages

classifiers = [
    'Developement Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='basiccalcexample',
    version='0.0.1',
    description='just a basic example for packages',
    long_description=long_description,
    long_description_contente_type="text/markdown",
    py_modules=["basiccalculator"],
    package_dir={'': 'src'},
    url='',
    author='Oliver Zott',
    author_email='zott_oliver@web.de',
    license='MIT',
    classifiers=classifiers,
    keywords='calculators',
    packages=find_packages(),
    install_requires=['']
)
