#!/bin/bash
git init
git add *
#git commit -a
git commit -m "my  commits"
git remote add origin git@github.com:superdebug/python-exam.git
git push -u origin master
#git push -u origin +master
