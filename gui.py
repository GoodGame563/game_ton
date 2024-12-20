from vispy import app, scene
import numpy as np

canvas = scene.SceneCanvas(keys='interactive', bgcolor='white')
view = canvas.central_widget.add_view()
view.camera = scene.cameras.TurntableCamera()

field = np.random.randint(0, 5, (10, 10, 10))
colors = np.array([
    [1, 1, 1, 1],  # Белый
    [1, 0, 0, 1],  # Красный
    [0, 1, 0, 1],  # Зеленый
    [0, 0, 1, 1],  # Синий
    [1, 1, 0, 1],  # Желтый
])

for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        for k in range(field.shape[2]):
            color = colors[field[i, j]]
            box = scene.visuals.Box(color=color, edge_color='black', parent=view.scene)
            box.transform = scene.transforms.STTransform(translate=(i, j, k))

canvas.show()
app.run()