import numpy as np
import re

def format_color(color):
  if type(color) != str:
    return np.nan
  if len(color) < 3:
    return ''
  _color = color.split(' ')

  if len(_color) == 1:
    return color

  _color1 = [element for element in _color if '_' in element]

  if len(_color1) == 1:
    return _color1[0]

  return 'colorful'

def color_general(color):
  if type(color) != str:
    return np.nan
  _color = color.split('_')
  return _color[-1]

def category_general(category):
  if type(category) != str:
    return np.nan
  _category = category.split('_')
  return _category[-1]

def money2float(money_value):
  if type(money_value) != str:
    return np.nan
  # Remove non-numeric characters
  numeric_string = re.sub(r'[^\d.]', '', money_value)

  if numeric_string == '':
    return np.nan
  # Convert to float
  numeric_value = float(numeric_string)

  return numeric_value

