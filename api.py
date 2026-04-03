import requests

params ={
  'q':'kigali',
  'appid':' '
}
response = requests.get("https://official-joke-api.appspot.com/random_joke")
if response.status_code == 200:
  data = response.json()
  print(data)
  print(data["setup"])
  print(data["punchline"])


else:
  print(f"something has gone wrong!😒:{response.status_code}")  
