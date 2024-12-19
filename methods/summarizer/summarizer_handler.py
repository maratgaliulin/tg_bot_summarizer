from methods.summarizer.summarizer_states import AddSummarizerStates
from methods.components.summarize_text import summarize_text

from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
import os

# all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

summarizer_handler_router = Router()

@summarizer_handler_router.message(Command("start"))
async def cmd_start_insert_text(message: types.Message, state:FSMContext):  
    await state.set_state(AddSummarizerStates.summarizer)   
    await message.answer(f"Здравствуйте! Введите пожалуйста текст для конспекта!")

@summarizer_handler_router.message(AddSummarizerStates.summarizer)
async def lets_see(message: types.Message, state:FSMContext): 
    await state.update_data(summarizer=message.text)
    await message.answer('Подождите, ваш запрос обрабатывается...')
    data = await state.get_data()
    await state.clear()
    summarized_string = summarize_text(data['summarizer'])
    
    await message.answer(f"Краткое содержание статьи:\n\n{summarized_string}")