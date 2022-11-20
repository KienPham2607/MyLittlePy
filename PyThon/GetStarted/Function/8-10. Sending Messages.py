"""
    Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
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

send_message(messages, sent_messages)

print(messages)
print(sent_messages)
