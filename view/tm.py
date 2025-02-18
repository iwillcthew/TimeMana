# Form implementation generated from reading ui file 'tm.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 384)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(712, 384))
        MainWindow.setMaximumSize(QtCore.QSize(712, 384))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(712, 384))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 712, 352))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(23, 10, 250, 40))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"border: 2px solid black;\n"
"border: 5px solid rgba(255,255,255,0%);\n"
"border-radius: 10px;\n"
"background: rgba(255,255,255,80%);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btnStart = QtWidgets.QPushButton(self.page)
        self.btnStart.setGeometry(QtCore.QRect(30, 15, 30, 30))
        self.btnStart.setStyleSheet("border:0px;")
        self.btnStart.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assert/start light mode.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setIconSize(QtCore.QSize(24, 24))
        self.btnStart.setObjectName("btnStart")
        self.chartStackedWidget = QtWidgets.QStackedWidget(self.page)
        self.chartStackedWidget.setGeometry(QtCore.QRect(10, 50, 691, 301))
        self.chartStackedWidget.setObjectName("chartStackedWidget")
        self.chart_1 = QtWidgets.QWidget()
        self.chart_1.setObjectName("chart_1")
        self.widgetChart1 = QtWidgets.QWidget(self.chart_1)
        self.widgetChart1.setGeometry(QtCore.QRect(30, 10, 631, 281))
        self.widgetChart1.setObjectName("widgetChart1")
        self.chartStackedWidget.addWidget(self.chart_1)
        self.chart_2 = QtWidgets.QWidget()
        self.chart_2.setObjectName("chart_2")
        self.widgetChart2 = QtWidgets.QWidget(self.chart_2)
        self.widgetChart2.setGeometry(QtCore.QRect(30, 10, 371, 281))
        self.widgetChart2.setObjectName("widgetChart2")
        self.widgetAdvise = QtWidgets.QWidget(self.chart_2)
        self.widgetAdvise.setGeometry(QtCore.QRect(420, 50, 251, 201))
        self.widgetAdvise.setObjectName("widgetAdvise")
        self.textAdvise = QtWidgets.QTextBrowser(self.widgetAdvise)
        self.textAdvise.setGeometry(QtCore.QRect(0, 32, 251, 170))
        self.textAdvise.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.textAdvise.setStyleSheet("border: 5px solid rgba(255,255,255,0%);\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background: rgba(255,255,255,80%);\n"
"")
        self.textAdvise.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textAdvise.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textAdvise.setLineWidth(0)
        self.textAdvise.setObjectName("textAdvise")
        self.textLabelAdvise = QtWidgets.QTextBrowser(self.widgetAdvise)
        self.textLabelAdvise.setGeometry(QtCore.QRect(0, 0, 251, 37))
        self.textLabelAdvise.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.textLabelAdvise.setStyleSheet("border: 5px solid rgba(255,255,255,0%);\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"background: rgba(255,255,255,80%);\n"
"")
        self.textLabelAdvise.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textLabelAdvise.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textLabelAdvise.setLineWidth(0)
        self.textLabelAdvise.setObjectName("textLabelAdvise")
        self.chartStackedWidget.addWidget(self.chart_2)
        self.chart_3 = QtWidgets.QWidget()
        self.chart_3.setObjectName("chart_3")
        self.widgetChart3 = QtWidgets.QWidget(self.chart_3)
        self.widgetChart3.setGeometry(QtCore.QRect(30, 10, 631, 281))
        self.widgetChart3.setObjectName("widgetChart3")
        self.chartStackedWidget.addWidget(self.chart_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 651, 291))
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.textBrowser.setStyleSheet("border: 5px solid rgba(255,255,255,0%);\n"
"border-radius: 10px;\n"
"background: rgba(255,255,255,80%);\n"
"")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.labelAbout = QtWidgets.QLabel(self.page_2)
        self.labelAbout.setGeometry(QtCore.QRect(20, 10, 221, 40))
        self.labelAbout.setStyleSheet("font: 600 24pt \"MS Shell Dlg 2\";")
        self.labelAbout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelAbout.setObjectName("labelAbout")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(40, 318, 81, 21))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.LayoutSocialMedia = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.LayoutSocialMedia.setContentsMargins(0, 0, 0, 0)
        self.LayoutSocialMedia.setObjectName("LayoutSocialMedia")
        self.btnFa = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.btnFa.setStyleSheet("border:0px;")
        self.btnFa.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assert/fa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFa.setIcon(icon2)
        self.btnFa.setIconSize(QtCore.QSize(16, 16))
        self.btnFa.setObjectName("btnFa")
        self.LayoutSocialMedia.addWidget(self.btnFa)
        self.btnIg = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.btnIg.setStyleSheet("border:0px;")
        self.btnIg.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assert/ig.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnIg.setIcon(icon3)
        self.btnIg.setIconSize(QtCore.QSize(16, 16))
        self.btnIg.setObjectName("btnIg")
        self.LayoutSocialMedia.addWidget(self.btnIg)
        self.btnWww = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.btnWww.setStyleSheet("border:0px;")
        self.btnWww.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assert/www.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnWww.setIcon(icon4)
        self.btnWww.setIconSize(QtCore.QSize(16, 16))
        self.btnWww.setObjectName("btnWww")
        self.LayoutSocialMedia.addWidget(self.btnWww)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.labelSetting = QtWidgets.QLabel(self.page_3)
        self.labelSetting.setGeometry(QtCore.QRect(20, 10, 151, 40))
        self.labelSetting.setStyleSheet("font: 600 24pt \"MS Shell Dlg 2\";")
        self.labelSetting.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting.setObjectName("labelSetting")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 120, 431, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Layout_2.setContentsMargins(0, 0, 0, 0)
        self.Layout_2.setObjectName("Layout_2")
        self.labelSetting_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelSetting_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelSetting_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting_2.setObjectName("labelSetting_2")
        self.Layout_2.addWidget(self.labelSetting_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Layout_2.addItem(spacerItem)
        self.checkBox_1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px;}")
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.Layout_2.addWidget(self.checkBox_1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 180, 431, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.Layout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.Layout_3.setContentsMargins(0, 0, 0, 0)
        self.Layout_3.setObjectName("Layout_3")
        self.labelSetting_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelSetting_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelSetting_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting_3.setObjectName("labelSetting_3")
        self.Layout_3.addWidget(self.labelSetting_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Layout_3.addItem(spacerItem1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px;}")
        self.checkBox_2.setText("")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.Layout_3.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(49, 240, 431, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.Layout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.Layout_4.setContentsMargins(0, 0, 0, 0)
        self.Layout_4.setObjectName("Layout_4")
        self.labelSetting_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.labelSetting_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelSetting_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting_4.setObjectName("labelSetting_4")
        self.Layout_4.addWidget(self.labelSetting_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Layout_4.addItem(spacerItem2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px;}")
        self.checkBox_3.setText("")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.Layout_4.addWidget(self.checkBox_3)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 60, 431, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.LayoutSetting_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.LayoutSetting_1.setContentsMargins(0, 0, 0, 0)
        self.LayoutSetting_1.setObjectName("LayoutSetting_1")
        self.labelSetting_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.labelSetting_1.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelSetting_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting_1.setObjectName("labelSetting_1")
        self.LayoutSetting_1.addWidget(self.labelSetting_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.LayoutSetting_1.addItem(spacerItem3)
        self.lineSetting_1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineSetting_1.setEnabled(True)
        self.lineSetting_1.setMaximumSize(QtCore.QSize(30, 35))
        self.lineSetting_1.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.lineSetting_1.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineSetting_1.setMaxLength(2)
        self.lineSetting_1.setFrame(False)
        self.lineSetting_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineSetting_1.setReadOnly(True)
        self.lineSetting_1.setClearButtonEnabled(False)
        self.lineSetting_1.setObjectName("lineSetting_1")
        self.LayoutSetting_1.addWidget(self.lineSetting_1)
        self.labelSetting_1i2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.labelSetting_1i2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelSetting_1i2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSetting_1i2.setObjectName("labelSetting_1i2")
        self.LayoutSetting_1.addWidget(self.labelSetting_1i2)
        self.btnReset = QtWidgets.QPushButton(self.page_3)
        self.btnReset.setGeometry(QtCore.QRect(80, 300, 71, 31))
        self.btnReset.setStyleSheet("QPushButton{\n"
"color: rgb(56, 56, 56);\n"
"background-color: rgb(255, 248, 82);\n"
"border: 1px soild grey;\n"
"border-radius: 10px;\n"
"font: 700 13pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 105)\n"
"}")
        self.btnReset.setIconSize(QtCore.QSize(24, 24))
        self.btnReset.setObjectName("btnReset")
        self.btnEdit = QtWidgets.QPushButton(self.page_3)
        self.btnEdit.setGeometry(QtCore.QRect(170, 10, 41, 41))
        self.btnEdit.setStyleSheet("border:0px;")
        self.btnEdit.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assert/not allow edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnEdit.setIcon(icon5)
        self.btnEdit.setIconSize(QtCore.QSize(30, 30))
        self.btnEdit.setObjectName("btnEdit")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 114, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.LayoutBtnAS = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.LayoutBtnAS.setContentsMargins(0, 0, 0, 0)
        self.LayoutBtnAS.setObjectName("LayoutBtnAS")
        self.btnAbout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAbout.setStyleSheet("border:0px;")
        self.btnAbout.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assert/about light mode.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAbout.setIcon(icon6)
        self.btnAbout.setIconSize(QtCore.QSize(24, 24))
        self.btnAbout.setObjectName("btnAbout")
        self.LayoutBtnAS.addWidget(self.btnAbout)
        self.btnSetting = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSetting.setStyleSheet("border:0px;")
        self.btnSetting.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assert/settings light mode.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSetting.setIcon(icon7)
        self.btnSetting.setIconSize(QtCore.QSize(24, 24))
        self.btnSetting.setObjectName("btnSetting")
        self.LayoutBtnAS.addWidget(self.btnSetting)
        self.btnQuestion = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnQuestion.setStyleSheet("border:0px;")
        self.btnQuestion.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assert/question.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnQuestion.setIcon(icon8)
        self.btnQuestion.setIconSize(QtCore.QSize(24, 24))
        self.btnQuestion.setObjectName("btnQuestion")
        self.LayoutBtnAS.addWidget(self.btnQuestion)
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, 712, 384))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QtCore.QSize(712, 384))
        self.Background.setMaximumSize(QtCore.QSize(712, 384))
        self.Background.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Background.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("border-image: url(assert/Background-min.png);")
        self.Background.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Background.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Background.setLineWidth(0)
        self.Background.setText("")
        self.Background.setScaledContents(True)
        self.Background.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Background.setObjectName("Background")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(330, 350, 71, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.LayoutBtnAS_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.LayoutBtnAS_2.setContentsMargins(0, 0, 0, 0)
        self.LayoutBtnAS_2.setObjectName("LayoutBtnAS_2")
        self.btnPrevious = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.btnPrevious.setStyleSheet("border:0px;")
        self.btnPrevious.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assert/back off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPrevious.setIcon(icon9)
        self.btnPrevious.setIconSize(QtCore.QSize(24, 24))
        self.btnPrevious.setObjectName("btnPrevious")
        self.LayoutBtnAS_2.addWidget(self.btnPrevious)
        self.btnNext = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.btnNext.setStyleSheet("border:0px;")
        self.btnNext.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assert/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnNext.setIcon(icon10)
        self.btnNext.setIconSize(QtCore.QSize(24, 24))
        self.btnNext.setObjectName("btnNext")
        self.LayoutBtnAS_2.addWidget(self.btnNext)
        self.Background.raise_()
        self.stackedWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.chartStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeMana"))
        self.label.setText(_translate("MainWindow", "-- hour -- min"))
        self.textLabelAdvise.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#616161;\">LỜI KHUYÊN</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.labelAbout.setText(_translate("MainWindow", "GIỚI THIỆU"))
        self.labelSetting.setText(_translate("MainWindow", "CÀI ĐẶT"))
        self.labelSetting_2.setText(_translate("MainWindow", "Khởi động cùng hệ thống"))
        self.labelSetting_3.setText(_translate("MainWindow", "Mở giao diện ứng dụng khi khởi động"))
        self.labelSetting_4.setText(_translate("MainWindow", "Âm thanh"))
        self.labelSetting_1.setText(_translate("MainWindow", "Nhắc nhở thời gian nghỉ ngơi"))
        self.lineSetting_1.setText(_translate("MainWindow", "30"))
        self.labelSetting_1i2.setText(_translate("MainWindow", "phút"))
        self.btnReset.setText(_translate("MainWindow", "RESET"))
