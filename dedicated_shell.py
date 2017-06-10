#!/usr/bin/env python3
import os
from plumbum import local
import argparse

def get_cli_args():
    parser = argparse.ArgumentParser(description='Tools for working with confluence rest api')
    parser.add_argument('message',
                    metavar = 'message',
                    type = str, 
                    default = None,
                    nargs = '?',
                    help = 'command to run')
    return parser.parse_args()

class Tmux:
    def __init__(self):
        self.tmux = local["tmux"]

    def get_panes(self):
        return self.tmux["list-panes"]().strip().split("\n")

    def create_pane(self, command=None):
        self.tmux["split-window", "-h", "-p", "70", "-c", os.getcwd(), command]()

    def delete_other_panes(self):
        self.tmux["killp", "-a"]()

TMUX = Tmux()

def create_dedicated_shell(command=None):
    panes = TMUX.get_panes()
    if len(panes) > 1:
        TMUX.delete_other_panes()
    TMUX.create_pane(command)

if __name__ == "__main__":
    args = get_cli_args()
    create_dedicated_shell(args.message)
