#!/usr/bin/env python3
"""
Why does my linter tell me to put this here???!?!?
"""

import mapper

CHAT = """
mZe12/15/2020
hi
mTvare12/15/2020
hello
mZe12/21/2020
hello
mTvare12/21/2020
hello
mZe12/21/2020
hello!
"""
for message_title in mapper.mapDM(contents=CHAT):
    print(message_title.user)
    for message in message_title:
        print("\t"+message)
