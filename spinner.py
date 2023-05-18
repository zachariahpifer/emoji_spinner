"""The module can be imported and used to display spinning animations in the terminal."""
from typing import Callable
import os
from itertools import cycle
import sys
import time
import threading
import cursor


class Spinners:
    """Spinners class contains a few different spinners that can be used"""
    clocks = cycle(["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"])
    moons = cycle(["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"])
    globes = cycle(["🌍", "🌎", "🌏"])
    circles = cycle(["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫️", "🟤"])
    squares = cycle(["⬛️", "🟥", "🟧", "🟨", "🟩", "🟦", "🟪"])


def SpinWhile(callback: Callable, *args, symbols: cycle = Spinners.clocks) -> None:
    """SpinWhile will spin a spinner while the callback function is running
    thread_wrapper is used to suppress the output of the callback function
    """
    def thread_wrapper(callback: Callable, *args) -> None:
        with open(os.devnull, "w", encoding="utf-8") as sys.stdout:
            callback(*args)

    def spin_loop(symbols, terminal, callback_thread):
        while callback_thread.is_alive():
            terminal.write(next(symbols))
            terminal.flush()
            terminal.write("\b\b")
            terminal.flush()
            time.sleep(0.25)
        cursor.show()

    cursor.hide()
    terminal = sys.stdout
    callback_thread = threading.Thread(
        target=thread_wrapper, args=(callback, *args)
    )
    callback_thread.start()
    spin_loop(symbols, terminal, callback_thread)


def printYForXSeconds(x: int, msg: str) -> None:
    """printYForXSeconds will print a message y times for x seconds"""
    for _ in range(x):
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    SpinWhile(printYForXSeconds, 5, "This wont print", symbols=Spinners.squares)
