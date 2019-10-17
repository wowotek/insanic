from {__project_name__}.models import Messages

class MessagesController:
    def get_message_by_id(self, id):
        return Messages()