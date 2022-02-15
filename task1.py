


from os import system


def dostat_iz_stroki_elementi(str, delim):
    elements = []
    element = ""
    for c in str:
        if c != delim:
            element = element + c
        else: 
            if len(element)==0:
                continue
            elements.append(element) 
            element = ""

    if len(element)>0:
        elements.append(element)
    return elements


class NonNumericError(Exception):
 pass

class InconsistentDataError(Exception):
 pass

a_input = input("Введите первые катеты треугольников: ")
b_input = input("Введите вторые катеты треугольников: ")

a_input_list = dostat_iz_stroki_elementi(a_input, " ")
# print(a_input_list)

b_input_list = dostat_iz_stroki_elementi(b_input, " ")
# print(b_input_list)

a = []
for s in a_input_list:
    try:
       d = int(s)
       a.append(d)
    except:
        print("Неправильные входные данные", s)
        raise NonNumericError

b = []
for s in b_input_list:
    d = int(s)
    b.append(d)

if len(a)!=len(b):
    print("Количество катетов не совпадает")
    raise InconsistentDataError


n = len(a)
for i in range(0,n,1):
    s = a[i]*b[i]/2
    hyp = (a[i]**2 + b[i]**2)**0.5
    print("Треугольник ",i+1," с катетами", a[i], "и" ,b[i], "имеет площадь",s, "и гипотенузу", hyp)
    

ab_input = input("Введите  катеты : ")




ab_input_list = dostat_iz_stroki_elementi(ab_input, " ")
# print(ab_input_list)

ab=[]
for f in ab_input_list:
    try:
        d = int(f)
        ab.append(d)   
    except:
        print("Неправильные входные данные", f)
        raise NonNumericError

a_1=[]
b_1 =[]
for i in range(0,len(ab)-1,2):
    a_1.append(ab[i])
    b_1.append(ab[i+1])
    
# print(a_1)
# print(b_1)
 
if len(a_1) != len(b_1):
    print("Количество катетов не совпадает")
    raise InconsistentDataError

n = len(a_1)
for i in range(0,n,1):
    s_1 = a_1[i]*b_1[i]/2
    hyp_1 = (a_1[i]**2 + b_1[i]**2)**0.5
    print("Треугольник ",i+1," с катетами", a_1[i], "и" ,b_1[i], "имеет площадь",s_1, "и гипотенузу", hyp_1)
  

   

        



 

      

    

   



   

























# if a and b 
# S1 = int((a*b)/2)
# 
# print ("Треугольник 1 с катетами (a1, ...a*n) и (b1, ...a*n) имеет площадь (S1,) и гипотенузой (c1) ")
# print("Треугольник 2 с катетами (a2) и (b2) имеет площадь (S1) и гипотенузой (c2) "
