import requests
import StackexchangeSettings
from UserSerializer import UserSerializer
import RecommenderRestSettings

class UserService:
    '''
    Attributes:
       userName: display name of the user on the stackoverflow site
       userId: the id of the given user
       user: a User model object containing the looaded data
       requestParams: the prameters used for a API request
    '''
    def __init__(self, userName = None, userId = None):
        self.userName = userName
        self.userId = userId
        self.requestParams = {
            'sort':'reputation',
            'order':'desc'
        }
        if userName is not None:
            self.requestParams['inname'] = userName
            self.__getUserByName__()
        if userId is not None:
            self.__getUserById__()

    def __getUserByName__(self):
        baseUrl = StackexchangeSettings.API_STACKEXCHANGE + 'users'
        self.requestParams.update(StackexchangeSettings.BASE_PARAMS)
        response = requests.get(baseUrl, params=self.requestParams)
        data = response.json()
        try:
            firstUserData = data['items'][0]
        except IndexError:
            raise
        self.userId = firstUserData['user_id']
        self.user = UserSerializer().createUserFromDictionary(firstUserData)
        return firstUserData

    def __getUserById__(self):
        baseUrl = StackexchangeSettings.API_STACKEXCHANGE + '/users/%s' % (self.userId)
        response = requests.get(baseUrl, params=StackexchangeSettings.BASE_PARAMS)
        data = response.json()['items'][0]
        self.user = UserSerializer().createUserFromDictionary(data)
        return data

    def getFavoriteQuestions(self):
        baseUrl = StackexchangeSettings.API_STACKEXCHANGE + '/users/%s/favorites' % (self.userId)
        response = requests.get(baseUrl, params=StackexchangeSettings.BASE_PARAMS)
        data = response.json()['items']
        return data

    def getRecommendedQuestionsBPR(self, top):
        url = RecommenderRestSettings.RECOMMENDATIONS_BPR
        params = {'userId':str(self.user.id), 'top':str(top)}
        response = requests.get(url, params=params)
        try:
            data = response.json()['topRecommendations']
        except:
            raise ValueError
        return data

    def getRecommendedQuestionsALS(self, top):
        url = RecommenderRestSettings.RECOMMENDATIONS_ALS
        params = {'userId':str(self.user.id), 'top':str(top)}
        response = requests.get(url, params=params)
        try:
            data = response.json()['topRecommendations']
        except:
            raise ValueError
        return data

    def getUser(self):
        return self.user