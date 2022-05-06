# Rainbowed (by iWas <3)

A tiny module to simply import colors in Python's stdout.

Uploaded in TestPyPI --> [rainbowed-iwas-1.0.0](https://test.pypi.org/project/rainbowed-iwas/1.0.0/)

### Installation with pip
```console
pip install -i https://test.pypi.org/simple/ --no-deps rainbowed-iwas==1.0.0
```

### Usage in code
```python

from rainbowed.rainbowed import *

print("This is normal")
print("{}This is red".format(rainbowed.RED))
print("{}This is cyan".format(rainbowed.CYAN))
print("{}This is green".format(rainbowed.GREEN))
print("{}Back to normal!".format(rainbowed.RESET))
print("Doing a bit of {}BOLD!".format(rainbowed.BOLD))
print("And {}underlining!{}".format(rainbowed.UNDERLINE, rainbowed.RESET))
print("This is wrong --> {}I love League of Legends".format(rainbowed.CROSSED))

```

### Result
![alt text](https://github.com/iwas-coder/rainbowed/blob/main/output_example.png?raw=true)

## Implementing built-in print functions (Coming soon!)

(...)
