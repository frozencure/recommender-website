from mysite import settings

if settings.RUN_CONFIG == 'gcloud':
    API_RECOMMENDER_REST = 'https://recommender-rest.appspot.com/api/v1.0/'
elif settings.RUN_CONFIG == 'local':
    API_RECOMMENDER_REST = 'http://127.0.0.1:8080/api/v1.0/'

SIMILAR_QUESTIONS = API_RECOMMENDER_REST + 'similarQuestions'

RECOMMENDATIONS_BPR = API_RECOMMENDER_REST + 'topRecommendationsBPR'
RECOMMENDATIONS_ALS = API_RECOMMENDER_REST + 'topRecommendationsALS'

