use std::time::{Duration, Instant}; //used for operations pr second counter
use std::thread::sleep; //-||-

fn main() {
    loop{
        start_prime();
    }
}
fn prime_checker(input:u32) -> bool{ //u32 means the number is a 32bit unsigned intiger. "->bool means the return is expected to be a boolean"
    let mut prime_flag = false;
    if input <= 1{
        prime_flag = false; //number is not prime
    }
    else{
        for prime_pointer in 2..input { //x..y works the same way as a python range(x,y), generates a list of numbers from x to y
            if (input % prime_pointer) == 0 {
                //number is not a factor found, set prime_flag to true
                prime_flag = true; 
                break; 
            }
        }
    }

    if prime_flag == true{
        return true;
    }
    else{
        return false; 
    }
}

fn start_prime(){
    let start_time = Instant::now(); // Mark the start time
    let mut iterations = 0; // Counter for the number of iterations

    let mut start_num = 0;    
    loop { //use loop instead of a while true to remove compiler warnings
        start_num +=1;
        let string = start_num.to_string();
        let boolean = prime_checker(start_num).to_string(); //converts bool to String
        let str_slice: &str = boolean.as_str(); //converts String to &str




        // Perform your operations here
        // For demonstration, we'll just increment the counter
        iterations += 1;

        // Check if approximately one second has passed
        if start_time.elapsed().as_secs_f32() >= 1.0 {
            println!("Iterations per second: {}", iterations);
            break;
        }
    }
    
}