# keyword parameter
from __future__ import print_function


def keywordParameter(name, **keywordParameter):
    print('name is', name)
    for (key, word) in keywordParameter.items():
        print(key, word, end=' ')


keywordParameter('Mike', age=24, country='China', education='bachelor')
