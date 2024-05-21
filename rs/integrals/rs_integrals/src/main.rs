fn main() {/*
    let mut start_num = 0;
    
    while true {
        start_num +=1;/*
        let string = start_num.to_string();
        println!("{}",string);*/


    }*/
    println!("{}", prime_checker(17))




}
fn prime_checker(input:u32) -> bool{ //u32 means the number is a 32bit unsigned intiger. "->bool means the return is expected to be a boolean"
    let mut prime_flag = false;
    if input <= 1{
        prime_flag = false; //number is not prime
    }
    else if input < 1{
        for prime_pointer in 2..input { //x..y works the same way as a python range(x,y), generates a list of numbers from x to y
            if (input/prime_pointer) == 0 {
                //number factor found, set prime_flag to true
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
