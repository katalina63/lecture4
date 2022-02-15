from itertools import count
from operator import ge
from this import d
from typing import OrderedDict
from unicodedata import name


persons = [
    {
         "name": "Lena",
         "age": 16,
         "gender": "female"

     }, {
        "name": "Petr",
        "age": 20,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 20,
         "gender": "female"
     },{
         "name": "Lena",
         "age": 16,
         "gender": "female"

     }, {

        "name": "Petr",
        "age": 37,
        "gender": "male"
     }, {
         "name": "Yana",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 20,
         "gender": "female"
     }, {
         "name": "Lena",
         "age": 22,
         "gender": "female"

     }, {

        "name": "Frol",
        "age": 20,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Natasha",
         "age": 20,
         "gender": "female"
     },{  
        "name": "Maxim",
        "age": 20,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 37,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 18,
         "gender": "female"
     },{
         "name": "Lena",
         "age": 16,
         "gender": "female"

     }, {

        "name": "Petr",
        "age": 17,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 20,
         "gender": "female"
     }, {
         "name": "Paul",
         "age": 16,
         "gender": "male"
    }, {
        "name": "Farr",
        "age": 40,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 23,
         "gender": "female"
     }, {  "name": "Petr",
        "age": 20,
        "gender": "male"
     }, {
         "name": "Olya",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 20,
         "gender": "female"
     },{
         "name": "Nina",
         "age": 16,
         "gender": "female"

     }, {
        "name": "Ivan",
        "age": 20,
        "gender": "male"
     }, {
         "name": "Alice",
         "age": 27,
         "gender": "female" 
     }, {
         "name": "Kat",
         "age": 20,
         "gender": "female"
     }, {
         "name": "Lena",
         "age": 16,
         "gender": "female"

     }, {
        "name": "Petr",
        "age": 27,
        "gender": "male"
     }, {
         "name": "Maria",
         "age": 13,
         "gender": "female" 
     }, {
         "name": "Sofia",
         "age": 20,
         "gender": "female"
     }
]

# def get_first(pair):
#     return pair[0]


print(persons)

print ("Количество всех людей:",len(persons))

mx = 0
fx = 0
ag_1 =0

for item in persons:
    gender = item["gender"]
    if gender == "male":
        mx = mx + 1
    elif gender == "female":
        fx = fx + 1

    if item["age"] >= 18:
        ag_1 = ag_1 + 1
    
    
print("Сколько мужчин:", mx)
print("А сколько женщин:", fx)
print("Посчитайте сколько совершеннолетних персон:" , ag_1)

names = []
for item in persons:
   names.append(item["name"])
print("Список всех имен:", names)


ages = set()
for item in persons:
    age = item["age"]
    ages.add(age)

ordered_ages = sorted(ages)

ordered_ages = []
for age in ages:
    ordered_ages.append(age)

ordered_ages.sort()


print("Список всех возрастов:", ordered_ages)

men = []
for elem in persons:
   gender = elem ["gender"]
   name = elem ["name"]
   age = elem ["age"]
   if gender =="male" and age >= 35 and name[0]=='F':
         men.append(elem["name"])   
print("Вывести все имена мужчин старше 35 лет, имя которых начинается с F:",men)  

from collections import Counter
repet_names = Counter(names)
most_common_names = repet_names.most_common(3)



result = list(map(lambda x: x[0],most_common_names))
print(result)
print("3 самых встречаемых имен:",result)







