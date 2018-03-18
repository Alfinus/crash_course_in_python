#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5-1 conditional_tests.py
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


car = 'subaru'
print('Is car == "subaru"? I predict True.')
print(car == 'subaru')

print("\n Is car == 'audi'? I predict False!")
print (car == 'audi')
if car != 'audi':
	print('\nwhoops, seems we took a wrong direction')

print('\nlets add another variable')

car_1 = 'audi'

car_2 = 'BMW'

car_3 = 'Toyota'

print('\nIs car_1 == "audi"? I predict true!')
print(car_1 == 'audi')

print('\nThere we go')

print('\nLets try another one')

print("\nIs car_2 == 'subaru'? I predict False.")
print(car_2 == 'subaru')

print('\nwhoops there we go again....')

print("\nIs car_2 == 'BMW'? I predict True!")
print(car_2 == 'BMW')
