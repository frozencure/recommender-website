from stackoverflowRecommender.models.User import User
from datetime import datetime

ID_KEY = 'user_id'
DISPLAY_NAME_KEY = 'display_name'
LOCATION_KEY = 'location'
REPUTATION_KEY = 'reputation'
WEBSITE_URL_KEY = 'website_url'
AGE_KEY = 'age'
PROFILE_IMAGE_KEY = 'profile_image'
LAST_ACCESS_DATE_KEY = 'last_access_date'
LINK_KEY = 'link'
BADGE_COUNTS_KEY = 'badge_counts'
GOLD_KEY = 'gold'
SILVER_KEY = 'silver'
BRONZE_KEY = 'bronze'
class UserSerializer:
    @staticmethod
    def createUserFromDictionary(userDict):
        id = userDict[ID_KEY]
        reputation = userDict[REPUTATION_KEY]
        displayName = userDict[DISPLAY_NAME_KEY]
        profileImage = userDict[PROFILE_IMAGE_KEY]
        link = userDict[LINK_KEY]
        lastAccessDate = userDict[LAST_ACCESS_DATE_KEY]
        lastAccessDate = datetime.fromtimestamp(lastAccessDate)
        badgeCounts = userDict[BADGE_COUNTS_KEY]

        # optional values
        try:
            websiteUrl = userDict[WEBSITE_URL_KEY]
        except KeyError:
            websiteUrl = None
        try:
            age = userDict[AGE_KEY]
        except KeyError:
            age = None
        try:
            location = userDict[LOCATION_KEY]
        except KeyError:
            location = None
        return User(id, reputation, displayName, profileImage, link, lastAccessDate, badgeCounts, websiteUrl, age, location)