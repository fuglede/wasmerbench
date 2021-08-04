# Wasmer as an alternative to Numba/Pythran/Cython/PyO3

||Language|Windows support|No compilation|No bundled runtime|Platform-independent builds|Small deployment|Just worked|Performance|
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|Numba|Python|✔️|✔️|❌|✔️|✔️|⚠|⚠|️
|Pythran|Python|✔️|❌|✔️|❌|⚠️|❌|✔|
|Cython|Cython|✔️|❌|✔️|❌|⚠️|✔|✔|
|PyO3|Rust|✔️|❌|✔️|❌|❌|✔|✔|
|Wasmer (Cranelift)|Multiple|✔️|❌|❌|✔️|✔|✔|❌|
|Wasmer (LLVM)|Multiple|❌|❌|❌|✔️|✔|✔|✔|