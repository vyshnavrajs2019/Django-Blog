from django import template

register = template.Library()

def para(value):
	text_pieces = value.split("\n")
	return text_pieces

def intro(value, length):
	text_pieces = para(value)
	for text in text_pieces:
		striped_text = text.strip()
		if len(striped_text):
			return striped_text[:length] + '...'
	return ''


register.filter('para', para)
register.filter('intro', intro)