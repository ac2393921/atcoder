#!/bin/bash

cat <<END
**************************************************
SETUP START!
**************************************************
END

if [ $# -ne 2 ]; then
  echo "コンテスト名と番号を入力してください。" 1>&2
  exit 1
fi

if [ ! -d $1 ]; then
  mkdir $1
fi

if [ ! -d $2 ]; then
  cd $1

  for i in {1..100}; do
    mkdir $(printf "%03d" $i)
    cd $(printf "%03d" $i)
    for rate in {a..f}; do
      mkdir $rate
      mkdir $rate/test
      mkdir $rate/test/in
      mkdir $rate/test/out
      touch $rate/solver.py
      for i in {1..3}; do
        touch $rate/test/in/in$i.txt
        touch $rate/test/out/out$i.txt
      done

      # echo "Makeing $rate"
    done
    cd ../
  done

else
  echo "コンテストが存在しています。" 1>&2
fi

cat <<END

**************************************************
SETUP FINISHED! bye.
**************************************************

END
