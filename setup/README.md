# Python プログラミング環境のセットアップ



ここでは，[高橋担当の2022年度の「数理情報演習」](https://www-tlab.math.ryukoku.ac.jp/wiki/?SJE/2022)（以下SJE2022）の授業のための Python プログラミング環境をセットアップする方法について説明します．

## はじめに

Python プログラミングのためには，次のようなものが必要です．

1. Python のプログラムを実行するための環境
1. Python のプログラムを作成するためのエディタ

一つ目のものを用意する方法にはいろいろあるのですが，この授業では https://www.python.org/ から素で Python をインストールする方法を採用します（無料です）． **他の方法でインストールした Python 環境がある（例: Anaconda 入れた， Microsoft Store から入れた，Homebrew で入れた，WSL2 入れたら入ってた，etc.）というひとは，どうするか相談してください**．

二つ目のものについては，Microsoft の [Visual Studio Code](https://code.visualstudio.com/) というソフトウェアを使います（無料です）． 他の授業等でインストール済みのひとは，インストール作業そのものはスキップして構いませんが，Python プログラミングのための設定等は必要ですので注意してください．

この授業では，これらに加えて Jupyter Notebook という，文書に Python などのプログラムコードを埋め込むことができる仕組みも利用します．

## 第一部 VSCode, Python のインストールとはじめての Python プログラミング

次のことを順次やりましょう．

1. VSCode のインストール
    - [Windows編](InstallVSCode_win.md)
    - [macOS編](InstallVSCode_mac.md)

1. Python のインストール
    - [Windows編](InstallPython_win.md)
    - [macOS編](InstallPython_mac.md)

1. 環境整備＋はじめての Python プログラミング
    - [Windows編](mkdir_hoge_py_win.md)
    - [macOS編](mkdir_hoge_py_mac.md)

## 第二部 OpenCV等のインストールとはじめての Notebook

### OpenCV 等のインストール

この授業では，**OpenCV** や **NumPy** といったソフトウェア・ライブラリを利用します．

- [OpenCV](https://opencv.org/): コンピュータビジョンのためのライブラリ．C++ や Python から呼び出して画像処理などいろんなことができる．
- [NumPy](https://numpy.org/): Python 用の科学技術計算ライブラリ

次のように `pip3` コマンドを実行することで，これらをインストールすることができます．

```
pip3 install opencv-python
```

一見 OpenCV しかインストールしてないようですが，OpenCV は NumPy に依存しているので，NumPy も自動的にインストールされます．
NumPy のインストールは

```
pip3 install numpy
```

でできますが，今の場合は `Requirement already satisfied` と言われるはずです．
