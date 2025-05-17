import logging
import subprocess
from concurrent.futures import ThreadPoolExecutor

import functools
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from qtpy import *
from qfluentwidgets import *
from qfluentwidgets.components.material import *
from qfluentwidgets import FluentIcon as FIF

import zbToolLib as zb
import zbWidgetLib as zbw
from qtpy import *


class Program:
    """
    程序信息
    """
    NAME = "zb的应用程序模板"  # 程序名称
    VERSION = "0.0.0"  # 程序版本
    TITLE = f"{NAME} {VERSION}"  # 程序标题
    URL = "https://ianzb.github.io/project/zbGuiTemplate.html"  # 程序网址
    LICENSE = "GPLv3"  # 程序许可协议
    INFO = "© 2022-2025 Ianzb. GPLv3 License."
    # UPDATE_URL = "http://123pan.ianzb.cn/Code/zbGuiTemplate/index.json"  # 更新网址
    # UPDATE_INSTALLER_URL = "http://123pan.ianzb.cn/Code/zbGuiTemplate/zbGuiTemplate_setup.exe"  # 更新安装包链接
    UNINSTALL_FILE = "unins000.exe"  # 卸载程序名称

    AUTHOR_NAME = "Ianzb"  # 作者名称
    AUTHOR_URL = "https://ianzb.github.io/"  # 作者网址
    GITHUB_URL = "https://github.com/Ianzb/zbGuiTemplate/"  # Github网址

    MAIN_FILE_PATH = sys.argv[0]  # 程序主文件路径
    MAIN_FILE_NAME = zb.getFileName(MAIN_FILE_PATH)  # 当前程序文件名称
    INSTALL_PATH = zb.getFileDir(MAIN_FILE_PATH)  # 程序安装路径
    SOURCE_PATH = r"source\img"  # 程序资源文件路径
    PROGRAM_PID = os.getpid()  # 程序pid
    DATA_PATH = zb.joinPath(zb.USER_PATH, "zb")  # 程序数据路径
    SETTING_FILE_PATH = zb.joinPath(DATA_PATH, "settings.json")  # 程序设置文件路径
    LOGGING_FILE_PATH = zb.joinPath(DATA_PATH, "logging.log")  # 程序日志文件路径
    ADDON_PATH = zb.joinPath(DATA_PATH, "addon")  # 程序插件路径

    STARTUP_ARGUMENT = sys.argv[1:]  # 程序启动参数
    THREAD_POOL = ThreadPoolExecutor()  # 程序公用线程池

    def __init__(self):
        # 创建数据目录
        zb.createDir(self.DATA_PATH)

        # 切换运行路径
        os.chdir(self.INSTALL_PATH)

        # 设置任务栏
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.NAME)

        # 打包后资源路径切换
        if self.isExe:
            self.SOURCE_PATH = sys._MEIPASS + r"\img"

    @property
    def ICON(self):
        return program.source("program.png")

    @property
    def isStartup(self):
        """
        判断程序是否为开机自启动
        @return: bool
        """
        return "startup" in self.STARTUP_ARGUMENT

    @property
    def isExe(self):
        """
        判断程序是否为
        @return:
        """
        return ".exe" in self.MAIN_FILE_NAME

    def source(self, *args):
        """
        快捷获取程序资源文件路径
        @param name: 文件名
        @return: 文件路径
        """
        return zb.joinPath(self.SOURCE_PATH, *args)

    def cache(self, *args):
        """
        快捷获取程序缓存文件路径
        @param name: 文件名
        @return: 文件路径
        """
        return zb.joinPath(self.DATA_PATH, "cache", *args)

    def close(self):
        """
        退出程序
        """
        logging.info("程序已退出！")
        os._exit(0)

    def restart(self):
        """
        重启程序
        """
        subprocess.Popen(self.MAIN_FILE_PATH)
        logging.info("程序正在重启中！")
        os._exit(0)


program = Program()
