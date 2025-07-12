// ============================================
// Different Ways to Create and Use Maps
// ============================================

// 1. Using plain object literal
let person = {
	name: "Alice",
	age: 30,
	city: "New York",
};

// 2. Using Object constructor
let car = new Object();
car.make = "Toyota";
car.model = "Camry";
car.year = 2020;

// 3. Creating object from entries
let entries = [["a", 1], ["b", 2]];
let objFromEntries = Object.fromEntries(entries);

// 4. Using Object.assign to merge
let base = { a: 1 };
let extended = Object.assign({}, base, { b: 2 });

// 5. Using the ES6 Map object (for ordered keys and any key type)
let grades = new Map();
grades.set("Alice", 95);
grades.set("Bob", 88);
grades.set("Charlie", 92);

// --------------------------------------------
// Access and Modification
// --------------------------------------------

// Access object value
let name = person.name; // Dot notation
let age = person["age"]; // Bracket notation

// Update or add
person.email = "alice@example.com";
person.age = 31;

// Delete
delete person.city;

// Access Map value
let bobGrade = grades.get("Bob");

// Check if key exists
let hasCharlie = grades.has("Charlie");

// Delete from Map
grades.delete("Alice");

// Iterating over object
console.log("Iterating object:");
for (let key in person) {
	console.log(`${key}: ${person[key]}`);
}

// Iterating over Map
console.log("\nIterating Map:");
for (let [key, value] of grades) {
	console.log(`${key}: ${value}`);
}

// Get object keys and values
let keys = Object.keys(person);
let values = Object.values(person);
let entriesList = Object.entries(person);

// Merge objects (ES6+)
let combined = { ...person, country: "USA" };

// Nested objects
let users = {
	alice: { age: 30, email: "alice@example.com" },
	bob: { age: 25, email: "bob@example.com" },
};

let bobEmail = users.bob.email;

// --------------------------------------------
// Console Outputs (for demo)
// --------------------------------------------
console.log("\nPerson:", person);
console.log("Car:", car);
console.log("Object from entries:", objFromEntries);
console.log("Merged object:", combined);
console.log("Grades Map:", grades);
console.log("Bob's grade:", bobGrade);
console.log("Keys in person:", keys);
console.log("Values in person:", values);
console.log("Nested users:", users);
console.log("Bob's email:", bobEmail);
