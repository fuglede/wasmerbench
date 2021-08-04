use pyo3::prelude::*;

#[pyfunction]
pub fn collatz(target: usize) -> PyResult<usize> {
    let mut start = 1;
    loop {
        let mut i = start;
        let mut steps = 0;
        while i != 1 {
            i = if i % 2 == 0 { i / 2 } else { 3 * i + 1 };
            steps += 1;
        }
        if steps == target {
            return Ok(start);
        }
        start += 1;
    }
}

#[pymodule]
fn collatzpyo3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(collatz, m)?)?;

    Ok(())
}
