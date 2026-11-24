enderecos_usuarios = ["Beco do batman", "Rua leonida, 56", "Mansão Wayne, Gotham", "Anhanguera, SP"]

def ordenar_enderecos(locais):
    if(locais):
        locais.sort()
        return locais
    else:
        return "Não há endereco"

enderecos_organizados = ordenar_enderecos(enderecos_usuarios)

for i in enderecos_organizados:
    print(i)
    