import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
mo2 = batRegex.search("Batmotorcycle lost a wheel")
print(mo2.group())