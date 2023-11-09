let currentSlideIndex = 0;

function showSlide(index) {
  let slides = document.querySelectorAll('#bannerCarousel .slide');
  if (index >= slides.length) {
    currentSlideIndex = 0; // Go back to the first slide
  } else if (index < 0) {
    currentSlideIndex = slides.length - 1; // Go to the last slide
  } else {
    currentSlideIndex = index;
  }

  // Hide all slides
  for (let slide of slides) {
    slide.style.display = 'none';
  }

  // Show the current slide
  slides[currentSlideIndex].style.display = 'block';
}

// Set up the click event to go to the next slide
document.getElementById('bannerCarousel').addEventListener('click', () => {
  showSlide(currentSlideIndex + 1);
});

// Initialize the carousel by showing the first slide
showSlide(currentSlideIndex);
