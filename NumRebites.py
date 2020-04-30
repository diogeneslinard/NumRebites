# A Figura 1 mostra uma junta de sobreposição rebitada, com rebites feito de aço SAE 1010 e diâmetro de 10 mm cada. 
# Os elementos são feitos de aço SAE 1020 estirados a frio, largura das chapas de 0,5 m e espessuras de 20 mm. 
# Admita um passo para uma boa vedação, um espaçamento entre a borda e o rebite mais próximo de pelo menos uma vez e meia o diâmetro do rebite.
# Encontre a carga F (em N) que pode ser aplicada a essa conexão que provê um fator de segurança mínimo igual a 2 para os seguintes 
# modos de falha: cisalhamento dos rebites, esmagamento dos rebites e cisalhamento da chapa.

# Dados
d_reb = 10           # [mm] Dado de entrada, é necessário editar
largura_chapa = 500 
P = 2.5*d_reb
l = 20;               # espessura das chapas [mm]
l_ext = 2*d_reb       # espaço de sobra do rebite a parte extrema da chapa [mm] Um mínimo de material entre a borda do furo e a aresta externa da peça é um diâmetro do pino e serve como ponto de partida razoável para seus cálculos de projeto.
n = 2                 # Coeficiente de segurança

N_reb = round((largura_chapa - 2*l_ext + P)/P);  # Número de rebites

print('~'*25)
print(f'Número de rebites é {N_reb}.')
print('~'*25)
Sy_reb = Sy_chapa = 180

while True:
    material_rebite  = str(input('Digite o material do rebite [ex. 1020HR, 1010CD, etc.]: ')).upper()[0]                    # 1 - 1010 HR; 2- 1010 CD; 3 - 1020 HR; 4 - 1020 CD; 5 - ferro fundido; 6 - cobre;
    
    if material_rebite == '1010HR':
        Sy_reb == 180
    elif material_rebite == '1010CD':
        Sy_reb == 300
    elif material_rebite == '1020HR':
        Sy_reb == 210
    elif material_rebite == '1020CD':
        Sy_reb == 390
    elif material_rebite == 'ferro fundido':
        Sy_reb == 165
    elif material_rebite == 'cobre':
        Sy_reb == 27

    material_chapa  = str(input('Digite o material da chapa [ex. 1020HR, 1010CD, etc.]: ')).upper()[0]                    # 1 - 1010 HR; 2- 1010 CD; 3 - 1020 HR; 4 - 1020 CD; 5 - ferro fundido; 6 - cobre;
    
    if material_chapa == '1010HR':
        Sy_chapa == 180
    elif material_chapa == '1010CD':
        Sy_chapa == 300
    elif material_chapa == '1020HR':
        Sy_chapa == 210
    elif material_chapa == '1020CD':
        Sy_chapa == 390
    elif material_chapa == 'ferro fundido':
        Sy_chapa == 165
    elif material_chapa == 'cobre':
        Sy_chapa == 27
   
    while True:
        if material_rebite in '102CDHRN':
            break
        print('ERRO! Responda apenas conforme a legenda.')
    if material_rebite == 'N':
        break 
    while True:
        if material_chapa in '102CDHRN':
            break
        print('ERRO! Responda apenas conforme a legenda.')
    if material_chapa == 'N':
        break 
    print(f'A resistência do material do rebite escolhida é de {Sy_reb} MPa.') 
    print(f'A resistência do material da chapa escolhida é de {Sy_chapa} MPa.') 

    Ssy_reb = 0.5*Sy_reb       #Tensão de cisalhamento do rebite
    Ssy_chapa = 0.5*Sy_chapa   #Tensão de cisalhamento da chapa    

    # Força devido ao cisalhamento dos rebites
    F_cis =  (N_reb*3.14*Ssy_reb*d_reb**2)/(4*n)

    # Força devido ao esmagamento dos rebites
    F_esm =  (N_reb*d_reb*l*Sy_reb)/n

    # Força devido ao cisalhamento da chapa
    F_cis_sup =  (N_reb*Ssy_chapa*2*l*l_ext)/n

    # Força mínima 
    print(f'Força devido ao esmagamento dos rebites: {F_esm} N \n ')
    print(f'Força devido ao cisalhamento dos rebites: {F_cis} N\n ')
    print(f'Força devido ao esmagamento dos rebites: {F_cis_sup} N\n ')

    F_min = min([F_esm,F_cis,F_cis_sup])
    print(f'Força mínima: {F_min} N\n ')


