from Gibbon_sqlite import execute_query

from utils.sql_snipets import Update

from telebot.apihelper import ApiTelegramException


def send_f(bot, id, sched_name):
		doc = open('Files/gibbon.txt', 'rb')
		try:
			bot.send_document(id, doc)

			query = Update("n_lesson = n_lesson + 1").where(f"name = '{sched_name}'")

			execute_query(query)

		except ApiTelegramException:
			print(f'chat with id({id}) not found')
