console.log("The File is loading!")

const $guess_form = $(".guess-from")
const $result = $(".result")
const $score = $(".score")
//const $timer = 60

async function handle_Submit(evt){
    evt.preventDefault();
    const $guess = $(".guess")
    let guess = $guess.val()
    //console.log($guess.val())

    const res = await axios.get("/word_check", {params: {guess: guess}});
    console.log(res.data)

    if (res.data.response === "not-on-board"){
        $result.text(`${guess} is not on the board`)
    } else if(res.data.response === "not-word"){
        $result.text(`${guess} is not a word`)
    }else{
        console.log($score.text(`Score: ${res.data.score}`))
    }

}
// guess = setInterval($guess_form.on("submit", handle_Submit), 60000)
// console.log('1 minute')
// clearInterval(guess)
$guess_form.on("submit", handle_Submit)
