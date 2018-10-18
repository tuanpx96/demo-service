# -*- coding: utf-8 -*-
#
# @author N307
# @create 10/4/2018
#
import abc
from rest_framework.views import APIView


class AbstractView(APIView, abc.ABC):
    @abc.abstractmethod
    def path(self): raise NotImplementedError
