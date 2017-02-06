#! /usr/bin/env python3
import argparse
import git

GIT_REPO_URL = "ssh://git@git/corp-dash/corp-dash-settings.git" 

class Repo():
    
    def __init__(self):
        self.repo = git.Git().clone(
            "git://gitorious.org/git-python/mainline.git"
        )


def get_cli_args():
    parser = argparse.ArgumentParser(
        description='EQ time updater'
    )
    parser.add_argument('time',
                        metavar = 'time',
                        type = str, 
                        nargs = 1,
                        help = 'eq time to set')

if __name__ == "__main__":
   args = get_cli_args()
   time = args.repo[0]
   print("update eq time") 
