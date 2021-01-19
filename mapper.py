from datetime import datetime
from os import _exit
from collections import OrderedDict
from pathlib import Path
import re
from datetime import datetime

DATE_HEAD = r'(.){3,32}\d{2}/\d{2}/\d{4}$'
YESTERDAY_HEAD_1 = r'(.){3,32}Yesterday\sat\s\d{1}:\d{2}\s(AM|PM)$'
TODAY_HEAD_1 = r'(.){3,32}Today\sat\s\d{1}:\d{2}\s(AM|PM)$'
YESTERDAY_HEAD_2 = r'(.){3,32}Yesterday\sat\s\d{2}:\d{2}\s(AM|PM)$'
TODAY_HEAD_2 = r'(.){3,32}Today\sat\s\d{2}:\d{2}\s(AM|PM)$'

class Message:

    '''
    Holds the instance of user name and list of message
    Used as getter and setter
    @param: the first message, the username
    '''
    def __init__(self, initMessage, entryUser):
        self.user = entryUser
        self.messages = []
        self.messages.append(initMessage)

    '''
    Adds a message to list
    @param: message to add
    '''
    def append(self, message):
        self.messages.append(message)

    '''
    Returns the final object
    @returns: self
    '''
    def returnObject(self):
        return self


def content_unloader(file='none'):
    '''
      Takes a file  and gives content
      @param: filePath of text
      @returns: content of file
    '''
    contents = Path(file).read_text()
    return contents

Today = datetime.today().strftime('%d/%m/%Y')
Yesterday = datetime.today().strftime('%d/%m/%Y')
tmp_date = str(int(Yesterday[0:2])-1)
Yesterday = list(Yesterday)
Yesterday[0] = tmp_date[0]
Yesterday[1] = tmp_date[1]
Yesterday = ''.join(Yesterday)
tmp_date = None
def map_to_dm(file='none'):
    '''
    Takes a file and returns mapped dictionary with messages
    @param: filePath, or content of text
    @returns: Dictionary with date and name mapped to a list containing message
    '''

    contents = content_unloader(file)
    contents_list = contents.split('\n')
    mapped_messages = []
    for line in contents_list:
        if re.match(DATE_HEAD, line):
            if len(mapped_messages)>0:
                mapped_messages[-1].append('')
            mapped_messages.append(Message('', line))
        elif re.match(YESTERDAY_HEAD_1, line):
            if len(mapped_messages)>0:
                mapped_messages[-1].append('')
            mapped_messages.append(Message('', line[:-20]+Yesterday))

        elif re.match(YESTERDAY_HEAD_2, line):
            if len(mapped_messages)>0:
                mapped_messages[-1].append('')
            mapped_messages.append(Message('', line[:-21]+Yesterday))

        elif re.match(TODAY_HEAD_1, line):
            if len(mapped_messages)>0:
                mapped_messages[-1].append('')
            mapped_messages.append(Message('', line[:-16]+Today))

        elif re.match(TODAY_HEAD_2, line):
            if len(mapped_messages)>0:
                mapped_messages[-1].append('')
            mapped_messages.append(Message('', line[:-17]+Today))

        else:
            mapped_messages[-1].append(line)
    return mapped_messages
