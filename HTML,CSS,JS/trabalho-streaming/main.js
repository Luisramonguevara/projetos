//swiper
const progressCircle = document.querySelector(".autoplay-progress svg");
    const progressContent = document.querySelector(".autoplay-progress span");
    var swiper = new Swiper(".popular-content", {
      slidesPerView: 1,
      spaceBetween: 10,
      autoplay: {
        delay: 5500,
        disableOnInteraction: false
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
      },
      breakpoints:{
        280:{
          slidesPerView: 1,
          spaceBetween: 10
        },
        320:{
          slidesPerView: 2,
          spaceBetween: 10
      },
      510:{
        slidesPerView: 2,
        spaceBetween: 10

      },
      758:{
        slidesPerView: 4,
        spaceBetween: 15
      },
      900:{
        slidesPerView: 5,
        spaceBetween: 20
      },
      on: {
        autoplayTimeLeft(s, time, progress) {
          progressCircle.style.setProperty("--progress", 1 - progress);
          progressContent.textContent = `${Math.ceil(time / 1000)}s`;
        },
        

        }


      }

    });