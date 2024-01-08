def isPhoneNumber(text): # 415-555-
    if (len(text) != 12):
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # no hyphen
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no exchange code
    if text[7]!= '-':
        return False # no hyphen
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # no phone number
    return True # phone number-sized

message = "Call me at 415-555-5555 tomorrow, or at 415-555-9999 for my office line"
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find a phone number")
    
print(isPhoneNumber("415-555-5555"))