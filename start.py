from erika import ErikaBot
import json

def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    bot = ErikaBot(config)
    bot.run()

if __name__ == '__main__':
    main()