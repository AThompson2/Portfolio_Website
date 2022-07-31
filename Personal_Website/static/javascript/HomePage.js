
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


const TimerDelay = document.querySelectorAll('.figcaption');

observer4 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      const myTimeout = setTimeout(timerDelay1, 1000);
      function timerDelay1() {
        entry.target.style.visibility="visible"
        entry.target.classList.add('slideUp');
        observer4.unobserve(entry.target);
        }

    } else {
      entry.target.classList.remove('slideUp');
    }
  });

  });

TimerDelay.forEach(item => {
  observer4.observe(item);
});
