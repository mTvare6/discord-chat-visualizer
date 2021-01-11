#!/usr/bin/env python3
'''
Why does my linter tell me to put this here???!?!?
'''

from os import _exit
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


def content_unloader(file='none'):
    '''
      Takes a file  and gives content
      @param: filePath of text
      @returns: content of file
    '''
    contents = Path(file).read_text()
    return contents


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
        if re.match(CHAT_HEAD, line):
            mapped_messages.append(Message('', line))
        else:
            mapped_messages[-1].append(line)
    return mapped_messages
