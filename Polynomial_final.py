import numpy as np
import scipy.spatial 
import shapely.geometry 
import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

#Αρχικοποιηση του πολυωνυμου + κυρτη του τομη
#Πολυωνυμικοι συντελεστες
coef=[10*random.random()-5] 
for i in range(5):
    coef=coef+[10*random.random()-5] 
    
r = np.roots(coef)
print(coef)

points=[]
for i in r:
    x=i.real
    y=i.imag
    points.append((x,y))

hull0=scipy.spatial.ConvexHull(points)
v0=hull0.points[hull0.vertices]

polly0 = shapely.geometry.Polygon(v0)
scipy.spatial.convex_hull_plot_2d(hull0, ax=ax)

intersection=shapely.intersection(polly0,polly0)

#Υπολοιπα πολυωνυμα
for i in range(-25,25,5):
    for k in range(-25,25,5):

        #Το καινουργιο πολυωνυμο
        coef2=coef.copy()
        l=1j
        coef2[-1]+=i+ k*l

        #ομοιως με το πρωτο για την κυρτη τομη
        r = np.roots(coef2)
        points=[]
        for i in r:
            x=i.real
            y=i.imag
            points.append((x,y))

        nhull=scipy.spatial.ConvexHull(points)
        nv=nhull.points[nhull.vertices]

        npolly = shapely.geometry.Polygon(nv)
        scipy.spatial.convex_hull_plot_2d(nhull, ax=ax)

        #Η τομη
        intersection=shapely.intersection(intersection,npolly)











#Κυρτη θηκη της παραγωγου
coef2=[]
n=len(coef)-1
for i in range(n):
    coef2.append(coef[i]*(n-i))

rp=np.roots(coef2)
points=[]
for i in rp:
    x=i.real
    y=i.imag
    points.append((x,y))
hullp=scipy.spatial.ConvexHull(points)
vp=hullp.points[hullp.vertices]

pollyp = shapely.geometry.Polygon(vp)
scipy.spatial.convex_hull_plot_2d(hullp, ax=ax)



# Γραφηκη Παρασταση
plt.axhline(0, color='black',linestyle='--', linewidth=1.2) 
plt.axvline(0, color='black',linestyle='--', linewidth=1.2)

plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Real')
plt.ylabel('Imaginary')

x_inter, y_inter = pollyp.exterior.xy
ax.fill(x_inter, y_inter, color='blue', alpha=0.5)

x_inter, y_inter = intersection.exterior.xy
ax.fill(x_inter, y_inter, color='red', alpha=0.5)

plt.show()