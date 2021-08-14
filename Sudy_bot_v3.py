# Конфигурация бота хранится
# во внешнем файле для сохранения
# анонимности токена.
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) # Указания пути
from config import token # Импорт токена

# Подключения модулей для бота
import discord
from discord.ext import tasks, commands # Возможность создания команд
from discord import utils
from discord.utils import get
from discord.voice_client import VoiceClient

# Префикс бота
bot = commands.Bot(command_prefix='~') 

# Токен бота
# Для прямого подключения
# удалить строку с 1 по 8
# и заменить переменную token
TOKEN = token

#id админа
ADMIN_ID = 412277201917050881

# Функция для проверки
# запущен ли бот
@bot.event
async def on_ready ():
	print(bot.user.name + ": I a'm here!")

# Функция для отслеживания
# чата в командной строке
@bot.event
async def on_message(message):
	print(message.author.name + ": " + message.content)
	await bot.process_commands(message)

# Простенькая команда
# для вызова картинки
@bot.command()
async def AWIX(ctx):
	await ctx.send('https://memepedia.ru/wp-content/uploads/2018/07/p19c48onct1f2j1f6k136m1qtr17bv33.jpg')

# Команда отключения бота
# работает только если id автора
# совпал с id создателем
@bot.command()
async def Sudy_off(ctx):
	print(ctx.message.author.id)
	if (ctx.message.author.id == ADMIN_ID):
		await ctx.send('Всем пока!')
		await ctx.bot.close()
	else:
		await ctx.send('От тебя такое слышать обидно!')

bot.run(TOKEN)
exit(1)