"""
    Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
    """


def show_message(messages: list):
    for mess in messages:
        print(mess)


def send_message(messages: list, sent_messages: list):
    while messages:
        sent_mess = messages.pop(0)
        print(sent_mess)
        sent_messages.append(sent_mess)


messages = ["I", "am", "falling in love", "with you"]
sent_messages = []
print(messages)
print(sent_messages)

send_message(messages[:], sent_messages)

print(messages)
print(sent_messages)
