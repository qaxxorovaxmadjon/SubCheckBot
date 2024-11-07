from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
CHANNEL_ID = list(map(int, env.str("CHANNEL_ID").split(',')))