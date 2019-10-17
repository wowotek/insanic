from random import randint


class Messages:
    msg_id = 106
    message = "".join([i[randint(0, 25)] for i in "abcdefghijklmnopqrstuvwxyz"])

    def __repr__(self):
        return f"<Message id:{self.msg_id}>"
