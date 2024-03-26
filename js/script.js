const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const regLink = document.querySelector('.register-link');
const joinLink = document.querySelector('.join-link');

regLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});