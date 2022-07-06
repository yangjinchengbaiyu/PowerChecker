# _*_ coding:UTF-8 _*_
from tkinter import Tk
from tkinter import messagebox


window = Tk()
window.withdraw()
window.update()


messagebox.showinfo('提示', 'PowerChecker已启动！')


def lower(e: int):
    """电量较低"""
    messagebox.showwarning(title='电量较低警告',
                           message=f'您的电量仅为{e}%，请及时充电！')


def very_low(e: int):
    """电量极低"""
    messagebox.showerror(title='电量极低警告',
                         message=f'您的电量仅为{e}%，请及时充电！')



