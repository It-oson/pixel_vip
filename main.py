import asyncio
from pyrogram import Client

# Укажите ваши учетные данные API
api_id = input('api id:')
api_hash = input('api hash:')

# Укажите ID ваших групп в виде списка строк
GROUP_IDS = []
user_input = input('чанд група добавиь мекни: ')
for i in range(int(user_input)):
    input_link = input('ссылкаи група пример( @tojokon )')
    GROUP_IDS.append(input_link)

# Текст для отправки
text_to_send = "Привет, это тестовое сообщение!\nбарои боти pixel"
# Инициализация клиента
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Функция для отправки сообщений в группы
async def send_messages():
    while True:
        for group_id in GROUP_IDS:
            try:
                await app.send_message(group_id, text_to_send)
                print(f"Сообщение отправлено в {group_id}")
            except Exception as e:
                print(f"Не удалось отправить сообщение в {group_id}: {e}")
        await asyncio.sleep(100)  # 3 минуты

# Главная функция
async def main():
    async with app:
        # Запуск задачи отправки сообщений
        await send_messages()

# Запуск бота
app.run(main())