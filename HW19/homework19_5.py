# 5. (необов'язкове виконання) Створити клас Bot та TelegramBot
# із першого завдання за допомогою функції type

def init_func(self, name):
    self.name = name


def send_message(self, message):
    print(message)


Bot = type("Bot", (),
           {
               "__init__": init_func,
               "send_message": send_message,
               "say_name": lambda self: print(f"My name is {self.name}")
           })

TelegramBot = type("TelegramBot", (Bot,),
                   {
                       "set_url": lambda self, url: setattr(self, "url", url),
                       "set_chat_id": lambda self, chat_id: setattr(self, "chat_id", chat_id),
                       "send_message": lambda self, message: print(
                           f"{self.name} bot say {message} to chat {self.chat_id} using {self.url}"),
                       "chat_id": None,
                       "url": None
                   })

if __name__ == "__main__":
    bot1 = Bot("Vasia")
    bot1.send_message("Hello")
    bot1.say_name()

    tg_bot = TelegramBot("TG")
    tg_bot.say_name()
    tg_bot.send_message("Hello")
    tg_bot.set_chat_id(1)
    tg_bot.send_message('Hello!')
