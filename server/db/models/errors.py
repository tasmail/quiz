class Errors:
    @staticmethod
    def user_is_already_exists(login):
        return dict(
            error='The specified login name "{}" is already exists!'.format(login),
            error_type='user_is_already_exists'
        )

    @staticmethod
    def user_not_found(login):
        return dict(
            error='The specified login name "{}" was not found!'.format(login),
            error_type='user_was_not_found'
        )

    @staticmethod
    def quiz_is_already_exists(name):
        return dict(
            error='The specified Quiz name "{}" is already exists!'.format(name),
            error_type='quiz_is_already_exists'
        )

    @staticmethod
    def quiz_not_found(name):
        return dict(
            error='The specified Quiz name "{}" was not found!'.format(name),
            error_type='quiz_not_found'
        )

    @staticmethod
    def question_is_already_exists(question):
        return dict(
            error='The specified Question "{}" is already exists!'.format(question),
            error_type='question_is_already_exists'
        )

    @staticmethod
    def question_not_found(question):
        return dict(
            error='The specified Question "{}" was not found!'.format(question),
            error_type='question_not_found'
        )

    @staticmethod
    def question_choice_is_already_exists(choice):
        return dict(
            error='The specified Question choice "{}" is already exists!'.format(choice),
            error_type='question_choice_is_already_exists'
        )

    @staticmethod
    def question_choice_not_found(choice):
        return dict(
            error='The specified Question choice "{}" was not found!'.format(choice),
            error_type='question_choice_not_found'
        )

    @staticmethod
    def user_quiz_is_already_exists(user_id, quiz_id):
        return dict(
            error='The specified User quiz user_id:{}, quiz_id:{} is already exists!'.format(user_id, quiz_id),
            error_type='user_quiz_is_already_exists'
        )

    @staticmethod
    def user_quiz_not_found(user_id, quiz_id):
        return dict(
            error='The specified User quiz user_id:{}, quiz_id:{} was not found!'.format(user_id, quiz_id),
            error_type='user_quiz_not_found'
        )

    @staticmethod
    def user_answer_is_already_exists(user_quiz_id, question_choice_id):
        return dict(
            error='The specified user answer user_quiz_id:{}, question_choice_id:{} is already exists!'.format(
                user_quiz_id, question_choice_id),
            error_type='user_answer_is_already_exists'
        )

    @staticmethod
    def user_answer_not_found(user_quiz_id, question_choice_id):
        return dict(
            error='The specified user answer user_quiz_id:{}, question_choice_id:{} was not found!'.format(
                user_quiz_id, question_choice_id),
            error_type='user_answer_not_found'
        )

    @staticmethod
    def no_error():
        return dict(
            error_type='none'
        )
