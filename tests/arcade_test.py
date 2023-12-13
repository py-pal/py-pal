import arcade

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pal1 Remaster"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # self.background = None
        self.background_color = arcade.color.BLACK
        self.text_angle = 0
        self.time_elapsed = 0.0
        music_file_name = "resource/pal1.mp3"

        self.my_music = arcade.Sound(music_file_name)
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """Set up the game variables. Call to re-start the game."""
        # Create your sprites and sprite lists here
        self.background = arcade.load_texture("resource/bg.jpeg")
        self.my_music.play()

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text(
            "Pal1 Remaster",
            start_x,
            start_y,
            arcade.color.WHITE,
            DEFAULT_FONT_SIZE * 2,
            width=SCREEN_WIDTH,
            align="center",
        )

        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.text_angle += 1
        self.time_elapsed += delta_time

        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        print(f"on_key_press:{key},{key_modifiers}")
        pass

    def on_key_release(self, key, key_modifiers):
        print(f"on_key_release:{key},{key_modifiers}")
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"on_mouse_press:{x},{y}")
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        print(f"on_mouse_release:{x},{y}")
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
