import re
from aiogram import types


# Функции для фильтрации реплик
def net_answer_filter(message: types.Message) -> bool:
    net_regex: str = r"^(?:(?:[нНNnH]+[\W_]*)+(?:[еЕEe]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_ь]*$"
    result: list = re.findall(net_regex, message.text)
    return len(result) != 0


def nit_answer_filter(message: types.Message) -> bool:
    nit_regex: str = r"\b(?:(?:[нНNnH]+[\W_]*)+(?:[иИiIl]+[\W_]*)+(?:[тТTt]+[\W_]*)+)+[\W_]*$"
    result: list = re.findall(nit_regex, message.text)
    return len(result) != 0


def no_answer_filter(message: types.Message) -> bool:
    no_regex: str = r"""\b(?:(?:[нНH]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[уУy]+[_\W]*)+|
                        (?:[Nn]+[_\W]*)+(?:[OoоО]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(no_regex, message.text, flags=re.VERBOSE)
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
    yes_regex: str = r"""\b(?:(?:[йЙ]*[_\W]*)+(?:[еЕeE]+[_\W]*)+(?:[сСcC]+[_\W]*)+|
                         (?:[yY]+[_\W]*)+(?:[eEеЕ]+[_\W]*)+(?:[sS]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(yes_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def da_answer_filter(message: types.Message) -> bool:
    da_regex: str = r"^(?:(?:[дДdD]+[_\W]*)+(?:[аАaA]+[_\W]*)+)+[\W_]*$"
    result: list = re.findall(da_regex, message.text)
    return len(result) != 0


def traktorista_answer_filter(message: types.Message) -> bool:
    traktorista_regex: str = r"""\b(?:[тТtT]+[_\W]*[рРrRpP]+[_\W]*[ыЫиИiIl]+[_\W]*[сСsScC]+
                                 [_\W]*[тТtT]+[_\W]*[аАaAоОoO]+|(?<!(?:[ояуе]) )[З3](?:[_\W]*[0О]){2})+[\W_]*$"""
    result: list = re.findall(traktorista_regex, message.text, flags=re.VERBOSE)
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


def kak_answer_filter(message: types.Message) -> bool:
    kak_regex: str = r"(?:(?:[эЭeE][тТtT][оОoO] )|но |и |^)(?:[кКkK]+[_\W]*)+(?:[аАaA]+[_\W]*)+(?:[кКkK]+[_\W]*)+[\W_]*$"
    result: list = re.findall(kak_regex, message.text)
    return len(result) != 0


def zdraste_answer_filter(message: types.Message) -> bool:
    zdraste_regex: str = r"""\b(?:(?:[зЗzZ]+[_\W]*)+(?:[дДdD]+[_\W]*)+(?:[рРrRPp]+[_\W]*)+(?:[аАaA]+[_\W]*)+
                             (?:[сСsScC]+[_\W]*)+(?:[ьЬ]+[_\W]*)+(?:[тТtT]+[_\W]*)+(?:[еЕeEиИiIl]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(zdraste_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def kogda_answer_filter(message: types.Message) -> bool:
    kogda_regex: str = r"""\b(?:(?:[кКkK]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[гГgG]+[_\W]*)+(?:[дДdD]+
                            [_\W]*)+(?:[аАaA]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(kogda_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def pochemu_answer_filter(message: types.Message) -> bool:
    pochemu_regex: str = r"""\b(?:(?:[пП]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[чЧ]+[_\W]*)+
                             (?:[еЕeE]+[_\W]*)+(?:[мМM]+[_\W]*)+(?:[уУy]+[_\W]*)+|
                             (?:[рРpP]+[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[сСcC]+[_\W]*)+
                             (?:[НhH]+[_\W]*)+(?:[еЕeE]+[_\W]*)+(?:[МmM]+[_\W]*)+(?:[uU]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(pochemu_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def zachem_answer_filter(message: types.Message) -> bool:
    zachem_regex: str = r"""\b(?:(?:[зЗ3]+[_\W]*)+(?:[аАaA]+[_\W]*)+(?:[чЧ]+[_\W]*)+
                            (?:[еЕeE]+[_\W]*)+(?:[мМM]+[_\W]*)+|
                            (?:[zZ]+[_\W]*)+(?:[аАaA]+[_\W]*)+(?:[сСcC]+[_\W]*)+
                            (?:[НhH]+[_\W]*)+(?:[еЕeE]+[_\W]*)+(?:[МmM]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(zachem_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def mne_answer_filter(message: types.Message) -> bool:
    mne_regex: str = r"""^(?:(?:[нНnNH]*[_\W]*)+(?:[уУuUy]+[_\W]*)+)?(?:(?:[аАaA]+[_\W]*)+
                                (?:[мМmM]+[_\W]*)+(?:[нНnNH]+[_\W]*)+(?:[еЕeE]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(mne_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def vot_ona_answer_filter(message: types.Message) -> bool:
    vot_ona_regex: str = r"""^(?:(?:[вВvVB]*[_\W]*)+(?:[оОoO]+[_\W]*)+(?:[тТtT]+[_\W]*)+)?
                             (?:(?:[оОoO]+[_\W]*)+(?:[нНnNH]+[_\W]*)+(?:[аАaA]+[_\W]*)+)+[\W_]*$"""
    result: list = re.findall(vot_ona_regex, message.text, flags=re.VERBOSE)
    return len(result) != 0


def chto_podelat_answer_filter(message: types.Message) -> bool:
    chto_podelat_regex: str = r"^(?:ну )?что (?:по)?(?:делать)+[\W_]*$"
    result: list = re.findall(chto_podelat_regex, message.text, flags=re.IGNORECASE)
    return len(result) != 0


def friday(message: types.Message) -> bool:
    friday: str = r"(?:пятница|p[iy]atnit*[sz]a)[\W_]*$"
    result: list = re.findall(friday, message.text, flags=re.IGNORECASE)
    return len(result) != 0
