fn main() {
    println!("Hello, world!");

    // Define the function to integrate
    let func = |x: f64| -> f64 { x.powi(2) };

    // Define the range [a, b]
    let a = 0.0;
    let b = 1.0;

    // Define the number of steps
    let steps = 1000;

    // Calculate the width of each step
    let step_width = (b - a) / steps as f64;

    // Initialize the sum
    let mut total_area = 0.0;

    // Loop through each step
    for i in 0..steps {
        // Calculate the x value for this step
        let x = a + (i as f64 * step_width);

        // Add the area of the rectangle formed by this step to the total
        total_area += func(x) * step_width;
    }

    println!("The approximate integral of x^2 from {} to {} is {}", a, b, total_area);
}
