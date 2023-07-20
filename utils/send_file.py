from Gibbon_sqlite import execute_query


def send_f(bot, id, sched_name):
        doc = open('Files/gibbon.txt', 'rb')
        bot.send_document(id, doc)

        query = f'''
                UPDATE Timer
                SET n_lesson = n_lesson + 1
                WHERE name = '{sched_name}'
        '''

        execute_query(query)