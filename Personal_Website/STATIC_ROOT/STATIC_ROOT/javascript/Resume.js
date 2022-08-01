const target4 = document.querySelectorAll('.animated-text');

observer = new IntersectionObserver(entries => {
  entries.forEach(items => {
    if (items.intersectionRatio > 0) {
      items.target.classList.add('visible')
      observer.unobserve(items.target);
    } else {
      items.target.classList.remove('visible')
    }
  });

  });
target4.forEach(item => {
  observer.observe(item);
});



const NewTarget = document.querySelectorAll('.animate-me');

observe1 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.intersectionRatio > 0) {
      entry.target.classList.add('side-entry');
      observe1.unobserve(entry.target);
    } else {
      entry.target.classList.remove('side-entry');
    }
  });

});

NewTarget.forEach(item => {
  observe1.observe(item);
});
