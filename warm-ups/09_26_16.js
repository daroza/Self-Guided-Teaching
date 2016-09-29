"use strict";
/*
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
*/

// 1. Normalize string
// 2. Map each letter to a numeric value
// 3. Increment the letter value in the map when duplicate is reached.
// 4. Reduce the keys of the object to string based on values.

function replaceDuplicates(str) {
	let normalized = str.toLowerCase();
	let charMap = {};

	for (let idx = 0; idx < normalized.length; idx++) {
		let currentChar = normalized[idx];
		if (!charMap.hasOwnProperty(currentChar)) {
			charMap[currentChar] = 1;
		} else {
			charMap[currentChar]++;
		}
	}

	let converted = normalized.split("").reduce((acc, ch) => {
	    return acc + ((charMap[ch] > 1) ? ")" : "(");
	}, "");

	return converted;
}

let input = process.argv[2] || "recede";

console.log(`${input} => ${replaceDuplicates(input)}`);
