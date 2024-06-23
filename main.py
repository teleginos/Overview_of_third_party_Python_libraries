import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image

get_number = int(input('''1. Библиотека request
2. Библиотека numpy
3. Библиотека matplotlib
4. Библиотека pandas
5. Библиотека pillow
Выберите демонстрацию какой библиотеки запустить: '''))

match get_number:
    case 1:
        print("""Использование библиотеки request с библиотекой BeautifulSoup 
для получения погоды с сервиса Yandex в городе Москва\n""")

        response = requests.get('https://yandex.ru/pogoda/moscow')
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        links = soup.find_all('a', class_='text')

        for link in links:
            link = [x.replace(',', '') for x in link.get('aria-label').split()]
            for element in range(len(link)):
                if link[element] == 'вчера':
                    break
                elif element == 3 or link[element] in ('днём', 'ночью'):
                    print()
                print(link[element], end=' ')
            print('\n')
    case 2:
        print("Использование библиотеки numpy\n")

        # Создание массива
        array = np.array([1, 2, 3, 4, 5])

        # Выполнение математических операций
        array_squared = array ** 2
        array_sum = np.sum(array)

        print("Массив:", array)
        print("Квадраты элементов массива:", array_squared)
        print("Сумма элементов массива:", array_sum)

    case 3:
        print("Использование библиотеки matplotlib")

        # Данные для графика
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Создание графика
        plt.plot(x, y, label='sin(x)')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.title('График функции sin(x)')
        plt.legend()
        plt.show()

    case 4:
        print("Использование библиотеки pandas")
        # Считывание данных из CSV файла
        data = pd.read_csv('sales_data.csv')

        # Вывод первых пяти строк данных
        print("Первые пять строк данных:")
        print(data.head())

        # Рассчет общих продаж для каждого продукта
        total_sales = data.groupby('Product')['Sales'].sum()
        print("\nОбщие продажи для каждого продукта:")
        print(total_sales)

        # Рассчет среднего уровня продаж для каждого продукта
        average_sales = data.groupby('Product')['Sales'].mean()
        print("\nСредний уровень продаж для каждого продукта:")
        print(average_sales)

        # Фильтрация данных: продажи выше 150
        filtered_data = data[data['Sales'] > 150]
        print("\nПродажи выше 150:")
        print(filtered_data)

    case 5:
        print("Использование библиотеки pillow")

        # Открытие изображения
        image = Image.open('Image.jpg')

        # Изменение размера изображения
        resized_image = image.resize((5200, 3467))

        # Применение эффекта черно-белого фильтра
        bw_image = resized_image.convert('L')

        # Сохранение обработанного изображения
        bw_image.save('resized_bw_image.png')

        print("Изображение успешно обработано и сохранено.")
