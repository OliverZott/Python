# Resources

## Docs 

- https://www.youtube.com/watch?v=-ARI4Cz-awo
- https://www.youtube.com/watch?v=jxmzY9soFXg
- https://docs.python.org/3/library/logging.html#logrecord-attributes

https://trello.com/c/K7f5Imup/14-logging


## Howto

- https://docs.python.org/3.9/howto/logging.html#logging-basic-tutorial
- https://docs.python.org/3.9/howto/logging.html#logging-advanced-tutorial
- https://docs.python.org/3.9/howto/logging-cookbook.html#logging-cookbook



------------------------------------------------------------------------------------
# Remarks

- In format, the name `root` means the **root logger**

### Basics

- Setup
  - `import logging`
  - `logging.debug('message)`
- Configure (write to text file)
  - https://docs.python.org/3.9/library/logging.html#logging.basicConfig
  - `logging.basicConfig(filename="")`
- Configure (format logs)
  - https://docs.python.org/3.9/library/logging.html#logrecord-attributes
  - `logging.basicConfig(format="")`

### Advanced

- Handlers
- Formatters
- Config
- Separate loggers




------------------------------------------------------------------------------------
# Log-Levels

- **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
- **INFO**: Confirmation that things are working as expected.
- **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
- **ERROR**: Due to a more serious problem, the software has not been able to perform some function.
- **CRITICAL**: A serious error, indicating that the program itself may be unable to continue running.