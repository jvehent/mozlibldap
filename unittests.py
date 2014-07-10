#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2014 Mozilla Corporation
# Author: gdestuynder@mozilla.com

# Requires:
# mozlibldap

import mozlibldap
import unittest

LDAP_URL='ldap://'
LDAP_BIND_DN=''
LDAP_BIND_PASSWD=''


class TestLDAPFunctions(unittest.TestCase):

	def setUp(self):
		self.dn = "mail=gdestuynder@mozilla.com"
		self.uid = 1663
		self.l = mozlibldap.MozLDAP(LDAP_URL, LDAP_BIND_DN, LDAP_BIND_PASSWD)

	def test_get_user_posix_uid(self):
		x = self.l.get_user_posix_uid(self.dn)
		print("uid+username:", x)
		self.assertItemsEqual(('gdestuynder', 1663), x)

	def test_get_user_dn_by_uid(self):
		x = self.l.get_user_dn_by_uid(self.uid)
		print("DN:", x)
		self.assertItemsEqual('mail=gdestuynder@mozilla.com,o=com,dc=mozilla', x)

	def test_get_user_email(self):
		x = self.l.get_user_email(self.dn)
		print("Email", x)
		self.assertItemsEqual(['gdestuynder@mozilla.com'], x)

	def test_get_user_attribute(self):
		x = self.l.get_user_attribute(self.dn, 'sn')
		print("sn", x)
		self.assertItemsEqual(['Destuynder'], x)

	def test_get_user_attributes(self):
		x = self.l.get_user_attributes(self.dn)
		print("Attributes", str(len(x)))
		self.assertGreater(len(x), 0)

	def test_get_all_disabled_users(self):
		x = self.l.get_all_disabled_users()
		print("disabled users:", str(len(x)))
		self.assertGreater(len(x), 0)

	def test_get_all_groups(self):
		x = self.l.get_all_groups()
		print("all groups:", str(len(x)))
		self.assertGreater(len(x), 0)

	def test_get_all_enabled_users_attr(self):
		x = self.l.get_all_enabled_users_attr('sn')
		print("enabled user's attr sn list:", str(len(x)))
		self.assertGreater(len(x), 0)

if __name__ == "__main__":
	unittest.main()
