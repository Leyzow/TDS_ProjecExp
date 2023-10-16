# Enzo & Ahmad : Projection exponentielle

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

def update(val):
    ax.cla()
    dz = slider.val * np.linalg.norm(p)
    d = dz * (v - p) / np.linalg.norm(v - p)
    v_projected = p + d

    ax.quiver(0, 0, 0, p[0], p[1], p[2], color='b', label='p')
    ax.quiver(p[0], p[1], p[2], d[0], d[1], d[2], color='r', linestyle='dashed', label='d (projeté)')
    ax.quiver(0, 0, 0, v_projected[0], v_projected[1], v_projected[2], color='g', label='v')

    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = np.linalg.norm(p) * np.cos(theta)
    y_circle = np.linalg.norm(p) * np.sin(theta)
    ax.plot(x_circle, y_circle, 0, color='gray', linestyle='--')

    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_zlim(0, 8)
    ax.set_box_aspect([8, 8, 8])
    ax.legend()
    plt.draw()

p = np.array([4, 1, 0])
v = np.array([2, 3, 4])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Taille de dz', 0, 1, valinit=0.5, valstep=0.01)
slider.on_changed(update)

update(0)

plt.show()

