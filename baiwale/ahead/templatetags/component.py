# -*- coding: utf-8 -*-
from django import template
from django.template import Library, Node

register = Library()

# 获得多语言配置文件
class ElementNode(Node):

    def __init__(self, loop):
        self.loop = template.Variable(loop)

    def render(self, context):
        loop = self.loop.resolve(context)
        if int(loop) % 4 == 0:
            return 'mr0'
        else:
            return ''

def getElement(parser, token):
    split = token.split_contents()
    return ElementNode(split[1])

getElement = register.tag(getElement)