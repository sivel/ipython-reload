# ipython-reload
IPython magic command to reload modules on demand

## Install

```shell
pip install ipython-reload
```

## Use

```
In [1]: %load_ext ipython_reload

In [2]: from foo import some_function

In [3]: some_function()
Out[3]: 42

In [4]: # open foo.py in an editor and change some_function to return 43

In [5]: %reload some_function

In [6]: some_function()
Out[6]: 43
```

The `%reload` magic can reload modules not directly imported, imported modules
in the local namespace, and imported variables.

Reloading imported variables may produce unexpected results if the name is
generic, such as in the case of `__version__`. Python does not track the source
of where a variable was defined, so this code loops all imported modules, and
looks for a matching name, that is the same type as the variable you want to
reload. If you have imported a _variable_ using `from foo import bar as baz`
this functionality will not work.
