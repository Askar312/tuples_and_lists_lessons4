names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
i = 0
while i<5:
    if i % 2 == 0:
        names.pop(i)
    if i % 2 == 1:
        names.pop(i)
    i+=1
print(names)
