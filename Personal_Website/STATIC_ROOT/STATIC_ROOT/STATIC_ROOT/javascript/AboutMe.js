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



  const TimerDelay = document.querySelectorAll('.TimeTwo');

  observer4 = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        const myTimeout = setTimeout(timerDelay1, 1000);
        function timerDelay1() {
          if (entry.target.classList == "card") {
            entry.target.style.visibility="visible"
            entry.target.classList.add('right_side-entry');
            observer4.unobserve(entry.target);
          } else {
          entry.target.style.visibility="visible"
          entry.target.classList.add('left_side-entry');
          observer4.unobserve(entry.target);
      }}} else {
        entry.target.classList.remove('left_side-entry');
      }
    });

    });

  TimerDelay.forEach(item => {
    observer4.observe(item);
  });




const TimeDelay = document.querySelectorAll('.TimeOne');
observer2 = new IntersectionObserver(entries => {
  var i = 3500
  entries.forEach(entry => {

    if(entry.isIntersecting){

      const myTimeout = setTimeout(timeDelay1, i);

      function timeDelay1() {
          if (entry.target.nodeName == "IMG") {
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


// slideUp


// const TimeDelay = document.querySelectorAll('#TimeOne');
//
// observer2 = new IntersectionObserver(entries => {
//   console.log(entries);
//   console.log('observer2:', observer2);
//   const myTimeout = setTimeout(timeDelay1, 5000);
//
//   function timeDelay1() {
//     document.getElementById('TimeOne').style.display="block";
//   }
//   });
//
// TimeDelay.forEach(item => {
//   observer2.observe(item);
// });
