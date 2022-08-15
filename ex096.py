def notas (*n, sit=False):
    r=dict()
    r['total']= len(n)
    r['maior']= max(n)
    r['menor']= min(n)
    r['media']= sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        if r['media'] <5:
            r['situação']= 'ruim'
    return r

resp=notas(5.9,7,9.8,sit=True)
print(resp)
