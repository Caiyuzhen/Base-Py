document.addEventListener('DOMContentLoaded', function() {
	let currentSlideIndex = 0;

	// 轮播图
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



	console.log(11)

	// 用 js 来提交表单请求
	document.addEventListener('DOMContentLoaded', function() {
		const form = document.getElementById('stockForm');
		console.log(form);
	
		if (form) {
			form.addEventListener('submit', function(event) {
				event.preventDefault(); // 阻止表单的默认提交行为
	
				const stockCodeElement = document.getElementById('stockCode');
				const noteInfoElement = document.getElementById('noteInfo');
	
				if (stockCodeElement && noteInfoElement) {
					const stockCode = stockCodeElement.textContent.trim();
					const noteInfo = noteInfoElement.value.trim();
	
					// 🚀🚀 构建 form 请求的目标 url
					const actionUrl = '/updateInfo/' + encodeURIComponent(stockCode) + '/' + encodeURIComponent(noteInfo) + '.html';
					
					// 设置表单的action属性
					form.action = actionUrl;
	
					// 提交表单
					form.submit();
				} else {
					console.error('Element IDs do not match or missing values.');
				}
			});
		}
	});
	
});