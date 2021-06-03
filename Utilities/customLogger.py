import logging

class LogGen:
    @staticmethod
    def loggen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(
            filename="C:\\Users\\lijin\\PycharmProjects\\Redfin\\Logs\\logfile.log")
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
