from django import template

register = template.Library()

def count_words(text):
    return len(text.split())