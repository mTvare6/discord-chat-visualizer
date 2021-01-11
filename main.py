#!/usr/bin/env python3
"""
Why does my linter tell me to put this here???!?!?
"""

import mapper

CHAT = """mZe12/15/2020
hi
mTvare12/15/2020
hello
mZe12/21/2020
hello
mTvare12/21/2020
hello
mZe12/21/2020
hello!"""
message_groups = mapper.map_to_dm(contents=CHAT)
for message_group in message_groups:
    print(message_group.user)
    for message in message_group.messages:
        print("\t"+message)
