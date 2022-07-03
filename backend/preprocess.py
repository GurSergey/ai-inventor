import re

SEP_TOKEN = ' [SEP] '
MAX_INPUT_LENGTH = 512


def check_concatenated_input(concatenated_input: str) -> bool:
    """

    :param input:
    :return:
    """
    if len(concatenated_input.split()) > MAX_INPUT_LENGTH:
        return False
    return True


def concatenate_question(industries: str, faults: str, targets: str, currents: str) -> str:
    """

    :param industries:
    :param faults:
    :param targets:
    :param currents:
    :return:
    """
    return industries + SEP_TOKEN + faults + SEP_TOKEN + targets + SEP_TOKEN + currents


def preprocess(text: str) -> str:
    """

    :param text:
    :return:
    """
    return re.sub(r'[^A-zА-я\[\]\s\-]', ' ', text)
