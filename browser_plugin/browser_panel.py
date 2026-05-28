from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QToolBar, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView


class BrowserPanel(QWidget):
    def __init__(self, homepage="https://www.google.com", parent=None):
        super().__init__(parent)
        self.homepage = homepage
        self.view = QWebEngineView(self)
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.load_url_from_bar)

        toolbar = QToolBar(self)
        back = QPushButton("Back", self)
        forward = QPushButton("Forward", self)
        reload_button = QPushButton("Reload", self)
        back.clicked.connect(self.view.back)
        forward.clicked.connect(self.view.forward)
        reload_button.clicked.connect(self.view.reload)
        toolbar.addWidget(back)
        toolbar.addWidget(forward)
        toolbar.addWidget(reload_button)

        bar_layout = QHBoxLayout()
        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.addWidget(self.url_bar)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(toolbar)
        layout.addLayout(bar_layout)
        layout.addWidget(self.view)

        self.view.urlChanged.connect(lambda url: self.url_bar.setText(url.toString()))
        self.load_url(self.homepage)

    def load_url_from_bar(self):
        self.load_url(self.url_bar.text().strip())

    def load_url(self, url):
        if not url:
            return
        if "://" not in url:
            url = "https://" + url
        self.view.setUrl(QUrl(url))
