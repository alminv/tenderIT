from django import template
register = template.Library()
from ..models import Company

# use {% load company_tags %}  in every template to use  tags

@register.simple_tag
def total_companies():
    return Company.objects.count()


@register.simple_tag
def get_company_id(user):
    company = user.company
    company_id = company.pk
    return company_id

