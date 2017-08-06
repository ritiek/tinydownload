tinydownload
============

|pypi.python.org| |build Status|

Download files from tinyupload.com.

Installation
------------

::

    sudo pip install -U tinydownload

or if you like to live on the bleeding edge:

::

    sudo python setup.py install

Run it using ``tinydownload``

Usage
-----

::

	usage: tinydownload [-h] [-o OUTPUT_FILE] query

	Download files from tinyupload.com

	optional arguments:
	  -h, --help            show this help message and exit

	required arguments:
	  query                 the file_id or the tinyupload link
	  -o OUTPUT_FILE, --output-file OUTPUT_FILE
							path and name of the file

Contributing
------------

Any PR's in bug fixes, features or even this documentation are most
welcome!

License
-------

``The MIT License``

.. |pypi.python.org| image:: https://img.shields.io/pypi/v/tinydownload.svg
   :target: https://pypi.org/project/tinydownload/
.. |build Status| image:: https://travis-ci.org/ritiek/tinydownload.svg?branch=master
   :target: https://travis-ci.org/ritiek/tinydownload/
