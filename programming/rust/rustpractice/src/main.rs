// const MAXIMUM_NUMBER: u8 = 20;
// enum Direction {
//     Up,
//     Down,
//     Left,
//     Right
// }

fn main() {
    // let mut x = 45;

    // println!("{}", x);

    // x = 60;

    // println!("{}", x);
    
    //________________________________________________
    // let x: u64 = 45; // u64
    // let f: f32 = 6.7; // f32
    // let b: bool = false; //bool
    //________________________________________________
    // let n = 55;

    // if n == 30 {
    //     println!("number is equal to 30!");
    // }
    // else if n < 50 {
    //     println!("num less than 50");
    // }
    // else {
    //     println!("num greater than 50");
    // }
    // ________________________________________________
    // let mut n = 0;

    // loop {
    //     n += 1;

    //     if n == 7 {
    //         continue;
    //     }

    //     if n > 10 {
    //         break;
    //     }

    //     println!("the value of n is {}", n)
    // }
    // ________________________________________________

    // let mut n = 1;

    // while n <=50 {
    //     if n % 5 == 0 {
    //         println!("n is {}", n)
    //     }

    //     // println!("n is {}", n);
        
        
    //     n += 1;

    
    // ________________________________________________

    // let animals = vec!["Rabbit", "Dog", "Cat"];

    // for (index, i) in animals.iter().enumerate() {
        
    //     println!("The index is {} animal name is {}", index, i);
    // }

    // ________________________________________________

    // let playerdirection:Direction = Direction::Up;

    // match playerdirection {
    //     Direction::Up => println!("We are heading up"),
    //     Direction::Down => println!("We are heading down"),
    //     Direction::Left => println!("We are heading left"),
    //     Direction::Right => println!("We are heading right"),
    // }

    // ________________________________________________
    
    // for n in 1..MAXIMUM_NUMBER {
    //     println!("{}", n);
    // }
    
    // ________________________________________________

    // let tup1 = (45, 6.7, "computer");
    // let (a,b,c) = tup1;

    // println!("a is {}", a);
    // println!("b is {}", b);
    // println!("c is {}", c);

    // ________________________________________________
    
    // let x = 10;
    
    // {

    //     let y =5;

    //     println!("x: {} y: {}", x, y);

    // }

    // ________________________________________________

    let mut x = 0;
    for i in x..10 {
        println!("at {} number is {}", i, x);
        x += 1
    }
    
}
// fn print_numbers_to(num: u32) {
//     for i in 1..num {
//         if is_even(i) {
//             println!("{} is even", i);
//         }
//         else {
//             println!("{} is odd", i);
//         }
//     }
// }

// fn is_even(num: u32) -> bool {
//     return num % 2 == 0;
// }