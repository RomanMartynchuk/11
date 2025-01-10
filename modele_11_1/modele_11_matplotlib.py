import matplotlib.pyplot as plt
import random
# визуализация графика изменения корса валюты
def exchange_rate(days):
    price = []
    day = []
    x = 0
    for i in range(1,days+1):
        height = random.randint(0,1)
        s = random.randint(0,20)
        day.append(i)
        if height == 0:
            x -= s
        else:
            x += s
        price.append(x)

    plt.plot(day, price)
    plt.title('exchange rate')
    plt.xlabel('day')
    plt.ylabel('price')
    plt.show()

exchange_rate(50)