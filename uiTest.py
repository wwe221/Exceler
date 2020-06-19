from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

conn = sqlite3.connect("Yesan.db")
cur = conn.cursor()
class Ui_Dialog(object):
    global sap
    sap = []
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1534, 867)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("새굴림")
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tap1 = QtWidgets.QWidget()
        self.tap1.setObjectName("tap1")
        self.comboBox_3 = QtWidgets.QComboBox(self.tap1)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 260, 111, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(self.tap1)
        self.label_3.setGeometry(QtCore.QRect(0, 230, 121, 16))
        font = QtGui.QFont()
        font.setFamily("새굴림")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tap1)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 180, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.tap1)
        self.label_2.setGeometry(QtCore.QRect(0, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("새굴림")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_1 = QtWidgets.QComboBox(self.tap1)
        self.comboBox_1.setGeometry(QtCore.QRect(10, 100, 111, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.label_1 = QtWidgets.QLabel(self.tap1)
        self.label_1.setGeometry(QtCore.QRect(0, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("새굴림")
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tap1)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 0, 81, 16))
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setObjectName("checkBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tap1)
        self.tableWidget.setGeometry(QtCore.QRect(140, 50, 1311, 741))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.tabWidget.addTab(self.tap1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Exceler"))
        self.label_3.setText(_translate("Dialog", "예산품의서 번호"))
        self.label_2.setText(_translate("Dialog", "단위사업"))
        self.label_1.setText(_translate("Dialog", "팀명"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "지출 일자"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "팀"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "사업"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "품의 제목"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "품의서 번호"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "지출결의서 번호"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "지출내용"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "계정목"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "예산"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "품의 금액"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "공급가액"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "세액"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "지출 금액"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tap1), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "쪽"))
        self.getTable()

    def setTableHeader(self):
        item = QTableWidgetItem("일자")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("지출내용")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem("팀")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem("품의서 번호")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem("지출서 번호")
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem("금액")
        self.tableWidget.setHorizontalHeaderItem(5, item)

    def teamChanged(self):
        team = self.comboBox.currentText()
        self.tableWidget.clear()
        self.setTableHeader()
        print(team)
        if team == "전체":
            result = sap
            idx = 0
            for row in result:
                item = QTableWidgetItem(row["Date"])
                self.tableWidget.setItem(idx, 0, item)
                item = QTableWidgetItem(row["Desc"])
                self.tableWidget.setItem(idx, 1, item)
                item = QTableWidgetItem(row["Team"])
                self.tableWidget.setItem(idx, 2, item)
                item = QTableWidgetItem(row["Pumnum"])
                self.tableWidget.setItem(idx, 3, item)
                item = QTableWidgetItem(row["Jinum"])
                self.tableWidget.setItem(idx, 4, item)
                idx += 1
        else:
            result =[]
            for tmp in sap:
                if tmp["Team"] == team:
                    result.append(tmp)
            idx = 0
            for row in result:
                item = QTableWidgetItem(row["Date"])
                self.tableWidget.setItem(idx, 0, item)
                item = QTableWidgetItem(row["Desc"])
                self.tableWidget.setItem(idx, 1, item)
                item = QTableWidgetItem(row["Team"])
                self.tableWidget.setItem(idx, 2, item)
                item = QTableWidgetItem(row["Pumnum"])
                self.tableWidget.setItem(idx, 3, item)
                item = QTableWidgetItem(row["Jinum"])
                self.tableWidget.setItem(idx, 4, item)
                idx += 1
        self.tableWidget.resizeRowsToContents()

    def teamChanged2(self):
        team = self.comboBox.currentText()
        print(team)
        self.tableWidget.clear()
        sql = "select * from Saup2"
        cur.execute(sql)
        result = cur.fetchall()
        idx = 0
        for row in result:
            if row[2] == team:
                for idx2 in range(6):
                    item = QTableWidgetItem(row[idx2])
                    self.tableWidget.setItem(idx, idx2, item)
                idx += 1
            self.tableWidget.resizeRowsToContents()

    def getTeam(self):
        cur.execute("select distinct Team from Saup2")
        teams = cur.fetchall()
        for team in teams:
            self.comboBox.addItem(team[0])

    global yesan
    global pum
    global spend
    def getTable(self):
        saup = []
        cur.execute("select * from Yesan")
        yesan = cur.fetchall()
        cur.execute("select * from Pum")
        pum = cur.fetchall()
        cur.execute("select * from spend")
        spend = cur.fetchall()
        idx = 0
        cur.execute("select count(*) from Spend")
        len = cur.fetchall()
        self.tableWidget.setRowCount(len[0][0])
        for row in spend:
            tmp = [5,0,4,7,6,10,11]
            for idx2,val in enumerate(tmp):
                item = QTableWidgetItem(str(row[idx2]))
                self.tableWidget.setItem(idx,val,item)
            sum = row[5] + row[6]
            item = QTableWidgetItem(str(sum))
            self.tableWidget.setItem(idx, 12, item)
            sql2 = "select * from Pum where Numb= '" + row[2] + "'"
            thisPum = cur.execute(sql2)
            tmp2 = [1,1,2,3,9]
            for row2 in thisPum:
                for idx2,val in enumerate(tmp2):
                    item = QTableWidgetItem(str(row2[idx2]))
                    self.tableWidget.setItem(idx, val, item)
                    team = row2[1]
                    busy = row2[2]
                    sql3 = "select * from Yesan where Team = ? And Busy = ?"
                    row3 = cur.execute(sql3,(team,busy))
                    for tmp2 in row3:
                        item = QTableWidgetItem(str(tmp2[2]))
                        self.tableWidget.setItem(idx, 8, item)
                        break
            idx +=1
    def getTableByBusy(self):
        saup = []
        cur.execute("select * from Yesan")
        yesan = cur.fetchall()
        cur.execute("select * from Pum")
        pum = cur.fetchall()
        cur.execute("select * from spend")
        spend = cur.fetchall()
        idx = 0
        cur.execute("select count(*) from Spend")
        len = cur.fetchall()
        self.tableWidget.setRowCount(len[0][0])
        for row in spend:
            tmp = [5,0,4,7,6,10,11]
            for idx2,val in enumerate(tmp):
                item = QTableWidgetItem(str(row[idx2]))
                self.tableWidget.setItem(idx,val,item)
            sum = row[5] + row[6]
            item = QTableWidgetItem(str(sum))
            self.tableWidget.setItem(idx, 12, item)
            sql2 = "select * from Pum where Numb= '" + row[2] + "'"
            thisPum = cur.execute(sql2)
            tmp2 = [1,1,2,3,9]
            for row2 in thisPum:
                for idx2,val in enumerate(tmp2):
                    item = QTableWidgetItem(str(row2[idx2]))
                    self.tableWidget.setItem(idx, val, item)
                    team = row2[1]
                    busy = row2[2]
                    sql3 = "select * from Yesan where Team = ? And Busy = ?"
                    row3 = cur.execute(sql3,(team,busy))
                    for tmp2 in row3:
                        item = QTableWidgetItem(str(tmp2[2]))
                        self.tableWidget.setItem(idx, 8, item)
                        break
            idx +=1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())