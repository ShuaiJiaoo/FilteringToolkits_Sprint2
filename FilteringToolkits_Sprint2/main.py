# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frame.promWindow import ProMWidget

# process stream
# choosing filter by given input ———————— 通过提交按钮设置权重
# analyse the filters ————— 设置
# assessment of filters
# sorting the filter
# choosing the most suitable filter


def main():
    # creating applicaiton
    app = QApplication(sys.argv)

    ui = ProMWidget()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
