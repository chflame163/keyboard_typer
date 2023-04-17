
import os
import sys
import threading
import time
import random
from pynput import keyboard
from arcade import load_sound, play_sound
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QColor, QFont, QFontDatabase
import ui_typefinish
'''
# windows/mac版在此更改导入ui_typer_win/ui_typer_mac
'''
# UI
import ui_typer_mac

# 全局变量
class Setting:
    # 资源文件夹
    RESOURCE_PATH = "res"
    # 子文件夹
    IMAGE_PATH = "image"
    SOUND_PATH = "sound"
    FONT_PATH = "font"
    ESSAY_PATH = "essay"
    # 文件名
    SOUND_NEW= "new.wav"
    SOUND_PRESS = "press.wav"
    SOUND_RETURN = "return.wav"
    SOUND_FINISH = "finish.wav"
    UI_FONT_FILE = "Turpis-Regular"
    TYPE_FONT_REGULAR_FILE = "XTypewriter-Bold"
    TYPE_FONT_BOLD_FILE = "XTypewriter-Regular.ttf"
    # 文章文件名前缀
    TXT_FILE_PREFIX = "essay_"
    # 键盘按键表文件名
    if sys.platform == "win32":
        INI_FILE = "87keyboard_win.ini"
    else:
        INI_FILE = "87keyboard_mac.ini"

    # 按下退格键计数
    count_of_backspace:int = 0
    # finish窗口弹出状态
    finish_is_active = False

# 发声
class PlaySound:

    # 播放
    def play(self, file_name):
        # 设置文件名
        sound_filename: str = os.path.join(os.path.join(os.path.join(os.path.dirname(sys.argv[0]),
                                           Setting.RESOURCE_PATH), Setting.SOUND_PATH),
                                           file_name)
        # 声音播放器
        sound = load_sound(sound_filename)
        play_sound(sound)

# GUI
class TypeFinishWidget(ui_typefinish.Ui_Form, QtWidgets.QWidget):
    def set_action(self):
        # 设置窗口阻塞
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        # 设置窗口无边框，透明，置顶
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        # 设置阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(1, 1)
        self.shadow.setBlurRadius(32)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.frame_finish.setGraphicsEffect(self.shadow)
        # 设置字体
        fontid = QFontDatabase.addApplicationFont(":font/res/font/Turpis-Regular.ttf")
        fontfamilies = QFontDatabase.applicationFontFamilies(fontid)
        title_font = QFont()
        info_font = QFont()
        title_font.setFamily(fontfamilies[0])
        info_font.setFamily(fontfamilies[0])
        if sys.platform == "win32":
            title_font.setPointSize(11)
            info_font.setPointSize(13)
            self.label_info.setIndent(15)
        else:
            title_font.setPointSize(16)
            info_font.setPointSize(18)
            self.label_info.setIndent(20)
        self.label_title.setFont(title_font)
        self.label_info.setFont(info_font)


        # 设置按钮信号
        self.btn_close.clicked.connect(self.quit)
        self.btn_quit.clicked.connect(self.quit)
        self.btn_next.clicked.connect(self.next)

    # 点击Next按钮
    def next(self):
        Setting.finish_is_active = False
        main.new_typing()
        self.close()

    def quit(self):
        main.quit()

    # 鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(TypeFinishWidget, self).mousePressEvent(event)
            self.start_x = int(event.position().x())
            self.start_y = int(event.position().y())

    # 鼠标弹起事件
    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    # 鼠标拖动事件
    def mouseMoveEvent(self, event):
        super(TypeFinishWidget, self).mouseMoveEvent(event)
        try:
            dis_x = int(event.position().x()) - self.start_x
            dis_y = int(event.position().y()) - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except Exception as e:
            print(repr(e))
