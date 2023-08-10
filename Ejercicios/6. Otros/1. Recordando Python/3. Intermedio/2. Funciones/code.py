# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

str = input("Introduce un texto con diversas palabras: ")

def create_dic(str):
    dic = dict()
    
    list = str.split(" ")
    
    for element in list:
        dic[element] = list.count(element)
    
    return dic


def common_word(dic):
    keys = []
    values = []
    for key,value in dic.items():
        keys.append(key)
        values.append(value)

    nmax = max(values)
    keymax = keys[values.index(nmax)]
    return keymax,nmax

word, ntimes = common_word(create_dic(str))

print(f"""La palabra que más se repite es "{word}" un total de {ntimes} veces.""")