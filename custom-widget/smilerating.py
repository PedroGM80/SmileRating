from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import (Property, QPoint, QPropertyAnimation, QRect,
                            QSequentialAnimationGroup, QSize, Qt, Signal)

import resources_rc


# SmileRating class that inherits from QtWidgets.QWidget
class SmileRating(QtWidgets.QWidget):
    myMsnChanged = Signal(str)
    # The constructor must receive "myMsn", that is, the message after rating
    def __init__(self, myMsn):
        super().__init__()
        self.myMsn_ = myMsn
        self.value = 0
        self.end = False
       
        layout = QtWidgets.QHBoxLayout()

        self.smileVeryBad = QtWidgets.QLabel()
        self.smileVeryBad.setObjectName(u"smileVeryBad")
        self.smileVeryBad.setGeometry(QRect(40, 20, 64, 64))
        self.smileVeryBad.setPixmap(QtGui.QPixmap(u":/ico/e.png"))

        self.smileVeryGood = QtWidgets.QLabel()
        self.smileVeryGood.setObjectName(u"smileVeryGood")
        self.smileVeryGood.setGeometry(QRect(320, 20, 64, 64))
        self.smileVeryGood.setPixmap(QtGui.QPixmap(u":/ico/a.png"))

        self.smileGood = QtWidgets.QLabel()
        self.smileGood.setObjectName(u"smileGood")
        self.smileGood.setGeometry(QRect(250, 20, 64, 64))
        self.smileGood.setPixmap(QtGui.QPixmap(u":/ico/b.png"))

        self.smileRegular = QtWidgets.QLabel()
        self.smileRegular.setObjectName(u"smileRegular")
        self.smileRegular.setGeometry(QRect(180, 20, 64, 64))
        self.smileRegular.setPixmap(QtGui.QPixmap(u":/ico/c.png"))

        self.smileBad = QtWidgets.QLabel()
        self.smileBad.setObjectName(u"smileBad")
        self.smileBad.setGeometry(QRect(110, 20, 64, 64))
        self.smileBad.setPixmap(QtGui.QPixmap(u":/ico/d.png"))

        self.smileVeryBad.setFixedHeight(64)
        self.smileVeryBad.setFixedWidth(64)
        self.smileVeryGood.setFixedWidth(64)
        self.smileVeryGood.setFixedHeight(64)
        self.smileGood.setFixedWidth(64)
        self.smileGood.setFixedHeight(64)
        self.smileRegular.setFixedWidth(64)
        self.smileRegular.setFixedHeight(64)
        self.smileBad.setFixedWidth(64)
        self.smileBad.setFixedHeight(64)

        self.msn = QtWidgets.QLabel("")
        self.msn.setObjectName(u"msn")
        font = QtGui.QFont()
        font.setFamilies([u"ArtBrush"])
        font.setBold(True)
        self.msn.setFont(font)
        self.msn.setAlignment(Qt.AlignCenter)
        self.msn.setWordWrap(True)

        layout.addWidget(self.smileVeryBad)
        layout.addWidget(self.smileBad)
        layout.addWidget(self.smileRegular)
        layout.addWidget(self.smileGood)
        layout.addWidget(self.smileVeryGood)
        layout.addWidget(self.msn)

        self.listLabel = [self.smileVeryGood,  self.smileGood,
                          self.smileRegular, self.smileBad, self.smileVeryBad]
        self.colorList = ["green", "lime", "yellow", "orange", "red"]
        self.setLayout(layout)

        self.smileVeryBad.enterEvent = lambda event: setValue(1)
        self.smileBad.enterEvent = lambda event: setValue(2)
        self.smileRegular.enterEvent = lambda event: setValue(3)
        self.smileGood.enterEvent = lambda event: setValue(4)
        self.smileVeryGood.enterEvent = lambda event: setValue(5)
        self.smileVeryBad.leaveEvent = lambda event: setValue(0)

        self.smileVeryBad.mousePressEvent = lambda event: valueConfirm(1)
        self.smileBad.mousePressEvent = lambda event: valueConfirm(2)
        self.smileRegular.mousePressEvent = lambda event: valueConfirm(3)
        self.smileGood.mousePressEvent = lambda event: valueConfirm(4)
        self.smileVeryGood.mousePressEvent = lambda event: valueConfirm(5)

        # The setValue function establishes with the value parameter the smiles to be displayed.
        def setValue(value: int):
            if(self.end == False):
                if(value == 0):
                    self.smileVeryBad.setStyleSheet(
                        u"\n""QLabel\n""{ \n""border-radius:30%;\n""background: transparent;\n""}")
                if(value == 1):
                    transparentAllAbove(self.smileVeryBad)
                if(value == 2):
                    transparentAllAbove(self.smileBad)
                if(value == 3):
                    transparentAllAbove(self.smileRegular)
                if(value == 4):
                    transparentAllAbove(self.smileGood)
                if(value == 5):
                    transparentAllAbove(self.smileVeryGood)
            self.update()

        # The hideAllExcept function hides the smile except the one passed by parameter
        # sets the color and makes your content scalable.
        def hideAllExcept(aLabel: QtWidgets.QLabel):

            for element in self.listLabel:
                if(element != aLabel):
                    element.setHidden(True)
                else:
                    element.setStyleSheet(
                        u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + self.colorList[self.listLabel.index(element)]+";\n""}")
                    self.child = element
                    self.child.setScaledContents(True)
            self.update()

        # The transparentAllAbove function makes the background of the smile translucent
        # except for the minor ones to the past by parameter to these it establishes the background color.
        def transparentAllAbove(aLabel: QtWidgets.QLabel):
            for element in self.listLabel:
                if(self.listLabel.index(element) < self.listLabel.index(aLabel)):
                    element.setStyleSheet(
                        u"\n""QLabel\n""{ \n""border-radius:30%;\n""background: transparent ;\n""}")
                else:
                    element.setStyleSheet(
                        u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + self.colorList[self.listLabel.index(element)]+";\n""}")
            self.update()
        # The setEnd function establishes that it is the end of the animation and with a label as a parameter
        # that sets fixed the value of its height and width and inserts the message to the text

        def setEnd(aLabel: QtWidgets.QLabel):
            if(self.end == False):
                aLabel.setFixedHeight(80)
                aLabel.setFixedWidth(80)
                self.msn.setText(self.myMsn_)
                self.end = True
            else:
                self.end = False
            self.update()
        # The valueConfirm function sets the smile to show to animate and hides the rest of the smile
        def valueConfirm(value: int):
            if(value == 1):
                hideAllExcept(self.smileVeryBad)
            if(value == 2):
                hideAllExcept(self.smileBad)
            if(value == 3):
                hideAllExcept(self.smileRegular)
            if(value == 4):
                hideAllExcept(self.smileGood)
            if(value == 5):
                hideAllExcept(self.smileVeryGood)
            animationStart()

        # The animationStart function starts the SmileRating animations
        def animationStart():
            self.child.resize(0, 0)
            self.animSmilePosition = QPropertyAnimation(self.child, b"pos")
            self.animMsnPosition = QPropertyAnimation(self.msn, b"pos")
            self.animSmileSize = QPropertyAnimation(self.child, b"size")

            self.animSmilePosition.setEndValue(QPoint(150, 1))
            self.animMsnPosition.setEndValue(QPoint(160, 10))
            self.animSmileSize.setEndValue(QSize(80, 80))

            self.animSmileSize.setDuration(100)
            self.animSmilePosition.setDuration(500)
            self.animMsnPosition.setDuration(200)

            self.anim_group = QSequentialAnimationGroup()

            self.anim_group.addAnimation(self.animSmileSize)
            self.anim_group.addAnimation(self.animMsnPosition)
            self.anim_group.addAnimation(self.animSmilePosition)

            self.anim_group.start()
            self.anim_group.finished.connect(setEnd(self.child))
            self.update()

    @property
    def myMsn(self):
        return self.myMsn_

    @myMsn.setter
    def myMsn(self, value):
        if value != self.myMsn_:
            if value != "":
                self.myMsn_ = value
                self.myMsnChanged.emit(value)
                print("Modifying the value")
                self.myMsn_ = value
            else:
                print("Error is empty")
