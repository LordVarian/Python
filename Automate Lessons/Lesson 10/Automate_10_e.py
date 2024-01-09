import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwowowowoman")
print(mo == None)

# \? this can appear 0 or 1 times in order to match this pattern

phoneRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo2.group())
mo3 = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
try:
    print(mo3.group())
except:
    print("No match")
    
phoneRegex = re.compile(r'(\d{3}-)?(\d{3})-(\d{4})')
mo4 = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
print(mo4.group())

batRegex2 = re.compile(r'Bat(wo)*man')
# \* matches zero or more times in order to match this pattern
print(batRegex2.search("Batman lost a wheel"))
print(batRegex2.search("Batwowowowoman lost a wheel"))

batRegex3 = re.compile(r'Bat(wo)+man')
# \+ match 1 or more times in order to match this pattern
mo5 = batRegex3.search("The Adventures of Batman")
try:
    print(mo5.group())
except:
    print("No match")
mo6 = batRegex3.search("The Adventures of Batwoman")
print(mo6.group())
print(batRegex3.search("Batwowowowoman lost a wheel"))

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))
regex2 = re.compile(r'(\+\*\?)+')
print(regex2.search('I learned about +*?+*?+*?+*?+*? regex syntax'))

haRegex = re.compile(r'(Ha){3}')
# {x} matches x amount of times in order to match this pattern
print(haRegex.search('HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa'))

phoneRegex2 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex2.search('My numbers are 415-555-1234,555-1234,215-555-0000'))

haRegex2 = re.compile(r'(Ha){3,5}')
print(haRegex2.search('HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa'))
# {x,y} matches a range of values in order to match this pattern

digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('123456789'))
# regular expression will match the maximum/longest possible string (greedy match)
digitRegex2 = re.compile(r'(\d){3,5}?')
# adding the \? will perform a non-greedy match (smallest possible string)
print(digitRegex2.search('123456789'))
# you can leave out the '3' or '5' to say that there is no minimum/maximum length