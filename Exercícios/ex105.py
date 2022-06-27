def notas(*n, aprov=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if aprov:
        if r['média'] > 6:
            r['Situação'] = 'Aprovado'
        else:
            r['Situação'] = 'Reprovado'
    return r


resp = notas( 5.5, 2.5, 8.5, aprov=True)
print(resp)