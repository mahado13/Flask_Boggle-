console.log("The File is loading!")

/*
- Author: Mahad Osman
- Date: Nov 26, 2022
- Assignment: Flask Boggle
*/


// Setting out vars once.
const $guess_form = $(".guess-from")
const $result = $(".result")
const $highscore = $(".highscore")
const $numOfPlays = $(".numberOfPlays")
const $score = $(".score")
const $guess = $(".guess")
const wordlist = new Set();
let $timer = 20
let score =0

/**
 * - Our handleclick function that:
 *  - shall receive our users input
 *  - make an axios request to check our word
 *  - based on the response shall either return feedback, or increment our score 
 *  - it shall handle checking for duplicate correct gussess
 */
async function handle_Submit(evt){
    evt.preventDefault();
    let guess = $guess.val()
    //console.log($guess.val())

    if (wordlist.has(guess)){
        $result.text(`${guess} has already been counted!!`)
    }

    const res = await axios.get("/word_check", {params: {guess: guess}});
    console.log(res.data)

    if (res.data.response === "not-on-board"){
        $result.text(`${guess} is not on the board`)
    } else if(res.data.response === "not-word"){
        $result.text(`${guess} is not a word`)
    }else{
        $score.text(`Score: ${res.data.score}`)
        wordlist.add(guess)
        score = res.data.score
        return score
    }

}

//Attaching our on click to the submit button
$guess_form.on("submit", handle_Submit)

//Setting our countdown
gametimer = setInterval(countDown, 1000);

//Our count down function. When it reaches zero is will handle ending the game calling the method for final scoring.
async function countDown(){
    $timer -= 1;
    console.log($timer)
    if ($timer === 0){
        clearInterval(gametimer)
        console.log("Game ending!")
        $guess_form.off("submit")
        $guess_form.hide();
        $result.text(`The game is over!`)
        await finalScore();
    }
}
/**
 * - Refactored to store the score on the backend as well 
 * - Although I've kept the working post example 
 * - It shall retrieve our highscore and number of plays via our backend and update our page text.
 */
async function finalScore(){
    // const res = await axios.post("/final_score",{score: score});
    // //console.log(res)

    const response = await axios.get("/final_score")
    console.log(response.data)

    $highscore.text(`Highscore: ${response.data.highscore}`)
    $numOfPlays.text(`Number of Plays: ${response.data.numofplays}`)

}

