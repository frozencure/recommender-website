import requests
import StackexchangeSettings
from QuestionSerializer import QuestionSerializer

class QuestionService:
    '''
    Attributes:
        questionId: the Stackoverflow id of the question
    '''

    def __init__(self, questionIds):
        self.questionIds = questionIds



    def getQuestions(self):
        baseRequest = StackexchangeSettings.API_STACKEXCHANGE + "questions/"
        questionIdsStr = ';'.join(str(questionId) for questionId in self.questionIds)
        baseRequest += questionIdsStr
        response = requests.get(baseRequest, params=StackexchangeSettings.BASE_PARAMS)
        data = response.json()['items']
        questions = [QuestionSerializer.crateQuestionFromDict(questionDict) for questionDict in data]
        return questions