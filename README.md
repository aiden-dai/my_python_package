# my_python_package
Test Python Package


## How to Build
Run in terminal 
```bash
$ python setup.py check

$ python setup.py build

$ python setup.py sdist bdist_wheel
```

## How to Install
Run in terminal 
```bash
$ pip install ad_python-0.0.1.tar.gz
```


## How to Test

Example:
```bash
$ pytest -v test/test_utils.py
```


## How to Use

Example:
```python
>>> import ad_python
>>> print(ad_python.__version__)
0.0.1
>>> from ad_python import utils
>>> print(utils.func_add(3, 4))
7
```
