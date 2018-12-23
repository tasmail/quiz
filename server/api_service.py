
class ApiService:
    @staticmethod
    def get_handlers():
        handlers = [
            ('/api/user', UserHandler),
            ('/api/card', CardHandler),
            ('/api/comment', CommentHandler),
            ('/api/category', CategoryHandler),
            ('/api/favorites', FavoritesHandler),
            ('/api/question', QuestionHandler),
            ('/api/answer', AnswerHandler),
        ]
        return handlers
