students = ['Salih','Emre','Berke','Gökhan']

print(students)
students.append('Ahmet')
print(students)
students.remove('Salih')
print(students)
students[0] = 'Ferhat'
print(students)

#list constructor
cities = list(("Istanbul","Ankara"))
print(cities)
print(len(cities))

#another functions
print(cities.count("Istanbul"))
print(cities.index("Ankara"))
cities.pop(1)
cities.insert(0,"Usak")
cities.reverse()
#print(cities.clear())
print(cities)

cities2 = cities 
cities2[0] = "Izmir"
print(cities)
print(cities2)
#cities2-cities are equal

cities3 = cities.copy()
print(cities3)

cities.extend(cities3)
cities.sort()
cities.reverse()
print(cities)