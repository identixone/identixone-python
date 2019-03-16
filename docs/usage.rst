=====
Usage
=====

To use Identix One Python in a project create instance of `Client`:

.. code:: python

   from identixone.api import Client

   version = 1
   token = 'XXX'
   client = Client(token, version)

Now just make calls using `client` instance as if you were interacting with HTTP API.

For example, create source:


.. code:: python

   response = client.sources.create(name='source_name')
   response.json()
   # {"id": 1, "name": "source_name", "pps_timestamp": False, ... }

Or list some records with filters:

.. code:: python

    import datetime

    period_start = datetime.datetime(
        year=2019, month=1, day=13, hour=19, minute=20, second=1)
    period_end = period_start + datetime.timedelta(days=1)
    response = client.records.list(
        new=True, nm=False, junk=False, exact=False,
        ha=False, det=False, period_start=period_start,
        period_end=period_end)
    response.json()
    # {"result": "ok", "totalqty": 0, "records": [], "sources": []}

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
