from tkinter import *
from tkinter import ttk
import config.config as config
import tkinter
import os
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

dirname = os.path.dirname(__file__)
win_bg = config.win_bg
btn_home_bg = win_bg
btn_family_bg = win_bg
btn_demand_bg = win_bg

padx = 5
pady = 10

font_header1 = "Arial 20 bold"
font_header2 = "Arial 16 bold"
font_header3 = "Arial 14 bold"
font_content = "Arial 12 bold"


root = Tk(className="Quản Lý")
root.resizable(False, False)
root.geometry(f"{config.win_w}x{config.win_h}")


def switch(frame):
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    global btn_home_bg, btn_family_bg, btn_demand_bg
    if (frame == f_home):
        btn_home_bg = config.selected_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        Home()
    elif (frame == f_family):
        btn_home_bg = win_bg
        btn_family_bg = config.selected_bg
        btn_demand_bg = win_bg
        Family()
    elif (frame == f_authen):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        Authen()
    elif (frame == f_add_person):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AddPerson()
    Nav()
    frame.tkraise()


def Authentication(hostId, message):
    if (hostId == "123456"):
        switch(f_add_person)
    else:
        message['text'] = f"Số hộ khẩu: {hostId} bị sai!. Vui lòng nhập lại"


someStyle = ttk.Style()
someStyle.configure('DropDownStyle.TMenubutton',
                    font=('Arial', 12, "bold"))
'''Load IMAGE'''
# Nav Bar
pathLogo = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
logoIcon = Image.open(pathLogo)
logoIcon = logoIcon.resize(
    (60, 60), Image.ANTIALIAS)
logoIcon = ImageTk.PhotoImage(logoIcon)
# ---------------
pathNavHomePageIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_home.png')
navHomePageImage = Image.open(pathNavHomePageIcon)
navHomePageImage = navHomePageImage.resize(
    (30, 30), Image.ANTIALIAS)
navHomePageImage = ImageTk.PhotoImage(navHomePageImage)
# -------------------------
pathNavFamilyIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_family.png')
navFamilyImage = Image.open(pathNavFamilyIcon)
navFamilyImage = navFamilyImage.resize(
    (30, 30), Image.ANTIALIAS)
navFamilyImage = ImageTk.PhotoImage(navFamilyImage)
# -------------------------
pathNavDemandIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_demand.png')
navDemandImage = Image.open(pathNavDemandIcon)
navDemandImage = navDemandImage.resize(
    (30, 30), Image.ANTIALIAS)
navDemandImage = ImageTk.PhotoImage(navDemandImage)
# -------------------------
pathHelpIcon = os.path.join(
    dirname, 'config\\image\\icon_help.png')
helpImage = Image.open(pathHelpIcon)
helpImage = helpImage.resize(
    (30, 30), Image.ANTIALIAS)
helpImage = ImageTk.PhotoImage(helpImage)
# ------------------------
pathSettingIcon = os.path.join(
    dirname, 'config\\image\\icon_setting.png')
settingImage = Image.open(pathSettingIcon)
settingImage = settingImage.resize(
    (30, 30), Image.ANTIALIAS)
settingImage = ImageTk.PhotoImage(settingImage)

'''HOME'''
# -- load icon schedule
pathSchedule = os.path.join(
    dirname, 'config\\image\\icon_schedule.png')
scheduleImage = Image.open(pathSchedule)
scheduleImage = scheduleImage.resize(
    (16, 16), Image.ANTIALIAS)
scheduleImage = ImageTk.PhotoImage(scheduleImage)
# ------------------------
# changePerson
pathChangePerson = os.path.join(
    dirname, 'config\\image\\change_person_button.png')
changePersonImage = Image.open(pathChangePerson)
changePersonImage = changePersonImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
changePersonImage = ImageTk.PhotoImage(changePersonImage)
# -------------------------
# changeInfo
pathChangeInfo = os.path.join(
    dirname, 'config\\image\\change_info_button.png')
