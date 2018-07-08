from datetime import datetime
from stackoverflowRecommender.models.Question import Question

ID_KEY = 'question_id'
TITLE_KEY = 'title'
CREATION_DATE_KEY = 'creation_date'
VIEW_COUNT_KEY = 'view_count'
LINK_KEY = 'link'
TAGS_KEY = 'tags'
IS_ANSWERED_KEY = 'is_answered'

class QuestionSerializer:
    @staticmethod
    def crateQuestionFromDict(questionDict):
        id = questionDict[ID_KEY]
        title = questionDict[TITLE_KEY]
        creationDate = datetime.fromtimestamp(questionDict[CREATION_DATE_KEY])
        viewCount = questionDict[VIEW_COUNT_KEY]
        link = questionDict[LINK_KEY]
        tags= questionDict[TAGS_KEY]
        isAnswered = questionDict[IS_ANSWERED_KEY]
        return Question(id, title, creationDate, viewCount, link, tags, isAnswered)
