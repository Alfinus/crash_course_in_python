#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  amusement_park.py
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


age = 12

if age < 4:
	print("your admission cost is $0!")
elif age < 18:
	print("Your admission cost is $5!")
else:
	print("Your admission cost is $10!")
	
age = 66

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("\nYour admission cost is $"+ str(price) + "!")
	
