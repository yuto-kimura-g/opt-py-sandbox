# HIGHS

## LOG
```console
$ uv add highspy

$ cd ~/dev/build

$ git clone https://github.com/ERGO-Code/HiGHS.git

$ cmake -S. -B build -DCMAKE_INSTALL_PREFIX=/Users/yuto/.local

$ cmake --build build --parallel

$ cmake --install build

$ cd build
$ ctest
Test project /Users/yuto/dev/build/HiGHS/build
    Start 1: cxx_examples_call_highs_from_cpp
1/2 Test #1: cxx_examples_call_highs_from_cpp .......   Passed    0.41 sec
    Start 2: c_examples_call_highs_from_c_minimal
2/2 Test #2: c_examples_call_highs_from_c_minimal ...   Passed    0.19 sec

100% tests passed, 0 tests failed out of 2

Total Test time (real) =   0.61 sec

$ highs --version
HiGHS version 1.9.0 Githash bdf95f2e0. Copyright (c) 2025 HiGHS under MIT licence terms
```
とりあえずインストールできた

python-mipから使ってみる
```console
$ uv run python src/run-mip.py
Traceback (most recent call last):
  File ".../opt-py-sandbox/src/run-mip.py", line 8, in <module>
    m = Model(solver_name="HIGHS")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../opt-py-sandbox/.venv/lib/python3.11/site-packages/mip/model.py", line 95, in __init__
    self.solver = mip.gurobi.SolverGurobi(self, name, sense)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../opt-py-sandbox/.venv/lib/python3.11/site-packages/mip/gurobi.py", line 369, in __init__
    raise InterfacingError(
mip.exceptions.InterfacingError: Gurobi environment could not be loaded, check your license.
```
あれ？なぜかGurobiが呼ばれている
`.venv/lib/python3.11/site-packages/mip/model.py` を見ると、そもそもHIGHSが無い？
GitHubを見ると、mipでhighsが使えるのはstableじゃなくて1.16-preだった(2025/2/22現在のlatest stableは1.15)。
> ref: https://github.com/coin-or/python-mip/releases/tag/1.16-pre

pyproject.tomlを編集してuv syncする

```console
$ uv run python src/run-mip.py
An error occurred while loading the HiGHS library:
not enough values to unpack (expected 1, got 0)
Traceback (most recent call last):
  File ".../opt-py-sandbox/src/run-mip.py", line 8, in <module>
    m = Model(solver_name="HIGHS")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../opt-py-sandbox/.venv/lib/python3.11/site-packages/mip/model.py", line 97, in __init__
    self.solver = mip.highs.SolverHighs(self, name, sense)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../opt-py-sandbox/.venv/lib/python3.11/site-packages/mip/highs.py", line 690, in __init__
    raise FileNotFoundError(
FileNotFoundError: HiGHS not found.Please install the `highspy` package, orset the `PMIP_HIGHS_LIBRARY` environment variable.
Exception ignored in: <function SolverHighs.__del__ at 0x1032cde40>
Traceback (most recent call last):
  File ".../opt-py-sandbox/.venv/lib/python3.11/site-packages/mip/highs.py", line 728, in __del__
    self._lib.Highs_destroy(self._model)
    ^^^^^^^^^
```
エラー文で言われたので、CBCと同様にPMIP_HIGHS_LIBRARYを設定する(~/.zshrc)
`export PMIP_HIGHS_LIBRARY="$HOME/.local/lib/libhighs.dylib"`

```console
$ uv run python src/run-mip.py
m.solver_name='HIGHS'
Running HiGHS 1.9.0 (git hash: bdf95f2e0): Copyright (c) 2025 HiGHS under MIT licence terms
Coefficient ranges:
  Matrix [1e+00, 1e+00]
  Cost   [1e+00, 1e+00]
  Bound  [1e+00, 1e+00]
  RHS    [1e+00, 1e+00]
Presolving model
0 rows, 0 cols, 0 nonzeros  0s
0 rows, 0 cols, 0 nonzeros  0s
Presolve : Reductions: rows 0(-2); columns 0(-2); elements 0(-4) - Reduced to empty
Solving the original LP from the solution after postsolve
Model status        : Optimal
Objective value     :  1.0000000000e+00
Relative P-D gap    :  0.0000000000e+00
HiGHS run time      :          0.00
```
python-mip経由でも動いた

## refs
- https://github.com/ERGO-Code/HiGHS
- https://github.com/coin-or/python-mip/releases/tag/1.16-pre
