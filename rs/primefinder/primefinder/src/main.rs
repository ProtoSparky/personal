fn main() {
    //list of numbers to check for primes
    let numbers: [i32; 4] = [10, 69, 420, 300];
    let numbers_length = numbers.len(); 
    println!("We are checking the numbers {:?}", numbers); 
    let mut numbers_checked: Vec<i32> = Vec::with_capacity(0); 

    let mut pointer = 0; 
    while pointer < numbers_length{
        let current_number = numbers[pointer]; 
        let is_prime = prime_checker(current_number.try_into().unwrap()); //we check if the selected number is prime or not
        if is_prime{
            numbers_checked.push(1);
            println!("The number {}", current_number.to_string() + " is prime"); 
        }
        else{
            numbers_checked.push(0); 
            println!("The number {}", current_number.to_string() + " is not prime ):"); 
        }

        pointer += 1; 
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




