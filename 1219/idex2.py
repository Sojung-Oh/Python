#쿠폰 추첨기

from tkinter import *
import random

# def on_click():
#     name_list = ["강성연", "김준식", "양건모", "오소정", "임유빈", "정태영", "조우성", "조효정"]

#     name = random.sample(name_list,2)

#     text.delete("1.0", END)
#     text.insert(END, name)

# window = Tk()
# window.title("쿠폰 추첨기")
# window.geometry("640x480")

# #이미지 넣기
# label_img = Label(window)
# img = PhotoImage(file = "./1219/ABC.png") #png 파일만 인식! jpg는 안됨
# label_img.config(image = img)
# label_img.pack()

# #추첨버튼
# Button(window, text = "추첨", command=on_click)

# #출력
# text = Text(window, width = 40, height = 5, bg = "green")
# text.pack()

# window.mainloop()

#------------------------실습. 로또 당첨 번호 확인 앱
from bs4 import BeautifulSoup
import requests

window = Tk()
window.title("로또 당첨 확인")
window.geometry("640x480")

label1 = Label(window, text = "당첨 회차 입력")
label1.pack(side="top", fill = 'x', padx = 10, pady = 10)

#----entry 창
entry = Entry(window, width = 30, bg = "lightblue")
entry.pack()

#num = 1150
#------------------------------------------------------------------------------------------------------

def get_num(num):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={num}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    selection = soup.select(".win_number_box .win_ball .winning_number")
    print(selection[0].text)
    sel_num = selection[0].text
    #print(type(sel_num)) #str
    bonus = soup.select_one(".win_number_box .win_ball .bonus_number").text
    print(bonus)

    return sel_num, bonus

#출력창
text = Text(window, width = 40, height = 5, bg = "lightblue")
text.pack()

#-----------------------------------출력 버튼 만들기
def show_lotto():
    num = entry.get()
    #print(num)
    sel, bon = get_num(num)

    text.delete("1.0", END)
    result = f"당첨번호: {sel} \n보너스번호: {bon}"
    text.insert(END, result)

button = Button(window, text = "당첨 번호 확인", command=show_lotto)
button.pack()

window.mainloop() #------------------------------------리더님 코드도 참고하기