import requests
from bs4 import BeautifulSoup

# вывод текста поздравлений с сайта
url = "https://pozdravok.com/pozdravleniya/den-rozhdeniya/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        greetings = soup.find_all(class_="sfst")
        for index, greeting in enumerate(greetings, 1):
            print(f"Поздравление {index}:\n{greeting.get_text(strip=True)}\n")

    else:
        print(f"Ошибка: не удалось загрузить страницу. Код ответа: {response.status_code}")

except requests.RequestException as e:
    print(f"Произошла ошибка: {e}")
