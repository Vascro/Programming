use std::io;
fn main() {
    println!("What is your name?");
    let mut name: String = String::new();
    let greeting: &str = "Nice to meet you";
    io::stdin().read_line(&mut name)
        .expect("Input Missing!");
    println!("Hello {}! {}", name.trim_end(), greeting);
}
