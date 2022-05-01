from logging import exception
import requests
import re
import os
import time
from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CGFw(object):
    def setupUi(self, CGFw):
        self.ver = 2.24
        self.app_dir = os.getcwd()
        self.fw_db = {"dir": self.app_dir + "\db\\", "name": "fw release date.ini"}
        self.db = {
            "dir": self.app_dir + "\db",
            "name": "PS4 db.txt",
            "link": "https://github.com/DEFAULTDNB/DEFAULTDNB.github.io/blob/master/ps4date.db",
            "data": "https://raw.githubusercontent.com/DEFAULTDNB/DEFAULTDNB.github.io/master/ps4date.db",
            "Local entries": 0,
            "Online entries": 0,
            "latest": True,
        }
        self.month = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
        }
        self.firmwares = []
        self.setting = {"show fw": 4, "fw": "9.51", "mode": "Offline"}
        self.logging = """<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
                          <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
                          p, li { white-space: pre-wrap; }\n
                          </style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"""
        self.colors = {"Fail": "#ff0c40;", "Warning": "#ffaa00", "Success": "#aaff00"}

        CGFw.setObjectName("CGFw")
        CGFw.setWindowModality(QtCore.Qt.WindowModal)
        CGFw.resize(1000, 680)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CGFw.sizePolicy().hasHeightForWidth())
        CGFw.setSizePolicy(sizePolicy)
        CGFw.setMinimumSize(QtCore.QSize(970, 680))
        CGFw.setStyleSheet(
            "color: rgb(255, 255, 255);\nbackground-color: rgb(65, 65, 65);"
        )
        CGFw.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        CGFw.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(CGFw)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BackgroundLayout = QtWidgets.QFormLayout()
        self.BackgroundLayout.setContentsMargins(30, 30, 30, 10)
        self.BackgroundLayout.setObjectName("BackgroundLayout")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.formLayout_5.setObjectName("formLayout_5")
        self.TopLeftLayout = QtWidgets.QFrame(self.centralwidget)
        self.TopLeftLayout.setFrameShape(QtWidgets.QFrame.Box)
        self.TopLeftLayout.setObjectName("TopLeftLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.TopLeftLayout)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(20, 1, 20, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.g_settings_label = QtWidgets.QLabel(self.TopLeftLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHeightForWidth(
            self.g_settings_label.sizePolicy().hasHeightForWidth()
        )
        self.g_settings_label.setSizePolicy(sizePolicy)
        self.g_settings_label.setMinimumSize(QtCore.QSize(0, 20))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.g_settings_label.setFont(font)
        self.g_settings_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.g_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.g_settings_label.setObjectName("g_settings_label")
        self.verticalLayout_3.addWidget(self.g_settings_label)
        self.select_fw_label = QtWidgets.QLabel(self.TopLeftLayout)

        sizePolicy.setHeightForWidth(
            self.select_fw_label.sizePolicy().hasHeightForWidth()
        )
        self.select_fw_label.setSizePolicy(sizePolicy)
        self.select_fw_label.setObjectName("select_fw_label")
        self.horizontalLayout_2.addWidget(self.select_fw_label)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )

        self.fw_selected = QtWidgets.QComboBox(self.TopLeftLayout)
        self.fw_selected.setSizePolicy(sizePolicy)
        self.fw_selected.setMinimumSize(QtCore.QSize(60, 0))
        self.fw_selected.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fw_selected.setObjectName("fw_selected")
        self.horizontalLayout_2.addWidget(self.fw_selected)
        sizePolicy.setHeightForWidth(self.fw_selected.sizePolicy().hasHeightForWidth())

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        self.show_latest_fw_label = QtWidgets.QLabel(self.TopLeftLayout)
        self.show_latest_fw_label.setSizePolicy(sizePolicy)
        self.show_latest_fw_label.setObjectName("show_latest_fw_label")
        sizePolicy.setHeightForWidth(
            self.show_latest_fw_label.sizePolicy().hasHeightForWidth()
        )
        self.horizontalLayout_2.addWidget(self.show_latest_fw_label)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )

        self.num_fw_selected = QtWidgets.QSpinBox(self.TopLeftLayout)
        self.num_fw_selected.setSizePolicy(sizePolicy)
        self.num_fw_selected.setFrame(True)
        self.num_fw_selected.setAlignment(QtCore.Qt.AlignCenter)
        self.num_fw_selected.setMinimum(2)
        self.num_fw_selected.setObjectName("num_fw_selected")
        sizePolicy.setHeightForWidth(
            self.num_fw_selected.sizePolicy().hasHeightForWidth()
        )

        self.horizontalLayout_2.addWidget(self.num_fw_selected)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )

        self.mode_label = QtWidgets.QLabel(self.TopLeftLayout)
        self.mode_label.setSizePolicy(sizePolicy)
        self.mode_label.setObjectName("mode_label")
        sizePolicy.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.horizontalLayout_3.addWidget(self.mode_label)

        self.Offline_mode = QtWidgets.QRadioButton(self.TopLeftLayout)
        self.Offline_mode.setSizePolicy(sizePolicy)
        self.Offline_mode.setMinimumSize(QtCore.QSize(100, 0))
        self.Offline_mode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Offline_mode.setChecked(True)
        self.Offline_mode.setObjectName("Offline_mode")
        sizePolicy.setHeightForWidth(self.Offline_mode.sizePolicy().hasHeightForWidth())
        self.horizontalLayout_3.addWidget(self.Offline_mode)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )

        self.Online_mode = QtWidgets.QRadioButton(self.TopLeftLayout)
        self.Online_mode.setSizePolicy(sizePolicy)
        self.Online_mode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Online_mode.setObjectName("Online_mode")
        self.horizontalLayout_3.addWidget(self.Online_mode)
        sizePolicy.setHeightForWidth(self.Online_mode.sizePolicy().hasHeightForWidth())

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.SubmitBtn = QtWidgets.QPushButton(self.TopLeftLayout)
        self.SubmitBtn.setSizePolicy(sizePolicy)
        self.SubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitBtn.setObjectName("SubmitBtn")
        self.SubmitBtn.clicked.connect(self.write_set_ini)
        self.verticalLayout_4.addWidget(self.SubmitBtn)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        sizePolicy.setHeightForWidth(self.SubmitBtn.sizePolicy().hasHeightForWidth())

        self.formLayout_5.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.TopLeftLayout
        )
        self.topRightLayout = QtWidgets.QFrame(self.centralwidget)
        self.topRightLayout.setFrameShape(QtWidgets.QFrame.Box)
        self.topRightLayout.setObjectName("topRightLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topRightLayout)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(20, 1, 20, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )

        font.setBold(True)
        font.setWeight(75)
        self.l_settings_label = QtWidgets.QLabel(self.topRightLayout)
        self.l_settings_label.setSizePolicy(sizePolicy)
        self.l_settings_label.setMinimumSize(QtCore.QSize(0, 30))
        self.l_settings_label.setFont(font)
        self.l_settings_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.l_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.l_settings_label.setObjectName("l_settings_label")
        self.verticalLayout_2.addWidget(self.l_settings_label)
        sizePolicy.setHeightForWidth(
            self.l_settings_label.sizePolicy().hasHeightForWidth()
        )

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.status_label = QtWidgets.QLabel(self.topRightLayout)
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_4.addWidget(self.status_label)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )

        self.status = QtWidgets.QLabel(self.topRightLayout)
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QtCore.QSize(0, 30))
        self.status.setStyleSheet("color: rgb(152, 255, 88);")
        self.status.setFrameShape(QtWidgets.QFrame.Box)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.horizontalLayout_4.addWidget(self.status)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.current_db_entries_lable = QtWidgets.QLabel(self.topRightLayout)
        self.current_db_entries_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.current_db_entries_lable.setObjectName("current_db_entries_lable")
        self.horizontalLayout_8.addWidget(self.current_db_entries_lable)

        font.setPointSize(6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.entries_num = QtWidgets.QLCDNumber(self.topRightLayout)
        self.entries_num.setFont(font)
        self.entries_num.setStyleSheet("color: rgb(73, 170, 255);")
        self.entries_num.setFrameShadow(QtWidgets.QFrame.Plain)
        self.entries_num.setLineWidth(1)
        self.entries_num.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.entries_num.setObjectName("entries_num")
        self.horizontalLayout_8.addWidget(self.entries_num)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )

        self.UpdateDbBtn = QtWidgets.QPushButton(self.topRightLayout)
        self.UpdateDbBtn.setSizePolicy(sizePolicy)
        self.UpdateDbBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.UpdateDbBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UpdateDbBtn.setObjectName("UpdateDbBtn")
        self.UpdateDbBtn.clicked.connect(self.Check_db)

        sizePolicy.setHeightForWidth(self.UpdateDbBtn.sizePolicy().hasHeightForWidth())
        self.horizontalLayout_5.addWidget(self.UpdateDbBtn)

        self.progressBar = QtWidgets.QProgressBar(self.topRightLayout)
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setStyleSheet("color: rgb(0, 0, 0);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.formLayout_5.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.topRightLayout
        )
        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.BottomLayout.setContentsMargins(-1, 50, -1, -1)
        self.BottomLayout.setSpacing(2)
        self.BottomLayout.setObjectName("BottomLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.BottomLayout.addWidget(self.line_2)

        self.BackgroundLayout.setLayout(
            2, QtWidgets.QFormLayout.SpanningRole, self.BottomLayout
        )
        self.BackgroundLayout.setLayout(
            0, QtWidgets.QFormLayout.SpanningRole, self.formLayout_5
        )

        font.setPointSize(8)
        self.My_twitter = QtWidgets.QLabel(self.centralwidget)
        self.My_twitter.setAlignment(QtCore.Qt.AlignCenter)
        self.My_twitter.setOpenExternalLinks(True)
        self.My_twitter.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse
        )
        self.My_twitter.setObjectName("My_twitter")
        self.KiiWii_twitter = QtWidgets.QLabel(self.centralwidget)
        self.PayPal = QtWidgets.QLabel(self.centralwidget)
        self.PayPal.setOpenExternalLinks(True)
        self.PayPal.setObjectName("PayPal")
        self.PayPal.setAlignment(QtCore.Qt.AlignCenter)
        self.KiiWii_twitter.setFont(font)
        self.KiiWii_twitter.setAlignment(QtCore.Qt.AlignCenter)
        self.KiiWii_twitter.setOpenExternalLinks(True)
        self.KiiWii_twitter.setObjectName("KiiWii_twitter")
        self.BottomLayout.addWidget(self.PayPal)
        self.BottomLayout.addWidget(self.My_twitter)
        self.BottomLayout.addWidget(self.KiiWii_twitter)
        self.MiddleLayout = QtWidgets.QFrame(self.centralwidget)
        self.MiddleLayout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MiddleLayout.setObjectName("MiddleLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MiddleLayout)
        self.gridLayout_3.setContentsMargins(100, 60, 100, 20)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.logs = QtWidgets.QTextBrowser(self.MiddleLayout)
        self.logs.setFrameShape(QtWidgets.QFrame.Box)
        self.logs.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logs.setObjectName("logs")
        self.gridLayout_3.addWidget(self.logs, 7, 1, 1, 1)

        font.setPointSize(13)
        self.LeastFw = QtWidgets.QLineEdit(self.MiddleLayout)
        self.LeastFw.setFont(font)
        self.LeastFw.setStyleSheet("color: rgb(73, 170, 255);")
        self.LeastFw.setMaxLength(100)
        self.LeastFw.setAlignment(QtCore.Qt.AlignCenter)
        self.LeastFw.setReadOnly(True)
        self.LeastFw.setObjectName("LeastFw")
        self.gridLayout_3.addWidget(self.LeastFw, 5, 1, 1, 1)

        self.GameReleaseDate = QtWidgets.QLineEdit(self.MiddleLayout)
        self.GameReleaseDate.setFont(font)
        self.GameReleaseDate.setStyleSheet("color: rgb(73, 170, 255);")
        self.GameReleaseDate.setAlignment(QtCore.Qt.AlignCenter)
        self.GameReleaseDate.setReadOnly(True)
        self.GameReleaseDate.setObjectName("GameReleaseDate")
        self.gridLayout_3.addWidget(self.GameReleaseDate, 4, 1, 1, 1)

        self.GameTitle = QtWidgets.QLineEdit(self.MiddleLayout)
        self.GameTitle.setFont(font)
        self.GameTitle.setStyleSheet("color:rgb(73, 170, 255);")
        self.GameTitle.setMaxLength(60)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName("GameTitle")
        self.GameTitle.setPlaceholderText("Enter Game title")
        self.GameTitle.setFocus()
        self.game_title_label = QtWidgets.QLabel(self.MiddleLayout)
        self.gridLayout_3.addWidget(self.GameTitle, 0, 1, 1, 1)

        self.Comp = QtWidgets.QLineEdit(self.MiddleLayout)
        self.Comp.setFont(font)
        self.Comp.setStyleSheet("color:rgb(73, 170, 255);")
        self.Comp.setAlignment(QtCore.Qt.AlignCenter)
        self.Comp.setReadOnly(True)
        self.Comp.setObjectName("Comp")
        self.gridLayout_3.addWidget(self.Comp, 3, 1, 1, 1)
        self.BackgroundLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.MiddleLayout
        )
        self.gridLayout_2.addLayout(self.BackgroundLayout, 0, 0, 1, 1)

        font.setPointSize(11)
        self.least_fw_label = QtWidgets.QLabel(self.MiddleLayout)
        self.least_fw_label.setFont(font)
        self.least_fw_label.setObjectName("least_fw_label")
        self.gridLayout_3.addWidget(self.least_fw_label, 5, 0, 1, 1)

        self.comp_label = QtWidgets.QLabel(self.MiddleLayout)
        self.comp_label.setFont(font)
        self.comp_label.setObjectName("comp_label")
        self.gridLayout_3.addWidget(self.comp_label, 3, 0, 1, 1)

        self.game_release_label = QtWidgets.QLabel(self.MiddleLayout)
        self.game_release_label.setFont(font)
        self.game_release_label.setObjectName("game_release_label")
        self.gridLayout_3.addWidget(self.game_release_label, 4, 0, 1, 1)

        self.game_title_label.setFont(font)
        self.game_title_label.setObjectName("game_title_label")
        self.gridLayout_3.addWidget(self.game_title_label, 0, 0, 1, 1)
        self.logs_label = QtWidgets.QLabel(self.MiddleLayout)
        self.logs_label.setFont(font)
        self.logs_label.setObjectName("logs_label")
        self.gridLayout_3.addWidget(self.logs_label, 7, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem)

        font.setPointSize(10)
        self.CheckBtn = QtWidgets.QPushButton(self.MiddleLayout)
        self.CheckBtn.setFont(font)
        self.CheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckBtn.setStyleSheet("background-color: rgb(73, 170, 255);")
        self.CheckBtn.setObjectName("CheckBtn")
        self.horizontalLayout_10.addWidget(self.CheckBtn)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.CheckBtn.clicked.connect(self.CheckGame)

        self.SuggestionLayout = QtWidgets.QFrame(self.MiddleLayout)
        self.SuggestionLayout.setFrameShape(QtWidgets.QFrame.Box)
        self.SuggestionLayout.setLineWidth(1)
        self.SuggestionLayout.setMidLineWidth(0)
        self.SuggestionLayout.setObjectName("SuggestionLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.SuggestionLayout)
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Suggestion_Label = QtWidgets.QLabel(self.SuggestionLayout)
        self.Suggestion_Label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Suggestion_Label.sizePolicy().hasHeightForWidth()
        )
        self.Suggestion_Label.setSizePolicy(sizePolicy)

        font.setPointSize(11)
        self.Suggestion_Label.setFont(font)
        self.Suggestion_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Suggestion_Label.setObjectName("Suggestion_Label")
        self.horizontalLayout_6.addWidget(self.Suggestion_Label)
        self.Suggestions = QtWidgets.QComboBox(self.SuggestionLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Suggestions.sizePolicy().hasHeightForWidth())
        self.Suggestions.setSizePolicy(sizePolicy)
        self.Suggestions.setMinimumSize(QtCore.QSize(0, 25))

        font.setPointSize(14)
        font.setWeight(50)
        self.Suggestions.setFont(font)
        self.Suggestions.setFrame(True)
        self.Suggestions.setObjectName("Suggestions")

        self.horizontalLayout_6.addWidget(self.Suggestions)
        self.SelectBtn = QtWidgets.QPushButton(self.SuggestionLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectBtn.sizePolicy().hasHeightForWidth())
        self.SelectBtn.setSizePolicy(sizePolicy)
        self.SelectBtn.setMinimumSize(QtCore.QSize(40, 0))
        self.SuggestionLayout.hide()

        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectBtn.setFont(font)
        self.SelectBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SelectBtn.setStyleSheet("background-color: rgb(73, 170, 255);")
        self.SelectBtn.setObjectName("SelectBtn")
        self.horizontalLayout_6.addWidget(self.SelectBtn)
        self.gridLayout_3.addWidget(self.SuggestionLayout, 1, 1, 1, 1)

        # Setup local database
        self.setupDb()  # Check and make sure for a vaild db, otherwise download
        self.Check_db("Found")  # update entries for next run
        self.updatelocal_db_settings()
        self.render_fws()


        CGFw.setCentralWidget(self.centralwidget)
        self.retranslateUi(CGFw)
        QtCore.QMetaObject.connectSlotsByName(CGFw)

    def retranslateUi(self, CGFw):
        _translate = QtCore.QCoreApplication.translate
        CGFw.setWindowTitle(_translate("CGFw", "CGFw v" + str(self.ver)))

        self.CheckBtn.setText(_translate("CGFw", "Search"))
        self.CheckBtn.setShortcut("Return")
        self.SelectBtn.setText(_translate("CGFw", "Select"))
        self.SelectBtn.setShortcut("Ctrl+Return")

        self.Comp.setText(_translate("CGFw", "None"))
        self.LeastFw.setText(_translate("CGFw", "None"))
        self.logs_label.setText(_translate("CGFw", "Logs: "))
        self.status_label.setText(_translate("CGFw", "Status:"))
        self.GameReleaseDate.setText(_translate("CGFw", "None"))
        self.mode_label.setText(_translate("CGFw", "Search mode: "))
        self.SubmitBtn.setText(_translate("CGFw", "Save and update changes"))
        self.comp_label.setText(_translate("CGFw", "Compatibility: "))
        self.UpdateDbBtn.setText(_translate("CGFw", "Update Database"))
        self.game_title_label.setText(_translate("CGFw", "Game Title: "))
        self.g_settings_label.setText(_translate("CGFw", "General Settings"))
        self.select_fw_label.setText(_translate("CGFw", "Select firmware: "))
        self.least_fw_label.setText(_translate("CGFw", "Least fw required:"))
        self.Suggestion_Label.setText(_translate("CGFw", "Did you mean ..."))
        self.game_release_label.setText(_translate("CGFw", "Game Release: "))
        self.Online_mode.setText(
            _translate("CGFw", "Online (Slower, more games)")
        )
        self.l_settings_label.setText(_translate("CGFw", "Local database Settings"))
        self.Offline_mode.setText(_translate("CGFw", "Offline (Faster, less games) "))
        self.show_latest_fw_label.setText(_translate("CGFw", "Show latest firmwares: "))
        self.current_db_entries_lable.setText(
            _translate("CGFw", "Current database entries: ")
        )
        self.My_twitter.setText(
            _translate(
                "CGFw",
                '<html><head/><body><p align="center"><a href="https://twitter.com/OfficialAhmed0"><span style=" font-family:\'verdana\'; font-size:12pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Created By @OfficialAhmed0</span></a></p></body></html>',
            )
        )
        self.PayPal.setText(
            _translate(
                "CGFw",
                '<html><head/><body><p align="center"><a href="https://www.paypal.com/paypalme/Officialahmed0"><span style=" font-family:\'verdana\'; font-size:12pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Support me (PayPal)</span></a></p></body></html>',
            )
        )
        self.KiiWii_twitter.setText(
            _translate(
                "CGFw",
                '<html><head/><body><p align="center"><a href="https://twitter.com/DefaultDNB"><span style=" font-family:\'verdana\'; font-size:11pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Special Thanks to @DefaultDNB aka KiiWii for the database</span></a></p></body></html>',
            )
        )

    def readSetting(self):
        # Local setting file (set.ini)
        try:
            with open("set.ini", "r") as setting_file:
                read = setting_file.readline().split(";")
                self.setting["show fw"] = int(read[0])
                self.db["Local entries"] = int(read[1])
                self.setting["fw"] = read[2]
                self.setting["mode"] = read[3] 
                
        except Exception as e:  
            print("Set.ini Not found", str(e))
            with open("set.ini", "w+") as setting_file:
                data = (
                    str(self.setting["show fw"])
                    + ";"
                    + str(self.db["Local entries"])
                    + ";"
                    + self.setting["fw"]
                    + ";"
                    + self.setting["mode"]
                )
                setting_file.write(data)
        
        try:
            with open(
                self.fw_db["dir"] + self.fw_db["name"],
                "r",
                encoding="utf-8",
            ) as fw_file:
                pos = 0
                read = fw_file.readlines()
                read.reverse()
                for i in read:
                    if self.setting["fw"].strip() == i.split(" ")[0]:
                        self.fw_selected.setCurrentIndex(pos)
                    else:
                        pos += 1
        except:
            self.fw_selected.setCurrentIndex(0)

    def setupDb(self):
        try:  # database dir found ?
            database_location = self.db["dir"] + "\\" + self.db["name"]
            database_size = round(
                os.path.getsize(database_location) / 1024
            )
            # local database found ? check size
            if os.path.exists(database_location) == True:
                if (database_size < 400):  # Always work with size greater than 400kb database else update it
                    self.Check_db("Not found")
                else:
                    try:
                        with open(database_location, encoding="UTF-8") as file:
                            self.db["Local entries"] = len(file.readlines())
                    except Exception as e:
                        self.updateLogs(
                            self.colors["Fail"]
                            + ';">[Database]: Couldn\'t read database.Try restarting, or update database. Otherwise, contact dev \nDev_Error: '
                            + str(e)
                        )
            else:
                self.Check_db("Not found")
        except:
            self.Check_db("Not found")

    def read_set_ini(self): 
        """
        ###############################################################################################
        ########                Fetch and set data from ini file                              #########
        ###############################################################################################
        """
        with open("set.ini") as file:
            data = file.readline().split(";")

            self.setting["show fw"] = int(data[0])
            self.db["Local entries"] = int(data[1])
            self.setting["fw"] = data[2]
            self.setting["mode"] = data[3]

            self.num_fw_selected.setValue(int(data[0]))
            self.entries_num.display(data[1])
            self.fw_selected.setCurrentIndex(self.fw_selected.findText(data[2]))
            if data[3] == "Online":
                self.Online_mode.setChecked(True)
            else:
                self.Offline_mode.setChecked(True)
    
    def write_set_ini(self):
        """
        ###############################################################################################
        ########                     Store set of data into ini                               #########
        ###############################################################################################
        """
        # Prepare and Double check data before overwiritting
        self.setting["show fw"] = self.num_fw_selected.value()
        if self.db["Online entries"] != 0:
            self.db["Local entries"] = self.db["Online entries"]
        else:
            #read db and get num of entries
            pass

        self.setting["fw"] = self.fw_selected.currentText()
        if self.Online_mode.isChecked():
            self.setting["mode"] = "Online"
        else:
            self.setting["mode"] = "Offline"

        # Save data
        with open("set.ini", "w+") as file:
            data = [
                self.setting["show fw"],
                self.db["Local entries"],
                self.setting["fw"],
                self.setting["mode"]]
    
            for new_data in data:
                file.write(str(new_data)+";")
              
    def updateLogs(self, l):
        start_style = '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; color:'
        end_style = "</span></p>\n"
        self.logging += start_style + l + end_style
        self.logs.setHtml(self.logging)
        self.logs.moveCursor(QtGui.QTextCursor.End)

    def updateStatus(self, color, line):
        self.status.setStyleSheet("color:" + color + ";")
        self.status.setText(line)

    def updatelocal_db_settings(self, updated=False):
        
        self.entries_num.setDigitCount(
            len(str(self.db["Local entries"])) # align digits => by num of digits "center"
        )
        self.entries_num.display(self.db["Local entries"])
        self.num_fw_selected.setProperty("value", self.setting["show fw"])
        if updated == False:
            self.updateStatus(self.colors["Warning"], "Click on check button")
        else:
            self.updateStatus(self.colors["Success"], "latest database")
            self.UpdateDbBtn.setEnabled(False)

    def GrabFwFrom(self, where="Online"):
        """
        Check for (Firmware) in database and exclude
        pre-installed , Patch Firmwares then grab only version num and date of release
        """
        with open(self.db["dir"] + "\PS4 db.txt", encoding="utf-8") as file:
            fws = []
            for i in file.readlines():
                if "Firmware" in i:
                    if "Pre-installed" not in i and "Pre-Installed" not in i:
                        if not "Patch Firmware" in i:
                            fwinfo = i.replace("\n", "").split(" ")
                            fw = (
                                str(
                                    fwinfo[0]
                                    + " "
                                    + fwinfo[2]
                                    + " "
                                    + fwinfo[3]
                                    + fwinfo[4]
                                )
                                .replace("[", "")
                                .replace("]", "")
                                .replace(",", " ")
                            )
                            if (
                                "1." not in fw
                                and "1." not in fw
                                and "1." not in fw 
                                and "0A" not in fw
                                and "0B" not in fw
                                and "0C" not in fw
                            ):
                                fws.append(fw)

        with open(
            self.fw_db["dir"] + self.fw_db["name"], "w+", encoding="utf-8"
        ) as write_fw_file:
            fws.sort()
            for fw in fws:
                slices = fw.split(" ")
                if (
                    len(slices) == 3
                ):  # Day and year are mixed together from deafaulDnb db
                    if len(slices[-1]) == 6:
                        day = slices[-1][:2]
                        year = slices[-1][2:]
                    elif len(slices[-1]) == 5:
                        day = slices[-1][0]
                        year = slices[-1][1:]
                    write_fw_file.write(
                        slices[0] + " " + slices[1] + " " + day + " " + year + "\n"
                    )
                else:
                    write_fw_file.write(fw + "\n")
                if where == "local":
                    self.firmwares.append(fw[: fw.find(" ")])

    def Check_db(self, Db_state="Look for update"):
        """
        Find from DEFAULTDNB a line that matches:
        xxxx+ lines (xxxx+ sloc) to parse total number of entries in db
        then fetch only first digits by spliting spaces
        and then download database
        """
        try:
            if Db_state == "Not found":
                self.GameTitle.setEnabled(False)
                self.CheckBtn.setEnabled(False)
                self.UpdateRequested()

            elif Db_state == "Found":
                self.entries_num.display(self.db["Local entries"])
                self.GrabFwFrom("local")
                self.render_fws()
                self.updatelocal_db_settings()

            else:  # if result == False
                self.UpdateRequested()
        except:
            self.updateLogs(
                self.colors["Warning"] + "[Database]: Cannot download."
            )

    def render_fws(self):
        firmwares_2_show = self.num_fw_selected.value()
    
        try:
            with open(self.fw_db["dir"] + self.fw_db["name"]) as file:
                self.fw_selected.clear()

                all_fws = [x.split(" ")[0] for x in file.readlines()]
                all_fws.reverse()
                self.num_fw_selected.setRange(1, len(all_fws))
                self.fw_selected.addItems(all_fws[:firmwares_2_show])

            self.updateLogs(
                self.colors["Success"]
                + ';">[Setting]: Generated cache'
            )
            self.readSetting()
            self.read_set_ini()
            
        except Exception as e:
            self.updateLogs(
                self.colors["Fail"]
                + ';">[Unknown]: Cannot fetch firmwares data. DEV_Error: Related to fw file => '
                + str(e)
            )
            self.updateStatus(self.colors["Fail"], "Download required")           

    def UpdateRequested(self):
        self.UpdateDbBtn.setEnabled(False)
        grabInfo = ""
        try:
            grabInfo = requests.get(self.db["data"]).text

        except:  # Couldnt request link
            database = self.db["dir"] + "\\" + self.db["name"]

            if os.path.exists(database):
                if os.path.getsize(database) / 1000 > 400:
                    self.UpdateDbBtn.setEnabled(True)
                    self.updateLogs(
                        self.colors["Success"]
                        + ';">[Database]: Current one is the latest'
                    )
                    self.updatelocal_db_settings(True)
            else:
                self.updatelocal_db_settings()
                self.updateLogs(
                    self.colors["Fail"]
                    + ';">[Internet]: Cannot download database. No Internet connection'
                )

        # No request means this block of code wont run
        # start of block
        if len(grabInfo) != 0:  # Data from DefaultDNB found
            self.db["Online entries"] = grabInfo.count("\n")

            if self.db["Online entries"] > self.db["Local entries"]:
                self.db["Local entries"] = self.db["Online entries"]
                Games = requests.get(self.db["data"]).text.split(
                    "\n"
                )  # all entries From DEFAULTDNB db
                if os.path.exists(self.db["dir"]) == False:
                    os.mkdir(self.db["dir"])

                progress = 0
                with open(
                    self.db["dir"] + "\\" + self.db["name"], "w+", encoding="utf-8"
                ) as local_db:
                    for Game in Games:
                        local_db.write(Game.title())
                        progress += 1
                        self.updateProgressBar(progress)

                self.GrabFwFrom("local")
                self.render_fws()
                self.write_set_ini()

                self.updateLogs(
                    self.colors["Success"] + ';">[Database]: Downloaded successfully. Restart required'
                )

                self.updateStatus(self.colors["Success"], "This is the latest database")

                self.CheckBtn.setEnabled(True)
                self.GameTitle.setEnabled(True)
                self.SubmitBtn.setEnabled(True)
                self.UpdateDbBtn.setEnabled(True)
                self.updatelocal_db_settings(True)
                self.GameTitle.setPlaceholderText("Enter Game title")
            else:
                self.updateStatus(self.colors["Success"], "This is the latest database")

        else:
            self.UpdateDbBtn.setEnabled(True)
            fw_database = self.fw_db["dir"] + self.fw_db["name"]
            errorFound = False

            if os.path.exists(fw_database):
                # Db firmwares must be greater than or equel 600 bytes
                if os.path.getsize(fw_database) < 600:
                    self.GameTitle.setPlaceholderText(
                        "Download Database required for PS4 firmwares"
                    )
                    errorFound = True
            else:
                errorFound = True

            if errorFound:
                self.GameTitle.setPlaceholderText(
                    "Download Database required for PS4 firmwares"
                )
                self.CheckBtn.setEnabled(False)
                self.GameTitle.setEnabled(False)
                self.SubmitBtn.setEnabled(False)

    def updateProgressBar(self, percent):
        max = self.db["Online entries"]
        num = int(max * (percent / 100))
        self.progressBar.setProperty("value", percent)

    def CheckGame(self):
        import random

        self.Suggestions.clear()
        funMessage = (
            "What the heck dude!",
            "Come on now bro...",
            "What are you doing?",
            "You kidding me?",
            "Have you lost your mind?",
            "You've gotta be kiddin' me...",
            "What in the world",
            "Ok now stop it...",
            "Stop confussing me...",
            "I'm not Google to guess the game title for you...",
            "Quit playing around...",
            "I ain't stupid...",
            "Seriously Stop it...",
        )

        Game = self.GameTitle.text().strip()
        randomMessage = random.choice(funMessage)
        # Avoid looking for big chunks of data
        if len(Game) == 0:
            self.updateLogs(
                self.colors["Warning"]
                + ';">[GameTitle]: '
                + randomMessage
                + " The game title field is empty."
            )  # :) just for fun
        elif len(Game) < 2:
            self.updateLogs(
                self.colors["Warning"]
                + ";\">[GameTitle]: Is this an abbreviation? Please type the game title or releaseDate"
            )

        else:
            self.setting["fw"] = self.fw_selected.currentText()
            fw = self.setting["fw"]

            if self.Online_mode.isChecked():
                """ 
                ####################################################################################################
                ###   use Google/PS store as search engine for Online mode to get the possible match of the user input 
                ####################################################################################################
                """
                self.setting["mode"] = "Online"
                try:
                    userSearch = self.GameTitle.text().replace(" ", "+")
                    GoogleSearch = requests.get(f"https://www.google.com/search?q={userSearch}+playstation+store").text
                    GoogleSearch = bs(GoogleSearch,"html.parser").prettify()
                    GoogleTags = GoogleSearch.split("\n")
                    links = []
                    HTMLTagCounter = 0
                    titleFound = ""
                    for tag in GoogleTags:
                        if "https://store.playstation.com" in tag and "href" in tag and "product" in tag:
                            try:
                                if userSearch.replace("+", " ").lower() in GoogleTags[HTMLTagCounter+4].lower():
                                    titleFound = GoogleTags[HTMLTagCounter+4].strip()
                                    links.append(tag[tag.find('https://'):tag.find('/&')])
                                HTMLTagCounter += 3
                            except IndexError:
                                pass
                        HTMLTagCounter += 1

                    if len(links) != 0: #Found ps store link
                        self.updateLogs(
                            self.colors["Success"] + ';">[Found]: '
                            + titleFound
                        )
                        print(f"found this link {links[0]}")

                    else:
                        self.updateLogs(
                            self.colors["Fail"]
                            + ';">[GameTitle]: '
                            + "Couldn't find " + userSearch.replace('+', ' ') + " on PlayStation Store"
                        )

                except Exception as e:
                    self.updateLogs(
                        self.colors['Fail'] 
                        + ';">[Connection]: Cannot search this game Online. \nDEV_Error: ' + str(e)
                        + ' Make sure you\'ve Internet connection. Otherwise, send me a screenshot of the Dev_error or submit an issue on Github'
                    )

            else:
                """ 
                ####################################################################################################
                ####    Simple Search engine for offline mode to get the possible match of the user input 
                ####################################################################################################
                """
                self.setting["mode"] = "Offline"

                self.relavent = []
                self.entry = ""
                with open(self.db["dir"] + "\PS4 db.txt", encoding="utf-8") as file:
                    entries = file.readlines()

                    for entry in entries:
                        if Game in entry or Game.title() in entry:
                            if "Firmware" not in entry and "Unreleased" not in entry:
                                self.relavent.append(entry)

                if len(self.relavent) > 1:  # Show Suggestions
                    for GameTitleFromDB in self.relavent:
                        title = GameTitleFromDB[: GameTitleFromDB.find("(")]
                        self.Suggestions.addItem(" " * 4 + title)
                    self.SuggestionLayout.show()
                    self.Suggestions.setFocus()
                    self.SelectBtn.clicked.connect(self.SelectGame)
                    self.updateLogs(
                        self.colors["Warning"]
                        + ';">[GameTitle]: found '
                        + str(len(self.relavent))
                        + " titles for "
                        + Game
                    )

                elif len(self.relavent) == 1:
                    GameTitleDisplay = self.relavent[0][: self.relavent[0].find("(")]
                    self.GameTitle.setText(GameTitleDisplay)
                    self.entry = self.relavent[0]
                    self.updateLogs(
                        self.colors["Success"]
                        + ';">[GameTitle]: Found '
                        + GameTitleDisplay
                    )
                    self.isCompatible()

                else:
                    self.updateLogs(
                        self.colors["Fail"]
                        + ';">[GameTitle]: '
                        + Game
                        + " Cannot be found in offline mode."
                    )
                    self.CheckBtn.setEnabled(True)

    def SelectGame(self):
        try:
            self.entry = self.relavent[self.Suggestions.currentIndex()]
            ChosenGameTitle = self.Suggestions.currentText().strip()
            self.GameTitle.setText(ChosenGameTitle)
            # Remove suggestions / relavent
            self.Suggestions.clear()
            self.SuggestionLayout.hide()
            self.isCompatible()
        except:
            """
            * Temporary fix *
            loop when search clicked more than once by clearing relavent list results
            handle occured error by passing empty exception
            """
            pass

    def isCompatible(self):
        self.relavent.clear()
        self.CheckBtn.setEnabled(False)

        # Firmware specifications
        FwReleaseDate = self.fw_selected.currentText()
        latest_fw = False
        if FwReleaseDate == self.firmwares[-1]:
            latest_fw = True

        self.fw_year, self.later_fw_year = 0, 0
        self.fw_month, self.later_fw_month = 0, 0
        self.fw_day, self.later_fw_day = 0, 0
        with open(self.fw_db["dir"] + self.fw_db["name"]) as fw_file:
            read = fw_file.readlines()
            for i in read:
                if FwReleaseDate in i:
                    slice = i.split(" ")
                    self.fw_year = slice[-1]
                    self.fw_month = self.month[slice[1]]
                    self.fw_day = slice[2]
                if latest_fw == False:  # Look for a later fw date
                    if self.firmwares[self.firmwares.index(FwReleaseDate) + 1] in i:
                        slice = i.split(" ")
                        self.later_fw_year = int(slice[-1].strip())
                        self.later_fw_month = self.month[slice[1]]
                        self.later_fw_day = int(slice[2].strip())
        # GameTitle specifications
        beginSlice = self.entry.find("[") + 1
        endSlice = self.entry.find("]")
        GameReleaseDate = self.entry[beginSlice:endSlice]
        self.Game_year = int(GameReleaseDate[-4:].strip())
        self.Game_month = self.month[GameReleaseDate[:3]]
        self.Game_day = int(
            GameReleaseDate[
                GameReleaseDate.find(" ") : GameReleaseDate.find(",")
            ].strip()
        )

        self.leastFw(self.Game_year, self.Game_month, self.Game_day)
        # 6 and fw year 4
        self.GameReleaseDate.setText(GameReleaseDate)
        if latest_fw == False:  # If this is not the latest official firmware available
            if self.Game_year == self.later_fw_year:
                if self.Game_month <= self.later_fw_month:
                    if self.Game_day <= self.later_fw_day:
                        self.DisplayCompatible()
                    else:
                        self.DisplayCompatible()
                else:
                    self.DisplayCompatible("Not sure")
            elif self.Game_year < self.later_fw_year:
                self.DisplayCompatible()
            else:
                self.DisplayCompatible("no")
        else:  # If this is the latest official firmware available
            self.DisplayCompatible()

    def DisplayCompatible(self, it_is="yes"):
        if it_is == "yes":
            self.Comp.setText("Compatible")
            self.Comp.setStyleSheet("color:" + self.colors["Success"] + ";")
            self.GameReleaseDate.setStyleSheet("color:" + self.colors["Success"] + ";")
            self.LeastFw.setStyleSheet("color:" + self.colors["Success"] + ";")
        elif it_is == "no":
            self.Comp.setText("Incompatible")
            self.Comp.setStyleSheet("color:" + self.colors["Fail"] + ";")
            self.GameReleaseDate.setStyleSheet("color:" + self.colors["Fail"] + ";")
            self.LeastFw.setStyleSheet("color:" + self.colors["Fail"] + ";")
        else:
            self.Comp.setText(
                "Incompatible unless it was built on older SDK ["
                + self.calculateChance()
                + "% might be compatible]"
            )
            self.Comp.setStyleSheet("color:" + self.colors["Warning"] + ";")
            self.GameReleaseDate.setStyleSheet("color:" + self.colors["Warning"] + ";")
            self.LeastFw.setStyleSheet("color:" + self.colors["Warning"] + ";")
        self.CheckBtn.setEnabled(True)

    def leastFw(self, year, month, day):
        with open(self.fw_db["dir"] + self.fw_db["name"]) as file:
            fws = file.readlines()
            pos = 0
            # fws.reverse()
            for fw in fws:
                fw_info = fw.split(" ")
                self.fw_year = fw_info[-1].strip()
                self.fw_month = self.month[fw_info[1]]
                if year <= int(self.fw_year):
                    if month <= self.fw_month:
                        break
                pos += 1
            # Get 2nd most early fw which most probably will be the least
            self.LeastFw.setText(fws[pos - 1].split(" ")[0])

    def calculateChance(self):
        """
        calculate the difference between the months to
        determine approx. % of compatiblity
        """
        diff = self.Game_month - self.later_fw_month  # difference
        temp = 21

        if diff >= 100:
            return "5"
        elif diff == 0:
            return "90"
        else:
            return str(100 - diff * temp)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CGFw = QtWidgets.QMainWindow()
    ui = Ui_CGFw()
    ui.setupUi(CGFw)
    CGFw.show()
    sys.exit(app.exec_())
