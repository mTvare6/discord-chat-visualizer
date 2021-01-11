#!/usr/bin/env python3
'''
Why does my linter tell me to put this here???!?!?
'''

from collections import OrderedDict
from pathlib import Path
import re

CHAT_HEAD = r'...+\d{2}/\d{2}/\d{4}$'


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


def map_to_dm(file='none', contents='none'):
    '''
    Takes a file and returns mapped dictionary with messages
    @param: filePath, or content of text
    @returns: Dictionary with date and name mapped to a list containing message
    '''

    if file == 'none' and contents == 'none':
        return 'Either provide file path or content'
    if contents == 'none' and file != 'none':
        contents = Path(file).read_text()
    if file == 'none' and contents != 'none':
        pass
    if file != 'none' and contents != 'none':
        return 'Either provide file path or content, not both'
    contents_list = contents.split('\n')
    mapped_messages = []
    for line in contents_list:
        if re.match(CHAT_HEAD, line):
            mapped_messages.append(Message('', line))
        else:
            mapped_messages[-1].append(line)
    return mapped_messages
