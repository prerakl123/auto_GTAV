import win32api as wapi

key_list = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.'$/\\":
    key_list.append(char)


def key_check():
    keys = []
    for key in key_list:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
