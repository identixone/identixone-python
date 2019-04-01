=====
Usage
=====

Get your free API token for development at https://identix.one

To use Identix One Python in a project create instance of `Client`:

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
