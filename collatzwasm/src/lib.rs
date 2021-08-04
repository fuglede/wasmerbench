use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn collatz(target: u32) -> u32 {
    let mut start = 1;
    loop {
        let mut i = start;
        let mut steps = 0;
        while i != 1 {
            i = if i % 2 == 0 { i / 2 } else { 3 * i + 1 };
            steps += 1;
        }
        if steps == target {
            return start;
        }
        start += 1;
    }
}
