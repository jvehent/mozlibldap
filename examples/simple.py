#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2014 Mozilla Corporation
# Author: gdestuynder@mozilla.com

# Requires:
# mozlibldap

import mozlibldap

LDAP_URL='ldaps://'
LDAP_BIND_DN=''
LDAP_BIND_PASSWD=''

def main():
	l = mozlibldap.MozLDAP(LDAP_URL, LDAP_BIND_DN, LDAP_BIND_PASSWD)
	x=l.getUserUID("gdestuynder@mozilla.com")
	print("UID:", x)

if __name__ == "__main__":
	main()
