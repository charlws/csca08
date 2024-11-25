"""
CSCA08: Winter 2024 -- Assignment 3: WackyChat

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

from typing import TextIO
from datetime import datetime
import tempfile

# This is an example of what the contents of a file might look like.
SAMPLE_TEXT_CONTEXT_1 = """
GROUP
9119
CSCA08
CHANNEL
48805
9119
Irene's Classroom
CHANNEL
6265
9119
Purva's Classroom
MESSAGE
12255
48805
2024/11/16 23:32:52
Charles Xu
I am working on CSCA08 Assignment 3!
DONE
"""

# This is the translation of the above contents as a series of dicts & arrays.
SAMPLE_DICT_CONTEXT_1 = {
    "groups": [{
        "id": 9119,
        "name": "CSCA08"
    }],
    "channels": [{
        "id": 48805,
        "group": 9119,
        "name": "Irene's Classroom"
    }, {
        "id": 6265,
        "group": 9119,
        "name": "Purva's Classroom"
    }],
    "messages": [{
        "id": 12255,
        "channel": 48805,
        "time": "2024/11/16 23:32:52",
        "name": "Charles Xu",
        "message": "I am working on CSCA08 Assignment 3!"
    }]
}


def is_valid_date(date: str) -> bool:
    '''
    Returns True if and only if the given string 'date' is valid and in the
    format of 'year/month/day hour:minute:second'.

    >>> is_valid_date('2024/11/16 23:32:52')
    True
    >>> is_valid_date('2024/13/13 25:25:25')
    False
    >>> is_valid_date('Banana')
    False
    '''
    try:
        datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        return True
    except ValueError:
        return False


def create_temporary_file() -> str:
    '''
    Create a temporary file inside the system's temporary directory and return
    its absolute path.

    >>> import os
    >>> file_path = create_temporary_file()
    >>> os.path.exists(file_path)
    True
    >>> os.remove(file_path)
    >>> os.path.exists(file_path)
    False
    '''
    return tempfile.NamedTemporaryFile(delete=False).name


def create_group(context: dict, group_id: int, name: str) -> bool:
    '''
    Create a group whose id is 'group_id' and name is 'name' to 'context'.
    Return True if successful, otherwise False.

    >>> context = {}
    >>> create_group(context, 100, "UofT")
    True
    >>> create_group(context, 100, "UTSC")
    False
    >>> context["groups"] == [{"id": 100, "name": "UofT"}]
    True
    '''
    if "groups" not in context:
        context["groups"] = []

    # id conflict
    if any(group["id"] == group_id for group in context["groups"]):
        return False

    context["groups"].append({"id": group_id, "name": name})
    return True


def create_channel(context: dict, group_id: int, channel_id: int,
                   name: str) -> bool:
    '''
    Create a channel whose id is 'channel_id', name is 'name' and belongs to
    group 'group_id' to 'context'. Return True if successful, otherwise
    False.

    >>> context = {"groups": [{"id": 100, "name": "UofT"}]}
    >>> create_channel(context, 100, 200, "Scarborough Campus")
    True
    >>> create_channel(context, 100, 200, "St. George Campus")
    False
    >>> create_channel(context, 99, 201, "WHAT")
    False
    >>> context["channels"] == [{"id": 200, "group": 100, \
        "name": "Scarborough Campus"}]
    True
    '''
    # no group in context
    if "groups" not in context:
        return False

    # group not found
    if not any(group["id"] == group_id for group in context["groups"]):
        return False

    if "channels" not in context:
        context["channels"] = []

    # id conflict
    if any(channel["id"] == channel_id for channel in context["channels"]):
        return False

    context["channels"].append({"id": channel_id, "group": group_id, \
        "name": name})
    return True


def send_message(context: dict, channel_id: int, message_id: int,
                 time: str, name: str, message: str) -> bool:
    '''
    Create a message whose id is 'message_id', content is 'message', sender is
    'name', timestamp is 'time' in 'channel'. Return True if successful,
    otherwise False.

    >>> context = {"groups": [{"id": 100, "name": "UofT"}],\
                  "channels": [{"id": 200, "group": 100, \
                    "name": "Scarborough Campus"}]}
    >>> send_message(context, 200, 1000, "2024/11/16 23:32:52", \
                      "Charles", "Dragon's here")
    True
    >>> send_message(context, 200, 1000, "2024/11/16 23:32:52", \
                      "Charles", "Dragon's here")
    False
    >>> send_message(context, 200, 1000, "2024/11/16 25:25:25", \
                      "Charles", "Dragon's here")
    False
    >>> send_message(context, 201, 1001, "2024/11/16 23:32:52", \
                      "Charles", "Dragon's here")
    False
    >>> context["messages"] == [{"id": 1000, "channel": 200, \
        "time": "2024/11/16 23:32:52", "name": "Charles", \
            "message": "Dragon's here"}]
    True
    '''
    # no channel in context
    if "channels" not in context:
        return False

    # channel not found
    if not any(channel["id"] == channel_id for channel in context["channels"]):
        return False

    if "messages" not in context:
        context["messages"] = []

    # id conflict
    if any(cmsg["id"] == message_id for cmsg in context["messages"]):
        return False

    # invalid date
    if not is_valid_date(time):
        return False

    context["messages"].append({"id": message_id, "channel": channel_id, \
        "time": time, "name": name, "message": message})
    return True


def read_context_from_file(file_io: TextIO) -> dict | None:
    '''
    Return the context dictionary parsed from the file 'file_io', if it is
    valid. Otherwise, return None.
    NOTE: We do not check content is correctly ordered.

    >>> file_path = create_temporary_file()
    >>> file = open(file_path, "w")
    >>> index = file.write(SAMPLE_TEXT_CONTEXT_1)
    >>> file.close()
    >>> file = open(file_path, "r")
    >>> context = read_context_from_file(file)
    >>> file.close()
    >>> context == SAMPLE_DICT_CONTEXT_1
    True
    '''
    data = file_io.read().split("\n")

    # load unordered data into temp vars
    groups = []
    channels = []
    messages = []

    i = 0
    while i < len(data):
        if data[i] == "GROUP":
            groups.append({"id": int(data[i+1]), "name": data[i+2]})
            i += 3
        elif data[i] == "CHANNEL":
            channels.append({"id": int(data[i+1]), "group": int(data[i+2]), \
                             "name": data[i+3]})
            i += 4
        elif data[i] == "MESSAGE":
            messages.append({"id": int(data[i+1]), "channel": int(data[i+2]), \
                             "time": data[i+3], "name": data[i+4], \
                                "message": data[i+5]})
            i += 6
        elif data[i] == "DONE":
            break
        else:
            # blank line
            # aka. first line in sample string
            i += 1

    # load data into context
    context = {}
    for group in groups:
        if not create_group(context, group["id"], group["name"]):
            return None
    for channel in channels:
        if not create_channel(context, channel["group"], channel["id"], \
                       channel["name"]):
            return None
    for message in messages:
        if not send_message(context, message["channel"], message["id"], \
                     message["time"], message["name"], message["message"]):
            return None
    return context

def get_user_word_frequency(context: dict, name: str) -> dict:
    '''
    Return the word frequency of user whose name is 'name' based on all
    messages theu have sent in 'context'.
    NOTE: Words are divided by whitespace and thus may contain puncutations.

    >>> freq = get_user_word_frequency(SAMPLE_DICT_CONTEXT_1, "Charles Xu")
    >>> freq == {"I": 1, "am": 1, "working": 1, "on": 1, "CSCA08": 1, \
        "Assignment": 1, "3!": 1}
    True
    >>> freq = get_user_word_frequency(SAMPLE_DICT_CONTEXT_1, "Charles Wong")
    >>> freq == {}
    True
    >>> freq = get_user_word_frequency({}, "Charles Wong")
    >>> freq == {}
    True
    '''
    if "messages" not in context:
        return {}

    ret = {}
    for message in context["messages"]:
        if message["name"] == name:
            for word in message["message"].split():
                if word not in ret:
                    ret[word] = 1
                else:
                    ret[word] += 1

    return ret


def get_user_character_frequency_percentage(context: dict, name: str) -> dict:
    '''
    Return the character frequency of user whose name is 'name' based on all
    messages they have sent in 'context'.
    NOTE: All characters, including whitespaces, are counted. This function
    is not case-sensitive.

    >>> freq = get_user_character_frequency_percentage(SAMPLE_DICT_CONTEXT_1, \
                                                "Charles Xu")
    >>> freq == {'I': 0.027777777777777776, ' ': 0.16666666666666666, \
        'a': 0.027777777777777776, 'm': 0.05555555555555555, \
        'w': 0.027777777777777776, 'o': 0.05555555555555555, \
        'r': 0.027777777777777776, 'k': 0.027777777777777776, \
        'i': 0.05555555555555555, 'n': 0.1111111111111111, \
        'g': 0.05555555555555555, 'C': 0.05555555555555555, \
        'S': 0.027777777777777776, 'A': 0.05555555555555555, \
        '0': 0.027777777777777776, '8': 0.027777777777777776, \
        's': 0.05555555555555555, 'e': 0.027777777777777776, \
        't': 0.027777777777777776, '3': 0.027777777777777776, \
        '!': 0.027777777777777776}
    True
    >>> freq = get_user_character_frequency_percentage(SAMPLE_DICT_CONTEXT_1, \
        "Charles Wong")
    >>> freq == {}
    True
    >>> freq = get_user_character_frequency_percentage({}, "Charles Wong")
    >>> freq == {}
    True
    '''
    if "messages" not in context:
        return {}

    cnt = {}
    for message in context["messages"]:
        if message["name"] == name:
            for char in message["message"]:
                if char not in cnt:
                    cnt[char] = 1
                else:
                    cnt[char] += 1

    total_char = sum(v for v in cnt.values())
    return {k: v / total_char for (k, v) in cnt.items()}


def get_most_popular_group(context: dict) -> int | None:
    '''
    Return the id of the group that has the sent the most amount of messages in
    'context' - use smallest group id if there are ties. Return None
    if there are no groups in 'context'.

    >>> get_most_popular_group(SAMPLE_DICT_CONTEXT_1)
    9119
    >>> get_most_popular_group({}) is None
    True
    '''
    if "channels" not in context or "groups" not in context or \
            "messages" not in context:
        return None

    channel2group = {}
    for channel in context["channels"]:
        channel2group[channel["id"]] = channel["group"]

    if len(channel2group) == 0:
        return None

    group_messages_cnt = {}
    for message in context["messages"]:
        group = channel2group[message["channel"]]
        if group not in group_messages_cnt:
            group_messages_cnt[group] = 1
        else:
            group_messages_cnt[group] += 1

    if len(group_messages_cnt) == 0:
        return None

    max_cnt = max(v for v in group_messages_cnt.values())
    min_group_id = min(k for (k, v) in group_messages_cnt.items() \
                        if v == max_cnt)
    return min_group_id

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # read_context_from_file(open("./test_file.txt", "r"))
    # print(get_user_word_frequency(SAMPLE_DICT_CONTEXT_1, "Charles Xu"))
    # print(get_user_character_frequency_percentage(SAMPLE_DICT_CONTEXT_1, \
                                                # "Charles Xu"))
    # print(get_most_popular_group(SAMPLE_DICT_CONTEXT_1))
