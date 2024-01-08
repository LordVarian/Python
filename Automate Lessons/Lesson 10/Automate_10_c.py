import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search("My number is 415-555-5555")
print(mo.group())

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo2 = phoneNumRegex.search("My number is 415-555-5555")
print(mo2.group(1))
print(mo2.group(2))

phoneNumRegex = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
mo3 = phoneNumRegex.search("My number is (415) 555-5555")
print(mo3.group())