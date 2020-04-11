import requests 

val1 = input("First Letter: ")
val2 = input("Second Letter: ")
 
response = requests.get(
    'http://127.0.0.1:5000/test',
    params={'val1': val1, 'val2' : val2},
)

print(response.content)