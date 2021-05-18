from configparser import ConfigParser
from engine.game import Game

class GameLoader():
    @staticmethod
    def load_game():
        config = ConfigParser()
        config.read("./engine/data/config.ini")
        defaults = config["DEFAULT"]
        default_properties = {"FPS":defaults.getint("FPS")}
        window_settings = config["WINDOW SETTINGS"]
        window_properties = {"size":(window_settings.getint("width"),window_settings.getint("height")),
                             "caption":window_settings.get("title")}
        return Game(default_properties, window_properties)
