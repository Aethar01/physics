use rand::Rng;
use std::thread;
use std::time::Instant;

#[derive(Copy, Clone, Debug)]
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
    for _i in 0..134217728 {
        _quads.insert(_i, Quad {a: rng.gen_range(1.0..100.0), b: rng.gen_range(1.0..100.0), c: rng.gen_range(1.0..100.0), r1: 0.0, r2: 0.0})
    }
    _quads
}

fn split_at(_v: Vec<Quad>, _i: usize) -> (Vec<Quad>, Vec<Quad>) {
    let _n = _v.len();
    assert!(_i < _n);

    let mut _a: Vec<Quad> = Vec::new();
    let mut _b: Vec<Quad> = Vec::new();
    for _k in 0.._i {
        _a.insert(_k, _v[_k]);
    }
    let mut _x = 0;
    for _k in _i.._n {
        _b.insert(_x, _v[_k]);
        _x += 1;
    }
    (_a, _b)
}

fn quadratic_eq(mut _quads1: Vec<Quad>, mut _quads2: Vec<Quad>) {
    let len1 = _quads1.len();
    let len2 = _quads2.len();
    let handle = thread::spawn(move || {
        for _i in 0..len1 {
            _quads1[_i].r1 = -_quads1[_i].b + ((_quads1[_i].b * _quads1[_i].b - 4.0 * _quads1[_i].a * _quads1[_i].c).sqrt()) / (2.0 * _quads1[_i].a);
            // thread::sleep(Duration::from_millis(1));
        }
    }); 
    for _i in 0..len2 {
        _quads2[_i].r2 = -_quads2[_i].b - ((_quads2[_i].b * _quads2[_i].b - 4.0 * _quads2[_i].a * _quads2[_i].c).sqrt()) / (2.0 * _quads2[_i].a);
        // thread::sleep(Duration::from_millis(1));
    }
    handle.join().unwrap()
}

fn main() {
    let a = fill_quads();
    let _halfquadslen = a.len() / 2;
    let (_quads1, _quads2) = split_at(a, _halfquadslen);
    let now = Instant::now();
    {
    quadratic_eq(_quads1, _quads2);
    }
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed)
}
