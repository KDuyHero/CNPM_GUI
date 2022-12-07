from tkinter import *
from tkinter import ttk
import config.config as config
import tkinter
import os
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)
win_bg = config.win_bg

win = Tk(className="Home Page")
win.resizable(False, False)
win.configure(bg="red")
win.geometry(f"{config.win_w}x{config.win_h}")

#navBar and Setting
leftFrame_win = tkinter.Frame(win)
leftFrame_win.place(relx=0, rely=0, relwidth=0.2, relheight=1, anchor=NW)


# request
rightFrame_win = tkinter.Frame(win)
rightFrame_win.place(relx=1, rely=0, relheight=1, relwidth=0.8, anchor=NE)


# separator in win
win_separator = ttk.Separator(win, orient=VERTICAL)
win_separator.place(relx=0.2, rely=0, relheight=1)

'''LEFT WIN'''
'''top in left win'''

topFrame_left = tkinter.Frame(leftFrame_win, padx=10, pady=5, bg=win_bg)
topFrame_left.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor=NW)

# -- load icon schedule
pathHomePageIcon = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
homePageImage = Image.open(pathHomePageIcon)
homePageImage = homePageImage.resize(
    (60, 60), Image.ANTIALIAS)
homePageImage = ImageTk.PhotoImage(homePageImage)

labelIcon = tkinter.Label(topFrame_left, text="", image=homePageImage,
                          anchor=CENTER, bg=win_bg, padx=5)
labelIcon.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
# end schedule icon

labelText = tkinter.Label(
    topFrame_left, text="Quản lý", font="Arial 20 bold", anchor=W, bg=win_bg, padx=5)
labelText.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)

'''middle'''
middleFrame_left = tkinter.Frame(leftFrame_win, bg=win_bg, pady=20)
middleFrame_left.place(relx=0, rely=0.15, relheight=0.6, relwidth=1, anchor=NW)

homeFrame_middle_left = tkinter.Frame(
    middleFrame_left, bg=win_bg, padx=5, pady=0)
homeFrame_middle_left.place(
    relx=0, rely=0, relheight=0.1, relwidth=1, anchor=NW)
pathNavHomePageIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_home.png')
navHomePageImage = Image.open(pathNavHomePageIcon)
navHomePageImage = navHomePageImage.resize(
    (30, 30), Image.ANTIALIAS)
navHomePageImage = ImageTk.PhotoImage(navHomePageImage)
labelIcon_home = tkinter.Label(homeFrame_middle_left, text="", image=navHomePageImage, bg=win_bg,
                               anchor=E, padx=5)
labelIcon_home.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
labelText_home = tkinter.Button(
    homeFrame_middle_left, text="Trang chủ", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
labelText_home.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)

# ---------------
familyFrame_middle_left = tkinter.Frame(
    middleFrame_left, bg=win_bg, padx=5, pady=0)
familyFrame_middle_left.place(
    relx=0, rely=0.1, relheight=0.1, relwidth=1, anchor=NW)
pathNavFamilyIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_family.png')
navFamilyImage = Image.open(pathNavFamilyIcon)
navFamilyImage = navFamilyImage.resize(
    (30, 30), Image.ANTIALIAS)
navFamilyImage = ImageTk.PhotoImage(navFamilyImage)
labelIcon_family = tkinter.Label(familyFrame_middle_left, text="", image=navFamilyImage, bg=win_bg,
                                 anchor=E, padx=5)
