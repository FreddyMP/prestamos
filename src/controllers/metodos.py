def search_keys(campos, data):
    lista = {}
    resultado = ''
    conteo = len(campos)

    contador = 0
    while contador < conteo:
        if campos[contador] in data:
            lista[campos[contador]] = data[campos[contador]]
        else:
            resultado = {"resultado":f"No se encontro el campo '{campos[contador]}' en el json"}
        contador = contador + 1

    if resultado =='':
        return ['1',lista]
    else:
        return ['0',resultado]


def find(campos, data):
    resultado = ''
    conteo = len(campos)

    contador = 0
    while contador < conteo:
        if campos[contador] != "cliente":
            if contador + 1 == conteo:
                if campos[contador] != "id":
                    resultado = resultado + campos[contador] + " like '%" + data[campos[contador]]+ "%' "
                else:
                    resultado = resultado + campos[contador] + " = '" + data[campos[contador]]+ "' "
            else:
                if campos[contador] != "id":
                    resultado = resultado + campos[contador] + " like '%"+ data[campos[contador]] + "%' and "
                else:
                    resultado = resultado + campos[contador] + " = '"+ data[campos[contador]] + "' and " 
        contador = contador + 1

    return resultado
        
def not_empty(campos, data):
    lista = {}
    resultado = ''
    conteo = len(campos)

    contador = 0
    while contador < conteo:
        if campos[contador] in data:
            if data[campos[contador]] == '':
                resultado = {"resultado":f"El campo '{campos[contador]}' no puede estar vacio"}
        contador = contador + 1

    if resultado =='':
        return ['1']
    else:
        return ['0',resultado]