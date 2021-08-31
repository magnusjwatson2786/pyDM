from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CustomPb(QWidget):
    def __init__(
        self,
        value = 0,
        progress_width = 2,
        # progress_length= 500,
        is_rounded = False,
        max_value = 100,
        # progress_color = "#ff79c6",
        progress_color = "#16A0FF",
        enable_text = True,
        font_family = "Segoe UI",
        font_size = 12,
        suffix = "%",
        # text_color = "#ff79c6",
        text_color = "#16A0FF",
        enable_bg = True,
        bg_color = "#44475a"
    ):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = value
        self.progress_width = progress_width
        # self.progress_length = progress_length
        self.progress_rounded_cap = is_rounded
        self.max_value = max_value
        self.progress_color = progress_color
        # Text
        self.enable_text = enable_text
        self.font_family = font_family
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        # BG
        self.enable_bg = enable_bg
        self.bg_color = bg_color

    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def setValue(self, value):
        self.value = value
        self.repaint() # Render progress bar after change value


    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width() - self.progress_width
        height = self.height() - self.progress_width
        margin = self.progress_width / 2
        y=0.75*self.height()+margin
        value =  (self.value / self.max_value) * width
        # length = self.progress_length

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE for the text value
        # rect = QRect(0, 0, self.width(), self.height())
        rect = QRect(self.width()/4, self.height()/4, self.width()/2, self.height()/2)
        paint.setPen(Qt.NoPen)

        # PEN
        pen = QPen()             
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setJoinStyle(Qt.RoundJoin)
        else:
            pen.setJoinStyle(Qt.MiterJoin)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)  
            paint.drawRect(margin, y ,width ,self.progress_width ) 

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)      
        paint.drawRect(margin, y ,value ,self.progress_width )       

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            pen.setWidth(40)
            font = QFont()
            # print(font.pointSize())
            font.setPointSize(12)
            paint.setFont(font)
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        paint.end()