import math
import re
def password_entropy(pwd):
	l=len(pwd)
	if l==0:
		return 0,0,"No password has been provided"
	reg=0
	if re.search(r'[a-z]',pwd):
		reg+=26
	if re.search(r'[A-Z]',pwd):
		reg+=26
	if re.search(r'\d',pwd):
		reg+=10
	if re.search(r'[^a-zA-z0-9]',pwd):
		reg+=32
	if reg==0:
		entropy=0
	else:
		entropy=l*math.log2(reg)
	if entropy<40:
		strength="Weak password"
	elif entropy<60:
		strength="Moderate(Could be better)"
	elif entropy<80:
		strength="Strong(Secure against most attacks)"
	else:
		strength="Unbreakable"
	return entropy,reg,strength
if __name__=="__main__":
	print("PASSWORD ENTROPY EVALUATOR")
	user_pwd=input("Enter a password to test")
	entropy_bits,pool_size,strength_level=password_entropy(user_pwd)
	print("RESULTS")
	print("Password length=",len(user_pwd))
	print("Character pool size=",pool_size)
	print("Calculated Entropy=",entropy_bits," bits")
	print("Overall strength=",strength_level)


