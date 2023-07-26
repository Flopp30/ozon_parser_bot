from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()

builder.button(
    text="Действие 1”", url="https://google.com/"
)
builder.button(
    text="Действие 2”", url="https://google.com/"
)
builder.button(
    text="Действие 3”", url="https://google.com/"
)
builder.adjust(1)

MAIN_BOARD = builder.as_markup()
