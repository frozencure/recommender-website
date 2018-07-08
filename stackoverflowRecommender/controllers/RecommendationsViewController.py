from stackoverflowRecommender.service.UserService import UserService
from stackoverflowRecommender.service.QuestionService import QuestionService
import operator

class RecommendationsViewController:

    USER_KEY = 'user'
    LENGTH_KEY = 'length'
    USER_NAME_REQUEST_KEY = 'userName'
    LABELS_KEY = 'labels'
    VALUES_KEY = 'values'
    BACKGROUND_COLORS_KEY = 'bgColors'
    BORDER_COLORS_KEY = 'borderColors'
    QUESTIONS_KEY = 'questions'
    TOP_KEY='top'

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



    def setContext(self, userId, model, top=10):
        service = UserService(userId=userId)
        self.context['model'] = model
        user = service.getUser()
        self.context[self.TOP_KEY] = top
        self.context[self.USER_KEY] = user
        questionIds = None
        if model == 'BPR':
            try:
                questionIds = service.getRecommendedQuestionsBPR(top=top)
            except:
                raise ValueError
        if model == 'ALS':
            try:
                questionIds = service.getRecommendedQuestionsALS(top=top)
            except:
                raise ValueError
        questionService = QuestionService(questionIds=questionIds)
        questions = questionService.getQuestions()
        self.context[self.QUESTIONS_KEY] = questions
        user.setRecommendedQuestions(questions)
        topTags = sorted(user.getTopRecommendedTags().items(), reverse=True, key=operator.itemgetter(1))
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