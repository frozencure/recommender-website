# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from .forms import QuestionForm
from stackoverflowRecommender.controllers.ProfileViewController import ProfileViewController
from stackoverflowRecommender.controllers.SimilarQuestionsViewController import SimilarQuestionsViewController
from stackoverflowRecommender.controllers.RecommendationsViewController import RecommendationsViewController


def loadProfile(request):
    if request.method == "GET":
        userName = request.GET.get('userName')
        viewController = ProfileViewController(template= 'profile.html')
        try:
            viewController.setContext(userName=userName)
        except:
            messages.warning(request, 'Error: User not found')
            return render(request, 'alert.html')
    return render(request, viewController.template, viewController.context)

def getSimilarQuestions(request):
    if request.method == "GET":
        questionId = request.GET.get('questionId')
        top = request.GET.get('top')
        userId = request.GET.get('userId')
        userName = request.GET.get('userName')
        viewController = SimilarQuestionsViewController(template='similarQuestions.html')
        if userId is not None:
            if top is not None:
                try:
                    viewController.setContext(questionId, userId=int(userId), top=top)
                except:
                    messages.warning(request, 'Error: Question has to few favourites')
                    return render(request, 'alert.html')
            else:
                try:
                    viewController.setContext(questionId, userId=int(userId))
                except:
                    messages.warning(request, 'Error: Question has to few favourites')
                    return render(request, 'alert.html')
        if userName is not None:
            if top is not None:
                try:
                    viewController.setContext(questionId, userName=userName, top=top)
                except:
                    messages.warning(request, 'Error: Question has to few favourites')
                    return render(request, 'alert.html')
            else:
                try:
                    viewController.setContext(questionId, userName=userName)
                except:
                    messages.warning(request, 'Error: Question has to few favourites')
                    return render(request, 'alert.html')
    return render(request, viewController.template, viewController.context)

def loadRecommendations(request):
    if request.method == "GET":
        userId = request.GET.get('userId')
        top = request.GET.get('top')
        model = request.GET.get('model')
        viewController = RecommendationsViewController(template='recommendations.html')
        if top is not None:
            try:
                viewController.setContext(userId=userId, model=model, top=int(top))
            except:
                messages.warning(request, 'Error: User has to few votes')
                return render(request, 'alert.html')
        else:
            try:
                viewController.setContext(userId=userId, model=model)
            except:
                messages.warning(request, 'Error: User has to few votes')
                return render(request, 'alert.html')
    return render(request, viewController.template, viewController.context)

def login(request):
    template = 'login.html'
    context = {}
    if request.method == "GET":
        form = QuestionForm()
        context['form'] = form
    return render(request, template, context)