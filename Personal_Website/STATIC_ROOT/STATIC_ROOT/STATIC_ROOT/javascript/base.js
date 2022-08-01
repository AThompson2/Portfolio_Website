const target3 = document.querySelectorAll('.animated-text');

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
  target3.forEach(item => {
    observer.observe(item);
  });



  const NewTarget1 = document.querySelectorAll('.animate-me');

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

  NewTarget1.forEach(item => {
    observe1.observe(item);
  });



  const TimeDelay = document.querySelectorAll('.link_one');
  observer3 = new IntersectionObserver(entries => {
    var i = 2000
    entries.forEach(entry => {

      if(entry.isIntersecting){

        const myTimeout = setTimeout(timeDelay1, i);

        function timeDelay1() {
            entry.target.style.visibility="visible"
            entry.target.classList.add('slideUp');
            observer3.unobserve(entry.target);
        }
      } else {
        entry.target.classList.remove('slideUp');
      }
    i = i + 0800
    console.log(i)
    });
    });

  TimeDelay.forEach(item => {
    observer3.observe(item);
  });
