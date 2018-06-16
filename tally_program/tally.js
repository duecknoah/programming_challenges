/* [2018-05-14] Challenge #361 [Easy] Tally Program
 * Solution
 * by Noah Dueck
 *
 * DESCRIPTION
 * 5 Friends (let's call them a, b, c, d and e) are playing 
 * a game and need to keep track of the scores. Each time 
 * someone scores a point, the letter of his name is typed 
 * in lowercase. If someone loses a point, the letter of his 
 * name is typed in uppercase. Give the resulting score from 
 * highest to lowest.
 *
 * LINK
 * https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
 */

function getTally(series) {
	let t = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}; 

    for (var key in series) {
        let lChar = series[key].toLowerCase();
        t[lChar] = (series[key] === lChar) ? t[lChar] + 1 : t[lChar] - 1;
    }

    return t;
}

function printTally(tally) { 
	var sortable = [];
	for (var key in tally) {
		sortable.push([key, tally[key]]);
	}
	sortable.sort(function(a, b) {
		return b[1] - a[1];
	});
	console.log(sortable);
}

printTally(getTally('abcde'));
printTally(getTally('dbbaCEDbdAacCEAadcB'));
printTally(getTally("EbAAdbBEaBaaBBdAccbeebaec"));
