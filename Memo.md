# 課題　ToDo
bit全探索 itertools.product((0, 1) repeat = N)でbitを全列挙せずbit演算だけで実装できるようにする

~~modの性質の理解度を深める~~

分割統治法や再帰に関するイメージが弱い

繰り返し二乗法復習

# 精進方針
最低でも解説ACはマスト

復習と応用に対応できるようにする

# アルゴリズムごとの所感と優良記事まとめ
気付きや留意点の言語化による学習効率の促進が目的


## 全探索
https://atcoder.jp/contests/abc296/tasks/abc296_d

## 順列全探索

## bit全探索
https://atcoder.jp/contests/abc293/tasks/abc293_c
https://atcoder.jp/contests/past201912-open/tasks/past201912_g
集合や組み分けの処理はbit

## クエリ処理
pythonでの留意点はstd::setのような
順序付き集合がないこと
https://atcoder.jp/contests/abc294/tasks/abc294_d

## 累積和
累積和っぽい考えで計算量制約をクリアするため工夫する問題
https://atcoder.jp/contests/abc221/tasks/abc221_d


## DP
https://atcoder.jp/contests/abc248/tasks/abc248_c

貰うDPだと難しいがO(NM)　dp + 累積和で計算量削減

配るDPだとO(NMK)

部分和問題
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

## 二部探索
https://atcoder.jp/contests/abc248/tasks/abc248_d

## 尺取り法
尺取り法とは端的に言うと、区間の左端と右端を尺取り虫のように動かすことで、条件を満たす区間を高速に見つける、というアルゴリズム

尺取法は固定する区間の左端をforで、右端をwhileで処理するとうまくいく。
https://atcoder.jp/contests/abc229/tasks/abc229_d
https://atcoder.jp/contests/abc250/tasks/abc250_d

## 数学関係の典型
2進数変換はformat(数字, 'b')が楽

0埋めver　format(n, '08b') 8桁

２辺のなす角＝sin関連＝外積

a*b*sin / 2 は三角形の面積　外積は平行四辺形

外積の公式忘れても行列式の１行余因子展開思い出したらok

bit周り
bitのANDは桁の繰り上がりなし　信号機の点灯感

https://atcoder.jp/contests/abc254/submissions/me
# dfs(再帰と非再帰)

## bfs
https://atcoder.jp/contests/abc211/tasks/abc211_d

## UnionFind

## Tree
## 平衡二分探索木
https://www.slideshare.net/iwiwi/2-12188757
## セグメント木
https://www.slideshare.net/iwiwi/ss-3578491

## 重み付きグラフの最小移動経路

## Binary indexed tree
フェニック木の実態は(実装上は)、部分和をなんかいい感じに詰め込んだ１次元配列

セグメントツリーの機能限定版　

2種類の操作add sumを高速で処理できるO(logN)
半開区間ではなく閉区間で考える

https://qiita.com/AkariLuminous/items/f2f7930e7f67963f0493
