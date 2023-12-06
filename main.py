from PyQt5 import uic, QtWidgets
import sqlite3
Form, _ = uic.loadUiType("1.ui")
#123
a = ''
#####################
class Ui(QtWidgets.QDialog, Form):#
    def __init__(self):#
        super(Ui, self).__init__()#
        self.setupUi(self)#
        self.p1.clicked.connect(self.gle)
        self.vr.clicked.connect(self.func)
        self.rv.clicked.connect(self.func1)
        self.rv.hide()
        self.l4.hide()
        self.l5.hide()
        self.l6.hide()
        self.r2.hide()
        self.r3.hide()
        self.r4.hide()
        self.l7.hide()
        self.lo.setText('')

        self.z1.hide()
        self.z2.hide()
        self.z3.hide()
        self.z4.hide()
        self.z5.hide()
        self.z6.hide()


    connect = sqlite3.connect('1.db')
    cursor = connect.cursor()
    connect.commit()
    def gle(self):
        connect = sqlite3.connect('1.db')
        cursor = connect.cursor()
        z = "'"
        try:
            a=0
            b=0
            cursor.execute('select user_name from users where user_name LIKE ' + z + self.v1.text() + z)
            m = cursor.fetchall()
            l = m[0][0]
            cursor.execute('select user_password from users where user_password LIKE ' + z + self.v2.text() + z)
            m = cursor.fetchall()
            p = m[0][0]

            if l == self.v1.text() and p == self.v2.text():
                self.z1.setVisible(True)
        except:
            self.lo.setText('Ошибка! Неправильно введён Логин или Пароль')

    def func(self):
        self.vr.hide()
        self.l1.hide()
        self.l2.hide()
        self.l3.hide()
        self.v1.hide()
        self.v2.hide()
        self.p1.hide()
        self.lo.setText('')

        self.rv.setVisible(True)
        self.l4.setVisible(True)
        self.l5.setVisible(True)
        self.l6.setVisible(True)
        self.r2.setVisible(True)
        self.r3.setVisible(True)
        self.r4.setVisible(True)
        self.l7.setVisible(True)
    def func1(self):
        self.vr.setVisible(True)
        self.l1.setVisible(True)
        self.l2.setVisible(True)
        self.l3.setVisible(True)
        self.v1.setVisible(True)
        self.v2.setVisible(True)
        self.p1.setVisible(True)
        self.lo.setText('')

        self.rv.hide()
        self.l4.hide()
        self.l5.hide()
        self.l6.hide()
        self.r2.hide()
        self.r3.hide()
        self.r4.hide()
        self.l7.hide()




##########################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())