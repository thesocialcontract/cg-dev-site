particlesJS.load('particles-js', 'static/assets/particles-hearts.json', function() {
    console.log('callback - particles.js config loaded');
  });


// let daysTilWeSeeEachOther = function(day) {
//     let today = new Date()
//     let msTilDay = day - today;
//     let dayInMs=1000*60*60*24;
//     days = Math.round(msTilDay / dayInMs)
//     return days;
// }

let getRandomItem = function(arr) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    const item = arr[randomIndex];
    return item;
}

let phrases = [
    "I love you!",
    "You are wonderful!",
    "You make me smile!",
    "❤️",
    "🥰",
    "💕",
    "💗",
    "You make my day brighter",
    "Thank you for taking me around Seattle.",
    "Thank you for listening to me when I'm down.",
    "Thank you for letting me geek out about Beat Saber lolol",
    "Thank you for caring so much.",
    "Thank you for being there for me.",
    "I feel so lucky to be with you.",
    "I adore you!",
    "Thank you for always working through things with me!",
    "I adore your heart! I hope mine can grow to half the size as yours! 💗",
    "Julia, you are the best!",
    "I love you Julia <3",
    "You're brilliant you radiant starlight!",
    "You're wonderful you delightful treasure!",
    "Kiss me 😘",
    "You're amazing you perfect gem!",
    "Your laugh is infectious!",
    "I almost have as much affection for you as River :3",
    "Thank you for being you ❤️",
];
let affirmationElems = document.getElementsByClassName("c-love");
for (elem in affirmationElems) {
    affirmationElems[0].innerHTML = getRandomItem(phrases)
}