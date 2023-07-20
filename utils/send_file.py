def send_f(bot, id):
        doc = open('Files/gibbon.txt', 'rb')
        bot.send_document(id, doc)
