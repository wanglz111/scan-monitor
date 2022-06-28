import imp
import telegram
import datetime
import asyncio


async def main():
    # proxy = telegram.utils.request.Request(proxy_url='socks5://127.0.0.1:7890')
    bot = telegram.Bot(token="")
    async with bot:
        # messages = await bot.get_updates()
        # for message in messages:
        #     print(message)
        # print(str(await bot.get_updates()))
        text = "Hello World!\n" + "I'm a bot!\n" + "time: " + str(datetime.datetime.now())
        await bot.send_message(text=text, chat_id=5437922280)
        # print(( await bot.get_updates())[0])


# print(bot.get_me())
#     async with bot:
#         print((await bot.get_updates())[0])


if __name__ == '__main__':
    asyncio.run(main())