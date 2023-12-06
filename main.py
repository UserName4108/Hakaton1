from PyQt5 import uic, QtWidgets
import sqlite3
Form, _ = uic.loadUiType("1.ui")
#12
a = ''
#####################
class Ui(QtWidgets.QDialog, Form):#
    def __init__(self):#
        super(Ui, self).__init__()#
        self.setupUi(self)#
        self.p1.clicked.connect(self.gle1)
        self.vr.clicked.connect(self.func)
        self.rv.clicked.connect(self.func1)
        self.p2.clicked.connect(self.reg)
        self.p3.clicked.connect(self.obn)
        self.p4.clicked.connect(self.ob)
        self.o2.clicked.connect(self.gl)
        self.z11.clicked.connect(self.v)
        self.rv.hide()
        self.l4.hide()
        self.l5.hide()
        self.l6.hide()
        self.r2.hide()
        self.r3.hide()
        self.r4.hide()
        self.l7.hide()
        self.p2.hide()
        self.lo.setText('')
        self.lr1.setText('')

        self.z1.hide()
        self.z2.hide()
        self.z3.hide()
        self.z4.hide()
        self.z5.hide()
        self.z6.hide()
        self.z7.hide()
        self.z8.hide()
        self.z9.hide()
        self.p3.hide()
        self.z11.hide()
        self.o1.hide()
        self.o2.hide()
        self.o3.hide()
        self.o4.hide()
        self.o5.hide()
        self.o6.hide()
        self.o7.hide()
        self.o8.hide()
        self.p4.hide()


    connect = sqlite3.connect('1.db')
    cursor = connect.cursor()
    connect.commit()
    def gle1(self):
        global q1
        q1= self.v1.text()
        connect = sqlite3.connect('1.db')
        cursor = connect.cursor()
        self.lr1.setText('')
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
                self.z2.setVisible(True)
                self.z3.setVisible(True)
                self.z4.setVisible(True)
                self.z5.setVisible(True)
                self.z6.setVisible(True)
                self.z7.setVisible(True)
                self.z8.setVisible(True)
                self.z9.setVisible(True)
                self.p3.setVisible(True)
                self.z11.setVisible(True)
                self.vr.hide()
                self.l1.hide()
                self.l2.hide()
                self.l3.hide()
                self.v1.hide()
                self.v2.hide()
                self.p1.hide()
                self.lo.setText('')
                self.lr1.setText('')
                print('Гл экран вход')
        except:
            self.lo.setText('Ошибка! Неправильно введён Логин или Пароль')
    def reg(self):
        global q1
        q1 = self.r2.text()
        self.lr1.setText('')
        connect = sqlite3.connect('1.db')
        cursor = connect.cursor()
        z = "'"
        cursor.execute('select user_name from users where user_name ='+ z + self.r2.text() + z)
        n1 = cursor.fetchall()
        n= len(n1)
        cursor.execute('select user_email from users where user_email =' + z + self.r4.text() + z)
        em1 = cursor.fetchall()
        em = len(em1)
        if n == 0:
            if em == 0:
                if '@' in self.r4.text():
                    if '.' in self.r4.text():
                        if self.r2.text() != '' and self.r2.text() != ' ' and self.r2.text() != ' ' and self.r3.text() != '' and self.r3.text() != ' ' and self.r3.text() != ' ' and self.r4.text() != '' and self.r4.text() != ' ' and self.r4.text() != ' ':
                            a = [self.r2.text(),self.r3.text(),self.r4.text(), '0','0','0']
                            sql ='insert into users(user_name, user_password, user_email, user_balance, user_rank, user_level) values(?,?,?,?,?,?)'
                            cursor.execute(sql, a)
                            connect.commit()
                            self.z1.setVisible(True)
                            self.z2.setVisible(True)
                            self.z3.setVisible(True)
                            self.z4.setVisible(True)
                            self.z5.setVisible(True)
                            self.z6.setVisible(True)
                            self.z7.setVisible(True)
                            self.z8.setVisible(True)
                            self.z9.setVisible(True)
                            self.p3.setVisible(True)
                            self.z11.setVisible(True)

                            self.p2.hide()
                            self.rv.hide()
                            self.l4.hide()
                            self.l5.hide()
                            self.l6.hide()
                            self.r2.hide()
                            self.r3.hide()
                            self.r4.hide()
                            self.l7.hide()
                            print('Гл экран рег')
                        else:
                            self.lr1.setText('Ошибка: Проверьте правильность написания данных')
                    else:
                        self.lr1.setText('Ошибка: Проверьте правильность написания данных')
                else:
                    self.lr1.setText('Ошибка: Проверьте правильность написания данных')
            else:
                self.lr1.setText('Данная почта уже привязана')
        else:
            self.lr1.setText('Данный пользователь уже существует')
    def ob(self):
        connect = sqlite3.connect('1.db')
        cursor = connect.cursor()
        z = "'"
        print(q1)
        cursor.execute('select id from users where user_name =' + z + q1 + z)
        x = cursor.fetchall()
        print(x)
        if self.o3.text() != '' and self.o3.text() != ' ' and self.o3.text() != ' ' and self.o5.text() != '' and self.o5.text() != ' ' and self.o5.text() != ' ' and self.o7.text() != '' and self.o7.text() != ' ' and self.o7.text() != ' ':
            a = [self.o3.text(), self.o5.text(), self.o7.text(), x[0][0]]
            sql = 'update users set user_name = ?, user_password = ?, user_email = ? where id = ?'
            cursor.execute(sql, a)
            connect.commit()
            self.z1.setVisible(True)
            self.z2.setVisible(True)
            self.z3.setVisible(True)
            self.z4.setVisible(True)
            self.z5.setVisible(True)
            self.z6.setVisible(True)
            self.z7.setVisible(True)
            self.z8.setVisible(True)
            self.z9.setVisible(True)
            self.p3.setVisible(True)
            self.z11.setVisible(True)

            self.p2.hide()
            self.rv.hide()
            self.l4.hide()
            self.l5.hide()
            self.l6.hide()
            self.r2.hide()
            self.r3.hide()
            self.r4.hide()
            self.l7.hide()
            print('Гл экран обн')
        else:
            self.lr1.setText('Ошибка: Проверьте правильность написания данных')
    def gl(self):
        self.o1.hide()
        self.o2.hide()
        self.o3.hide()
        self.o4.hide()
        self.o5.hide()
        self.o7.hide()
        self.o8.hide()
        self.p4.hide()

        self.z1.setVisible(True)
        self.z2.setVisible(True)
        self.z3.setVisible(True)
        self.z4.setVisible(True)
        self.z5.setVisible(True)
        self.z6.setVisible(True)
        self.z7.setVisible(True)
        self.z8.setVisible(True)
        self.z9.setVisible(True)
        self.p3.setVisible(True)
        self.z11.setVisible(True)
    def obn(self):
        self.vr.hide()
        self.l1.hide()
        self.l2.hide()
        self.l3.hide()
        self.v1.hide()
        self.v2.hide()
        self.p1.hide()
        self.lo.setText('')
        self.lr1.setText('')

        self.o1.setVisible(True)
        self.o2.setVisible(True)
        self.o3.setVisible(True)
        self.o4.setVisible(True)
        self.o5.setVisible(True)
        self.o6.setVisible(True)
        self.o7.setVisible(True)
        self.o8.setVisible(True)
        self.p4.setVisible(True)

        self.z1.hide()
        self.z2.hide()
        self.z3.hide()
        self.z4.hide()
        self.z5.hide()
        self.z6.hide()
        self.z7.hide()
        self.z8.hide()
        self.z9.hide()
        self.z11.hide()
        self.p3.hide()






    def func(self):
        self.vr.hide()
        self.l1.hide()
        self.l2.hide()
        self.l3.hide()
        self.v1.hide()
        self.v2.hide()
        self.p1.hide()
        self.lo.setText('')
        self.lr1.setText('')

        self.p2.setVisible(True)
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
        self.lr1.setText('')

        self.p2.hide()
        self.rv.hide()
        self.l4.hide()
        self.l5.hide()
        self.l6.hide()
        self.r2.hide()
        self.r3.hide()
        self.r4.hide()
        self.l7.hide()
    def v(self):
        self.z1.hide()
        self.z2.hide()
        self.z3.hide()
        self.z4.hide()
        self.z5.hide()
        self.z6.hide()
        self.z7.hide()
        self.z8.hide()
        self.z9.hide()
        self.p3.hide()
        self.z11.hide()

        self.vr.setVisible(True)
        self.l1.setVisible(True)
        self.l2.setVisible(True)
        self.l3.setVisible(True)
        self.v1.setVisible(True)
        self.v2.setVisible(True)
        self.p1.setVisible(True)


##########################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())