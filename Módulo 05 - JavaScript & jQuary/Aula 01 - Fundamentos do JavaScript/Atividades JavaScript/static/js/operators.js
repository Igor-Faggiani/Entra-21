// Exercise 1:

// What are the final values of all variables a, b, c and d after the code below?

// let a = 1, b = 1;

// let c = ++a; // 2
// let d = b++; // 1

// alert (c);
// alert (d);

// ---------------------------------------------------------------- //

// Exercise 2:

// What are the values of A and X after the code below?

// let a = 2;

// let x = alert(1 + (a *= 2)); // Result: 5

// ---------------------------------------------------------------- //

// Exercise 3:

// What are results of these expressions?

"" + 1 + 0 // Result: "10"
"" - 1 + 0 // Result: -1
true + false // Result: 1
6 / "3" // Result: 2
"2" * "3" // Result: 6
4 + 5 + "px" // Result: "9px"
"$" + 4 + 5 // Result: "$45"
"4" - 2 // Result: 2
"4px" - 2 // Result: NaN
"  -9  " + 5 // Result: "  -9  5"
"  -9  " - 5 // Result: -14
null + 1 // Result: 1
undefined + 1 // Result: NaN
" \t \n" - 2 // Result: -2

// ---------------------------------------------------------------- //

// Exercise 4:

// Here’s a code that asks the user for two numbers and shows their sum.

// It works incorrectly. The output in the example below is 12 (for default prompt values).

// Why? Fix it. The result should be 3.

// let a = prompt("First number?", 1);
// let b = prompt("Second number?", 2);

// alert(a + b); // 12

let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(+a + +b); // 12