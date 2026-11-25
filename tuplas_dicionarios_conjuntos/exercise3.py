def retornar_valores(valor):

    quantidade_valores = len(valor)
    min_valor = min(valor)

    return quantidade_valores, min_valor

numeros_usuario = [50, 100, 20, 90, 200]
consulta_dados = retornar_valores(numeros_usuario)

print(consulta_dados)
print(type(consulta_dados))
