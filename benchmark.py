import timeit

import pandas as pd
import matplotlib.pyplot as plt
from wasmer import engine, Store, Module, Instance
import wasmer_compiler_cranelift
import wasmer_compiler_llvm

import collatznumba
import collatzpythran
import collatzcython
import collatzpyo3


store_cranelift = Store(engine.JIT(wasmer_compiler_cranelift.Compiler))
module_cranelift = Module(store_cranelift, open("collatzwasm_bg.wasm", "rb").read())
instance_cranelift = Instance(module_cranelift)
collatz_cranelift = instance_cranelift.exports.collatz

store_llvm = Store(engine.JIT(wasmer_compiler_llvm.Compiler))
module_llvm = Module(store_llvm, open("collatzwasm_bg.wasm", "rb").read())
instance_llvm = Instance(module_llvm)
collatz_llvm = instance_llvm.exports.collatz

cases = {
    "Numba": collatznumba.collatz,
    "Pythran": collatzpythran.collatz,
    "Cython": collatzcython.collatz,
    "PyO3": collatzpyo3.collatz,
    "Wasmer (Cranelift)": collatz_cranelift,
    "Wasmer (LLVM)": collatz_llvm,
}

# Warm up and check that results agree
assert len({c(200) for c in cases.values()}) == 1

fig, ax = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.35)
ax[0].set_ylabel("Time [s]")
for i, (target, repeats, description) in enumerate(
    ((10, 1000000, "Small"), (200, 400, "Large"))
):
    ax[i].set_title(f"Problem size: {description}")
    res = []
    for name, case in cases.items():
        time = timeit.timeit(lambda: case(target), number=repeats)
        res.append([name, time])
    pd.DataFrame(res, columns=["name", "Time"]).set_index("name").plot.bar(
        ax=ax[i], legend=False
    )
    ax[i].set_xlabel("")

fig.subplots_adjust(bottom=0.32)
plt.savefig("result.png", dpi=200)
