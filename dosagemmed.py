print('Remédios disponíveis:')
print('[ 1 ] ASPIRINA \
    [ 2 ] BRUFEN \
    [ 3 ] TYLENOL')
while True:
    remedio = int(input('Qual é a opção escolhida? '))
    if remedio <=3:
        peso = int(input('Qual é o seu peso? '))

        if remedio == 1:
            if peso <= 50:
                print(f'A medicação solicitada é ASPIRINA, e de acordo com o seu peso, a dosagem \
adequada é de 100mcg.')
            elif peso >= 51  and peso <= 70:
                print(f'A medicação solicitada é ASPIRINA, e de acordo com o seu peso, a dosagem \
adequada é de 150mcg.')
            elif peso >= 71:
                print(f'A medicação solicitada é ASPIRINA, e de acordo com o seu peso, a dosagem \
adequada é de 200mcg.')
        
        elif remedio == 2:
            if peso <= 50:
                print(f'A medicação solicitada é BRUFEN, e de acordo com o seu peso, a dosagem \
adequada é de 100mcg.')
            elif peso >= 51  and peso <= 70:
                print(f'A medicação solicitada é BRUFEN, e de acordo com o seu peso, a dosagem \
adequada é de 150mcg.')
            elif peso >= 71:
                print(f'A medicação solicitada é BRUFEN, e de acordo com o seu peso, a dosagem \
adequada é de 200mcg.')
    
        elif remedio == 3:
            if peso <= 50:
                print(f'A medicação solicitada é TYLENOL, e de acordo com o seu peso, a dosagem \
adequada é de 100mcg.')
            elif peso >= 51  and peso <= 70:
                print(f'A medicação solicitada é TYLENOL, e de acordo com o seu peso, a dosagem \
adequada é de 150mcg.')
            elif peso >= 71:
                print(f'A medicação solicitada é TYLENOL, e de acordo com o seu peso, a dosagem \
adequada é de 200mcg.')

        break
    else:
        print('Opção incorreta. Escolha novamente.')