changeInfoImage = Image.open(pathChangeInfo)
changeInfoImage = changeInfoImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
changeInfoImage = ImageTk.PhotoImage(changeInfoImage)
# ------------------------
# tách khẩu
pathTachKhau = os.path.join(
    dirname, 'config\\image\\tach_khau_button.png')
tachKhauImage = Image.open(pathTachKhau)
tachKhauImage = tachKhauImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tachKhauImage = ImageTk.PhotoImage(tachKhauImage)
# ------------------------
# tạm trú
pathTamTru = os.path.join(
    dirname, 'config\\image\\tam_tru_button.png')
tamTruImage = Image.open(pathTamTru)
tamTruImage = tamTruImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamTruImage = ImageTk.PhotoImage(tamTruImage)
# ------------------------
# tạm vắng
pathTamVang = os.path.join(
    dirname, 'config\\image\\tam_vang_button.png')
tamVangImage = Image.open(pathTamVang)
tamVangImage = tamVangImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamVangImage = ImageTk.PhotoImage(tamVangImage)
# ---------------------
# kiến nghị
pathDemand = os.path.join(
    dirname, 'config\\image\\demand_button.png')
demandImage = Image.open(pathDemand)
demandImage = demandImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
DemandImage = ImageTk.PhotoImage(demandImage)


f_home = tkinter.Frame(root)
f_family = tkinter.Frame(root)
f_authen = tkinter.Frame(root)
f_add_person = tkinter.Frame(root)
# set các frame chồng lên nhau.
frames = (f_home, f_family, f_authen, f_add_person)
for f in frames:
    f.place(relx=1, rely=0, relheight=1, relwidth=0.8, anchor=NE)

# separator in root
win_separator = ttk.Separator(root, orient=VERTICAL)
win_separator.place(relx=0.199, rely=0, relheight=1, anchor=NW)
# nav_bar
nav_bar = tkinter.Frame(root, bg=win_bg)
nav_bar.place(relx=0, rely=0, relheight=1, relwidth=0.198, anchor=NW)


'''Code Nav Bar'''


def Nav():
    # 1.Top
    topFrameNav = tkinter.Frame(nav_bar, padx=10, pady=5, bg=win_bg)
    topFrameNav.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor=NW)
    # 1.1 In top nav
    labelLogoApp = tkinter.Label(topFrameNav, image=logoIcon,
                                 anchor=CENTER, bg=win_bg, padx=5)
    labelLogoApp.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    # 1.2 App name
    labelAppName = tkinter.Label(
        topFrameNav, text="Quản lý", font="Arial 20 bold", anchor=W, bg=win_bg, padx=5)
    labelAppName.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # ------------------------
    # 2.Middle
    middleFrameNav = tkinter.Frame(nav_bar, bg=win_bg, pady=20)
    middleFrameNav.place(relx=0, rely=0.15, relheight=0.6,
                         relwidth=1, anchor=NW)
    # 2.1 Home Butotn
    homeFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_home_bg, padx=5, pady=0)
    homeFrame_middle_nav.place(
        relx=0, rely=0, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_home = tkinter.Label(homeFrame_middle_nav, image=navHomePageImage, bg=btn_home_bg,
                                   anchor=E, padx=5)
    labelIcon_home.place(relx=0, rely=0, relheight=1,
                         relwidth=0.3, anchor=NW)
    labelText_home = tkinter.Button(
        homeFrame_middle_nav, text="Trang chủ", font="Arial 12 bold", anchor=W, bg=btn_home_bg, borderwidth=0, cursor="hand2", command=lambda: switch(f_home))
    labelText_home.place(relx=1, rely=0, relheight=1,
                         relwidth=0.7, anchor=NE)

    # 2.2 Family Button

    familyFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_family_bg, padx=5, pady=0)
    familyFrame_middle_nav.place(
        relx=0, rely=0.1, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_family = tkinter.Label(familyFrame_middle_nav, image=navFamilyImage, bg=btn_family_bg,
                                     anchor=E, padx=5)
    labelIcon_family.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_family = tkinter.Button(
        familyFrame_middle_nav, text="Family", font="Arial 12 bold", anchor=W, bg=btn_family_bg, borderwidth=0, cursor="hand2", command=lambda: switch(f_family))
    labelText_family.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 2.3 Demand Button

    demandFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_demand_bg, padx=5, pady=0)
    demandFrame_middle_nav.place(
        relx=0, rely=0.2, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_demand = tkinter.Label(demandFrame_middle_nav, image=navDemandImage, bg=btn_demand_bg,
                                     anchor=E, padx=5)
    labelIcon_demand.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_demand = tkinter.Button(
        demandFrame_middle_nav, text="Demand", font="Arial 12 bold", anchor=W, bg=btn_demand_bg, borderwidth=0, cursor="hand2", command="")
    labelText_demand.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 3. Button
    bottomFrame_nav = tkinter.Frame(nav_bar, bg=win_bg, padx=10, pady=20)
    bottomFrame_nav.place(relx=0, rely=1, relheight=0.25,
                          relwidth=1, anchor=SW)
    # 3.1 Support
    helpFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=win_bg, padx=5, pady=0)
    helpFrame_bottom_nav.place(
        relx=0, rely=0, relheight=0.3, relwidth=1, anchor=NW)

    labelIcon_help = tkinter.Label(helpFrame_bottom_nav, text="", image=helpImage, bg=win_bg,
                                   anchor=E, padx=5)
    labelIcon_help.place(relx=0, rely=0, relheight=1,
                         relwidth=0.3, anchor=NW)
    labelText_help = tkinter.Button(
        helpFrame_bottom_nav, text="Help", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
    labelText_help.place(relx=1, rely=0, relheight=1,
                         relwidth=0.7, anchor=NE)
    # 3.2 Setting
    settingFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=win_bg, padx=5, pady=0)
    settingFrame_bottom_nav.place(
        relx=0, rely=0.3, relheight=0.3, relwidth=1, anchor=NW)

    labelIcon_setting = tkinter.Label(settingFrame_bottom_nav, image=settingImage, bg=win_bg,
                                      anchor=E, padx=5)
    labelIcon_setting.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_setting = tkinter.Button(
        settingFrame_bottom_nav, text="Setting", font="Arial 12 bold", anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
    labelText_setting.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)


