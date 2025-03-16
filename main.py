import win32gui

window = win32gui.GetForegroundWindow()
print(f"Active window: {window}")
print(f"Active window title: {win32gui.GetWindowText(window)}")
print(f"Active window class: {win32gui.GetClassName(window)}")
# print(f"Active window handle: {win32gui.GetForegroundWindow()}")
# print(f"Active window process name: {win32gui.GetWindowText(window)}")
# print(f"Active window rect: {win32gui.GetWindowRect(window)}")
