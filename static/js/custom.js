const navLinks = document.querySelectorAll('.nav-link');
const pathName = location.pathname.substring(1);
const titleInput = document.querySelector('.title');
const slugInput = document.querySelector('.slug');

pathName === '' ? navLinks[0].classList.add('active') : '';
pathName === 'posts/' ? navLinks[1].classList.add('active') : '';
pathName === 'destinations/' ? navLinks[2].classList.add('active') : '';

titleInput.addEventListener('keyup', () => {
  let inputText = titleInput.value.split(' ');
  slugInput.value = inputText.join('-').toLowerCase();
});
