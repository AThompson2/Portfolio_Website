const TimeDelay1 = document.querySelectorAll('.link_one');
observer3 = new IntersectionObserver(entries => {
  var i = 800
  entries.forEach(entry => {

    if(entry.isIntersecting){

      const myTimeout = setTimeout(timeDelay1, i);
      const mediaQuery = windo.matchMedia('(min-width: 767px)')
      function timeDelay1() {
          if(mediaQuery.matches) {
            entry.target.classList.remove('slideUp');
          }
          else {
            entry.target.style.visibility="visible"
            entry.target.classList.add('slideUp');
            observer3.unobserve(entry.target);
          }

      }
    } else {
      entry.target.classList.remove('slideUp');
    }
  i = i + 0600
  });
  });

TimeDelay1.forEach(item => {
  observer3.observe(item);
});
