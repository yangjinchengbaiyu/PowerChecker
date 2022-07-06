# PowerChecker

### 项目介绍
会检查笔记本的电量、CPU温度、CPU占用、内存占用等。当获取的值超出安全范围时，会通过弹窗提示用户。


### 版本

#### v0.1版本

##### 介绍
初步制作了代码的框架（如获取电量，分析等），并配合tkinter实现了在合适的时机弹窗。

##### 文件结构
1. PowerChecker.pyw为主程序，它依赖messageboxs.py模块。
2. start.py为设置模块，它可将PowerChecker.pyw设为开机启动项（如果您并不想此程序开机运行，可以在“任务管理器”->“启动”中禁用。

##### 注意事项
1. PowerChecker.pyw依赖psutil库，可通过在“命令提示符”内使用以下代码下载和安装：

```
pip install psutil
```
2. start.py依赖pywin32库中的win32api和win32api和win32con，可通过在“命令提示符”内使用以下代码下载和安装：

```
pip install pywin32
```
