from datetime import datetime

from PySide2.QtCore import QMetaObject, QRect, Qt
from PySide2.QtGui import QColor, QCursor, QFont, QPalette, QIcon
from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMenu, QMenuBar, QMainWindow
from textblob import TextBlob


class Translate(QMainWindow):
    def __init__(self):
        super(Translate, self).__init__()
        self.resize(640, 480)
        self.setMinimumSize(640, 480)
        self.setMaximumSize(640, 480)
        self.setWindowTitle('Translate')
        self.setWindowIcon(QIcon('arti.PNG'))

        self.setFont(QFont('Roboto', 12))

        palette = QPalette()
        palette.setColor(palette.Window, QColor('#000000'))
        palette.setColor(palette.WindowText, QColor('#FFFFFF'))
        palette.setColor(palette.Button, QColor("#00FF00"))
        palette.setColor(palette.ButtonText, QColor("#000000"))
        self.setPalette(palette)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(0, 0, 682, 21)
        self.menubar.setFont(QFont('Roboto', 10))

        self.date_menu = QMenu(self.menubar)
        self.date_menu.setTitle(str(datetime.now().strftime('%d-%m-%Y')))

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.date_menu.menuAction())

        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 40, 631, 91))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Welcome to Translate \n Tip: The language for text you enter below is always English.')

        self.to_translate = QLineEdit(self)
        self.to_translate.setGeometry(QRect(10, 180, 611, 41))
        self.to_translate.setPlaceholderText('Initial Text:')

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(10, 270, 151, 31))
        self.label_2.setText('Select Language -->')

        self.translate_button = QPushButton(self)
        self.translate_button.setGeometry(QRect(400, 260, 191, 51))
        self.translate_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.translate_button.setText('Let\'s Translate!!')
        self.translate_button.clicked.connect(lambda: self.button_press())

        self.translated_text = QLabel(self)
        self.translated_text.setGeometry(QRect(20, 350, 601, 71))
        self.translated_text.setAlignment(Qt.AlignCenter)
        self.translated_text.setWordWrap(True)

        self.language = QComboBox(self)
        self.language.addItem("None")
        self.language.addItem("Afrikaans")  # 1
        self.language.addItem("Albanian")  # 2
        self.language.addItem("Amharic")  # 3
        self.language.addItem("Arabic")  # 4
        self.language.addItem("Armenian")  # 5
        self.language.addItem("Azerbaijani")  # 6
        self.language.addItem("Basque")  # 7
        self.language.addItem("Belarusian")  # 8
        self.language.addItem("Bengali")  # 9
        self.language.addItem("Bosnian")  # 10
        self.language.addItem("Bulgarian")  # 11
        self.language.addItem("Catalan")  # 12
        self.language.addItem("Cebuano")  # 13
        self.language.addItem("Chinese (Simplified)")  # 14
        self.language.addItem("Chinese (Traditional)")  # 15
        self.language.addItem("Corsican")  # 16
        self.language.addItem("Croatian")  # 17
        self.language.addItem("Czech")  # 18
        self.language.addItem("Danish")  # 19
        self.language.addItem("Dutch")  # 20
        self.language.addItem("English")  # 21
        self.language.addItem("Esperanto")  # 22
        self.language.addItem("Estonian")  # 23
        self.language.addItem("Finnish")  # 24
        self.language.addItem("French")  # 25
        self.language.addItem("Frisian")  # 26
        self.language.addItem("Galician")  # 27
        self.language.addItem("Georgian")  # 28
        self.language.addItem("German")  # 29
        self.language.addItem("Greek")  # 30
        self.language.addItem("Gujarati")  # 31
        self.language.addItem("Haitian Creole")  # 32
        self.language.addItem("Hausa")  # 33
        self.language.addItem("Hawaiian")  # 34
        self.language.addItem("Hebrew")  # 35
        self.language.addItem("Hindi")  # 36
        self.language.addItem("Hmong")  # 37
        self.language.addItem("Hungarian")  # 38
        self.language.addItem("Icelandic")  # 39
        self.language.addItem("Igbo")  # 40
        self.language.addItem("Indonesian")  # 41
        self.language.addItem("Irish")  # 42
        self.language.addItem("Italian")  # 43
        self.language.addItem("Japanese")  # 44
        self.language.addItem("Javanese")  # 45
        self.language.addItem("Kannada")  # 46
        self.language.addItem("Kazakh")  # 47
        self.language.addItem("Khmer")  # 48
        self.language.addItem("Kinyarwanda")  # 49
        self.language.addItem("Korean")  # 50
        self.language.addItem("Kurdish")  # 51
        self.language.addItem("Kyrgyz")  # 52
        self.language.addItem("Lao")  # 53
        self.language.addItem("Latin")  # 54
        self.language.addItem("Latvian")  # 55
        self.language.addItem("Lithuanian")  # 56
        self.language.addItem("Luxembourgish")  # 57
        self.language.addItem("Macedonian")  # 58
        self.language.addItem("Malagasy")  # 59
        self.language.addItem("Malay")  # 60
        self.language.addItem("Malayalam")  # 61
        self.language.addItem("Maltese")  # 62
        self.language.addItem("Maori")  # 63
        self.language.addItem("Marathi")  # 64
        self.language.addItem("Mongolian")  # 65
        self.language.addItem("Mayanmar (Burmese)")  # 66
        self.language.addItem("Nepali")  # 67
        self.language.addItem("Norwegian")  # 68
        self.language.addItem("Nyanja (Chichewa)")  # 69
        self.language.addItem("Odia (Oriya)")  # 70
        self.language.addItem("Pashto")  # 71
        self.language.addItem("Persian")  # 72
        self.language.addItem("Polish")  # 73
        self.language.addItem("Portugese (Portugal, Brazil)")  # 74
        self.language.addItem("Punjabi")  # 75
        self.language.addItem("Romanian")  # 76
        self.language.addItem("Russian")  # 77
        self.language.addItem("Samoan")  # 78
        self.language.addItem("Scots Gaelic")  # 79
        self.language.addItem("Serbian")  # 80
        self.language.addItem("Sesotho")  # 81
        self.language.addItem("Shona")  # 82
        self.language.addItem("Sindhi")  # 83
        self.language.addItem("Sinhala (Sinhalese)")  # 84
        self.language.addItem("Slovak")  # 85
        self.language.addItem("Slovenian")  # 86
        self.language.addItem("Somali")  # 87
        self.language.addItem("Spanish")  # 88
        self.language.addItem("Sundanese")  # 89
        self.language.addItem("Swahili")  # 90
        self.language.addItem("Swedish")  # 91
        self.language.addItem("Tagalong (Filipino)")  # 92
        self.language.addItem("Tajik")  # 93
        self.language.addItem("Tamil")  # 94
        self.language.addItem("Tatar")  # 95
        self.language.addItem("Telugu")  # 96
        self.language.addItem("Thai")  # 97
        self.language.addItem("Turkish")  # 98
        self.language.addItem("Turkmen")  # 99
        self.language.addItem("Ukrainian")  # 100
        self.language.addItem("Urdu")  # 101
        self.language.addItem("Uyghur")  # 102
        self.language.addItem("Uzbek")  # 103
        self.language.addItem("Vietnamese")  # 104
        self.language.addItem("Welsh")  # 105
        self.language.addItem("Xhosa")  # 106
        self.language.addItem("Yiddish")  # 107
        self.language.addItem("Yoruba")  # 108
        self.language.addItem("Zulu")  # 109
        self.language.setGeometry(QRect(180, 270, 171, 31))
        QMetaObject.connectSlotsByName(self)

    def translate(self, final_lang):
        self.translated_text.setText(str(self.translator.translate(to=str(final_lang))))

    def button_press(self):
        self.query = self.to_translate.text()
        self.translator = TextBlob(self.query)
        self.to_translate.clear()

        if self.language.currentIndex() == 0:
            self.translated_text.setText('Please choose a Language First.')

        try:
            if self.language.currentIndex() == 1:
                self.translate('af')

            elif self.language.currentIndex() == 2:
                self.translate('sq')

            elif self.language.currentIndex() == 3:
                self.translate('am')

            elif self.language.currentIndex() == 4:
                self.translate('ar')

            elif self.language.currentIndex() == 5:
                self.translate('hy')

            elif self.language.currentIndex() == 6:
                self.translate('az')

            elif self.language.currentIndex() == 7:
                self.translate('eu')

            elif self.language.currentIndex() == 8:
                self.translate('be')

            elif self.language.currentIndex() == 9:
                self.translate('bn')

            elif self.language.currentIndex() == 10:
                self.translate('bs')

            elif self.language.currentIndex() == 11:
                self.translate('bg')

            elif self.language.currentIndex() == 12:
                self.translate('ca')

            elif self.language.currentIndex() == 13:
                self.translate('ceb')

            elif self.language.currentIndex() == 14:
                try:
                    self.translate('zh-CN')
                except:
                    self.translate('zh')

            elif self.language.currentIndex() == 15:
                self.translate('zh-TW')

            elif self.language.currentIndex() == 16:
                self.translate('co')

            elif self.language.currentIndex() == 17:
                self.translate('hr')

            elif self.language.currentIndex() == 18:
                self.translate('cs')

            elif self.language.currentIndex() == 19:
                self.translate('da')

            elif self.language.currentIndex() == 20:
                self.translate('nl')

            elif self.language.currentIndex() == 21:
                self.translate('en')

            elif self.language.currentIndex() == 22:
                self.translate('eo')

            elif self.language.currentIndex() == 23:
                self.translate('et')

            elif self.language.currentIndex() == 24:
                self.translate('fi')

            elif self.language.currentIndex() == 25:
                self.translate('fr')

            elif self.language.currentIndex() == 26:
                self.translate('fy')

            elif self.language.currentIndex() == 27:
                self.translate('gl')

            elif self.language.currentIndex() == 28:
                self.translate('ka')

            elif self.language.currentIndex() == 29:
                self.translate('de')

            elif self.language.currentIndex() == 30:
                self.translate('el')

            elif self.language.currentIndex() == 31:
                self.translate('gu')

            elif self.language.currentIndex() == 32:
                self.translate('ht')

            elif self.language.currentIndex() == 33:
                self.translate('ha')

            elif self.language.currentIndex() == 34:
                self.translate('haw')

            elif self.language.currentIndex() == 35:
                try:
                    self.translate('he')
                except:
                    self.translate('iw')

            elif self.language.currentIndex() == 36:
                self.translate('hi')

            elif self.language.currentIndex() == 37:
                self.translate('hmn')

            elif self.language.currentIndex() == 38:
                self.translate('hu')

            elif self.language.currentIndex() == 39:
                self.translate('is')

            elif self.language.currentIndex() == 40:
                self.translate('ig')

            elif self.language.currentIndex() == 41:
                self.translate('id')

            elif self.language.currentIndex() == 42:
                self.translate('ga')

            elif self.language.currentIndex() == 43:
                self.translate('it')

            elif self.language.currentIndex() == 44:
                self.translate('ja')

            elif self.language.currentIndex() == 45:
                self.translate('jv')

            elif self.language.currentIndex() == 46:
                self.translate('kn')

            elif self.language.currentIndex() == 47:
                self.translate('kk')

            elif self.language.currentIndex() == 48:
                self.translate('km')

            elif self.language.currentIndex() == 49:
                self.translate('rw')

            elif self.language.currentIndex() == 50:
                self.translate('ko')

            elif self.language.currentIndex() == 51:
                self.translate('ku')

            elif self.language.currentIndex() == 52:
                self.translate('ky')

            elif self.language.currentIndex() == 53:
                self.translate('lo')

            elif self.language.currentIndex() == 54:
                self.translate('la')

            elif self.language.currentIndex() == 55:
                self.translate('lv')

            elif self.language.currentIndex() == 56:
                self.translate('lt')

            elif self.language.currentIndex() == 57:
                self.translate('lb')

            elif self.language.currentIndex() == 58:
                self.translate('mk')

            elif self.language.currentIndex() == 59:
                self.translate('mg')

            elif self.language.currentIndex() == 60:
                self.translate('ms')

            elif self.language.currentIndex() == 61:
                self.translate('ml')

            elif self.language.currentIndex() == 62:
                self.translate('mt')

            elif self.language.currentIndex() == 63:
                self.translate('mi')

            elif self.language.currentIndex() == 64:
                self.translate('mr')

            elif self.language.currentIndex() == 65:
                self.translate('mn')

            elif self.language.currentIndex() == 66:
                self.translate('my')

            elif self.language.currentIndex() == 67:
                self.translate('ne')

            elif self.language.currentIndex() == 68:
                self.translate('no')

            elif self.language.currentIndex() == 69:
                self.translate('ny')

            elif self.language.currentIndex() == 70:
                self.translate('or')

            elif self.language.currentIndex() == 71:
                self.translate('ps')

            elif self.language.currentIndex() == 72:
                self.translate('fa')

            elif self.language.currentIndex() == 73:
                self.translate('pl')

            elif self.language.currentIndex() == 74:
                self.translate('pt')

            elif self.language.currentIndex() == 75:
                self.translate('pa')

            elif self.language.currentIndex() == 76:
                self.translate('ro')

            elif self.language.currentIndex() == 77:
                self.translate('ru')

            elif self.language.currentIndex() == 78:
                self.translate('sm')

            elif self.language.currentIndex() == 79:
                self.translate('gd')

            elif self.language.currentIndex() == 80:
                self.translate('sr')

            elif self.language.currentIndex() == 81:
                self.translate('st')

            elif self.language.currentIndex() == 82:
                self.translate('sn')

            elif self.language.currentIndex() == 83:
                self.translate('sd')

            elif self.language.currentIndex() == 84:
                self.translate('si')

            elif self.language.currentIndex() == 85:
                self.translate('sk')

            elif self.language.currentIndex() == 86:
                self.translate('sl')

            elif self.language.currentIndex() == 87:
                self.translate('so')

            elif self.language.currentIndex() == 88:
                self.translate('es')

            elif self.language.currentIndex() == 89:
                self.translate('su')

            elif self.language.currentIndex() == 90:
                self.translate('sw')

            elif self.language.currentIndex() == 91:
                self.translate('sv')

            elif self.language.currentIndex() == 92:
                self.translate('tl')

            elif self.language.currentIndex() == 93:
                self.translate('tg')

            elif self.language.currentIndex() == 94:
                self.translate('ta')

            elif self.language.currentIndex() == 95:
                self.translate('tt')

            elif self.language.currentIndex() == 96:
                self.translate('te')

            elif self.language.currentIndex() == 97:
                self.translate('th')

            elif self.language.currentIndex() == 98:
                self.translate('tr')

            elif self.language.currentIndex() == 99:
                self.translate('tk')

            elif self.language.currentIndex() == 100:
                self.translate('uk')

            elif self.language.currentIndex() == 101:
                self.translate('ur')

            elif self.language.currentIndex() == 102:
                self.translate('ug')

            elif self.language.currentIndex() == 103:
                self.translate('uz')

            elif self.language.currentIndex() == 104:
                self.translate('vi')

            elif self.language.currentIndex() == 105:
                self.translate('cy')

            elif self.language.currentIndex() == 106:
                self.translate('xh')

            elif self.language.currentIndex() == 107:
                self.translate('yi')

            elif self.language.currentIndex() == 108:
                self.translate('yo')

            elif self.language.currentIndex() == 109:
                self.translate('zu')


        except:
            self.translated_text.setText("An error occurred. Either the initial and final language is same or try "
                                         "again. \n"
                                         "Tip2: You cannot translate numbers; only words. 😭😭")
