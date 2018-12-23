from .api.user.user_handler import UserHandler


class ApiService:
    @staticmethod
    def get_handlers():
        handlers = [
            ('/api/v1/user', UserHandler),
        ]
        return handlers
