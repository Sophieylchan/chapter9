from math import pi, tan, cos
g= 9.81
v0= 44
theta= 80
x= 0.5
y0= 1

print("components :", g, v0, theta, y0, x)
# checking it works

# not sure if we need to convert to m/s (v0 = v0/3.6)
theta = theta*(pi/180)
# checking theta along the way
print("theta :",theta)

# (attempt 1) y = y0 + x math.tan(theta) - (g**2/2(v0 math.cos(theta))**2)
# (attempt 2) y = x*tan(theta) - 1/(2*v0**2)*g*x**2/((cos(theta))**2) + y0
y = y0 + x*tan(theta) - g*x**2 / (2*(v0*cos(theta))**2)

print("answer :", y)