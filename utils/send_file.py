from Gibbon_sqlite import execute_query, execute_read_query

from utils.sql_orm import Update, Select

from telebot.apihelper import ApiTelegramException


def send_f(bot, id, sched_name):
		n_lesson = execute_read_query(Select(['n_lesson']).where(f'name = "{sched_name}"'))[0][0]
		doc = open(f'Files/CW{n_lesson}.pdf', 'rb')
		doc2 = open(f'Files/HW{n_lesson}.pdf', 'rb')

		docs = [doc, doc2]

		try:
			for d in docs:
				bot.send_document(id, d)

			query = Update("n_lesson = n_lesson + 1").where(f"name = '{sched_name}'")

			execute_query(query)

		except ApiTelegramException as e:
			print(e)
