#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stages_of_life.py
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

age = 15

if age < 2:
	print('You are a baby')
elif age >= 2 and age < 4:
	print('You are a toddler')
elif age <= 4 and age < 13:
	print('You are a kid')
elif age >=13 and age < 20:
	print('You are a teenager')
elif age >=20 and age <65:
	print('You are an adult')
else:
	print('You are an elder')
