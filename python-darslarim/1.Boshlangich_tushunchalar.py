# 6-dars(sonlar)
r = float(input('radiusni kiriting r='))
PI = 3.1465658
l = (2 * PI * r)
s = (PI * (r ** 2))
print('Aylana uzunligi=', l)
print('Aylana yuzi=', s)
print('PI=', PI)

# 7-dars(1)
q = ['', 'bexi', 'nok']
q[1] = ('banan')
q[0] = ('xurmo')
q[-2] = ('shaftoli')
q.append('tarvuz')
q.insert(2, 'anjir')
q.insert(5, 'o`rik')
print(q)

# 7-dars(2)
cars = []
cars.append('malibu')
cars.append('captiva')
cars.append('nexia')
cars.append('gentra')
cars.append('cobalt')
# del cars[-2]
cars.remove('captiva')
print(cars)

