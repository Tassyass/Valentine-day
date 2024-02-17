document.addEventListener('DOMContentLoaded', function() {
  // Event listener for the login form submission
  const loginForm = document.querySelector('.form-container form');
  loginForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission behavior
      // Your login form handling code here

      // Redirect the user to the gift list page
      window.location.href = 'giftlist.html';
  });

  // Other JavaScript code
  // Add event listeners or perform other DOM manipulations here
});