'''End Nav Bar'''
# --------------------------------------------------------------------------------------
"""Start Home"""


def Home():
    # Create a child frame to destroy when no use parent frame
    f_all_home = tkinter.Frame(f_home)
    f_home.grid_columnconfigure(0, weight=1)
    f_home.grid_rowconfigure(0, weight=1)
    f_all_home.grid(column=0, row=0, sticky='news')

    topFrame_home = tkinter.Frame(f_all_home, bg=win_bg, pady=20, padx=5)
    topFrame_home.place(
        relx=0, rely=0, relheight=0.15, relwidth=1, anchor=NW)
    tkinter.Label(topFrame_home, text="Trang chủ", font="Arial 20 bold", bg=win_bg,
                  justify=LEFT, anchor=CENTER).grid(column=0, row=0, sticky=W)
    tkinter.Label(topFrame_home, text="", image=scheduleImage, bg=win_bg,
                  justify=LEFT, anchor=E).grid(column=1, row=0, sticky=W)
    tkinter.Label(topFrame_home, text=config.currentDate, font="Arial 10", bg=win_bg,
                  justify=RIGHT, anchor=E).grid(column=2, row=0)
    topFrame_home.grid_columnconfigure(0, weight=1)
    topFrame_home.grid_rowconfigure(1, weight=1)

    '''BOTTOM'''
    # create FRAME
    bottomFrame_home = tkinter.Frame(f_all_home, bg=win_bg)
    bottomFrame_home.place(
        relx=0, rely=1, relheight=0.85, relwidth=1, anchor=SW)

    requestFrame_bottom_home = tkinter.Frame(bottomFrame_home, bg=win_bg)
    requestFrame_bottom_home.place(
        relx=0, rely=0, relheight=1, relwidth=0.4, anchor=NW)
    # label
    labelText_request = tkinter.Label(
        requestFrame_bottom_home, text="Gửi yêu cầu", font=font_header2, anchor=W, padx=20, pady=10, bg=win_bg)
    labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)
    # ---------------------------------------

    buttonChangePerson = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=changePersonImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen))
    buttonChangePerson.place(
        relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07, anchor=NW)
    # -----------------------------------------

    buttonChangeInfo = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=changeInfoImage, borderwidth=0, bg=win_bg, command="")
    buttonChangeInfo.place(
        relx=0.1, rely=0.18, relwidth=0.8, relheight=0.07, anchor=NW)
    # -------------------------------------------

    buttonTachKhau = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tachKhauImage, borderwidth=0, bg=win_bg, command="")
    buttonTachKhau.place(
        relx=0.1, rely=0.26, relwidth=0.8, relheight=0.07, anchor=NW)
    # ---------------------------------------------

    buttonTamTru = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamTruImage, borderwidth=0, bg=win_bg, command="")
    buttonTamTru.place(
        relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07, anchor=NW)
    # ------------------------------------------------

    buttonTamVang = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamVangImage, borderwidth=0, bg=win_bg, command="")
    buttonTamVang.place(
        relx=0.1, rely=0.42, relwidth=0.8, relheight=0.07, anchor=NW)

    # ------------------------------------------------

    buttonDemand = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=DemandImage, borderwidth=0, bg=win_bg, command="")
    buttonDemand.place(
        relx=0.1, rely=0.50, relwidth=0.8, relheight=0.07, anchor=NW)

    # RESPONSE
    responseFrame_bottom_home = tkinter.Frame(
        bottomFrame_home, bg=win_bg)
    responseFrame_bottom_home.place(
        relx=1, rely=0, relheight=1, relwidth=0.5, anchor=NE)

    # label
    labelText_request = tkinter.Label(
        responseFrame_bottom_home, text="Phản hồi kiến nghị", font="Arial 16 bold", anchor=W, padx=20, pady=10, bg=win_bg)
    labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)

    # subFrame kiến nghị
    response_demand_frame = tkinter.Frame(
        responseFrame_bottom_home, bg=config.response_demand_bg, borderwidth=1)
    response_demand_frame.place(
        relx=0.05, rely=0.1, relheight=0.85, relwidth=0.9, anchor=NW)

    for i in range(0, len(config.list_kien_nghi)):
        tkinter.Label(response_demand_frame,
                      text=config.list_kien_nghi[i][0], font="Arial 14 bold", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+0, padx=5, pady=5, sticky=W)
        tkinter.Label(response_demand_frame,
                      text=config.list_kien_nghi[i][1], font="Arial 12", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+1, padx=5, pady=5, sticky=W)

        ttk.Separator(response_demand_frame, orient=HORIZONTAL).grid(
            column=0, row=3*i+2, ipadx=500, pady=5)


