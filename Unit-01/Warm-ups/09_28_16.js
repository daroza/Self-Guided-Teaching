// REVERSE OR ROTATE
// The input is a string str of digits. Cut the string into chunks of size sz (ignore the last chunk if its size is less than sz).
//
// If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse it; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
//
// If sz is <= 0 or if str is empty return ""
// If sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
// Examples:
// revrot("123456987654", 6) --> "234561876549"
// revrot("123456987653", 6) --> "234561356789"
// revrot("66443875", 4) --> "44668753"
// revrot("66443875", 8) --> "64438756"
// revrot("664438769", 8) --> "67834466"
// revrot("123456779", 8) --> "23456771"
// revrot("", 8) --> ""
// revrot("123456779", 0) --> ""

function revrot(digits, sz) {
	if (sz <= 0 || digits.length === 0) {
		return "";
	}
	let splitDigits = digits.split("");
	let chunks = [];
	while (splitDigits.length >= sz) {
		chunks.push(splitDigits.splice(0, sz));
	}
	chunks = chunks.map((chunk) => {
		let cubeSum = chunk.reduce((acc, c) => {
			return acc + Math.pow(c, 3);
		}, 0);

		if (cubeSum % 2 === 0) {
			chunk.reverse();
		} else {
			let shiftValue = chunk.shift();
			chunk.push(shiftValue);
		}

		return chunk;
	}).reduce((acc, c) => {
		return acc.concat(c)
	}, []).join("");

	return chunks;
}

console.log(revrot("123456987654", 6) + " --> 234561876549");
console.log(revrot("123456987653", 6) + " --> 234561356789");
console.log(revrot("66443875", 4) + " --> 44668753");
console.log(revrot("66443875", 8) + " --> 64438756");
console.log(revrot("664438769", 8) + " --> 67834466");
console.log(revrot("123456779", 8) + "--> 23456771");
console.log(revrot("", 8) + "--> ''");
console.log(revrot("123456779", 0) + " --> ''");

