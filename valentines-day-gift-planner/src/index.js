document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    // Perform login logic here
    // Redirect to gift list page or perform other actions after login
    window.location.href = 'gift-list.html'; // Redirect to gift list page
  });
});
