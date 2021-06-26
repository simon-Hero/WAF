

class FileNotFound(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return "{} error, Please check if your configuration file path is in the root directory".format(self.info)


class NoDataError(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return "not find the {} key".format(self.info)
