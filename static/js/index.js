layui.use(['element', 'carousel'], function() {
	var $ = layui.jquery,
		layer = layui.layer, //导航的hover效果、二级菜单等功能，需要依赖element模块
		carousel = layui.carousel; //轮播
	//图片轮播
	carousel.render({
		elem: '#lunbo',
		width: '100%', //设置容器宽度
		height: '260',
		arrow: 'hover', //始终显示箭头
		anim: 'fade', //切换动画方式
		interval: 4000,
	});
	//无线端悬浮菜单
	$(document).ready(function(ev) {
		$(".layui-nav-item dd").each(function() {
			$(this).parent().parent().addClass('');
//			console.log($(k))
//			if($(v).html()!=""){
				console.log($(this).parent().parent())
//				$(v).prev().prev();
//			}
		});
//		console.log($(".layui-nav-item").find("dl:eq(4)").text())

		var toggle = $('#miss_toggle');
		var menu = $('#miss_nav');
		var rot;
		var i = 0;
		$('#miss_toggle').on('click', function(ev) {
			i++;
			setTimeout(function() {
				i = 0;
			}, 500);
			if(i > 1) {
				window.location.href = "music.html";
				i = 0;
			};
			rot = parseInt($(this).data('rot')) - 180;
			menu.css('transform', 'rotate(' + rot + 'deg)');
			menu.css('webkitTransform', 'rotate(' + rot + 'deg)');
			if(rot / 180 % 2 == 0) {
				toggle.parent().addClass('miss_active');
				toggle.addClass('close');
			} else {
				toggle.parent().removeClass('miss_active');
				toggle.removeClass('close');
			}
			$(this).data('rot', rot);
		});
		menu.on('transitionend webkitTransitionEnd oTransitionEnd', function() {
			if(rot / 180 % 2 == 0) {
				$('#miss_nav div i').addClass('miss_animate');
			} else {
				$('#miss_nav div i').removeClass('miss_animate');
			}
		});
		//search	
		$(".searchico").click(function() {
			$(".search").toggleClass("open");
		});
		//searchclose	
		$(".searchclose").click(function() {
			$(".search").removeClass("open");
		});
		
	});

});