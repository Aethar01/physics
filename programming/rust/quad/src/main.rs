use rand::Rng;
#[derive(Debug)]
struct Quad {
    a: f32,
    b: f32,
    c: f32,
    r1: f32,
    r2: f32,
}

fn fill_quads() -> Vec<Quad> {
    let mut rng = rand::thread_rng();
    let mut _quads: Vec<Quad> = Vec::new();
    for _i in 0..134217727 {
        _quads.insert(_i, Quad {a: rng.gen_range(1.0..100.0), b: rng.gen_range(1.0..100.0), c: rng.gen_range(1.0..100.0), r1: 0.0, r2: 0.0})
    }
    _quads
}

fn quadratic_eq(mut _quads: Vec<Quad>) {
    for _i in 0..134217727 {
        _quads[_i].r1 = -_quads[_i].b + ((_quads[_i].b * _quads[_i].b - 4.0 * _quads[_i].a * _quads[_i].c).sqrt()) / (2.0 * _quads[_i].a);    
        _quads[_i].r2 = -_quads[_i].b - ((_quads[_i].b * _quads[_i].b - 4.0 * _quads[_i].a * _quads[_i].c).sqrt()) / (2.0 * _quads[_i].a);
    }
}

fn main() {
    use std::time::Instant;
    let a = fill_quads();
    let now = Instant::now();
    {
    quadratic_eq(a);
    }
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed)
}