"""END HOME"""
# --------------------------------------------------------------------------------------
"""Start Family"""


def Family():
    # Create a child frame to destroy when no use parent frame
    f_all_family = tkinter.Frame(f_family)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_family.grid(column=0, row=0, sticky='news')

    tkinter.Label(f_all_family, text="Family", font=font_header1).place(
        relx=0.5, rely=0.5, anchor=N)


"""END Family"""


def Authen():
    # Create a child frame to destroy when no use parent frame
    f_all_authen = tkinter.Frame(f_authen)
    f_authen.grid_columnconfigure(0, weight=1)
    f_authen.grid_rowconfigure(0, weight=1)
    f_all_authen.grid(column=0, row=0, sticky='news')
    f_all_authen.config(padx=10, pady=30)
    labelHostId = tkinter.Label(
        f_all_authen, text="Nhập mã hộ khẩu", font=font_content, anchor=W)
    labelHostId.grid(column=0, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(f_all_authen, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen, text="Gửi", font=font_content, command=lambda: Authentication(entryHostId.get(), labelMessage))
    buttonSubmit.grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)


def AddPerson():
    # Create a child frame to destroy when no use parent frame
    f_all_add_person = tkinter.Frame(f_add_person)
    f_add_person.grid_columnconfigure(0, weight=1)
    f_add_person.grid_rowconfigure(0, weight=1)
    f_all_add_person.grid(column=0, row=0, sticky='news')

    f_all_add_person.config(padx=50, pady=0)
    f_all_add_person.grid_columnconfigure(0, weight=1)

    # row 0
    labelRelationShip = tkinter.Label(f_all_add_person, text="Quan hệ với chủ hộ:",
                                      font=font_header3, anchor=W)
    labelRelationShip.grid(row=0, column=0, columnspan=2,
                           padx=padx, pady=pady, sticky=W)
    entryRelationShip = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryRelationShip.grid(row=0, column=2, padx=padx,
                           pady=pady, sticky=W, columnspan=2)

    # row 1
    labelFullName = tkinter.Label(
        f_all_add_person, text="Họ và tên: ", font=font_content, anchor=W)
    labelFullName.grid(column=0, row=1, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    entryFullName = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    entryFullName.grid(column=1, row=1, padx=padx, pady=pady, columnspan=3)

    # row 2
    labelOtherName = tkinter.Label(
        f_all_add_person, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
    labelOtherName.grid(column=0, row=2, sticky=W,
                        padx=padx, pady=pady, columnspan=2)

    entryOtherName = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryOtherName.grid(column=2, row=2, padx=padx, pady=pady, columnspan=2)

    # row 3
    labelBirthDay = tkinter.Label(
        f_all_add_person, text="Ngày sinh: ", font=font_content, anchor=W)
    labelBirthDay.grid(column=0, row=3, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    dateEntryBirthDay = DateEntry(f_all_add_person, font=font_content)
    dateEntryBirthDay.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    labelGender = tkinter.Label(
        f_all_add_person, text="Giới tính: ", font=font_content, anchor=W)
    labelGender.grid(column=2, row=3, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    option = ("Male", "Female", "Other")
    chosed = StringVar(f_all_add_person)

    dropDownGender = ttk.OptionMenu(
        f_all_add_person, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=3, row=3, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 4
    labelRealAddress = tkinter.Label(
        f_all_add_person, text="Nguyên quán: ", font=font_content, anchor=W)
    labelRealAddress.grid(column=0, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    entryRealAddress = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    entryRealAddress.grid(column=1, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=3)

    # row 5
    labelCCCD = tkinter.Label(
        f_all_add_person, text="Số căn cước công dân: ", anchor=W, font=font_content)
    labelCCCD.grid(column=0, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    entryCCCD = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    entryCCCD.grid(column=2, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    # row 6
    labelEthnic = tkinter.Label(
        f_all_add_person, text="Dân tộc: ", font=font_content, anchor=W)
    labelEthnic.grid(column=0, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    entryEthnic = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    entryEthnic.grid(column=1, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    labelNational = tkinter.Label(
        f_all_add_person, text="Quốc tịch: ", font=font_content, anchor=W)
    labelNational.grid(column=2, row=6, sticky=W,
                       padx=padx, pady=pady, columnspan=1)
    entryNational = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    entryNational.grid(column=3, row=6, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    # row 6
    labelJob = tkinter.Label(
        f_all_add_person, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
    labelJob.grid(column=0, row=7, sticky=W,
                  padx=padx, pady=pady, columnspan=2)

    entryJob = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    entryJob.grid(column=2, row=7, padx=padx, pady=pady, columnspan=2)

    # row 8
    labelCurrentAddress = tkinter.Label(
        f_all_add_person, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
    labelCurrentAddress.grid(column=0, row=8, sticky=W,
                             padx=padx, pady=pady, columnspan=2)

    entryCurrentAddress = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryCurrentAddress.grid(
        column=2, row=8, padx=padx, pady=pady, columnspan=2)

    # row 9
    labelCurrentDate = tkinter.Label(
        f_all_add_person, text="Hôm nay: ", font=font_content, anchor=W)
    labelCurrentDate.grid(column=0, row=9, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    dateEntryCurrentDate = DateEntry(f_all_add_person, font=font_content)
    dateEntryCurrentDate.grid(column=1, row=9, sticky=W,
                              padx=padx, pady=pady, columnspan=1)


switch(f_home)

root. mainloop()
