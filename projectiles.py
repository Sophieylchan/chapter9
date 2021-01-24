from math import pi, tan, cos
g= 9.81
v0= 44
theta= 80
x= 0.5
y0= 1

# checking theta
theta = theta*(pi/180)
print("Acceleration =", g,"m/s")
print("Velocity =", v0, "m/s")
print("Theta =",theta, "radians")
print("Horizontal distance =", x, "m")
print("Barrel height =", y0, "m")

y = y0 + x*tan(theta) - g*x**2 / (2*(v0*cos(theta))**2)
print("\n")
print(y0, "+", x, "x", tan(theta), "-", g*x**2, "/", (2*(v0*cos(theta))**2), "=", y)
print("Height of projectile =", y,"m")