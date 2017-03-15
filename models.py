from utils import file_extension, file_name

class CodeFile(object):
    def __init__(self, path, name, extension):
        self.path = path
        self.name = name
        self.extension = extension
        self.is_valid = True
        f = None
        try:
            f = open(self.path, 'r')
            self.lines = f.readlines()
        except:
            self.lines = []
            self.is_valid = False
        finally:
            if f:
                f.close()

    def __str__(self):
        line_count = str(len(self.lines))
        return '[path="{}", is_valid={}, line_count={}]'.format(self.path, self.is_valid, line_count)
        