import pymongo
from bson import ObjectId
from pymongo import MongoClient

from steps import Step, CheckVariant

client = MongoClient('mongo', 27017)
db = client.m_bot
base_scenario_collection = db.base_scenario_collection
polls_scenario_collection = db.polls_scenario_collection
check_func_collection = db.check_func_collection


def get_available_check_funcs():
    return list(check_func_collection.find())


def new_poll():
    return polls_scenario_collection.insert_one({
        'current_step': 0,
        'steps': [],
        'answers': []
    }).inserted_id


def get_current_step_num(poll_id):
    poll = polls_scenario_collection.find_one({'_id': ObjectId(poll_id)})
    if poll:
        return poll['current_step']


def get_steps(poll_id):
    poll = polls_scenario_collection.find_one({'_id': ObjectId(poll_id)})
    if poll:
        return poll['steps']


def add_step(poll_id, step):
    polls_scenario_collection.update_one(
        {'_id': ObjectId(poll_id)},
        {'$push': {'steps': step}}
    )


def insert_step(poll_id, step, position: int):
    current_steps = get_steps(poll_id)
    current_steps.insert(position, step)
    polls_scenario_collection.update_one(
        {'_id': ObjectId(poll_id)},
        {'$set': {'steps': current_steps}}
    )


def clear_steps(poll_id):
    polls_scenario_collection.update_one(
        {'_id': ObjectId(poll_id)},
        {'$set': {'steps': []}}
    )


def add_answer(poll_id, question, answer, hint):
    polls_scenario_collection.update_one(
        {'_id': ObjectId(poll_id)},
        {'$push': {'answers': {
            'question': question,
            'answer': answer,
            'hint': hint
        }}}
    )


def inc_step_number(poll_id):
    polls_scenario_collection.update_one(
        {'_id': ObjectId(poll_id)},
        {'$inc': {'current_step': 1}}
    )


def get_answers(poll_id):
    poll = polls_scenario_collection.find_one({'_id': ObjectId(poll_id)})
    return poll['answers']


# id = new_poll()
# step = Step(
#     pre_question='Ваши родственники болели гриппом в последние 2 месяца?',
#     check_function_name='positive_negative',
#     check_variants={
#         '0': CheckVariant(),
#         '1': CheckVariant(
#             additional_steps=[
#                 Step(
#                     pre_question='Как давно они болели?',
#                     check_function_name='no',
#                     check_variants={
#                         '0': CheckVariant()
#                     }
#                 )
#             ]
#         ),
#         '2': CheckVariant(
#             hint='Здоровые родственники'
#         )
#     }
# )
# print(add_step(id, step.to_dict()))
# print(add_step(id, step.to_dict()))
# print(add_step(id, step.to_dict()))


# print(add_answer('5c177f06d9c3702c494049a7', 'Вопрос', 'Ответ', 'Подсказка'))
