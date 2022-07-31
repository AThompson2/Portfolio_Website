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



const TimeDelay = document.querySelectorAll('.TimeOne');
observer2 = new IntersectionObserver(entries => {
  var i = 3500
  entries.forEach(entry => {

    if(entry.isIntersecting){

      const myTimeout = setTimeout(timeDelay1, i);

      function timeDelay1() {
          if (entry.target.nodeName == "I") {
            entry.target.style.visibility="visible"
            entry.target.classList.add('right_side-entry');
            observer2.unobserve(entry.target);
          } else {
          entry.target.style.visibility="visible"
          entry.target.classList.add('left_side-entry');
          observer2.unobserve(entry.target);
      }}
    } else {
      entry.target.classList.remove('left_side-entry');
    }
  i = i + 600
  });
  });

TimeDelay.forEach(item => {
  observer2.observe(item);
});
