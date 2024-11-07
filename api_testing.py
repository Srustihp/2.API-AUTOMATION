import requests
url = "https://reqres.in/api/users?page=2"
#url = "https:hvkabch.com"
response = requests.get(url)
if response.status_code == 200:
    print("Test Passed: Status code is 200")
else:
    print(f"Test Failed: Expected status code 200, but got {response.status_code}")
