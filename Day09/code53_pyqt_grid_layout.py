# 레이아웃 그리드배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0) # row(열), col(행) =0, 0
        grid.addWidget(QLabel('Author'), 1, 0) 
        grid.addWidget(QLabel('Review'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1) # 0행 1렬
        grid.addWidget(QLineEdit(), 1, 1) # 1행 1렬
        grid.addWidget(QTextEdit(), 2, 1) # 2행 1렬

        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')
   
        grid    .addWidget(btnOk, 3, 1)
        grid.addWidget(btnCancel, 4, 1)

        # 필수 설정
        self.setWindowTitle('그리드 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())