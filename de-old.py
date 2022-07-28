import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('images/wedding_square.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
