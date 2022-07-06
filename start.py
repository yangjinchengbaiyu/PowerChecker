import win32api as w1
import win32con as w2
import sys
sys.setrecursionlimit(1000000)
 
name = 'PowerChecker'
path = 'PowerChecker.exe'
 
KeyName = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
 

try:
    key = w1.RegOpenKey(w2.HKEY_CURRENT_USER, KeyName, 0, w2.KEY_ALL_ACCESS)
    w1.RegSetValueEx(key, name, 0, w2.REG_SZ, path)
except:
    print('添加失败！')
else:
    print('添加成功！')

input('输入回车以退出此程序')
