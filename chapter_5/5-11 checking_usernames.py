#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5-11 checking_usernames.py
#  
#  Copyright 2018 Devon <Devon@BETSY>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


current_users = ['admin', 'bob', 'eric', 'devon', 'bill']
new_users = ['bob', 'eric', 'megan', 'gabi', 'rosa']
for user in new_users:
	if user in current_users:
		print("\nPlease enter a new user name, " + user + " is already taken.")
	else:
		print("\n" + user + " is an available username") 