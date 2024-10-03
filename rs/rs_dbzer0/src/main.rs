fn main() {
    let mut counter:i128 = 0; 
    let mut tmp:i128 = 0; 
    let skip_every = 100000000; 
    loop{
        counter += 1;
        tmp += 1; 
        if tmp > skip_every {
            tmp = 0; 
            println!("The current number is {}", (counter / 30)*counter);
        }
    }
}
