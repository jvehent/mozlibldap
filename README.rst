mozlibldap
==========

Python lib for common OpenLDAP queries @ Mozilla.
This only works with LDAP databases using a schema similar to Mozilla's.

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

Testing
~~~~~~~
Fill in the LDAP URL, login, password in tests.py and run it :)

From the code/integrate in my code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add to your project with:

.. code::

   git submodule add https://github.com/mozilla-it/mozlibldap
   git commit -a

Python dependencies
~~~~~~~~~~~~~~~~~~~

* python-ldap

Usage
-----

.. code::

	import mozlibldap
	
	l = mozlibldap.MozLDAP(LDAP_URL, LDAP_BIND_DN, LDAP_BIND_PASSWD)
	print(l.get_user_posix_uid("gdestuynder@mozilla.com"))
