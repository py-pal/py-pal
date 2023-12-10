

import pyglet
from pyglet.gl import *




#window = pyglet.window.Window(800, 600)
window = pyglet.window.Window(visible=False, resizable=True)



version_label = pyglet.text.Label(text="仙剑奇侠传1 高清重制版....",
                                x=window.width // 2 ,
                                y=window.height // 2 - 200,
                                font_size=14,
                                # anchor_x='center',
                                # anchor_y='center',
                                font_name='黑体')

# player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

@window.event
def on_draw():
    # window.clear()
    background.blit_tiled(0, 0, 0, window.width, window.height)
    img.blit(window.width // 2, window.height // 2, 0)
    #
    version_label.draw()


if __name__ == "__main__":
    # Tell pyglet to do its thing
    # pyglet.app.run()
    img = pyglet.image.load("tests/bg.jepg")
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

    checks = pyglet.image.create(32, 32, pyglet.image.CheckerImagePattern())
    background = pyglet.image.TileableTexture.create_for_image(checks)

    # Enable alpha blending, required for image.blit.
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    window.width = img.width
    window.height = img.height
    window.set_visible()

    pyglet.app.run()