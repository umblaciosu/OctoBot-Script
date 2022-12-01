import logging.config as config
import os.path
import octobot.logger


def load_logging_config(config_file="logging_config.ini"):
    if octobot.logger.BOT_CHANNEL_LOGGER is not None:
        # logs already initialized
        return
    logs_folder = "logs"
    if not os.path.exists(logs_folder):
        os.mkdir(logs_folder)
    config.fileConfig(config_file)
    octobot.logger.init_bot_channel_logger()