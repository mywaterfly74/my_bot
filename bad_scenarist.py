from db import *


def positive_negative_check(text):
    result = '0'
    if text.lower() == 'да':
        result = '1'
    elif text.lower() == 'нет':
        result = '2'
    return result


def no_check(text):
    return '0'


checks = {
    'positive_negative': {
        'function': positive_negative_check,
        'variants': {
            '0': 'Нейтральный',
            '1': 'Положительный',
            '2': 'Отрицательный'
        }
    },
    'no': {
        'function': no_check,
        'variants': {
            '0': 'Нейтральный'
        }
    },
}


def run_next_step(poll_id, message):
    answer = 'Опрос закончен. Спасибо за прохождение'
    current_step_num = get_current_step_num(poll_id)
    steps = get_steps(poll_id)
    if current_step_num <= len(steps):
        if current_step_num != 0:
            current_step = steps[current_step_num - 1]
            check_res = checks[current_step['check_function_name']]['function'](message)
            add_answer(poll_id, current_step['pre_question'], message, current_step['check_variants'][check_res]['hint'])
            for i, additional_step in enumerate(current_step['check_variants'][check_res]['additional_steps']):
                insert_step(poll_id, additional_step, current_step_num + 1)
        inc_step_number(poll_id)
    if current_step_num < len(get_steps(poll_id)):
        answer = get_steps(poll_id)[current_step_num]['pre_question']
    return answer
