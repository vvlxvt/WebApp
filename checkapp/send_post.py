import requests

url = "http://127.0.0.1:5000/get_form"
data = {
    "email": "user@example.com",
    "phone": "+75556661122",
    # "date": "2022-12-12",
    # "bill": "total 210.3$",
}

response = requests.post(url, data=data)
print("Status Code:", response.status_code)  # Выводим код ответа

if response.status_code == 200:  # Проверяем успешный код ответа
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Server returned non-JSON response:", response.text)
else:
    print("Error:", response.status_code, response.text)