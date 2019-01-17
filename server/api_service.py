from server.api.handlers import UserHandler, QuestionHandler, QuestionChoiceHandler, QuizHandler, UserAnswerHandler, \
    UserQuizHandler, QuizCategoryHandler


class ApiService:
    @staticmethod
    def get_handlers():
        handlers = {
            ('/api/v1/question/([0-9]+)', QuestionHandler),
            ('/api/v1/question', QuestionHandler),
            ('/api/v1/question-choice/([0-9]+)', QuestionChoiceHandler),
            ('/api/v1/question-choice', QuestionChoiceHandler),
            ('/api/v1/quiz/([0-9]+)', QuizHandler),
            ('/api/v1/quiz', QuizHandler),
            ('/api/v1/quiz-category/([0-9]+)', QuizCategoryHandler),
            ('/api/v1/quiz-category', QuizCategoryHandler),
            ('/api/v1/user/([0-9]+)', UserHandler),
            ('/api/v1/user', UserHandler),
            ('/api/v1/user-answer/([0-9]+)', UserAnswerHandler),
            ('/api/v1/user-answer', UserAnswerHandler),
            ('/api/v1/user-quiz/([0-9]+)', UserQuizHandler),
            ('/api/v1/user-quiz', UserQuizHandler),
        }
        return handlers
