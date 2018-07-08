from django.apps import apps
from stackoverflowRecommender.service.QuestionService import QuestionService
from stackoverflowRecommender.processing.CollaborativeFilteringService import CollaborativeFilteringService
from stackoverflowRecommender.service.UserService import UserService

class SimilarQuestionsViewController:

    QUESTIONS_KEY = 'similarQuestions'
    QUESTION_KEY = 'question'
    USER_KEY = 'user'
    TOP_KEY = 'top'

    def __init__(self, template, context = {}, n=5):
        self.template = template
        self.context = context
        self.n = n


    def setContext(self, questionId, userId=None, userName=None, top=5):
        service = UserService(userId=userId, userName=userName)
        self.context[self.TOP_KEY] = top
        user = service.getUser()
        try:
            questionsData = CollaborativeFilteringService.getSimilarQuestions(questionId, n=top)
        except:
            raise AttributeError
        questionService = QuestionService(questionsData)
        questions = questionService.getQuestions()
        questionService.questionIds = [questionId]
        question = questionService.getQuestions()
        self.context['questionId'] = questionId
        self.context[self.QUESTION_KEY] = question
        self.context[self.QUESTIONS_KEY] = questions
        self.context[self.USER_KEY] = user