'''
# windows/mac版在此更改继承ui_typer_win/ui_typer_mac
'''
# 主UI
class KeyboardWidget(ui_typer_mac.Ui_Form, QtWidgets.QWidget, QtCore.QThread):

    # 计时变量
    taked_time:int = 0

    # 信号槽变量
    signal_enter = QtCore.Signal(bool)
    signal_text_change = QtCore.Signal(str) # lineEdit.Text()

    # 设置窗口无标题栏，透明，置顶
    def set_action(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        # 阴影
        self.kb_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.kb_shadow.setOffset(1, 1)
        self.kb_shadow.setBlurRadius(32)
        self.kb_shadow.setColor(QColor(0, 0, 0, 120))
        self.frame_keyboard.setGraphicsEffect(self.kb_shadow)
        self.tp_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.tp_shadow.setOffset(1, 1)
        self.tp_shadow.setBlurRadius(32)
        self.tp_shadow.setColor(QColor(0, 0, 0, 120))
        self.frame_typer.setGraphicsEffect(self.tp_shadow)
        # 按钮信号槽
        self.btn_close.clicked.connect(self.quit)
        # lineEdit 信号槽
        self.lineEdit_input.returnPressed.connect(self.press_enter)
        self.lineEdit_input.textChanged.connect(self.text_changed)
        # 设置焦点
        self.lineEdit_input.setFocus()
        self.lineEdit_input.setText("")
        # 设置字体
        label_fontid = QFontDatabase.addApplicationFont(":font/res/font/Turpis-Regular.ttf")
        label_fontfamilies = QFontDatabase.applicationFontFamilies(label_fontid)
        regular_fontid = QFontDatabase.addApplicationFont(":font/res/font/XTypewriter-Regular.ttf")
        regular_fontfamilies = QFontDatabase.applicationFontFamilies(regular_fontid)
        bold_fontid = QFontDatabase.addApplicationFont(":font/res/font/XTypewriter-Bold.ttf")
        bold_fontfamilies = QFontDatabase.applicationFontFamilies(bold_fontid)
        line1_font = QFont()
        line1_font.setFamily(regular_fontfamilies[0])
        line2_font = QFont()
        line2_font.setFamily(bold_fontfamilies[0])
        label_font = QFont()
        label_font.setFamily(label_fontfamilies[0])
        if sys.platform == "win32":
            line1_font.setPointSize(12)
            line2_font.setPointSize(14)
            label_font.setPointSize(10)
        else:
            line1_font.setPointSize(18)
            line2_font.setPointSize(20)
            label_font.setPointSize(14)
        self.label_line1.setFont(line1_font)
        self.label_line2.setFont(line2_font)
        self.label_line3.setFont(line1_font)
        self.lineEdit_input.setFont(line2_font)
        self.label_essay_title.setFont(label_font)
        self.label_time.setFont(label_font)
        self.label_speed.setFont(label_font)
        self.label_accuracy.setFont(label_font)

    def refresh_texts(self, texts:list):
        self.label_line1.setText(texts[0])
        self.label_line2.setText(texts[1])
        self.label_line3.setText(texts[2])

    # lineEdit控件按下回车
    def press_enter(self):
        self.signal_enter.emit(True)

    # lineEdit控件文本改变
    def text_changed(self, text):
        self.signal_text_change.emit(text)

    # 鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(KeyboardWidget, self).mousePressEvent(event)
            self.start_x = int(event.position().x())
            self.start_y = int(event.position().y())

    # 鼠标弹起事件
    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    # 鼠标拖动事件
    def mouseMoveEvent(self, event):
        super(KeyboardWidget, self).mouseMoveEvent(event)
        try:
            dis_x = int(event.position().x()) - self.start_x
            dis_y = int(event.position().y()) - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except Exception as e:
            print(repr(e))

    def quit(self):
        main.quit()
# 键盘事件
class KeyboardMonitor():

    # 弹起灰色按键qss
    qss_release = '''
QPushButton{            
background-color: rgb(137,137, 137);
border:2px solid rgba(199, 199, 199,50);
border-radius:9px;
}
QPushButton:pressed {
    background-color: rgb(111, 111, 111);
}
'''
    # 按下黄色按键qss
    qss_press = '''
QPushButton{            
background-color: rgb(255, 200, 100);
border-radius:9px;
}
'''


    # 按下按键
    def on_press(self, key):
        if not Setting.finish_is_active:
            # 获取UI按钮属性名
            attr_name = main.CODE2ATTR.get(str(key), '')
            # 显示按下颜色
            if attr_name:
                # print(f"press:{attr_name}")
                key_obj = getattr(main.keyboard_gui, attr_name)
                key_obj.setStyleSheet(self.qss_press)
                setattr(main.keyboard_gui, attr_name, key_obj)
            if str(key) == "Key.backspace":
                Setting.count_of_backspace += 1

    # 松开按键
    def on_release(self, key):
        if not Setting.finish_is_active:
            # 获取UI按钮属性名
            attr_name = main.CODE2ATTR.get(str(key), '')
            # 恢复按钮颜色
            if attr_name:
                # print(f"release:{attr_name}")
                key_obj = getattr(main.keyboard_gui, attr_name)
                key_obj.setStyleSheet(self.qss_release)
                setattr(main.keyboard_gui, attr_name, key_obj)

# 键盘监听线程
def run_monitor():
    kb_monitor = KeyboardMonitor()
    listener = keyboard.Listener(on_press=kb_monitor.on_press, on_release=kb_monitor.on_release)
    listener.start()
    listener.join()


class Main(QtWidgets.QWidget):

    # 初始化按键对应显示名称，对应控件名称表
    def load_map(self):
        ini_file = os.path.join(os.path.join(os.path.dirname(sys.argv[0]),
                                             Setting.RESOURCE_PATH), Setting.INI_FILE)
        name: list = []
        attr: list = []
        try:
            with open(ini_file, "r", encoding="utf-8") as f:
                for i in f.readlines():
                    # 排除#开头的行和空行
                    if (not i.startswith("#")) and (i.strip().strip("\n")):
                        # 排除空键
                        line = i.strip("\n").split("\t")
                        if len(line) == 3:
                            name.append([line[0], line[1]])
                            attr.append([line[0], line[2]])

        except Exception as e:
            print("load keymap file error: " + repr(e))
            sys.exit(1)
        return dict(name), dict(attr)

    CODE2NAME, CODE2ATTR = load_map(None)

    # txt文件名列表指针
    txt_filename_pointer = 0

    # txt路径
    txt_path = os.path.join(os.path.join(os.path.dirname(sys.argv[0]), Setting.RESOURCE_PATH), Setting.ESSAY_PATH)

    # 发声实例对象
    sound = PlaySound()

    # 读取文章内容
    def load_essay(self):
        file_name = Setting.TXT_FILE_PREFIX + str(self.essay_list[self.txt_filename_pointer]) + ".txt"
        txt_file = os.path.join(self.txt_path, file_name)
        try:
            with open(txt_file, 'r') as f:
                txt = f.readlines()
                text_title = txt[0].replace("# ", "").strip("\n")
                text = txt[2:]
                if self.txt_filename_pointer < len(self.essay_list)-1:
                    self.txt_filename_pointer += 1
                else:
                    self.txt_filename_pointer = 0
                return text_title, text
        except Exception as e:
            print(repr(e))

    # 变量初始化
    def new_typing(self):
        # 用于显示的文本（line2是当前行，line1是输入过的上一行，line3是待输入的下一行）
        self.line1: str = ""
        self.line2: str = ""
        self.line3: str = ""

        # 当前行清零
        self.current_line: int = 0
        # 当前输入字符的位置清零
        self.count_typed_chars: int = 0
        self.count_pointer: int = 0
        # 输入有效字符总计清零
        self.total_input_chars: int = 0
        self.total_input_pointer: int =0
        # 正确字符总计清零
        self.count_matched_chars: int = 0
        self.count_match_pointer: int = 0
        # 当前输入错字表清零
        self.match_list:list = []
        self.previous_match_list:list = []
        # 错键汇总清零
        self.wrong_keys_dict.clear()
        # 重置退格统计
        Setting.count_of_backspace = 0

        # 开始输入标记清零
        self.begin: bool = False
        # 设置UI
        self.TEXT_TITLE, self.TEXT = self.load_essay()
        self.keyboard_gui.label_essay_title.setText(self.TEXT_TITLE)
        self.line2 = self.TEXT[self.current_line].rstrip()
        self.line3 = self.TEXT[self.current_line + 1].rstrip()
        self.keyboard_gui.lineEdit_input.setMaxLength(len(self.line2))
        self.refresh_texts()
        self.keyboard_gui.label_speed.setText("Speed: 0 Char/Min")
        self.keyboard_gui.label_accuracy.setText("Accuracy: 0%")
        self.keyboard_gui.label_time.setText("00:00:00")
        self.sound.play(Setting.SOUND_NEW)

    # 入口
    def start(self):
        # 生成随机文章顺序
        self.essay_list = self.generate_random_list(20)
        # 错键汇总字典
        self.wrong_keys_dict: dict = dict()
        # 定时器用于显示运行时间
        self.timer = QtCore.QBasicTimer()
        # 设置GUI
        self.finish_gui = TypeFinishWidget()
        self.finish_gui.setupUi(self.finish_gui)
        self.finish_gui.set_action()
        self.keyboard_gui = KeyboardWidget()
        self.keyboard_gui.setupUi(self.keyboard_gui)
        self.keyboard_gui.set_action()
        # 设置信号槽
        self.keyboard_gui.signal_enter.connect(self.enter_pressed)
        self.keyboard_gui.signal_text_change.connect(self.text_changed)
        # 初始化变量
        self.new_typing()
        # 显示UI
        self.keyboard_gui.show()

    # 定时器事件，刷新事件
    def timerEvent(self, e):
        self.keyboard_gui.taked_time += 1
        self.keyboard_gui.label_time.setText(time.strftime('%H:%M:%S',
                                             time.gmtime(self.keyboard_gui.taked_time)))

    # 生成随机数列表
    def generate_random_list(self, lenth:int) -> list:
        return random.sample(range(1,lenth+1),lenth)

    # 文章输入完成
    def type_finish(self):
        # 设置窗口变量，使按键事件停止触发
        Setting.finish_is_active = True
        # 播放声音
        self.sound.play(Setting.SOUND_FINISH)
        # 停止计时器
        self.timer.stop()
        # 生成时间文本
        tmp_list = time.strftime('%H:%M:%S', time.gmtime(self.keyboard_gui.taked_time)).split(":")
        time_txt = ""
        if not tmp_list[0] == "00":
            time_txt = str(int(tmp_list[0])) + " Hour "
        if not tmp_list[1] == "00":
            time_txt = time_txt + str(int(tmp_list[1])) + " Minute "
        if not  tmp_list[2] == "00":
            time_txt = time_txt + str(int(tmp_list[2])) + " Second"
        # 计算正确率
        if not self.count_pointer == 0:
            accuracy = int(self.count_match_pointer / self.count_pointer * 100)
        else:
            accuracy = 0
        # 计算速度
        if self.keyboard_gui.taked_time:
            speed = self.total_input_pointer * 60 // self.keyboard_gui.taked_time
        else:
            speed = 0
        # 计算错误率最高的键
        if " " in self.wrong_keys_dict:
            del self.wrong_keys_dict[" "]
        wrong_max: list = []
        try:
            max_value = max(self.wrong_keys_dict.values())
            for i in self.wrong_keys_dict.items():
                if i[1] == max_value:
                    wrong_max.append(i[0].upper())
        except Exception as e:
            wrong_max = ["None"]

        # 显示文字
        self.finish_gui.label_title.setText(self.TEXT_TITLE)
        self.finish_gui.label_info.setText(
                f"You Takes {time_txt}\n" +
                f"Input {self.total_input_chars} Chars\n" +
                f"Type Speed is {speed} Char/Minute\n" +
                f"Type Accuracy Rate is {accuracy}%\n" +
                f"'BackSpace' Key Pressed {Setting.count_of_backspace} Times\n" +
                f"Key(s) of the Highest Wrong Rate is:\n" +
                f"{', '.join(wrong_max)}"
                )
        self.finish_gui.show()

    # 更新文章文字显示
    def refresh_texts(self):
        texts:list = [self.line1, self.line2, self.line3]
        self.keyboard_gui.refresh_texts(texts)


    # 当输入完一行
    def enter_pressed(self, enter:bool):
        self.sound.play(Setting.SOUND_RETURN)
        if not self.begin:
            self.timer.start(1000, self)
            self.begin = True
        self.count_typed_chars += len(self.line2)
        match_list = self.match_input(self.keyboard_gui.lineEdit_input.text().strip("\n"))
        if match_list:
            self.count_matched_chars += match_list.count(1)
            self.total_input_chars += len(self.match_list)
            # print(f"total={self.total_input_pointer},matched={self.count_match_pointer}")
        if self.current_line == len(self.TEXT) - 1:
            self.type_finish()
        line1_txt = self.keyboard_gui.label_line2.text()
        line1_txt = line1_txt.replace(" #E00000>", " #EF9999>")
        line1_txt = line1_txt.replace(" #0050E0>", " #99BBEF>")
        line1_txt = line1_txt.replace(" #000000>", " #999999>")
        self.line1 = line1_txt
        self.line2 = self.line3
        if self.current_line < len(self.TEXT) - 2:
            self.line3 = self.TEXT[self.current_line + 2].rstrip()
        else:
            self.line3 = ""
        self.current_line += 1
        self.keyboard_gui.lineEdit_input.clear()
        self.keyboard_gui.lineEdit_input.setMaxLength(len(self.line2))
        self.refresh_texts()


    # 比较输入的字符串与文章是否匹配，正确的字符位置返回1，错误的返回0
    def match_input(self, input:str) -> list:
        ret = []
        if len(input) < len(self.line2):
            length = len(input)
        else:
            length = len(self.line2)
        for i in range(length):
            if input[i] == self.line2[i]:
                ret.append(1)
            else:
                ret.append(0)
        return ret


    # 为正确/错误的文字设置不同颜色
    def refresh_display(self, input):
        # 获取错字符列表
        self.previous_match_list = self.match_list
        self.match_list = self.match_input(input)
        # 如果新的错字符列表有新增0，加入到错字总列表
        if len(self.match_list) - len(self.previous_match_list) == 1 and self.match_list[-1] == 0:
            key = self.line2[len(self.match_list) -1]
            self.wrong_keys_dict.update({key : self.wrong_keys_dict.get(key, 0) + 1})
            # print(self.wrong_keys_dict)
        # 显示计数
        self.total_input_pointer = self.total_input_chars + len(input)
        self.count_pointer = self.count_typed_chars + len(input)
        self.count_match_pointer = self.count_matched_chars + self.match_list.count(1)

        if self.keyboard_gui.taked_time:
            speed = self.total_input_pointer * 60 // self.keyboard_gui.taked_time
        else:
            speed = 0
        self.keyboard_gui.label_speed.setText(f"Speed: {speed} Char/Min")
        if not self.count_pointer == 0:
            accuracy = int(self.count_match_pointer / self.count_pointer * 100)
        else:
            accuracy = 0
        self.keyboard_gui.label_accuracy.setText(f"Accuracy: {accuracy}%")

        # 文字颜色
        mark_dismatch:str = "<font color = #E00000>"
        mark_match:str = "<font color = #0050E0>"
        mark_orig:str = "<font color = #000000>"
        mark_end:str = "</font>"

        color_list = []
        for i in range(len(self.match_list)):
            if self.match_list[i]==1:
                color_list.append(mark_match + self.line2[i] + mark_end)
            else:
                color_list.append(mark_dismatch + self.line2[i] + mark_end)
        orig_txt = self.line2[len(self.match_list):]
        color_txt = "".join(color_list) + mark_orig + orig_txt + mark_end
        self.keyboard_gui.label_line2.setText(color_txt)

    # 输入字符事件
    def text_changed(self, string:str):
        self.sound.play(Setting.SOUND_PRESS)
        if not self.begin:
            self.timer.start(1000, self)
            self.begin = True
        self.refresh_display(string)

    # 退出
    def quit(self):
        self.timer.stop()
        for w in QtWidgets.QApplication.instance().allWidgets():
            if w != self:
                del w
        os._exit(0)

# 返回当前工作文件夹路径
def source_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    # 工作路径设置
    cd = source_path('')
    os.chdir(cd)
    # 设置监听
    thread_kb_monitor = threading.Thread(target=run_monitor)
    thread_kb_monitor.setDaemon(True)
    thread_kb_monitor.start()
    # 设置QT
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.start()
    sys.exit(app.exec())


