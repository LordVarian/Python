import requests

res = requests.get('https://folger-main-site-assets.s3.amazonaws.com/uploads/2022/11/romeo-and-juliet_TXT_FolgerShakespeare.txt')
print(res.status_code)
print(len(res.text))
res.raise_for_status()
# badRes = requests.get('https://automatetheboringstuff.com/files/rj.text')
# badRes.raise_for_status() 
# stop the program if an unexpected error occurs
playFile = open('RomeoAndJuliet.txt', 'wb')
# use 'wb' to write to a binary file to maintain the unicode encoding
for chunk in res.iter_content(100000):
# iter_content() returns a generator object that yields chunks of data of the bytes data type
    playFile.write(chunk)
    playFile.close()
    
