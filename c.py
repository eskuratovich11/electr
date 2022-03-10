import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
a=149*10**9


sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

def electr_func(s,t):
     
     (xa, v_x_a, ya, v_y_a,
     xb, v_x_b, yb, v_y_b, 
     xc, v_x_c, yc, v_y_c) = s
      
     dxdt_a= v_x_a
     dv_xdt_a= (k*qa*qb/ma*(xa-xb)/ ((xa-xb)**2+(ya-yb)**2)**1.5
                +k*qa*qc/ma*(xa-xc)/ ((xa-xc)**2+(ya-yc)**2)**1.5)
     dydt_a= v_y_a
     dv_ydt_a= (k*qa*qb/ma*(ya-yb)/ ((xa-xb)**2+(ya-yb)**2)**1.5
                +k*qa*qc/ma*(ya-yc)/ ((xa-xc)**2+(ya-yc)**2)**1.5)
     
     dxdt_b= v_x_b
     dv_xdt_b= (k*qb*qa/mb*(xb-xa)/ ((xb-xa)**2+(yb-ya)**2)**1.5
                +k*qb*qc/mb*(xb-xc)/ ((xb-xc)**2+(yb-yc)**2)**1.5)
     dydt_b= v_y_b
     dv_ydt_b= (k*qb*qa/mb*(yb-ya)/ ((xb-xa)**2+(yb-ya)**2)**1.5
                +k*qb*qc/mb*(yb-yc)/ ((xb-xc)**2+(yb-yc)**2)**1.5)
    
     dxdt_c= v_x_c
     dv_xdt_c= (k*qc*qa/mc*(xc-xa)/ ((xc-xa)**2+(yc-ya)**2)**1.5
                +k*qc*qb/mc*(xc-xb)/ ((xc-xb)**2+(yc-yb)**2)**1.5)
     dydt_c= v_y_c
     dv_ydt_c= (k*qc*qa/mc*(yc-ya)/ ((xc-xa)**2+(yc-ya)**2)**1.5
                +k*qc*qb/mc*(yc-yb)/ ((xc-xb)**2+(yc-yb)**2)**1.5)
     
     return(dxdt_a, dv_xdt_a, dydt_a, dv_ydt_a,
            dxdt_b, dv_xdt_b, dydt_b, dv_ydt_b,
            dxdt_c, dv_xdt_c, dydt_c, dv_ydt_c)

qa= 1.6*10**20
qb= 1.6*10**20
qc= -1.6*10**20

ma=106*10**30
mb=60*10**30
mc=30*10**30

xa0=-a
v_xa0=-10**4
ya0=0
v_ya0=0

xb0= a
v_xb0=-15*10**3
yb0=0
v_yb0=0

xc0= 0
v_xc0=-20*10**3
yc0=a
v_yc0=0

k=8.98755*10**9

s0= (xa0, v_xa0, ya0,v_ya0,
     xb0, v_xb0, yb0,v_yb0,
     xc0, v_xc0, yc0,v_yc0)  
  
sol=odeint(electr_func, s0, t)

fig=plt.figure()
objects=[]  
for i in range(0, len(t), 1):
    a, = plt.plot(sol[:i,0], sol[:i, 2], 'r-')
    a_line, = plt.plot(sol[i,0], sol[i, 2], 'ro')
    
    b,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    b_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    c,= plt.plot(sol[:i,8], sol[:i, 10],  '-', color= 'y')
    c_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='y')

    objects.append([a, a_line, b, b_line, c, c_line])
ani = ArtistAnimation(fig, objects, interval= 50)
plt.axis('equal')
plt.show()