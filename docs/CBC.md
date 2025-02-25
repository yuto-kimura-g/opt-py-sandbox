# CBC

## LOG
ボツ
```console
$ brew tap coin-or-tools/coinor
$ brew list cbc
$ brew install cbc
$ which cbc
$ cbc
# 無理だった
$ brew uninstall --zap cbc
```

成功
```console
$ cd ~/dev/build
$ git clone git@github.com:coin-or/coinbrew.git
$ cd coinbrew
$ ./coinbrew --help
$ ./coinbrew fetch build Cbc@master --prefix=/Users/yuto/.local --parallel-jobs=8 --no-prompt --tests=none
# prefixは$HOMEではなくフルパスで指定しないとだめだった
```
pathを通す
```
# ~/.zshrc
# coin-or/cbc
export PMIP_CBC_LIBRARY="$HOME/.local/lib/libCbc.dylib"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/.local/lib"
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$HOME/.local/lib"
```
**TODO: LD_LIBRARY_PATHとDYLD_LIBRARY_PATHの違いを調べる**

## refs
- https://github.com/coin-or/python-mip/blob/master/docs/install.rst#using-your-own-cbc-binaries-optional
- https://github.com/coin-or/Cbc
- https://github.com/coin-or/coinbrew
- https://formulae.brew.sh/formula/cbc
- https://qiita.com/nariaki3551/items/ea1117afb7f8ffbf7e90
