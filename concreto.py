larg = float(input("Digite a largura: "))
comp = float(input("Digite o comprimento: "))

area = larg * comp

tipoTrafego = {
    "leve": 10,
    "moderado": 15,
    "pesado": 20
}

trafego = input(
    'Digite o tipo de tráfego : Leve/Moderado/Pesado: '
).lower().strip()

escolhas = ['leve', 'moderado', 'pesado']

while trafego not in escolhas:
    print('Opção inválida!')

    trafego = input(
        'Digite o tipo de tráfego : Leve/Moderado/Pesado: '
    ).lower().strip()


espessura = tipoTrafego[trafego]

consumoConcreto = area * (espessura / 100)


tipoMalha = {
    'leve': 'Q138',
    'moderado': 'Q138',
    'pesado': 'Q196',
    'especial': 'Q283'
}


tipoTrelica = {
    'leve': 'Sem treliça',
    'moderado': 'TR10',
    'pesado': 'TR12'
}


malha = tipoMalha[trafego]
trelica = tipoTrelica[trafego]


print('\n--- RESULTADO ---')

print(f'Área: {area:.2f} m²')
print(f'Tráfego: {trafego.title()}')
print(f'Espessura: {espessura} cm')
print(f'Volume de concreto: {consumoConcreto:.2f} m³')
print(f'Malha: {malha}')
print(f'Treliça: {trelica}')
