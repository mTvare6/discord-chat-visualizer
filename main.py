#!/usr/bin/env python3
"""
Why does my linter tell me to put this here???!?!?
"""

import mapper
from colorit import background, color
from os import get_terminal_size


def generate_spaces(content, sep=" "):
    raw_term_size = str(get_terminal_size).split(" ")
    terminal_size = int(raw_term_size[0][25:][:-1])
    addable_chars = int((terminal_size-len(content))/2)
    return (sep*addable_chars+content+sep*addable_chars)
file = "./message.txt"
message_groups = mapper.map_to_dm(file)
for message_group in message_groups:
    date = message_group.user[-12:]
    name = message_group.user[:-12]
    printable_group_title = generate_spaces(name + "  " + date)
    for submessage in message_group.messages:
        printable_submessage = generate_spaces(submessage)
        print(
            background(
                color(printable_submessage, Colors.blue), Colors.white
            )
        )