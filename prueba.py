import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.n

x = np.linspace(start=0, stop= 2*np.pi, num=100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x,y)
ax.set_facecolor('whitesmoke')
ax.set_title("Mi senoidal")
ax.set_ylabel("amplitud")
ax.set_xlabel("[rad]")
plt.show()
