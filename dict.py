dict1={'disciplina':'Limba Romana','note':[9,9,10,10],'teza':10}
dict2={'disciplina':'Limba Engleza','note':[9,9,9,9],'teza':10}
dict3={'disciplina':'Matematica','note':[8,8,9,9],'teza':9}

a=dict1['teza']
if a<5:
    print('restanta')
b=dict2['teza']
if b<5:
    print('restanta')
c=dict3['teza']
if c<5:
    print('restanta')

a=(((sum(dict1['note'])/4)+dict1['teza'])/2)
print(a)
b=(((sum(dict2['note'])/4)+dict2['teza'])/2)
print(b)
c=(((sum(dict3['note'])/4)+dict3['teza'])/2)
print(c)

if (a>9):
    print('eminent')
if (a>8) and (a<9):
    print('proeminent')
if (a<8):
    print('codas')

if (b>9):
    print('eminent')
if (b>8) and (b<9):
    print('proeminent')
if (b<8):
    print('codas')

if (c>9):
    print('eminent')
if (c>8) and (c<9):
    print('proeminent')
if (c<8):
    print('codas')




