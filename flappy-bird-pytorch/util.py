# -*- coding: utf-8 -*-
"""输出打印工具模块。
"""


def print_bar(epoch, epochs, etc=None, bar_size=50):
    """打印进度条。

    Parameters
    ----------
    epoch : int
        当前进度
    epochs : int
        总进度
    etc : Any, optional
        打印后缀, by default None
    bar_size : int, optional
        进度条长度, by default 50
    """
    process = bar_size * epoch / epochs
    process = int(process + (int(process) < process))
    strs = [
        f"Epoch {epoch}/{epochs}",
        f" |\033[1;30;47m{' ' * process}\033[0m{' ' * (bar_size-process)}| ",
    ]
    if etc is not None:
        strs.append(str(etc))
    if epoch:
        strs.insert(0, "\033[A")
    print("".join(strs) + "    ")
