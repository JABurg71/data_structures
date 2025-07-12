// ============================================
// Different Ways to Create and Use Arrays
// ============================================

// 1. Using square brackets
let fruits = ["apple", "banana", "cherry"];

// 2. Using Array constructor
let numbers = new Array(1, 2, 3, 4);

// 3. Creating an empty array and pushing
let colors = [];
colors.push("red");
colors.push("blue");

// 4. Creating an array of length n
let tenZeros = Array(10).fill(0);

// 5. Using Array.from
let squares = Array.from({ length: 5 }, (_, i) => i * i);

// 6. Using spread and map
let doubleValues = [...Array(5)].map((_, i) => i * 2);

// 7. Nested arrays (2D array)
let matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
];

// --------------------------------------------
// Common Array Operations
// --------------------------------------------

// Add/remove from end
fruits.push("date");
let last = fruits.pop();

// Add/remove from beginning
fruits.unshift("avocado");
let first = fruits.shift();

// Splice: insert/delete at specific index
fruits.splice(1, 0, "blueberry"); // insert at index 1
fruits.splice(2, 1); // remove 1 item at index 2

// Slice: create a shallow copy
let someFruits = fruits.slice(0, 2);

// Indexing
let secondFruit = fruits[1];

// Check presence
let hasApple = fruits.includes("apple");

// Find index
let index = fruits.indexOf("cherry");

// Iteration
fruits.forEach((fruit, index) => {
  console.log(`${index}: ${fruit}`);
});

// Map/filter/reduce
let evenNumbers = numbers.filter(n => n % 2 === 0);
let doubled = numbers.map(n => n * 2);
let total = numbers.reduce((acc, val) => acc + val, 0);

// Sorting
let sorted = [...numbers].sort((a, b) => a - b);

// Reversing
let reversed = [...numbers].reverse();

// Destructuring
let [a, b, ...rest] = numbers;

// Flattening nested arrays
let flat = matrix.flat();

// Zipping (via map)
let names = ["Alice", "Bob"];
let scores = [90, 85];
let zipped = names.map((name, i) => [name, scores[i]]);

// --------------------------------------------
// Console Outputs (for demo)
// --------------------------------------------
console.log("Fruits:", fruits);
console.log("Numbers:", numbers);
console.log("Squares:", squares);
console.log("Some fruits:", someFruits);
console.log("Even numbers:", evenNumbers);
console.log("Zipped:", zipped);
console.log("Matrix:", matrix);
console.log("Flat matrix:", flat);

