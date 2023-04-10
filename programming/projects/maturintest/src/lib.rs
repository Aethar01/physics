use pyo3::prelude::*;
use std::time::Instant;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn facloop(mut fac: usize, mut i: usize) -> PyResult<Vec<(usize, usize)>> {
    let mut result: Vec<(usize, usize)> = Vec::new();
    let now = Instant::now();
    while i < 10 {
        fac = fac * i;
        result.push((i ,fac));
        i=i+1; 
    }
    let elapsed = now.elapsed();
    println!("Rust Elapsed: {:.2?}", elapsed);
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn maturintest(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(facloop, m)?)?;
    Ok(())
}
