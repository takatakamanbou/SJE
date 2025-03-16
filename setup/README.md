# Python プログラミング環境のセットアップ



ここでは，[高橋担当の2025年度の「数理情報演習」](https://www-tlab.math.ryukoku.ac.jp/wiki/?SJE/2025)（以下SJE2025）の授業のための Python プログラミング環境をセットアップする方法について説明します．

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

次のように `pip` コマンドを実行（PowerShell 上で実行すればok）することで，これらをインストールすることができます．

**【注意】この文書で説明している手順で macOS に Python をインストールした場合， `pip` ではなく `pip3` を使います．以下読みかえてね．**

```
pip install opencv-python
```

一見 OpenCV しかインストールしてないようですが，OpenCV は NumPy に依存しているので，NumPy も自動的にインストールされます．
NumPy のインストールは

```
pip install numpy
```

でできますが，今の場合は `Requirement already satisfied` と言われるはずです．

### Jupyter Notebook を扱えるようにする

Jupyter Notebook というのは，ブラウザを利用して Python のコードを書いたり実行したりできる仕組みです．「データ分析」などの授業で Google Colaboratory (Colab) という似たようなものを触ったことがあるはずです．Colab はクラウドの仮想Linuxマシン上で実行されるものでしたが，Jupyter Notebook の方は自分のPCにインストールした Python 環境でプログラムが実行されます．

(1) Jupyter をインストールする
```
pip install jupyter
```

(2) notebook ファイルを入手

1. 以下のリンクをクリックしてブラウザで開く．
1. その画面の右上の方にダウンロードボタン（カーソルを重ねると「Download raw file」と表示される）があるので押す．
1. `ex00.ipynb` というファイルがダウンロードされるはず．`SJE`ディレクトリへ移動させておきましょう．

[ex00.ipynb](../ex00.ipynb)

(3) VSCode で開いてみる

入手したファイルを SJE フォルダに置いて VSCode で開きましょう．はじめてこのファイルを開いたときは，次のように設定が必要です．

1. ウィンドウ右上に「カーネルの選択」という表示があるのでクリック > 「拡張機能を探す」というような選択肢を選ぶ．
1. 拡張機能がインストールされる．さきほど「カーネルの選択」と表示されていた箇所をクリックすると，インストールした Python が選択肢に出てくるはずなので，それを選択．
1. 表示が「Python 3.13.2」のようになるはず．

上記の設定ができたら，この notebook に書いてあることを実行してみましょう．うまくいかないときは takataka に尋ねてね．

