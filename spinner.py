from typing import Callable
import os
from itertools import cycle
import sys
import time
import threading
import cursor


class Spinner:
    clocks = cycle(["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"])
    moons = cycle(["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"])
    globes = cycle(["🌍", "🌎", "🌏"])
    circles = cycle(["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫️", "🟤"])

    @staticmethod
    def thread_wrapper(callback: Callable, *args) -> None:
        with open(os.devnull, "w") as sys.stdout:
            callback(*args)

    @staticmethod
    def spin(callback: Callable, *args, symbols: cycle = moons) -> None:
        cursor.hide()
        terminal = sys.stdout
        callback_thread = threading.Thread(
            target=Spinner.thread_wrapper, args=(callback, *args)
        )
        callback_thread.start()
        while callback_thread.is_alive():
            terminal.write(next(symbols))
            terminal.flush()
            terminal.write("\b\b")
            terminal.flush()
            time.sleep(0.25)
        cursor.show()


def printYForXSeconds(x: int, msg: str) -> None:
    for _ in range(x):
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    Spinner.spin(printYForXSeconds, 5, "This wont print", symbols=Spinner.circles)
