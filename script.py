import rows

### importando os dados

horas = rows.import_from_csv(input('nome do arquivo .csv: '))

### Calculando a quantidade de horas trabalhadas
users = []
resultados = []

for row in horas:
    if row.user not in users:
        users.append(row.user)

for user in users:
    fds = duteis = 0
    for row in horas:
         if row.user==user:
             print (row.user,row.task,row.date,row.hours)
             if row.task==('Fds e Feriados'):
                 fds += row.hours
             if row.task==('Dias úteis'):
                 duteis += row.hours
    resultados += [{'nome': user,'duteis': duteis,'fds': fds}]

for i in resultados:
    print ('%s \t %d \t %d' %(i.get('nome'),i.get('duteis'),i.get('fds')))
