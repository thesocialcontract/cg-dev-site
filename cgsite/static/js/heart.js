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
    "I love you Julia ❤️",
    "You're brilliant you radiant starlight!",
    "You're wonderful you delightful treasure!",
    "Kiss me 😘",
    "You're amazing you perfect gem!",
    "Your laugh is infectious!",
    "I almost have as much affection for you as River :3",
    "Thank you for being you ❤️",
    "You have my whole heart.",
    "When I feel the warmth of sunlight on my face, I think of you.",
    "We can do anything together.",
    "When we're together, time is meaningless.",
    "You're such a joy!",
    "Empirical evidence indicates that just thinking about you makes the world ~76.58% brighter",
    "I love how understanding you are and how you strive for empathy and love.",
    "I love how you're there for your friends.",
    "I love how disciplined you are and how you use it to strive for great things. 💪",
    "I love how you check-in with me to see where I'm at and how I'm feeling.",
    "I love how communicative you are, and how we've worked through distance.",
    "❤️ I love how you love. ❤️",
    "The world melts away when we hug.",
    "I love whenever we share our time together.  I'm so happy you share your time with mine.",
    "You make me feel so loved and cared about.",
    "You make me feel like the luckiest guy alive."
];
let affirmationElems = document.getElementsByClassName("c-love");
for (elem in affirmationElems) {
    affirmationElems[0].innerHTML = getRandomItem(phrases)
}