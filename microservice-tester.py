import requests

def test_add_adjective():
    url = 'http://127.0.0.1:5000/addAdjective'
    item = {
        "itemName": "Potion"
    }
    response = requests.post(url, json=item)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    test_add_adjective()
