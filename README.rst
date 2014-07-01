mozlibldap
==========

Python lib for common OpenLDAP queries @ Mozilla_.

Install
--------
As a python module
~~~~~~~~~~~~~~~~~~

Manually:
.. code::

    make install

As a rpm/deb package
.. code::

   make rpm
   make deb
   rpm -i <package.rpm>
   dpkg -i <package.deb>

From the code/integrate in my code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add to your project with:

.. code::

   git submodule add https://github.com/mozilla-it_lib mozlibldap
   git commit -a

Python dependencies
~~~~~~~~~~~~~~~~~~~

* python-ldap

Usage
-----

N/A
