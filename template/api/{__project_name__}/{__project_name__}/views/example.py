from random import randint
from sanic import response

from {__project_name__}.controller.example import MessagesController



ec = MessagesController()


async def root(request):
    msg = ec.get_message_by_id(106)
    return response.json(
        {
            "message": "hello world, this is {__project_name__}",
            "content": {
                "id": msg.msg_id,
                "message": msg.message
            }
        },
        status=200
    )
