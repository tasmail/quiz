class Errors:
    @staticmethod
    def user_is_already_exists(login):
        return dict(
            error='The specified login name "{}" is already exists!'.format(login),
            error_type='login_is_already_exists'
        )

    @staticmethod
    def user_not_found(login):
        return dict(
            error='The specified login name "{}" was not found!'.format(login),
            error_type='login_was_not_found'
        )

    @staticmethod
    def no_error():
        return dict(
            error_type='none'
        )
