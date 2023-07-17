def check_user(message):
    return message.from_user.id != 806745936

def check_admin(message):
    return message.from_user.id == 806745936