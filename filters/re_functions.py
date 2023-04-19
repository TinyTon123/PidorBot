import re
from aiogram import types


def net_answer_filter(message: types.Message) -> bool:
    net_regex: str = r"\b(?:(?:[нНNnH]+[\W_]*)+(?:[еЕEe]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_ь]*$"
    result: list = re.findall(net_regex, message.text)
    return len(result) != 0


def nit_answer_filter(message: types.Message) -> bool:
    nit_regex: str = r"\b(?:(?:[нНNnH]+[\W_]*)+(?:[иИiIl]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(nit_regex, message.text)
    return len(result) != 0


def no_answer_filter(message: types.Message) -> bool:
    no_regex: str = r"\b(?:(?:[нНH]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[уУy]+[_\W]*)+|(?:[Nn]+[_\W]*)+(?:[OoоО]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(no_regex, message.text)
    return len(result) != 0


def nope_answer_filter(message: types.Message) -> bool:
    nope_regex: str = r"\b(?:(?:[нНNnH]+[_\W]*)+(?:[оОOo]+[_\W]*)+(?:[уУpP]+[_\W]*)+(?:[пПeEеЕ]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(nope_regex, message.text)
    return len(result) != 0


def nein_answer_filter(message: types.Message) -> bool:
    nein_regex: str = r"\b(?:(?:[нНNnH]+[_\W]*)+(?:[АаEe]+[_\W]*)+(?:[ЙйIi]+[_\W]*)+(?:[нНNnH]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(nein_regex, message.text)
    return len(result) != 0


def yes_answer_filter(message: types.Message) -> bool:
    yes_regex: str = r"\b(?:(?:[йЙ]*[_\W]*)+(?:[еЕeE]+[_\W]*)+(?:[сСcC]+[_\W]*)+|(?:[yY]+[_\W]*)+(?:[eEеЕ]+[_\W]*)+(?:[sS]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(yes_regex, message.text)
    return len(result) != 0


def da_answer_filter(message: types.Message) -> bool:
    da_regex: str = r"^(?:(?:[дДdD]+[_\W]*)+(?:[аАaA]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(da_regex, message.text)
    return len(result) != 0


def traktorista_answer_filter(message: types.Message) -> bool:
    traktorista_regex: str = r"\b(?:[тТtT]+[_\W]*[рРrRpP]+[_\W]*[ыЫиИiIl]+[_\W]*[сСsScC]+[_\W]*[тТtT]+[_\W]*[аАaAоОoO]+|(?<!(?:[ояуе]) )[З3](?:[_\W]*[0О]){2})+[\W_]*$"
    result: list = re.findall(traktorista_regex, message.text)
    return len(result) != 0


def gde_answer_filter(message: types.Message) -> bool:
    gde_regex: str = r"\b(?:(?:[gGгГ]+[\W_]*)+(?:[дДdD]+[\W_]*)+(?:[еЕeE]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(gde_regex, message.text)
    return len(result) != 0


def nu_answer_filter(message: types.Message):
    nu_regex: str = r"\b(?:(?:[нНnNH]+[\W_]*)+(?:[уУuUy]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(nu_regex, message.text)
    return len(result) != 0


def kto_answer_filter(message: types.Message) -> bool:
    kto_regex: str = r"\b(?:(?:[кКkK]+[_\W]*)+(?:[тТtT]+[_\W]*)+(?:[оОoO]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(kto_regex, message.text)
    return len(result) != 0


def cho_answer_filter(message: types.Message) -> bool:
    cho_regex: str = r"\b(?:(?:[чЧ]+[_\W]*)+(?:[оОеЕeEёЁoO]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(cho_regex, message.text)
    return len(result) != 0
