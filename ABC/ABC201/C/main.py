#!/usr/bin/env python3

# 入力の受け取り
S=input()

# 暗証番号としてありうるものをカウントする変数
count=0

# num=0~9999まで
for num in range(10000):
    # 暗証番号として適するならTrue,適さないならFalse
    OK=True

    # numを文字列へ変換
    num=str(num)
    # 4桁になるよう先頭に0埋め
    num=num.zfill(4)

    # i=0~9まで
    for i in range(10):
        # S[i]が「○」なら
        if S[i]=="o":
            # iがnumに含まれていなければ
            if str(i) not in num:
                # 暗証番号に適さない
                OK=False
        # S[i]が「x」なら
        if S[i]=="x":
            # iがnumに含まれるなら
            if str(i) in num:
                # 暗証番号に適さない
                OK=False

    # 暗証番号に適していれば
    if OK==True:
        # カウントする
        count+=1

# 答えの出力
print(count)
