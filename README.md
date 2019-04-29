# Package Explorer
A small tool I built to explore through the various methods in a python package from the terminal. The tool currently works only for unpacking methods that sit within a library directory inside the package (methods that are 2 levels away). e.g. methods within the `timeit` library.

The tool currently supports both **plain-text** and **regex** params for conducting queries.

---

### To use

1. Run `$ python3`

1. Import package to be explored: `import timeit`

1. Import the `Explore` class with `$ from explore import Explore`

1. Assign to variable `$ e = Explore(timeit)`

1. Pass search strings to see methods available. Example:
    ```
    $ e.find('thread')
    
    {'thread_info': 'sys',
     'thread_time': 'time',
     'thread_time_ns': 'time'}
    ```
1. Pass search strings to see docstrings for methods found. Example: 
    ```
    $ e.describe('thread')
    
    Call with: timeit.sys.thread_info
    sys.thread_info

    A struct sequence holding information about the thread implementation.
    -----

    Call with: timeit.time.thread_time
    thread_time() -> float

    Thread time for profiling: sum of the kernel and user-space CPU time.
    -----

    Call with: timeit.time.thread_time_ns
    thread_time() -> int

    Thread time for profiling as nanoseconds:
    sum of the kernel and user-space CPU time.
    
    ```