labelIcon_family.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
labelText_family = tkinter.Button(
    familyFrame_middle_left, text="Family", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
labelText_family.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
# ---------------------------
demandFrame_middle_left = tkinter.Frame(
    middleFrame_left, bg=win_bg, padx=5, pady=0)
demandFrame_middle_left.place(
    relx=0, rely=0.2, relheight=0.1, relwidth=1, anchor=NW)
pathNavDemandIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_demand.png')
navDemandImage = Image.open(pathNavDemandIcon)
navDemandImage = navDemandImage.resize(
    (30, 30), Image.ANTIALIAS)
navDemandImage = ImageTk.PhotoImage(navDemandImage)
labelIcon_demand = tkinter.Label(demandFrame_middle_left, text="", image=navDemandImage, bg=win_bg,
                                 anchor=E, padx=5)
labelIcon_demand.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
labelText_demand = tkinter.Button(
    demandFrame_middle_left, text="Demand", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
labelText_demand.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)


'''bottom'''
bottomFrame_left = tkinter.Frame(leftFrame_win, bg=win_bg, padx=10, pady=20)
bottomFrame_left.place(relx=0, rely=1, relheight=0.25,
                       relwidth=1, anchor=SW)
# help
helpFrame_bottom_left = tkinter.Frame(
    bottomFrame_left, bg=win_bg, padx=5, pady=0)
helpFrame_bottom_left.place(
    relx=0, rely=0, relheight=0.3, relwidth=1, anchor=NW)
pathHelpIcon = os.path.join(
    dirname, 'config\\image\\icon_help.png')
helpImage = Image.open(pathHelpIcon)
helpImage = helpImage.resize(
    (30, 30), Image.ANTIALIAS)
helpImage = ImageTk.PhotoImage(helpImage)
labelIcon_help = tkinter.Label(helpFrame_bottom_left, text="", image=helpImage, bg=win_bg,
                               anchor=E, padx=5)
labelIcon_help.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
labelText_help = tkinter.Button(
    helpFrame_bottom_left, text="Help", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
labelText_help.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)

# setting
settingFrame_bottom_left = tkinter.Frame(
    bottomFrame_left, bg=win_bg, padx=5, pady=0)
settingFrame_bottom_left.place(
    relx=0, rely=0.3, relheight=0.3, relwidth=1, anchor=NW)
pathSettingIcon = os.path.join(
    dirname, 'config\\image\\icon_setting.png')
settingImage = Image.open(pathSettingIcon)
settingImage = settingImage.resize(
    (30, 30), Image.ANTIALIAS)
settingImage = ImageTk.PhotoImage(settingImage)
labelIcon_setting = tkinter.Label(settingFrame_bottom_left, text="", image=settingImage, bg=win_bg,
                                  anchor=E, padx=5)
labelIcon_setting.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
labelText_setting = tkinter.Button(
    settingFrame_bottom_left, text="Setting", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
labelText_setting.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
'''END LEFT WIN'''
# --------------------------------------------------------------------------------------
'''START RIGHT WIN'''
'''TOP'''
# -- load icon schedule
pathSchedule = os.path.join(
    dirname, 'config\\image\\icon_schedule.png')
scheduleImage = Image.open(pathSchedule)
scheduleImage = scheduleImage.resize(
    (16, 16), Image.ANTIALIAS)
scheduleImage = ImageTk.PhotoImage(scheduleImage)
# create Frame
topFrame_right = tkinter.Frame(rightFrame_win, bg=win_bg, pady=20, padx=5)
topFrame_right.place(relx=0, rely=0, relheight=0.15, relwidth=1, anchor=NW)
tkinter.Label(topFrame_right, text="Trang chủ", font="Arial 20 bold", bg=win_bg,
              justify=LEFT, anchor=CENTER).grid(column=0, row=0, sticky=W)
tkinter.Label(topFrame_right, text="", image=scheduleImage, bg=win_bg,
              justify=LEFT, anchor=E).grid(column=1, row=0, sticky=W)
tkinter.Label(topFrame_right, text=config.currentDate, font="Arial 10", bg=win_bg,
              justify=RIGHT, anchor=E).grid(column=2, row=0)
topFrame_right.grid_columnconfigure(0, weight=1)
topFrame_right.grid_rowconfigure(1, weight=1)

'''BOTTOM'''
# create FRAME
bottomFrame_right = tkinter.Frame(rightFrame_win, bg=win_bg)
bottomFrame_right.place(relx=0, rely=1, relheight=0.85, relwidth=1, anchor=SW)

requestFrame_bottom_right = tkinter.Frame(bottomFrame_right, bg=win_bg)
requestFrame_bottom_right.place(
    relx=0, rely=0, relheight=1, relwidth=0.4, anchor=NW)
# label
labelText_request = tkinter.Label(
    requestFrame_bottom_right, text="Gửi yêu cầu", font="Arial 16 bold", anchor=W, padx=20, pady=10, bg=win_bg)
labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)
# ---------------------------------------
# changePerson
pathChangePerson = os.path.join(
    dirname, 'config\\image\\change_person_button.png')
changePersonImage = Image.open(pathChangePerson)
changePersonImage = changePersonImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
changePersonImage = ImageTk.PhotoImage(changePersonImage)

buttonChangePerson = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=changePersonImage, borderwidth=0, bg=win_bg, command="")
buttonChangePerson.place(
    relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07, anchor=NW)
