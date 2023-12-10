import pyglet

window = pyglet.window.Window(1024, 768)
label = pyglet.text.Label("仙剑奇侠传一 高清重制版",
                        font_size=24,
                        italic=False,
                        x=300,
                        y=700,
                        color=(255, 255, 255, 255),
                    )

bg_music_file_name = "/Users/alan/mywork/pypal/tests/pal1.mp3"
# bg_music_file_name = "1.mp3"

media_file_obj = pyglet.media.load(bg_music_file_name)
media = pyglet.media.StaticSource(media_file_obj)

image = pyglet.resource.image('bg.jpeg')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    media.play()
    label.draw()


pyglet.app.run()