from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from scraping.scraping_info import circulating_supply_coins


async def circulating_supply(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    supply = await circulating_supply_coins(data["coin"])
    await call.message.answer(supply)


def register_circulating_supply(dp: Dispatcher):
    dp.register_callback_query_handler(circulating_supply, lambda callback: callback.data == "circulating_supply")
