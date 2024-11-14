import numpy as np
import matplotlib.pyplot as plt
# Define the function f(t)
t = np.linspace(0, 4 * np.pi, 1000)  # Two cycles over 0 to 4*pi
f_t = np.cos(t) * np.cos(5 * t) + np.cos(5 * t)

# Plot the function
# plt.plot(t, f_t)
# plt.title("Plot of f(t) = cos(t)cos(5t) + cos(5t)")
# plt.xlabel("t")
# plt.ylabel("f(t)")
# plt.grid(True)
# plt.show()

# # Plot the histogram of f(t)
# plt.hist(f_t, bins=10)
# plt.title("Histogram of f(t)")
# plt.xlabel("f(t)")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()

fig,a = plt.subplots(2,1)
a[0].plot(t,f_t)
a[0].set_title('Plot of f(t) = cos(t)cos(5t) + cos(5t)')
a[0].set_xlabel("t")
a[0].set_ylabel("f(t)")

a[1].hist(f_t,bins=10)
a[1].set_title("Histogram of f(t)")
a[1].set_xlabel("f(t)")
a[1].set_ylabel("Frequency")

plt.subplots_adjust(hspace=1)

plt.show()