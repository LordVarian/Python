import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob'))
# sub will find and replace the matched text with the regular expression. 
# the first argument is the text to replace
namesRegex2 = re.compile(r'Agent (\w)\w*')
print(namesRegex2.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex2.sub('Agent \1****','Agent Alice gave the secret documents to Agent Bob'))
# \1 will use the text from group 1 to replace the matched text with the regular expression. 

re.compile(r'''
           (\d{3}-)|    # area code (without parentheses, with dash)
           (\(\d{3}) )  # -or- area code with parens and no dash
           \d{3}        # first 3 digits
           -            # second dash
           \d{4}        # last 4 digits
           \sx\d{2,4}   # extension, like x1234
           ''', re.I | re.DOTALL | re.VERBOSE) # if you want to pass multiple arguments, combine 
                                               # them with the | bitwise operator