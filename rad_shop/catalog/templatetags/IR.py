from django import template

register = template.Library()


@register.filter(name='persian_numbers')
def persian_numbers(english_int):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    latin_nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    number = str(english_int)
    persian_number = ''
    for i in number:
        if i in latin_nums:
            persian_number += devanagari_nums[int(i)]
        else:
            persian_number += i
    return persian_number


@register.filter(name='price')
def price(input_int):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    persian_price = ''
    for i in f'{int(input_int):,d}':
        if i == ',':
            persian_price += ','
        else:
            persian_price += devanagari_nums[int(i)]
    return persian_price
