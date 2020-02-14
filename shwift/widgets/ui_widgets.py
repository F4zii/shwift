from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Popup(QWidget):
    def __init__(self, title: str, text: str, icon):
        super().__init__(self)
        self.title = title
        self.text = text
        self.icon = icon

    def show_popup(self):
        self.msg = QMessageBox()

        self.msg.setWindowTitle(self.title)

        self.msg.setText(self.text)

        self.msg.setIcon(self.icon)

        e = msg.exec_()


class Editor(QPlainTextEdit):
    def __init__(self, centralwidget):
        super(QPlainTextEdit, self).__init__(centralwidget)
        self.setGeometry(QRect(180, 40, 1650, 850))
        # self.lineNumberArea = LineNumberArea(self)

        # self.connect(self, SIGNAL('blockCountChanged(int)'), self.updateLineNumberAreaWidth)
        # self.connect(self, SIGNAL('updateRequest(QRect,int)'), self.updateLineNumberArea)
        # self.connect(self, SIGNAL('cursorPositionChanged()'), self.highlightCurrentLine)

        # self.updateLineNumberAreaWidth(0)

    def goto_buffer_end(self):
        sb = self.verticalScrollBar()
        sb.setValue(sb.maximum())

#     def clear_text():
#         self.textEdit.setText("")

#     def textAlign(self, action):
#         if action == self.actionAlignLeft:
#             self.textEdit.setAlignment(Qt.AlignLeft | Qt.AlignAbsolute)
#         elif action == self.actionAlignCenter:
#             self.textEdit.setAlignment(Qt.AlignHCenter)
#         elif action == self.actionAlignRight:
#             self.textEdit.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)
#         elif action == self.actionAlignJustify:
#             self.textEdit.setAlignment(Qt.AlignJustify)


#     def lineNumberAreaWidth(self):
#         digits = 1
#         count = max(1, self.blockCount())
#         while count >= 10:
#             count /= 10
#             digits += 1
#         space = 3 + self.fontMetrics().width('9') * digits
#         return space


#     def updateLineNumberAreaWidth(self, _):
#         self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)


#     def updateLineNumberArea(self, rect, dy):

#         if dy:
#             self.lineNumberArea.scroll(0, dy)
#         else:
#             self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(),
#                        rect.height())

#         if rect.contains(self.viewport().rect()):
#             self.updateLineNumberAreaWidth(0)


#     def resizeEvent(self, event):
#         super().resizeEvent(event)

#         cr = self.contentsRect();
#         self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(),
#                     self.lineNumberAreaWidth(), cr.height()))


#     def lineNumberAreaPaintEvent(self, event):
#         mypainter = QPainter(self.lineNumberArea)

#         mypainter.fillRect(event.rect(), Qt.lightGray)

#         block = self.firstVisibleBlock()
#         blockNumber = block.blockNumber()
#         top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
#         bottom = top + self.blockBoundingRect(block).height()

#         # Just to make sure I use the right font
#         height = self.fontMetrics().height()
#         while block.isValid() and (top <= event.rect().bottom()):
#             if block.isVisible() and (bottom >= event.rect().top()):
#                 number = str(blockNumber + 1)
#                 mypainter.setPen(Qt.black)
#                 mypainter.drawText(0, top, self.lineNumberArea.width(), height,
#                  Qt.AlignRight, number)

#             block = block.next()
#             top = bottom
#             bottom = top + self.blockBoundingRect(block).height()
#             blockNumber += 1


#     def highlightCurrentLine(self):
#         extraSelections = []

#         if not self.isReadOnly():
#             selection = QTextEdit.ExtraSelection()

#             lineColor = QColor(Qt.yellow).lighter(160)

#             selection.format.setBackground(lineColor)
#             selection.format.setProperty(QTextFormat.FullWidthSelection, True)
#             selection.cursor = self.textCursor()
#             selection.cursor.clearSelection()
#             extraSelections.append(selection)
#         self.setExtraSelections(extraSelections)


# class NumberBar(QWidget):
#     def __init__(self, parent = None):
#         super(NumberBar, self).__init__(parent)
#         self.editor = parent
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         self.editor.blockCountChanged.connect(self.update_width)
#         self.editor.updateRequest.connect(self.update_on_scroll)
#         self.update_width('1')

#     def update_on_scroll(self, rect, scroll):
#         if self.isVisible():
#             if scroll:
#                 self.scroll(0, scroll)
#             else:
#                 self.update()

#     def update_width(self, string):
#         width = self.fontMetrics().width(str(string)) + 10
#         if self.width() != width:
#             self.setFixedWidth(width)

#     def paintEvent(self, event):
#         if self.isVisible():
#             block = self.editor.firstVisibleBlock()
#             height = self.fontMetrics().height()
#             number = block.blockNumber()
#             painter = QPainter(self)
#             painter.fillRect(event.rect(), lineBarColor)
#             painter.drawRect(0, 0, event.rect().width() - 1, event.rect().height() - 1)
#             font = painter.font()

#             current_block = self.editor.textCursor().block().blockNumber() + 1

#             condition = True
#             while block.isValid() and condition:
#                 block_geometry = self.editor.blockBoundingGeometry(block)
#                 offset = self.editor.contentOffset()
#                 block_top = block_geometry.translated(offset).top()
#                 number += 1

#                 rect = QRect(0, block_top, self.width() - 5, height)

#                 if number == current_block:
#                     font.setBold(True)
#                 else:
#                     font.setBold(False)

#                 painter.setFont(font)
#                 painter.drawText(rect, Qt.AlignRight, '%i'%number)

#                 if block_top > event.rect().bottom():
#                     condition = False

#                 block = block.next()

#             painter.end()


