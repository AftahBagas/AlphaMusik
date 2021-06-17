from telethon import Client
from teletgcalls import teleTgCalls

import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
teletgcalls = teleTgCalls(client)


@teletgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        teletgcalls.leave_group_call(chat_id)
    else:
        teletgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"]
        )


run = teletgcalls.run
