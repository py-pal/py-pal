import pyglet

window = pyglet.window.Window(1600, 1000)
# window = pyglet.window.Window(resizable=True)
label = pyglet.text.Label("仙剑奇侠传一 高清重制版",
                        font_size=24,
                        bold=True,
                        italic=False,
                        x=400, y=700,
                        color=(255, 255, 255, 255),
                    )

image = pyglet.resource.image('bg.jpeg')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()


pyglet.app.run()