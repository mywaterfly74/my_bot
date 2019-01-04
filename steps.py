class CheckVariant:
    def __init__(self, hint=None, additional_steps=None):
        self.hint = hint
        self.additional_steps = additional_steps or []

    def to_dict(self):
        return {
            'hint': self.hint,
            'additional_steps': [step.to_dict() for step in self.additional_steps]
        }


class Step:
    def __init__(self, pre_question, check_function_name, check_variants):
        self.pre_question = pre_question
        self.check_function_name = check_function_name
        self.check_variants = check_variants

    def to_dict(self):
        return {
            'pre_question': self.pre_question,
            'check_function_name': self.check_function_name,
            'check_variants': {k: self.check_variants[k].to_dict() for k in self.check_variants.keys()}
        }