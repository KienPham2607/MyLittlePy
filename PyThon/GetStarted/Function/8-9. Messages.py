"""
    Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
    """
def show_message(messages: list):
    for mess in messages:
        print(mess)

messages = ["I", "am", "falling in love", "with you"]
show_message(messages)