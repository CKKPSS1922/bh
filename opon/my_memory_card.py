#создай приложение для запоминания информации

from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QGroupBox, QRadioButton, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QMessageBox
#создание приложения и главного окна
a = QApplication([])
b = QWidget()
b.setWindowTitle('Очень лёгкие вопросы')

#создание виджетов главного окна
Q = QLabel('В флаге какой страны отсутствует красный цвет?')
an0 = QRadioButton('Мадагаскар')
an1 = QRadioButton('Ангола')
an2 = QRadioButton('ЮАР')
an3 = QRadioButton('Уругвай')
button = QPushButton('Ответить')
group = QGroupBox('Варианты ответов')
yo = QVBoxLayout()
you = QVBoxLayout()
yout = QVBoxLayout()
line = QHBoxLayout()
a1 = QHBoxLayout()
a2 = QVBoxLayout()
a3 = QVBoxLayout()
a4 = QHBoxLayout()
button_group = QButtonGroup()
button_group.addButton(an0)
button_group.addButton(an1)
button_group.addButton(an2)
button_group.addButton(an3)
s1 = QLabel('Правильно/Неправильно')
s2 = QLabel('Правильно')
a5 = QVBoxLayout()
gro = QGroupBox('Результат теста')
#расположение виджетов по лэйаутам
you.addWidget(Q, alignment = Qt.AlignCenter)
yout.addWidget(an0, alignment = Qt.AlignCenter)
yout.addWidget(an1, alignment = Qt.AlignCenter)
yo.addWidget(an2, alignment = Qt.AlignCenter)
yo.addWidget(an3, alignment = Qt.AlignCenter)
a5.addWidget(s1, alignment = Qt.AlignLeft)
a5.addWidget(s2, alignment = Qt.AlignCenter)
line.addLayout(yout)
line.addLayout(yo)
group.setLayout(line)
you.addWidget(group, alignment = Qt.AlignCenter)
gro.setLayout(a5)
you.addWidget(gro, alignment = Qt.AlignCenter)
you.addWidget(button, alignment = Qt.AlignCenter)
b.setLayout(you)
gro.hide()
def show_result():
    group.hide()
    gro.show()
    button.setText('Следующий вопрос')
def show_question():
    gro.hide()
    group.show()
    button.setText('Ответить')
    button_group.setExclusive(False)
    an0.setChecked(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    button_group.setExclusive(True)

answers = [an0, an1, an2, an3]
def ask(question,riteanswer,bronk0,bronk1,bronk2):
    shuffle(answer)
    answers[0].setText(riteanswer)
    answers[1].setText(bronk0)
    answers[2].setText(bronk1)
    answers[3].setText(bronk2)
    Q.setText(question)
    s2.setText(riteanswer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        show_correct('Неверно')

def show_correct(res):
    s1.setText(res)
    show_result()

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()
button.clicked.connect(start_test)



b.show()
a.exec_()
#обработка нажатий на переключатели

#отображение окна приложения 
