my_dict = {'Kostya': 1996, 'Alina': 1994, 'Ira': 1986}
print(my_dict)
print(my_dict.get('Kostya'))
print(my_dict.get('Kostya1'))
my_dict.update({'Anna': 1997,
                'Alex': 1995})
k = my_dict.pop('Kostya')
print(k)
print(my_dict)

my_set = {(1,2,3),(1,2,3),1,1,2,2,'Kostya','Kostya','Alina','Alina',19.96,19.96,19.94,19.94}
print(my_set)
print(my_set.add(3))
print(my_set.add(True))
print(my_set.remove((1,2,3)))
print(my_set)