import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# Show all h2 tag
for heading in soup.find_all("h2"):
    print(heading.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : 'foo',
#     "body" : 'bar',
#     "userId" : 1,
# }
# headers = {
#     'Content-type' : 'application/json; charset=UTF-8',}

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

