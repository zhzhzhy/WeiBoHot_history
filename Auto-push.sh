#!/bin/bash

<<Title
MIT License

Copyright (c) 2020 Geek_cat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

  Author: Geek_cat (https://github.com/zhzhzhy)
  Usage: This is a Linux Server script for auto-git-push
  Set this script running with Crontab!(For example: * * * * * ~/Auto-push.sh {YOU GIT DIRECTORY})
  Example: ~/Auto-push.sh {YOU GIT DIRECTORY}
Title

cd $1
git push origin master
if [ $? == 0 ]; then
	echo "Finish push"
else
	echo "Error with this push!"
fi
