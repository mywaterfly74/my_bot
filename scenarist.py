# class Step:
#     def __init__(self, pre_mess, check_func):
#         self.pre_mess = pre_mess
#         self.check_func = check_func
#         self.check_results
#
#
# class CheckFunc:
#     def __init__(self, name, func, check_result_variants):
#         self.name = name
#         self.func = func
#         self.check_result_variants = check_result_variants
#
#
# class CheckResultVariant:
#     def __init__(self, check_result_id, name, description, kwargs_name_list):
#         self.check_result_id = check_result_id
#         self.name = name
#         self.description = description
#         self.kwargs_name_list = kwargs_name_list
#
#
# def positive_negative_check(text, keywords):
#     result = 0
#     if text.lower() == 'да':
#         result = 1
#     elif text.lower() == 'нет':
#         result = 2
#     return result
#
#
# positive_negative_check = CheckFunc(
#     name='positive_negative_check',
#     func=positive_negative_check,
#     check_result_variants=[
#         CheckResultVariant(
#             check_result_id=1,
#             name='positive',
#             description='Положительный ответ',
#             kwargs_name_list=['text', 'keywords']
#     )
# )