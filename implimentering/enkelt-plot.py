import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x,y) #opretter ett plot
plt.show() #Hviser plottet

x = [0, 1, 2, 3, 4, 5]
y= []

for tall in x:
    y.append(3*tall+2)

plt.plot(x,y)
plt.show()

def f(x):
    return 3*x+2

x = []
y = []


for i in range(0,6):
    x.append(i)
    y.append(f(i))


plt.scatter() #gir punkter