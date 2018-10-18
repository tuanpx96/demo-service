# -*- coding: utf-8 -*-
#
# @author N307
# @create 10/4/2018
# 
import json


class Config(object):
    instance = None

    def __new__(cls):
        if not Config.instance:
            Config.instance = Config.__Config()
        return Config.instance

    class __Config:
        def __init__(self):
            print('Load config')
            with open('applications.json') as f:
                self.properties = json.loads(f.read())

        def get(self, *keys):
            root = self.properties
            for key in keys:
                try:
                    root = root[key]
                except KeyError:
                    return None
            return root

        def get_as_int(self, *keys):
            root = self.get(*keys)
            return int(root)

        def get_as_float(self, *keys):
            root = self.get(*keys)
            return float(root)

        def get_as_bool(self, *keys):
            root = self.get(*keys)
            if root is None:
                return None
            else:
                return bool(root)


