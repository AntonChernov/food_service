from channels import Group


def ws_add(message):
    message.reply_channel.send({'accept': True})
    Group('accept_order').add(message.reply_channel)


def ws_message(message):
    Group('accept_order').send({'text': '{}'.format(message.content['new_order'])})


def ws_disconnect(message):
    Group("accept_order").discard(message.reply_channel)

