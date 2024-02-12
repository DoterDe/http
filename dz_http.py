from bs4 import BeautifulSoup
import requests

base_url = 'https://books.toscrape.com/'
url = 'https://books.toscrape.com/catalogue/category/books/science_22/index.html'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

url1='https://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_938/index.html'
recuest= requests.get(url1)
html1 = recuest.text
soup1 = BeautifulSoup(html1, 'html.parser')
des1= soup1.find_all('p')
description = [i for i in (des1)]

url2='https://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html'
recuest= requests.get(url2)
html2 = recuest.text
soup2 = BeautifulSoup(html2, 'html.parser')
des2= soup2.find_all('p')
description2 = [i for i in (des2)]

url3='https://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html'
recuest= requests.get(url3)
html3 = recuest.text
soup3 = BeautifulSoup(html3, 'html.parser')
des3= soup3.find_all('p')
description3 = [i for i in (des3)]

url4='https://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html'
recuest= requests.get(url4)
html4 = recuest.text
soup4 = BeautifulSoup(html4, 'html.parser')
des4= soup4.find_all('p')
description4 = [i for i in (des4)]


url5='https://books.toscrape.com/catalogue/the-fabric-of-the-cosmos-space-time-and-the-texture-of-reality_572/index.html'
recuest= requests.get(url5)
html5 = recuest.text
soup5 = BeautifulSoup(html5, 'html.parser')
des5= soup5.find_all('p')
description5 = [i for i in (des5)]


url6='https://books.toscrape.com/catalogue/diary-of-a-citizen-scientist-chasing-tiger-beetles-and-other-new-ways-of-engaging-the-world_517/index.html'
recuest= requests.get(url6)
html6 = recuest.text
soup6 = BeautifulSoup(html6, 'html.parser')
des6= soup6.find_all('p')
description6 = [i for i in (des6)]


url7='https://books.toscrape.com/catalogue/the-origin-of-species_499/index.html'
recuest= requests.get(url7)
html7 = recuest.text
soup7 = BeautifulSoup(html7, 'html.parser')
des7= soup7.find_all('p')
description7 = [i for i in (des7)]


url8='https://books.toscrape.com/catalogue/the-grand-design_405/index.html'
recuest= requests.get(url8)
html8 = recuest.text
soup8 = BeautifulSoup(html8, 'html.parser')
des8= soup8.find_all('p')
description8 = [i for i in (des8)]

url9='https://books.toscrape.com/catalogue/peak-secrets-from-the-new-science-of-expertise_389/index.html'
recuest= requests.get(url9)
html9 = recuest.text
soup9 = BeautifulSoup(html9, 'html.parser')
des9= soup9.find_all('p')
description9 = [i for i in (des9)]


url10='https://books.toscrape.com/catalogue/the-elegant-universe-superstrings-hidden-dimensions-and-the-quest-for-the-ultimate-theory_245/index.html'
recuest= requests.get(url10)
html10 = recuest.text
soup10 = BeautifulSoup(html10, 'html.parser')
des10= soup10.find_all('p')
description10 = [i for i in (des10)]

url11='https://books.toscrape.com/catalogue/the-disappearing-spoon-and-other-true-tales-of-madness-love-and-the-history-of-the-world-from-the-periodic-table-of-the-elements_244/index.html'
recuest= requests.get(url11)
html11 = recuest.text
soup11 = BeautifulSoup(html11, 'html.parser')
des11= soup11.find_all('p')
description11 = [i for i in (des11)]

url12='https://books.toscrape.com/catalogue/surely-youre-joking-mr-feynman-adventures-of-a-curious-character_227/index.html'
recuest= requests.get(url12)
html12 = recuest.text
soup12 = BeautifulSoup(html12, 'html.parser')
des12= soup12.find_all('p')
description12 = [i for i in (des12)]


url13='https://books.toscrape.com/catalogue/seven-brief-lessons-on-physics_219/index.html'
recuest= requests.get(url13)
html13 = recuest.text
soup13 = BeautifulSoup(html13, 'html.parser')
des13= soup13.find_all('p')
description13 = [i for i in (des13)]


url14='https://books.toscrape.com/catalogue/the-selfish-gene_81/index.html'
recuest= requests.get(url14)
html14 = recuest.text
soup14 = BeautifulSoup(html14, 'html.parser')
des14= soup14.find_all('p')
description14 = [i for i in (des14)]



names = soup.find_all('h3')
prices = soup.find_all('p', class_='price_color')
imgs = soup.find_all('img', class_='thumbnail')
print(' Какую книгу желаете приобрести?  ')
for index,i in enumerate(names):
    print(f"{index+1}){names[index].text}")
choice= int(input())
choice1=[i for i in (names)]
price = [i for i in (prices)]
img = [base_url + i.get('src').replace('../', '') for i in (imgs)]

    # print(f"{index+1}){names[index].text}")
if choice == 1 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название: {choice1[0].text}')
    print(f'Цена: {price[0].text}')
    print(f'Картинка: {img[0]}')
    print(f'Описание: {description[3]}')

if choice == 2 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[1].text}')
    print(f'Цена:{price[1].text}')
    print(f'Картинка: {img[1]}')
    print(f'Описание: {description2[3]}')
if choice == 3 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[2].text}')
    print(f'Цена:{price[2].text}')
    print(f'Картинка: {img[2]}')
    print(f'Описание: {description3[3]}')
if choice == 4 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[3].text}')
    print(f'Цена:{price[3].text}')
    print(f'Картинка: {img[3]}')
    print(f'Описание: {description4[3]}')
if choice == 5 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[4].text}')
    print(f'Цена:{price[4].text}')
    print(f'Картинка: {img[4]}')
    print(f'Описание: {description5[3]}')
if choice == 6 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[5].text}')
    print(f'Цена:{price[5].text}')
    print(f'Картинка: {img[5]}')
    print(f'Описание: {description6[3]}')
if choice == 7 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[6].text}')
    print(f'Цена:{price[6].text}')
    print(f'Картинка: {img[6]}')
    print(f'Описание: {description7[3]}')
if choice == 8 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[7].text}')
    print(f'Цена:{price[7].text}')
    print(f'Картинка: {img[7]}')
    print(f'Описание: {description8[3]}')
if choice == 9 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[8].text}')
    print(f'Цена:{price[8].text}')
    print(f'Картинка: {img[8]}')
    print(f'Описание: {description9[3]}')
if choice == 10 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[9].text}')
    print(f'Цена:{price[9].text}')
    print(f'Картинка: {img[9]}')
    print(f'Описание: {description10[3]}')
if choice == 11 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[10].text}')
    print(f'Цена:{price[10].text}')
    print(f'Картинка: {img[10]}')
    print(f'Описание: {description11[3]}')
if choice == 12 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[11].text}')
    print(f'Цена:{price[11].text}')
    print(f'Картинка: {img[11]}')
    print(f'Описание: {description12[3]}')
if choice == 13 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[12].text}')
    print(f'Цена:{price[12].text}')
    print(f'Картинка: {img[12]}')
    print(f'Описание: {description13[3]}')
if choice == 14 :
    print('Хорошо! Вот данные об этой книге')
    print(f'Название:{choice1[13].text}')
    print(f'Цена:{price[13].text}')
    print(f'Картинка: {img[13]}')
    print(f'Описание: {description14[3]}')
    # print(base_url + i.get('src').replace('../', ''))