# -----------------------------------------
# changeInfo
pathChangeInfo = os.path.join(
    dirname, 'config\\image\\change_info_button.png')
changeInfoImage = Image.open(pathChangeInfo)
changeInfoImage = changeInfoImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
changeInfoImage = ImageTk.PhotoImage(changeInfoImage)

buttonChangeInfo = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=changeInfoImage, borderwidth=0, bg=win_bg, command="")
buttonChangeInfo.place(
    relx=0.1, rely=0.17, relwidth=0.8, relheight=0.07, anchor=NW)
# -------------------------------------------
pathTachKhau = os.path.join(
    dirname, 'config\\image\\tach_khau_button.png')
tachKhauImage = Image.open(pathTachKhau)
tachKhauImage = tachKhauImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tachKhauImage = ImageTk.PhotoImage(tachKhauImage)

buttonTachKhau = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=tachKhauImage, borderwidth=0, bg=win_bg, command="")
buttonTachKhau.place(
    relx=0.1, rely=0.24, relwidth=0.8, relheight=0.07, anchor=NW)
# ---------------------------------------------
pathTamTru = os.path.join(
    dirname, 'config\\image\\tam_tru_button.png')
tamTruImage = Image.open(pathTamTru)
tamTruImage = tamTruImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamTruImage = ImageTk.PhotoImage(tamTruImage)

buttonTamTru = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=tamTruImage, borderwidth=0, bg=win_bg, command="")
buttonTamTru.place(
    relx=0.1, rely=0.31, relwidth=0.8, relheight=0.07, anchor=NW)
# ------------------------------------------------
pathTamVang = os.path.join(
    dirname, 'config\\image\\tam_vang_button.png')
tamVangImage = Image.open(pathTamVang)
tamVangImage = tamVangImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamVangImage = ImageTk.PhotoImage(tamVangImage)

buttonTamVang = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=tamVangImage, borderwidth=0, bg=win_bg, command="")
buttonTamVang.place(
    relx=0.1, rely=0.38, relwidth=0.8, relheight=0.07, anchor=NW)

# ------------------------------------------------
pathDemand = os.path.join(
    dirname, 'config\\image\\demand_button.png')
demandImage = Image.open(pathDemand)
demandImage = demandImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
DemandImage = ImageTk.PhotoImage(demandImage)

buttonDemand = tkinter.Button(
    requestFrame_bottom_right, text="", cursor="hand2", image=DemandImage, borderwidth=0, bg=win_bg, command="")
buttonDemand.place(
    relx=0.1, rely=0.38, relwidth=0.8, relheight=0.07, anchor=NW)

# RESPONSE
responseFrame_bottom_right = tkinter.Frame(bottomFrame_right, bg=win_bg)
responseFrame_bottom_right.place(
    relx=1, rely=0, relheight=1, relwidth=0.5, anchor=NE)

# label
labelText_request = tkinter.Label(
    responseFrame_bottom_right, text="Phản hồi kiến nghị", font="Arial 16 bold", anchor=W, padx=20, pady=10, bg=win_bg)
labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)

# subFrame kiến nghị
response_demand_frame = tkinter.Frame(
    responseFrame_bottom_right, bg=config.response_demand_bg, borderwidth=1)
response_demand_frame.place(
    relx=0.05, rely=0.1, relheight=0.85, relwidth=0.9, anchor=NW)

for i in range(0, len(config.list_kien_nghi)):
    tkinter.Label(response_demand_frame,
                  text=config.list_kien_nghi[i][0], font="Arial 14 bold", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+0, padx=5, pady=5, sticky=W)
    tkinter.Label(response_demand_frame,
                  text=config.list_kien_nghi[i][1], font="Arial 12", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+1, padx=5, pady=5, sticky=W)

    ttk.Separator(response_demand_frame, orient=HORIZONTAL).grid(
        column=0, row=3*i+2, ipadx=500, pady=5)
'''END RIGHT WIN'''


win.mainloop()
