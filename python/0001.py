'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

import string
import random

words = string.ascii_letters + string.digits
# print(string.ascii_letters)
# print(string.digits)
# print(words)
for i in range(50):
	txt_list=[random.choice(words) for t in range(10)]
	txt=''.join(txt_list)
	print(txt)