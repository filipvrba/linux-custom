#!/bin/bash

dir=`dirname "$0"`
cp $dir/home/bashrc ~/.bashrc &&
cp -r $dir/home/themes/* ~/.themes &&
cp -r $dir/home/local/* ~/.local &&

pip install transfv &&

echo "All a files is installed."
