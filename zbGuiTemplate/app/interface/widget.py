import webbrowser

from ..program import *


class ErrorMessageBox(zbw.ScrollMessageBox):
    def __init__(self, title: str, content: str, parent=None):
        super().__init__(title, content, parent)
        logging.error(content)

        self.contentLabel.setSelectable()
        self.cancelButton.setText("关闭")
        self.yesButton.hide()
        self.yesButton.deleteLater()

        self.reportButton = PrimaryPushButton("反馈", self, FIF.FEEDBACK)
        self.reportButton.clicked.connect(lambda: webbrowser.open(zb.joinUrl(program.GITHUB_URL, "issues/new")))

        self.restartButton = PrimaryPushButton("重启", self, FIF.SYNC)
        self.restartButton.clicked.connect(program.restart)
        self.buttonLayout.insertWidget(0, self.reportButton, 2)
        self.buttonLayout.insertWidget(1, self.restartButton, 2)
