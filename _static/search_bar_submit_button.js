// Add a submit button to the search form for accessibility
document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.querySelector('form.bd-search');
  if (searchForm) {
    const submitBtn = document.createElement('button');
    submitBtn.type = 'submit';
    submitBtn.className = 'visually-hidden';  // Keeps it hidden visually but accessible to screen readers
    submitBtn.textContent = 'Submit Search';
    searchForm.appendChild(submitBtn);
  }
});
