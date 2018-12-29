'''
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image, ImageDraw, ImageFont

def add_num(img,num):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40-10, height-40-10), str(num), font=myfont, fill=fillcolor) # -10 为了不紧贴边
    img.save('result.jpg','jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image,82)