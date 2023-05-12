# 1. Створити клас Bot з атрибутом name та методами say_name та send_message.
# send_message має приймати параметри self і message і має друкувати message.
# Метод say_name має друкувати значення атрибуту name.


class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


# 2. Створити клас TelegramBot, який має бути унаслідуваний від Bot та має містити:
# власні атрибути url, chat_id (None за замовчуванням)
# методи send_message, set_url та set_chat_id.

class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        self.set_url(url)
        self.set_chat_id(chat_id)
        super().__init__(name)

    def send_message(self, message):
        print(f"{self.name} bot say {message} to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


if __name__ == "__main__":
    bot1 = Bot('Vania')
    bot1.send_message('Hello!')
    bot1.say_name()

    tg_bot = TelegramBot('TG')
    tg_bot.send_message('Hello!')
    tg_bot.say_name()
    tg_bot.set_chat_id(1)
    tg_bot.send_message('Hello!')
