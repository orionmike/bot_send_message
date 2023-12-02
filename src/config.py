
import sys
from datetime import datetime
from pathlib import Path

from colorama import Fore, init

from loguru import logger

# ABS_PATH = ''  # for win
# ABS_PATH = f'{sys.path[0]}/app/'  # for linux

ABS_PATH = Path(__file__).parent.resolve()
APP_NAME = 'bot_send_message'

init(autoreset=True)

# =====================================
# load config

try:

    if sys.version_info.major == 3 and sys.version_info.minor >= 11:

        import tomllib

        with open(f"{ABS_PATH}/config.toml", "rb") as f:
            config = tomllib.load(f)
    else:

        import toml  # pip install toml

        with open(f"{ABS_PATH}/config.toml", "r") as f:
            config = toml.load(f)

    # print(config)

    IND = config['utils']['console_indent']

    DB_FILE = Path(f"{ABS_PATH}/{config['db_sqlite']['db_dir']}/{config['db_sqlite']['db_file']}")

    TG_BOT_TOKEN = config['telegram']['bot_token']
    TG_USER_ID = config['telegram']['user_id']

    # logging

    log_file_name = f'{datetime.now().strftime("%Y-%m-%d")}'
    logger.remove()
    logger.add(f'{ABS_PATH}/logs/{log_file_name}_error.log', format='{time} {level} {message}', level='ERROR', rotation='1 day')

    # print(f'{datetime.now()} start app: {APP_NAME}')
    # print(f'{IND} python {sys.version_info.major}.{sys.version_info.minor}')
    # print(f'{IND} config loaded: OK')

except Exception as e:
    raise Exception(f'config load -> error: {e}')
