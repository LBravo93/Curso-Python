def voto(ano):
    
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos: Opcional!'
    elif idade >= 18 and idade <= 65:
        return f'Com {idade} anos: Voto obrigatório!'
    elif idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    

        
nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))