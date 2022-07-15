#!/bin/bash

git add -N .
set +e
git diff --name-only --exit-code

echo 'There are changes'
git config --global user.email "ac2393921@gmail.com"
git config --global user.name "ac2393921"
git add .
git commit -m "add: solver"
git push origin main
if [ $? -eq 1 ]; then
    echo 'There are changes'
    git add .
    git commit -m "add: solver"
    git push origin main
else
    echo 'There are no changes'
fi