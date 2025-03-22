motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati' #make in list changes
print(motorcycle)

motorcycle.append('bmw'.upper())
print(motorcycle)

motorcycle = []
motorcycle.append('opel')
motorcycle.append('reno')
motorcycle.append('fiat')

print(motorcycle)

motorcycle.insert(0, 'honda')
print(motorcycle)

del motorcycle[2]
print(motorcycle)

del motorcycle[1]
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

popped_motorcycle = motorcycle.pop(0)
print(motorcycle)
print(popped_motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycle.pop()
print(f'The last motorcycle I owned {last_owned.title()}')
