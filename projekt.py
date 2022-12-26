# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as m

N=100
theta=np.random.uniform(0,2*np.pi,N)
z=np.random.uniform(-1,1,N)
x=[]
y=[]
for i in range(len(z)):
    xi=np.sqrt(1-z[i]**2)*np.cos(theta[i])
    x.append(xi)
    yk=np.sqrt(1-z[i]**2)*np.sin(theta[i])
    y.append(yk)

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
# %%
l=np.random.uniform(10,200,N)
l=l.tolist()
xl=[]
yl=[]
zl=[]
for i in range(len(l)):
    xl_i=x[i]*l[i]
    yl_i=y[i]*l[i]
    zl_i=z[i]*l[i]
    xl.append(xl_i)
    yl.append(yl_i)
    zl.append(zl_i)

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(xl,yl,zl)
# %%
k=5.76*10**(-7)
S=3.7*10**10 #[Bq]
E=0.662 #[MeV]
mac=0.029
#mac=0.0326
lac=1.289
d=0
dose_rate=[]
for i in range(len(l)):
    D=k*S*E*mac*np.exp(-lac*d)/(4*np.pi*l[i]**2)
    dose_rate.append(D)


plt.scatter(l,dose_rate)
plt.xlabel('Odległość od źródła [cm]')
plt.ylabel('Moc dawki [Gray/h]')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for i in range(N):
    if dose_rate[i]<0.05:
        ax.scatter(xl[i],yl[i],zl[i],c='r')
    elif 0.05<=dose_rate[i]<0.1:
        ax.scatter(xl[i],yl[i],zl[i],c='b')
    elif 0.1<=dose_rate[i]<0.15: 
        ax.scatter(xl[i],yl[i],zl[i],c='g')
    else:
        ax.scatter(xl[i],yl[i],zl[i],c='y')
ax.set(xlabel='X axis', ylabel='Y axis', zlabel='Z axis')
plt.show()
# %%
points=[]
for i in range(len(xl)):
    points.append([])
    points[i].append(xl[i])
    points[i].append(yl[i])
    points[i].append(zl[i])

plane_x1=[]
plane_y1=[]
plane_dose=[]
for i in range(len(points)):
    if np.absolute(points[i][2]) <1:
        plane_x1.append(points[i][0])
        plane_y1.append(points[i][1])
        plane_dose.append(dose_rate[i])

plane_dose=plane_dose+plane_dose+plane_dose+plane_dose
plane_x2=[item*(-1) for item in plane_x1]
plane_y2=[item*(-1) for item in plane_y1]
plane_x=plane_x1+plane_x2+plane_x1+plane_x2
plane_y=plane_y1+plane_y2+plane_y2+plane_y1

plt.figure()
for i in range(len(plane_x)):
    if plane_dose[i]<0.05:
        plt.scatter(plane_x[i],plane_y[i],c='r')
    elif 0.05<=plane_dose[i]<0.1:
        plt.scatter(plane_x[i],plane_y[i],c='b')
    elif 0.1<=plane_dose[i]<0.15: 
        plt.scatter(plane_x[i],plane_y[i],c='g')
    else:
        plt.scatter(plane_x[i],plane_y[i],c='y')

plt.show()
# %%
# %%

# %%
