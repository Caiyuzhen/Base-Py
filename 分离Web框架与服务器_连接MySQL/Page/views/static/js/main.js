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



	print(11)

	// 发送表单请求
	const formInfo = document.getElementById('stockForm')
	if(formInfo) {
		formInfo.addEventListener('submit', function(event) {
			print(12)
			event.preventDefault(); // 阻止表单的默认提交行为
	
			var stockCode = document.getElementById('stockCode').value;
			var noteInfo = document.getElementById('noteInfo').textContent;
	
			// 构建目标URL
			var targetUrl = 'http://localhost:8080/update/' + stockCode + '/' + noteInfo + '.html';
			print("打印出提交路径:", targetUrl)
	
			// 导航到目标URL
			window.location.href = targetUrl;
		});
	}
	
});