from django.template import Library

register = Library()

@register.inclusion_tag('inc-review-summary.html')
def show_review_summary(review):
    return {'review': review}