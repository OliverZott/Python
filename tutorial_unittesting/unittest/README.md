# Unit Testing - unittest

- https://docs.python.org/3.8/library/unittest.html

---
# Remarks

- test have to be isolated!
- Context Manager: `with ...: `
- naming convention: `test_filename.py`
- method has to be named: `test_methodname`
- run test:
    - `python3 unittest test_filename.py` or use
    - `unittest.main()` in`if __name__ ... unittest.main()`
- `setUp(self)` and `tearDown(self)` run before/after each test
- `@classmethod` `setUpClass(cls)` and `tearDownClass(cls)` run before/after whole test file

### Mocking (e.g. Website / Database / ...)
- `from unittest.mock import patch`
- `with patch('function') as name: `

---
# Questions
- why import with autosuggestion for custom files not working in vs code?
- where put test in project?
- where put tests in module/package?
- general package structure(init, tests, src, ...)
