import operator
from collections import defaultdict

class User():

    """
    Attributes:
        id: The Stackoverflow user id
        reputation: the reputation of the user
        displayName: Name of the user (String)
        websiteUrl: The user specicified personal websiet (URL)
        age: The age of the user (int)
        profileImage: The profile image or avatar (URL img)
        lastAccessDate: The last stackoverflow accesdate (Date)
        link: The stackoverflow profile link(URL)
        badgeCounts: {gold silver bronze} Int dictionary
    """

    def __init__(self, id, reputation, displayName, profileImage, link, lastAccessDate, badgeCounts, websiteUrl="", age=0, location=""):
        self.id = id
        self.reputation = reputation
        self.displayName = displayName
        self.profileImage = profileImage
        self.link = link
        self.lastAccessDate = lastAccessDate
        self.badgeCounts = badgeCounts

        #optional values
        self.websiteUrl = websiteUrl
        self.age = age
        self.location = location


    def setFavoriteQuestions(self, questions):
        self.favorites = questions

    def getFavoriteQuestions(self):
        return self.favorites

    def getTopTags(self):
        tagsDict = defaultdict(int)
        for question in self.favorites:
            # questionTags =dict(zip(question.tags, [1] * len(question.tags)))
            for question in question.tags:
                tagsDict[question] += 1
        # return sorted(tagsDict.items(), reverse=True, key=operator.itemgetter(1))
        return tagsDict

    def setRecommendedQuestions(self, questions):
        self.recommendedQuestions = questions

    def getRecommendedQuestions(self):
        return self.recommendedQuestions

    def getTopRecommendedTags(self):
        tagsDict = defaultdict(int)
        for question in self.recommendedQuestions:
            # questionTags =dict(zip(question.tags, [1] * len(question.tags)))
            for question in question.tags:
                tagsDict[question] += 1
        # return sorted(tagsDict.items(), reverse=True, key=operator.itemgetter(1))
        return tagsDict