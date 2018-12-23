from .api.user.user_handler import UserHandler


class ApiService:
    @staticmethod
    def get_handlers():
        handlers = [
            ('/api/user', UserHandler),
        ]
        return handlers
