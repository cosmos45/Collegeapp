from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
import textwrap
import re
import os
import requests
import sys
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage


def resumewi(request):
    print('\n YaY')
    if request.method == "POST":
        global template_loc, tmp, img_h, data
        data = request.POST

        template_loc = "resume/static/images/ResumeSite.jpg"
        tmp = Image.open(template_loc)  # Cft = Certificate
        linedrw = ImageDraw.Draw(tmp)
        s_size = 15
        m_size = 22

        xCrnt, yCrnt = drawtext(data['name'], 50, 35, 41, 30, (255, 255, 255))

        experience = re.split("[#*]", data["experience"])

        for i in range(0, len(experience)):
            xCrnt = 41
            t = 15
            if i == 0:
                t = 25
            if (i % 2) != 0:  # Even
                if i == len(experience) - 1:
                    xCrnt, yCrnt = drawtext(experience[i], s_size + 4, 50, xCrnt, yCrnt + t, (0, 0, 0), 1)
                else:
                    xCrnt, yCrnt = drawtext(experience[i], s_size + 4, 50, xCrnt, yCrnt + t, (0, 0, 0))
            else:
                if i == len(experience) - 1:
                    xCrnt, yCrnt = drawtext(experience[i], s_size, 50, xCrnt, yCrnt + 6, (0, 0, 0), 1)
                else:
                    xCrnt, yCrnt = drawtext(experience[i], s_size, 50, xCrnt, yCrnt + 6, (0, 0, 0))

        return render(request, "resume/resume_ready.html")
    return render(request, "resume/resume_with_image.html")

def temp1(request):
    if request.method == "POST":
        global tmp, img_h, data
        data = request.POST

        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        print(filename)
        fileurl = fs.open(filename)
        templateurl = fs.url(filename)
        print('file raw url', filename)
        print('file full url', fileurl)

        im1 = Image.open("images/ResumeSite.jpg")
        im2 = Image.open(fileurl)
        back_im = im1.copy()
        back_im.paste(im2)
        saving = back_im.save('D:/pycharm/Collegeapp/putem' + filename + '.jpg', resolution=100.0,
                              quality=100)

        tmp = Image.open('D:/pycharm/Collegeapp/putem' + filename + '.jpg')
        linedrw = ImageDraw.Draw(tmp)
        s_size = 15
        m_size = 22

        # Drawing Name ----------------------------------------------------------
        xCrnt, yCrnt = drawtext(data['name'], 50, 35, 41, 30, (255, 255, 255))

        experience = re.split("[#*]", data["experience"])

        for i in range(0, len(experience)):
            xCrnt = 41
            t = 15
            if i == 0:
                t = 25
            if (i % 2) != 0:  # Even
                if i == len(experience) - 1:
                    xCrnt, yCrnt = drawtext(experience[i], s_size + 4, 50, xCrnt, yCrnt + t, (0, 0, 0), 1)
                else:
                    xCrnt, yCrnt = drawtext(experience[i], s_size + 4, 50, xCrnt, yCrnt + t, (0, 0, 0))
            else:
                if i == len(experience) - 1:
                    xCrnt, yCrnt = drawtext(experience[i], s_size, 50, xCrnt, yCrnt + 6, (0, 0, 0), 1)
                else:
                    xCrnt, yCrnt = drawtext(experience[i], s_size, 50, xCrnt, yCrnt + 6, (0, 0, 0))

        return render(request, "resume/resume_ready.html")
    return render(request, "resume/temp1.html")


def drawimg(loc1, x, y):
    img = Image.open(loc1).resize((img_h + 8, img_h + 8)).convert("L")
    tmp.paste(img, (x, y))


def drawtext(text, size, nwords, x, y, fontcolor, print=0, path='arial.ttf'):
    # --------------------- Making the Resume ---------------------
    # Wrapping the text
    draw = ImageDraw.Draw(tmp)
    font = ImageFont.truetype(path, size)
    lines = textwrap.wrap(text, nwords)

    for line in lines:
        w, h = font.getsize(line)
        draw.text(xy=(x, y), text=line, fill=fontcolor, font=font)
        y = y + h + 6

    if print:
        tmp.save('C:/Users/DELL/Downloads/' + str(data["name"].replace(" ", "")) + '.pdf', resolution=100.0,
                 quality=100)
        # os.startfile('C:/Users/Admin/Downloads/' + str(data["name"].replace(" ", "")) + '.pdf')
    return x, y


def Rbase(request):
    return render(request, "resume/base.html")
