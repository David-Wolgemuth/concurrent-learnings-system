import re
from utils import file_extension, file_name, line_comment_tokens

TAG_START = '<*-- (.+$)'
TAG_ENDING = '--*>'

class CodeFile(object):
    def __init__(self, path, name, extension):
        self.path = path
        self.name = name
        self.extension = extension
        self.is_valid = True
        self.blocks = []
        file = None
        try:
            file = open(self.path, 'r')
            self.lines = file.readlines()
            self.read()
        except:
            self.lines = []
            self.is_valid = False
        finally:
            if file:
                file.close()

    def __str__(self):
        line_count = str(len(self.lines))
        return '[path="{}", is_valid={}, line_count={}]'.format(self.path, self.is_valid, line_count)

    def read(self):
        if len(self.blocks) == 0:
            sections = ''.join(self.lines).split(TAG_ENDING)
            for section in sections:
                block_name = None
                block_lines = []
                for line in section.split('\n'):
                    extract = re.search(TAG_START, line)
                    if extract and not block_name:
                        block_name = extract.group(1)
                    elif block_name:
                        block_lines.append(line)
                if block_name:
                    self.blocks.append(ContentBlock(block_name, block_lines, self.extension))

        
class ContentBlock(object):
    def __init__(self, name, lines, extension):
        self.name = name
        self.lines = []
        for line in lines:
            self.lines.append(line.replace(line_comment_tokens[extension], ''))

    def __str__(self):
        return '[name="{}", line_count={}]'.format(self.name, str(len(self.lines)))