#!/bin/bash
DIR="/Users/ac2393921/work/github.com/ac2393921/atcoder"
cd $DIR

git add -N .
set +e
git diff --name-only --exit-code

if [ $? -eq 1 ]; then
    echo 'There are changes'
    git config --global user.email "ac2393921@gmail.com"
    git config --global user.name "ac2393921"
    git add .
    git commit -m "add: solve $1"
    git remote add origin git@github.com:ac2393921/atcoder
    git push origin main
else
    echo 'There are no changes'
fi
