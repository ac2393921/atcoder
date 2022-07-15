#!/bin/bash

git add -N .
set +e
git diff --name-only --exit-code
echo $(git diff --name-only --exit-code)

if [[ $? -eq 1 ]]; then
    echo 'There are changes'
    git commit -m "add: solver"
    git push origin main
else
    echo 'There are no changes'
fi