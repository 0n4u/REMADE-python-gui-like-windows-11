from pathlib import Path
from PyQt6.QtCore import QUrl, QSize
from PyQt6.QtGui import QIcon, QDesktopServices, QGuiApplication
from PyQt6.QtWidgets import QApplication

from qfluentwidgets import (
    NavigationAvatarWidget,
    NavigationItemPosition,
    MessageBox,
    FluentWindow,
    SplashScreen,
)
from qfluentwidgets import FluentIcon as FIF

from .utils.gallery_interface import GalleryInterface
from .utils.setting_interface import SettingInterface
from .utils.blank_interface import BlankInterface
from .utils.widgets_interface import WidgetsInterface
from .utils.table_view_interface import TableViewInterface

from .home.home_interface import HomeInterface

from ..common.config import SUPPORT_URL, Lang
from ..common.signal_bus import signalBus
from ..common.translator import Translator
from ..common.Translate import Translate


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.trans = Translate(Lang().current).text

        self.homeInterface = HomeInterface(self)
        self.widgetsInterface = WidgetsInterface(self)
        self.tableViewInterface = TableViewInterface(self)
        self.blankInterface = BlankInterface(self)
        self.settingInterface = SettingInterface(self)
        self.initLayout()

        self.initNavigation()
        self.splashScreen.finish()

    def initLayout(self):
        signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

    def initNavigation(self):
        t = Translator()
        self.addSubInterface(self.homeInterface, FIF.HOME, "Home")
        self.addSubInterface(self.widgetsInterface, FIF.GAME, self.trans["widgets"])
        self.addSubInterface(
            self.tableViewInterface, FIF.LAYOUT, self.trans["table_view"]
        )
        self.addSubInterface(self.blankInterface, FIF.DOCUMENT, t.blank)
        self.navigationInterface.addSeparator()

        base_dir = Path(__file__).resolve().parent.parent
        user_image = str(base_dir / "resource" / "images" / "user.png")
        self.navigationInterface.addWidget(
            routeKey="avatar",
            widget=NavigationAvatarWidget("Georginot", user_image),
            onClick=self.onSupport,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(
            self.settingInterface,
            FIF.SETTING,
            self.tr("Settings"),
            NavigationItemPosition.BOTTOM,
        )

    def initWindow(self):
        self.resize(960, 670)
        self.setMinimumWidth(760)
        base_dir = Path(__file__).resolve().parent.parent
        logo_path = str(base_dir / "resource" / "images" / "logo.png")
        self.setWindowIcon(QIcon(logo_path))
        self.setWindowTitle("PyQt-Fluent-Widgets")

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QGuiApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def onSupport(self):
        w = MessageBox(
            "View my profile", "Do you want to view my profile on the web?", self
        )
        w.yesButton.setText("Yes")
        w.cancelButton.setText("No")
        if w.exec():
            QDesktopServices.openUrl(QUrl(SUPPORT_URL))

    def switchToSample(self, routeKey, index):
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == routeKey:
                self.stackedWidget.setCurrentWidget(w, False)
                w.scrollToCard(index)
