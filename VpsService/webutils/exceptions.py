# -*- coding: utf-8 -*-
#
# @author N307
# @create 10/4/2018
#


class VPSException(BaseException):
    def __index__(self, message):
        self.message = message
