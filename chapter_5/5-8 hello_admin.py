#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5-8 hello_admin.py
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

users = ['admin', 'bob', 'eric', 'devon', 'bill']

for user in users:
	if user == 'admin':
		print("Hello Admin, would you like to see a status report?")
	elif user != 'admin':
		print("Hello " + user + ", thank you for logging in again") 
if users == []:
	print('We need to find some users!')
