import json
import codecs
from pathlib import Path
from PyQt6.QtCore import QLocale


class Translate:
    def __init__(self, lang):
        self.translations = {}
        base_dir = Path(__file__).resolve().parent.parent
        lang_path = base_dir / "config" / "lang.json"
        with codecs.open(lang_path, "r", "utf-8") as file:
            self.translations = json.load(file)

        language = lang
        if not lang:
            language = QLocale.system().name()
            if language not in self.translations:
                language = "en_US"
        self.text = self.translations[language]
