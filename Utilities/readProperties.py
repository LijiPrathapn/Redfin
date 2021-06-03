import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\lijin\\PycharmProjects\\Redfin\\Configurations\\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getCity():
        Location=config.get('common info','City')
        return Location



