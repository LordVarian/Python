import re

phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneRegex.findall("415-555-5555, 415-555-9999, or 415-555-5555"))
# when searching for zero or one groups, findall will return a list of strings

phoneRegex2 = re.compile(r'((\d{3})-(\d{3}-\d{4}))')
print(phoneRegex2.findall("415-555-5555, 415-555-9999, or 415-555-5555"))
# when there are groups, findall will return a list of tuples of strings

# character classes
# \d - any numberic digit from 0 to 9
# \D - any character that is not a numberic digit from 0 to 9
# \w - any letter, numeric digit, or the underscore character. 
# (Think of this as matching "word" characters)
# \W - any character that is not a letter, numeric digit, or the underscore character. 
# \s any space, tab, or newline character. (Think of this as matching "whitespace" characters)
# \S any character that is not a space, tab, or newline character.

lyrics = '''On the first day of Christmas,
my true love gave to me
A partridge in a pear tree.
On the second day of Christmas,
my true love gave to me
2 turtle doves,
And a partridge in a pear tree.
On the third day of Christmas,
my true love gave to me
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the fourth day of Christmas,
my true love gave to me
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the fifth day of Christmas,
my true love gave to me
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the sixth day of Christmas,
my true love gave to me
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the seventh day of Christmas,
my true love gave to me
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the eighth day of Christmas,
my true love gave to me
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the ninth day of Christmas,
my true love gave to me
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the tenth day of Christmas,
my true love gave to me
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the eleventh day of Christmas,
my true love gave to me
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree.
On the twelfth day of Christmas,
my true love gave to me
12 drummers drumming,
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves,
And a partridge in a pear tree!'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# you can also make your own character classes using []

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food and drinks'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food and drinks'))

# you can also make a negative character class by add the ^ caret symbol to the start of the pattern
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food and drinks'))