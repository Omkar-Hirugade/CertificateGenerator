import gspread
from PIL import Image, ImageDraw, ImageFont
import time

gc = gspread.service_account(filename='certi.json') # Path to credentials.json.
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1VJHaWNJq886B7Y19oqmFRZCoPJCZF21OEu-bC0HW3lk/edit#gid=0") # Link to Google sheet.
worksheet = sh.worksheet("Sheet1")
uid_list = worksheet.col_values(1)
names_list = worksheet.col_values(5)
uid_list.remove(uid_list[0])
names_list.remove(names_list[0])
n = len(names_list)
for i in range(0, n):
    uid = uid_list[i]
    name = names_list[i]
    img = Image.open('5.png') # Path to certificate template.
    img = img.convert('RGB')
    myFont = ImageFont.truetype(r"LibreBaskerville-Italic.ttf", 65) # Path to fonts.
    myFont2 = ImageFont.truetype(r"arial.ttf", 12)
    W = img.width
    H = img.height
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(name, font=myFont)
    draw.text(((W - w) / 2, (H - 130) / 2), name, font=myFont, fill="black")
    draw.text((135, 189), uid, font=myFont2, fill="black")
    str1 = uid
    str2 = '.jpg'
    fname = str1 + str2
    # fname2='certis/'+fname
    img.save(fname)
    # worksheet.update_cell(i+2, 3, fname)
    # str3 = 'certi-img/'
    # str4 = str3 + fname
    # worksheet.update_cell(i + 2, 4, str4)
    # str5 = 'https://isavesit.org.in/isa-app/certificate/certi-img/'
    # str6 = str5 + fname
    # worksheet.update_cell(i + 2, 8, str6)
    # time.sleep(3)hello