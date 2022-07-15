#!/bin/bash

if [ $# -ne 2 ]; then
  echo "コンテスト名と番号を入力してください。" 1>&2
  exit 1
fi

if [ ! -d $1 ]; then
  mkdir $1
fi

if [ ! -d $2 ]; then
  cd $1
  mkdir $2
  cd $2
  for rate in {a..f}
  do
    touch $rate.py
  done
else
  echo "コンテストが存在しています。" 1>&2
fi