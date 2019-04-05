identixone-python
=================

.. image:: https://img.shields.io/pypi/v/identixone.svg
   :target: https://pypi.python.org/pypi/identixone
.. image:: https://secure.travis-ci.org/identixone/identixone-python.png?branch=master
   :target: https://travis-ci.org/identixone/identixone-python
.. image:: https://readthedocs.org/projects/identixone-python/badge/?version=latest
   :target: https://identixone-python.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://pyup.io/repos/github/identixone/identixone-python/shield.svg
   :target: https://pyup.io/repos/github/identixone/identixone-python/
   :alt: Updates

A Python package for interacting with the Identix.one API

* Free software: MIT license
* Package documentation: https://identixone-python.readthedocs.io/
* API documentation: https://kb.identix.one/
* API changelog: https://kb.identix.one/#/apichangelog
* Current supported most recent API version: **1.10.0**
* Current stable package version: **0.1.3**


Installation
------------

Install from PyPi using
`pip <http://www.pip-installer.org/en/latest/>`__, a package manager for
Python.

::

   pip install identixone

Don't have pip installed? Try installing it, by running this from the
command line:

::

   $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can `download the source code
(ZIP) <https://github.com/identixone/identixone-python/zipball/master>`__ for
``identixone-python``, and then run:

::

   python setup.py install

You may need to run the above commands with ``sudo``.


API Credentials
~~~~~~~~~~~~~~~

Get your free API token for development at https://identix.one


Getting Started
---------------

First of all, specify your API token and API version in `Client`:

.. code:: python

    from identixone.api import Client

    version = 1
    token = 'XXX'
    client = Client(token, version)

You can also configure `Client` using environment variables with prefix `IDENTIXONE_` and uppercase key (e.g. TOKEN, VERSION):

.. code:: python

    from identixone.api import Client

    os.environ['IDENTIXONE_TOKEN'] = 'XXX'
    os.environ['IDENTIXONE_VERSION'] = '1'
    client = Client()

Now just make calls using `client` instance as if you were interacting with HTTP API.

For example, create source:


.. code:: python

    response = client.sources.create(name='source_name')
    response.json()
    # {"id": 1, "name": "source_name", "pps_timestamp": False, ... }

Or list some entries with filters:

.. code:: python

    import datetime

    date_from = datetime.datetime(year=2019, month=1, day=13, hour=19,
                                     minute=20, second=1)
    date_to = datetime.datetime(year=2019, month=1, day=22, hour=19,
                                   minute=20, second=1)
    r = client.entries.list(date_from=date_from, date_to=date_to)
    print(r.json())
    # {"count": 1, "next": "url", "previous": "url", "results": [{ ... }]}

Or even compare two faces how similar they are:

.. code:: python

    from identixone.base.choices import Conf

    response = client.utility.compare(
        photo1, photo2,
        liveness_photo1=False, liveness_photo2=False,
        conf=Conf.JUNK)
    response.json()
    # {"similar": True, "conf": "ha", "liveness_photo1": False, "liveness_photo2": True}

Full examples are inside `examples.py` file in the root of this repo.

To explore all of the API endpoints visit https://kb.identix.one/

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
