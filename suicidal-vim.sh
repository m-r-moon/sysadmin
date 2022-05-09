#!/bin/bash
vim | ps aux | grep vim | grep -v grep | awk '{print $2}' | xargs kill -9
