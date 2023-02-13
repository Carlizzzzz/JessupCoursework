import matplotlib.pyplot as plt
x_data1 = [0.1, 0.2, 0.3, 0.4]
y_data1 = [1, 2, 3, 4]

x_data2 = [0.1, 0.2, 0.3, 0.4]
y_data2 = [1, 4, 9, 16]

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(x_data1, y_data1,'b-', dashes = (5,1) ,label='data 1')
ax2.plot(x_data2, y_data2,'gP', label='data 2')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Scale (Bananas)')
ax1.set_title('This is a dash line')
ax1.legend()
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Scale (Bananas)')
ax2.set_title('This is question two')
ax2.legend()

plt.show()