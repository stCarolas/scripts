#!/usr/bin/env python3

import sys
import os.path
import subprocess

# GRADLE_PATH = "/home/stcarolas/Coding/soft/gradle-3.0/bin/gradle"
GRADLE_PATH = "/home/stcarolas/Coding/soft/gradle-3.1/bin/gradle"

if __name__ == '__main__':
    rootPath = "."
    buildSystemArgs = sys.argv[1:]
    if len(buildSystemArgs) == 0:
        buildSystemArgs = ["clean", "build"]
    if not os.path.exists("gradlew"):
        if os.path.exists("build.gradle"):
            subprocess.run([GRADLE_PATH, "wrapper"])
        else:
            subprocess.run([GRADLE_PATH, "init"])
    if os.path.exists("gradlew"):
            subprocess.run([GRADLE_PATH] + buildSystemArgs)
    # if Path(rootPath).joinpath("build.gradle").exists():
        # subprocess.run([GRADLE_PATH, "clean","build"] + buildSystemArgs)
    # if Path(rootPath).joinpath("pom.xml").exists():
        # subprocess.run(["mvn","clean","install"] + buildSystemArgs)
    # if Path(rootPath).joinpath("Makefile").exists():
        # subprocess.run(["make"] + buildSystemArgs)
