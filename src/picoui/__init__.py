from multiprocessing.connection import Connection, Pipe
import os
import sys
from typing import Any
from rich.live import Live
from multiprocessing import Process
from readchar import readkey, key


def kb_handler(pipe: Connection, stdin: Any):
    sys.stdin = stdin
    while True:
        if pipe.poll():
            if pipe.recv() == "STOP":
                break
        pipe.send(readkey())


def test():
    content = []
    send, recv = Pipe()
    process = Process(
        target=kb_handler, args=[send, os.fdopen(os.dup(sys.stdin.fileno()))]
    )
    process.start()
    with Live(str(content), refresh_per_second=10) as live:
        while True:
            if recv.poll():
                new_key = recv.recv()
                if new_key == key.ENTER:
                    content += "ENTER"
                elif new_key == key.ESC:
                    break
                else:
                    content += new_key
                live.update(str(content))
    recv.send("STOP")
