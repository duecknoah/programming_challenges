/* [2018-06-18] Challenge #364 [Easy] Create a Dice Roller
 * Create a dice roller that is based off D&D
 *
 * Link: https://old.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
 */

function getOutput(input) {
	var inputNums = input.split('d');
	var sum = 0;
	var results = [];

	for (var i = 0; i < inputNums[0]; i ++) {
		let val = (Math.random() * inputNums[1]) + 1 | 0
		sum += val;
		results.push(val);
	}

	console.log('%s: %s', sum, results);
}

rolls = ['5d12', '6d4', '1d2', '1d8', '3d6', '4d20', '100d100']
for (i in rolls)
	getOutput(rolls[i]);