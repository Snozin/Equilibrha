import csv

male = 0
female = 0
total_salary = 0
counted_employees = []

with open('data.csv','r') as data:
    csv_reader  = csv.reader(data, delimiter=';')
    for value in csv_reader:
        if value[4] == 'H':
            male += 1
        
        if value[4] == 'M':
            female += 1
        
        if value[8] == 'Equilibrha IT' and value[9] == 'CT2':
            total_salary += int(value[6])
        
        if value[8] == 'Equilibrha RRHH' and int(value[6]) >= 28000:
            aux = value[0], value[1], value[2], value[6], value[8]
            counted_employees.append(aux)
            
# Mostrar total de empleados, mujeres y hombres
print('total de empleados: ', male + female)
print('total mujeres: ', female)
print('total hombres: ', male, '\n')

# Mostrar salario bruto empleados Equilibra IT + CT2
print('total salario bruto: ', total_salary, '\n')

# Mostrar datos empleados empresa Equilibra RRHH, salario > 28000
for employee in counted_employees:
    print('{id} {name} {surname} {salary} {company}'.format(
        id = employee[0], name = employee[1], surname = employee[2], salary = employee[3], company = employee[4]))
