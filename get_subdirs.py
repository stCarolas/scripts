#!/usr/bin/env python3

import sys
import os
import os.path
import subprocess

PROJECT_DIR = "/home/stcarolas/Coding/projects"

if __name__ == '__main__':
    for child in os.listdir(PROJECT_DIR):
        test_path = os.path.join(PROJECT_DIR, child)
        if os.path.isdir(test_path):
            print(test_path)
