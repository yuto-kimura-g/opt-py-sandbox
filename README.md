# opt-py-sandbox

Mathematical Optimization with Python: sandbox

## Software
### Modeler
- `COIN-OR/PuLP`
  - GitHub: https://github.com/coin-or/pulp
  - docs: https://coin-or.github.io/pulp/
- `COIN-OR/python-mip`
  - GitHub: https://github.com/coin-or/python-mip
  - docs: https://python-mip.com/
- `PySCIPOpt`
  - GitHub: https://github.com/scipopt/PySCIPOpt
  - docs: https://pyscipopt.readthedocs.io/en/latest/
- `DOcplex`
  - docs: https://ibmdecisionoptimization.github.io/docplex-doc/
- `gurobipy`
  - docs: https://docs.gurobi.com/current/
### Solver
- `COIN-OR/Cbc`
  - GitHub: https://github.com/coin-or/Cbc
- `HiGHS`
  - GitHub: https://github.com/ERGO-Code/HiGHS
  - docs: https://highs.dev/
- `SCIP`
  - GitHub: https://github.com/scipopt/scip
  - docs: https://scipopt.org/
- `IBM ILOG CPLEX`
  - docs: https://www.ibm.com/docs/en/icos/
- `Gurobi`
  - docs: https://docs.gurobi.com/current/

## Verify
### Environment
- Arm64 architecture (Apple Silicon M4 Pro chip)
- homebrew
- Python@3.11
- uv (see also [`pyproject.toml`](./pyproject.toml))

### Result
|Modeler|Solver|Status|
|:-:|:-:|:-:|
|`pulp`|`cbc`|o|
|`pulp`|`highs`|o|
|`pulp`|`scip`|?|
|`pulp`|`cplex`|o|
|`pulp`|`gurobi`|o|
|---|---|---|
|`mip`|`cbc`|o|
|`mip`|`highs`|o|
|`mip`|`scip`|x *1|
|`mip`|`cplex`|x *1|
|`mip`|`gurobi`|o|
|---|---|---|
|`pyscipopt`|`scip`|?|
|`docplex`|`cplex`|o *2|
|`gurobipy`|`gurobi`|o|

- o: 正常に動作した
- x: エラーが発生した
- ?: 未検証
- *1: `we plan to support CPLEX/SCIP in the future` (https://github.com/coin-or/python-mip/blob/eb3dd63cf2e6dd632ec645997c2dc49e01af3e2b/mip/constants.py#L26, 2025/2/22閲覧)
- *2: pipの`cplex`が`<=python@3.10`な上に、uvだとexternally nmanagedと言ってくるので、brewでglobalに入れたpython@3.10で実行する必要がある
