import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt, QTime

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q') #단축키 지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        actPrint = QAction(QIcon('./Day09/print.png'), 'print', self)
        actPrint.setShortcut('Ctrl+P')
        actPrint.setStatusTip('인쇄')

        actEdit = QAction(QIcon('./Day09/edit.png'), 'Edit', self)
        actEdit.setShortcut('Ctrl+E')
        actEdit.setStatusTip('수정')

        menubar =self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actEdit)
        filemenu.addAction(actSave)
        filemenu.addAction(actPrint)
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar') # 툴바타이틀은 없어도 됨
        toolbar.addAction(actEdit)
        toolbar.addAction(actSave)
        toolbar.addAction(actPrint)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate() # 현재 일자
        time = QTime.currentTime() # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString('hh:mm:ss'))
        #self.statusBar().showMessage(now.toString(Qt.DefaultLocaleLongDate))
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        # self.move(200, 200)
        self.resize(400, 200)
        self.setCenter()
        self.show() # 핵심!!
    
    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =MyApp()
    sys.exit(app.exec_())