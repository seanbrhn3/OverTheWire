import requests

hack_it = requests.get("http://natas9.natas.labs.overthewire.org/?needle=needle&submit=Search")
print(hack_it.text)
