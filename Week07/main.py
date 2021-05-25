from engine.game_loader import GameLoader

def main():
    g = GameLoader.load_game()
    g.run()

if __name__ == "__main__":
    main()
