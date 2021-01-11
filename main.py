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
message_titles = mapper.mapDM(contents=CHAT)
for message_title in message_titles:
    print(message_title.user())
    for message in message_title.messages():
        print("\t"+message)
