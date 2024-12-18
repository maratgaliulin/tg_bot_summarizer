from aiogram.filters.state import State, StatesGroup

class AddSummarizerStates(StatesGroup):
    summarizer = State()

class EditSummarizerStates(StatesGroup):
    summarizer = State()

class DeleteSummarizerStates(StatesGroup):
    delete_command = State()