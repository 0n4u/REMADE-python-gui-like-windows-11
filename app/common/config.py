from enum import Enum
import json
from pathlib import Path

from PyQt6.QtCore import QLocale
from qfluentwidgets import (
    qconfig,
    QConfig,
    ConfigItem,
    OptionsConfigItem,
    BoolValidator,
    OptionsValidator,
    RangeConfigItem,
    RangeValidator,
    FolderListValidator,
    FolderValidator,
    ConfigSerializer,
    __version__,
)


class Language(Enum):
    CHINESE_SIMPLIFIED = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Language.Chinese, QLocale.Country.HongKong)
    ENGLISH = QLocale(QLocale.Language.English)
    AUTO = QLocale()


class Lang:
    def __init__(self):
        self.current = "en_US"
        base_dir = Path(__file__).resolve().parent.parent
        config_path = base_dir / "config" / "config.json"
        with open(config_path, "r") as config:
            self.current = json.load(config)["MainWindow"]["Language"]

    def current(self) -> str:
        return self.current


class LanguageSerializer(ConfigSerializer):
    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "en_US"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "en_US" else Language.AUTO


class Config(QConfig):
    musicFolders = ConfigItem("Folders", "LocalMusic", [], FolderListValidator())
    _base_dir = Path(__file__).resolve().parent.parent
    downloadFolder = ConfigItem(
        "Folders", "Download", str(_base_dir / "download"), FolderValidator()
    )

    dpiScale = OptionsConfigItem(
        "MainWindow",
        "DpiScale",
        "Auto",
        OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]),
        restart=True,
    )
    language = OptionsConfigItem(
        "MainWindow",
        "Language",
        Language.AUTO,
        OptionsValidator(Language),
        LanguageSerializer(),
        restart=True,
    )

    blurRadius = RangeConfigItem(
        "Material", "AcrylicBlurRadius", 15, RangeValidator(0, 40)
    )

    # software update
    checkUpdateAtStartUp = ConfigItem(
        "Update", "CheckUpdateAtStartUp", True, BoolValidator()
    )


YEAR = 2025
AUTHOR = "zhiyiYo"
VERSION = __version__
HELP_URL = "https://pyqt-fluent-widgets.readthedocs.io/zh_CN/latest"
REPO_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets"
EXAMPLE_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/master/examples"
FEEDBACK_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues"
RELEASE_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/releases/latest"
SUPPORT_URL = "https://github.com/raherygino"

V_BOX = "vertical"
H_BOX = "horizontal"

cfg = Config()
base_dir = Path(__file__).resolve().parent.parent
config_path = base_dir / "config" / "config.json"
qconfig.load(str(config_path), cfg)
