import re
import urllib.request

username_input = input("Insert username here (Just username, no complete URL):")
firstUrl = 'https://www.instagram.com/' + username_input + '/?__a=1'
pageSource = urllib.request.urlopen(firstUrl)
pageStr = pageSource.read()

result = re.search('profilePage_(.*)","show' , pageStr)
username_id = result.group(1)

secondUrl = 'https://i.instagram.com/api/v1/users/'+ username_id +'/info/'
pageSource_second = urllib.request.urlopen(secondUrl)
pageStr_second = pageSource_second.read()


findurl = re.search('"hd_profile_pic_url_info":(.*)}' , pageStr_second)
urlWithInfo = findurl.group(1)

# extracting raw url from bracketed url (urlWithInfo) [Update : failed]
findurl2 = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', urlWithInfo)
print(findurl2)



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print('First url:  '  + firstUrl)
print('ID:' + str(username_id))
print("Second url:  " + secondUrl)
print('')

print('')
print('')
print('')

print(color.BOLD + "Copy the following URL and paste it into your web browser:" + color.END)
print(urlWithInfo)


