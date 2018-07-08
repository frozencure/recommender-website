import requests
from stackoverflowRecommender.service import RecommenderRestSettings


class CollaborativeFilteringService:

    BASE_URL = RecommenderRestSettings.SIMILAR_QUESTIONS

    @staticmethod
    def getSimilarQuestions(questionId, n):
        url = CollaborativeFilteringService.BASE_URL
        params = {'questionId': str(questionId), 'top': str(n)}
        response = requests.get(url, params=params)
        content = response.json()['similarQuestions']
        try:
            return [int(key) for key in content.keys()]
        except:
            raise AttributeError