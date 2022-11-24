console.log("The File is loading!")

const $guess_form = $(".guess-from")

async function handle_Submit(evt){
    evt.preventDefault();
    const $guess = $(".guess")
    console.log($guess.val())
}

$guess_form.on("submit", handle_Submit)
