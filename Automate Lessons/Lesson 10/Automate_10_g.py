import re

beginsWithHelloRegex = re.compile(r'^Hello')
# you can also use the caret ^ symbol at the beggining of a regular expression to ensure that 
# the match is at the beginning of the searched text
print(beginsWithHelloRegex.search('Hello there'))
print(beginsWithHelloRegex.search('He said "Hello there!"') == None)
# you can also put a $ dollar sign at the end of a regular expression to ensure that the match 
# is at the end of the searched text
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
# you can use both to indicate that the pattern must match the entire string
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('123456789'))
print(allDigitsRegex.search('12345x6789') == None) 

# . in your regular expression will match any single character except a new line
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

# common thing is the .* pattern, which will match any pattern (Note that .* is greedy and
# will match as many characters as possible)

'First Name: James Last Name: Metke'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: James Last Name: Metke'))

# in order to get the non-greedy match, you need to use the .*? pattern

serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(r'<.*?>')
print(nonGreedy.search(serve))
greedy = re.compile(r'<.*>')
print(greedy.search(serve))

prime = 'Service the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
# matches until the new line
dotStar2 = re.compile(r'.*', re.DOTALL)
print(dotStar2.search(prime))
# This will match all the characters in the string including the new line character 

vowelRegex = re.compile(r'[aeiou]', re.I)
# re.I or re.IGNORECASE will be case insensitive
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))