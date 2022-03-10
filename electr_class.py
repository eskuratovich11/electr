import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
a=149*10**9
k=8.98755*10**9

sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

class Particle:

  def __init__ (self, x0, y0, v_x, v_y, q, m):
      self.x0 = x0
      self.y0 = y0
      self.v_x = v_x
      self.v_y = v_y
      self.q = q
      self.m = m

  def  electr_func(self,s,t, other):

      (x, v_x, y, v_y) = s


      for i in range(3):

        dxdt= v_x
        dv_xdt = 0

        dv_xdt += k*self.q*other.q /self.m*(self.x-other.x)/ ((self.x-other.x)**2+(self.y-other.x)**2)**1.5

        dydt =  v_y
        dv_ydt = 0
        dv_ydt += k*self.q*other.q /self.m*(y-other.y)/ ((self.x-other.x)**2+(self.y-other.x)**2)**1.5

        return(dxdt, dv_xdt, dydt, dv_ydt)


s0= (x0, v_x0, y0,v_y0)