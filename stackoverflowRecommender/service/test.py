from UserService import UserService
from QuestionSerializer import QuestionSerializer


service = UserService(userName='jezrael')
questionsData = service.getFavoriteQuestions()
questions = []
for questionData in questionsData:
    question = QuestionSerializer.crateQuestionFromDict(questionData)
    questions.append(question)
user = service.getUser()
user.setFavoriteQuestions(questions)
print(user.getTopTags().keys())