document.addEventListener('DOMContentLoaded', function() {
	// 发送表单请求
	const formInfo = document.getElementById('stockForm')
	if(formInfo) {
		formInfo.addEventListener('submit', function(event) {
			event.preventDefault(); // 阻止表单的默认提交行为
	
			var stockCode = document.getElementById('stockCode').textContent;
			var noteInfo = document.getElementById('noteInfo').value;

			console.log(stockCode);  // 检查这个值是否正确
			console.log(noteInfo);   // 检查这个值是否正确

	
			// 构建目标URL
			var targetUrl = 'http://localhost:8080/update/' + stockCode + '/' + noteInfo + '.html';
			console.log("打印出提交路径:", targetUrl)
	
			// 导航到目标URL
			// window.location.href = targetUrl;
		});
	}
	
});