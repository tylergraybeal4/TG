import requests

url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":"eldersburg,MD"}

headers = {
	"X-RapidAPI-Key": "a4252eb27amsh8f96714dade185ap16b7b0jsnb837dbd0f8d4",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())