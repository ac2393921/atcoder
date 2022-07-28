if [ $# -ne 3 ]; then
    echo "コンテスト名と番号を入力してください。" 1>&2
    exit 1
fi

cd $1/$2/$3

FILE_NUM=$(ls -U1 test/in | wc -l)

for i in $(seq 1 $FILE_NUM); do
    python solver.py <test/in/in$i.txt
done
