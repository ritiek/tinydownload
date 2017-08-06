tinydownload
============

|pypi.python.org| |build Status|

Download files from tinyupload.com.

Installation
------------

::

    sudo pip install -U tinyupload-downloader

or if you like to live on the bleeding edge:

::

    sudo python setup.py install

Run it using ``tinydownload``

Usage
-----

::

    usage: tinydownload [-h] -n NAME [QUERY [QUERY ...]]

    Download files from tinyupload.com

    positional arguments:
      QUERY                 the file_id or the tinyupload link

    optional arguments:
      -h, --help            show this help message and exit

    required arguments:
      -n NAME, --name NAME  path and name of the file

Contributing
------------

Any PR's in bug fixes, features or even this documentation are most
welcome!

License
-------

``The MIT License``

.. |pypi.python.org| image:: https://img.shields.io/pypi/v/tinyupload-downloader.svg
   :target: https://pypi.org/project/tinyupload-downloader/
.. |build Status| image:: https://travis-ci.org/ritiek/tinyupload-downloader.svg?branch=master
   :target: https://travis-ci.org/ritiek/tinyupload-downloader/
