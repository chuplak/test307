from string import ascii_lowercase as az
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def check(text):
	return set(text.lower()).issuperset(set(az))
	
	
	print(check("abc") == False)
	print(check("abcdefghijklmnopqrstuvwxyz") == True)
	print(check("ABCDEFGHIGKLMNOPQRSTUVWXYZ") == True)
	print(check("Quick brown fox jump over the lazy dog"))