from stackoverflowRecommender.service.QuestionSerializer import QuestionSerializer
from stackoverflowRecommender.service.UserService import UserService
import operator

class ProfileViewController:

    USER_KEY = 'user'
    LENGTH_KEY = 'length'
    USER_NAME_REQUEST_KEY = 'userName'
    LABELS_KEY = 'labels'
    VALUES_KEY = 'values'
    BACKGROUND_COLORS_KEY = 'bgColors'
    BORDER_COLORS_KEY = 'borderColors'
    QUESTIONS_KEY = 'questions'

    colors = [
        'rgba(244,122,32,',
        'rgba(244,138,31,',
        'rgba(210,138,41,',
        'rgba(192,148,82,',
        'rgba(166,138,110,',
        'rgba(129,129,133,',
    ]


    def __init__(self, template, context = {}, bars=5):
        self.template = template
        self.context = context
        self.bars = bars



    def setContext(self, userName):
        try:
            service = UserService(userName=userName)
        except IndexError:
            raise IndexError
        user = service.getUser()
        self.context[self.USER_KEY] = user
        questions = [QuestionSerializer.crateQuestionFromDict(questionData) for questionData in
                     service.getFavoriteQuestions()]
        self.context[self.QUESTIONS_KEY] = questions
        user.setFavoriteQuestions(questions)
        topTags = sorted(user.getTopTags().items(), reverse=True, key=operator.itemgetter(1))
        labels = []
        values = []
        for index, tag in enumerate(topTags):
            if index == self.bars:
                break
            labels.append(tag[0])
            values.append(tag[1])
        self.context[self.LABELS_KEY] = labels
        self.context[self.VALUES_KEY] = values
        self.context[self.LENGTH_KEY] = len(labels)
        self.context[self.BACKGROUND_COLORS_KEY] = self.__generateColors__(0.7)
        self.context[self.BORDER_COLORS_KEY] = self.__generateColors__(1)

    def __generateColors__(self, opacity = 0.3):
        tempColors = []
        for index, colorString in enumerate(self.colors):
            if index == self.bars:
                break;
            colorString += str(opacity) + ')'
            tempColors.append(colorString)
        return tempColors