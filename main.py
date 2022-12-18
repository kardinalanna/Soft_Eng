from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from youtube_search import YoutubeSearch
import hashlib

def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    return res
    
@dp.inline_handler() #работает в inline режиме
async def inline_handler(query: types.InlineQuery, search=""):
    text = query.query or 'echo' #сюда попадает запрос
    links = searcher(text) #запрос отправляем на парсинг
        articles = [types.InlineQueryResultArticle( #окно с результатами парсинга
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}'
        )
    )for link in links]
    
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)