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
                resultado = resultado + campos[contador] + " like '%" + data[campos[contador]]+ "%' "
            else:
                resultado = resultado + campos[contador] + " like '%"+ data[campos[contador]] + "%' and "
        contador = contador + 1

    return resultado
        