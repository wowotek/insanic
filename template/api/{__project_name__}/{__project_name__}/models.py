from random import randint


class Messages:
    msg_id = 106
    message = "".join(["abcdefghijklmnopqrstuvwxyz"[randint(0, 24)] for _ in range(10)])

    def __repr__(self):
        return f"<Message id:{self.msg_id}>"