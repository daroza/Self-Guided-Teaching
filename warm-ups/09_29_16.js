// SMS Shortener
// ============
// SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long. Your task is to shorten the message to 160 characters, starting from end, by replacing spaces with camelCase, as much as necessary.
//
// For example:
//
// Original message (169 chars):
//
// 	No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.
//
// Shortened message (160 chars):
//
// 	No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.

function smsShortener(message) {
	let charCount = message.length;
	if (charCount < 161) { return message; }
	let words = message.split(" ");
	let excessCount = charCount-160;
	let camelCaseWords = words.splice(words.length - excessCount, excessCount)
		.map((word) => {
			return word[0].toUpperCase() + word.slice(1);
		})
		.join("");
	let output = words.join(" ") + camelCaseWords;
	return output;
}


let input = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it."
let output = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt."

console.log(`
input: ${input}

expected output: ${output}

actual output: ${smsShortener(input)}
		`.trim());

console.log("\n");

let input2 = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that w."
let output2 = "No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that w."

console.log(`
input: ${input2}

expected output: ${output2}

actual output: ${smsShortener(input2)}
		`.trim());
