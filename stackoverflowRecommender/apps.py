# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.apps import AppConfig

class StackoverflowrecommenderConfig(AppConfig):
    name = 'stackoverflowRecommender'

    def __init__(self, app_name, app_module):
        super(StackoverflowrecommenderConfig, self).__init__(app_name, app_module)
        # self.sparseDf = None

    # def getResourcesPath(self):
    #     # repo_path = str(pathlib.Path(os.getcwd()).parent)
    #     repo_path = "C:/Users/Iancu/PycharmProjects/Stackoverflow_Recommendations/stackoverflow-recommendations"
    #     return repo_path + '/resources/matrix.npz'

    # def ready(self):
    #     if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    #         path = self.read_file('recomme-196220.appspot.com/matrix.npz')
    #     else:
    #         path = self.getResourcesPath()
    #     if self.sparseDf is None:
    #         self.sparseDf = SparseDataframe(filePath=path)
    #         print('Dataframe initialized')
    #         del (path)
