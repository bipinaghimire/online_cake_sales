let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
// for the search button actions

let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close');
// to cancel the login form

// for 3 bars in nav bar for smaller devices
let menu= document.querySelector('#menu-bar');
let navbar= document.querySelector('.navbar');

// to play different videos on home screen
let videoBtn= document.querySelectorAll('.vid-btn');


// dissapear when scrolled down
window.onscroll = ()=>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');
}
// appear all the navigation option when clicked in the 3 bars
menu.addEventListener('click', ()=>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

// appear container with other search icon when click the search icon 
searchBtn.addEventListener('click', ()=>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});

// for opening and closing the login form

formBtn.addEventListener('click', ()=>{
    loginForm.classList.add('active');
});

formClose.addEventListener('click', ()=>{
    loginForm.classList.remove('active');
});

// for the dots to play different videos
videoBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src=src;
    });
});
