# Regular Expressions for specifying text patterns

import re, pprint

message = "Call me at 415-555-5555 tomorrow, or at 415-555-9999 for my office line"

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search(message)
print(mo.group())

mo_all = phoneNumRegex.findall(message)
pprint.pprint(mo_all)