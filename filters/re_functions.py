import re
from aiogram import types


def net_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[нНNnH]+[\W_]*)+(?:[еЕEe]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_ь]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def nit_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[нНNnH]+[\W_]*)+(?:[иИiIl]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def no_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[нНH]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[уУy]+[_\W]*)+|(?:[Nn]+[_\W]*)+(?:[OoоО]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def nope_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[нНNnH]+[_\W]*)+(?:[оОOo]+[_\W]*)+(?:[уУpP]+[_\W]*)+(?:[пПeEеЕ]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def nein_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[нНNnH]+[_\W]*)+(?:[АаEe]+[_\W]*)+(?:[ЙйIi]+[_\W]*)+(?:[нНNnH]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def yes_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[йЙ]*[_\W]*)+(?:[еЕeE]+[_\W]*)+(?:[сСcC]+[_\W]*)+|(?:[yY]+[_\W]*)+(?:[eEеЕ]+[_\W]*)+(?:[sS]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def da_otvet_filter(message: types.Message) -> bool:
    regex: str = r"^(?:(?:[дДdD]+[_\W]*)+(?:[аАaA]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def traktorista_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:[тТtT]+[_\W]*[рРrRpP]+[_\W]*[ыЫиИiIl]+[_\W]*[сСsScC]+[_\W]*[тТtT]+[_\W]*[аАaAоОoO]+|(?<!(?:[ояуе]) )[З3](?:[_\W]*[0О]){2})+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def gde_otvet_filter(message: types.Message) -> bool:
    regex: str = r"\b(?:(?:[gGгГ]+[\W_]*)+(?:[дДdD]+[\W_]*)+(?:[еЕeE]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0


def nu_otvet_filter(message: types.Message):
    regex: str = r"\b(?:(?:[нНnNH]+[\W_]*)+(?:[уУuUy]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(regex, message.text)
    return len(result) != 0
