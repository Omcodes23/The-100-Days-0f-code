const jokeContainer = document.getElementById("joke");
const btn = document.getElementById("btn");
const url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,political,racist,sexist,explicit&type=single";
let getJoke = () => {
    fetch(url)
        .then((res) => res.json())
        

        .then((data) => {
            jokeContainer.innerHTML = data.joke;
        });
}
btn.addEventListener("click", getJoke);
getJoke();
