def func (x,y):
  return 6 * (x**2) +5*x+y
def euler (x_0=1,
            y_0=1,
            step= 0.01,
            n=1000):
  x, y = x_0, y_0 
  x_list= []
  y_list= []
  x_list.append(x)
  y_list.append(y)

  for _ in range (n):
    y = y+ step*func(x,y)
    x= x+ step
  return x_list, y_list
print( euler())
 