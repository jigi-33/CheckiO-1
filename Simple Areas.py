simple_areas = lambda *a: [lambda: 3.1415926*0.25*a[0]**2, lambda: a[0]*a[1], lambda: 0.25*(4*a[0]**2*a[1]**2-(a[0]**2+a[1]**2-a[2]**2)**2)**0.5][len(a)-1]()