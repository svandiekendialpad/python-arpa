Python ARPA Package
===================

[![PyPI Version](https://img.shields.io/pypi/v/arpa.svg)](https://pypi.python.org/pypi/arpa) [![Travis](https://img.shields.io/travis/sfischer13/python-arpa.svg)](https://travis-ci.org/sfischer13/python-arpa) [![Coverage Status](https://coveralls.io/repos/sfischer13/python-arpa/badge.svg?branch=master&service=github)](https://coveralls.io/github/sfischer13/python-arpa?branch=master)

This is a library for reading ARPA n-gram models.  
It was initiated by Stefan Fischer and is developed and maintained by many others.

-   [Questions](mailto:sfischer13@ymail.com) can be asked via e-mail.
-   [Source code](http://github.com/sfischer13/python-arpa) is tracked on GitHub.
-   [Changes](https://github.com/sfischer13/python-arpa/blob/master/HISTORY.md) between releases are documented.
-   [Bugs](https://github.com/sfischer13/python-arpa/issues) can be reported on the issue tracker.

Install
-------

[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/arpa.svg)](https://pypi.python.org/pypi/arpa)

The package is available on [PyPI](https://pypi.python.org/pypi/arpa):

    $ pip install arpa

Use
---

The package may be imported directly:

    import arpa
    models = arpa.loadf("foo.arpa")
    lm = models[0]  # ARPA files may contain several models.

    # probability p(end|in, the)
    lm.p("in the end")
    lm.log_p("in the end")

    # sentence score w/ sentence markers
    lm.s("This is the end .")
    lm.log_s("This is the end .")

    # sentence score w/o sentence markers
    lm.s("This is the end .", sos=False, eos=False)
    lm.log_s("This is the end .", sos=False, eos=False)

Contribute
----------

Write a bug report or send a pull request.  
Other [contributors](https://github.com/sfischer13/python-arpa/graphs/contributors) have done so before.

License
-------

Copyright (c) 2015-2018 Stefan Fischer  
The source code is available under the **MIT License**.  
See [LICENSE](https://github.com/sfischer13/python-arpa/blob/master/LICENSE) for further details.
