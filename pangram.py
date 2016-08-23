# Copyright 2016
from string import ascii_lowercase as az
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check(text):
	return set(text.lower()).issuperset(set(az))


print(check("abc"))
