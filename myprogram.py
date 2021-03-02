# Use the Request library
import requests
# Set the target webpage
url = "http://172.18.58.238/headers.php" #change to sch ip /headers.php
r = requests.get(url)
# This will get the full page
#print(r.text)
h = requests.head(url)
headers = {
    'User-Agent' : "Mobile"
}
# This will get the status code
if (r.status_code == 200):
    print("Status Code " + str(r.status_code) + " OK")
    for x in h.headers:
        print("\t ", x, ":", h.headers[x])SS
    getRequest = requests.get(url, headers=headers)
    print(getRequest.text)
else:
    print("error")

# This will just get just the headers


#print("Header:")
#print("**********")
# To print line by line\
'''
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
'''

# This will modify the headers user-agent

# Test it on an external site
'''

rh = requests.get(url2, headers=headers)
print(rh.text)
'''

