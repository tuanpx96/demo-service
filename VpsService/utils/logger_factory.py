# -*- coding: utf-8 -*-
#
# @author N307
# @create 10/4/2018
# 

import logging
from logging.handlers import RotatingFileHandler


def get_log(name, level=logging.INFO):
    handler = RotatingFileHandler(name + '.log', mode='a', maxBytes=20*1024*1024, backupCount=1)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
