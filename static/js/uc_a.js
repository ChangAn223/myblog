function CaoNiMaDeUc() {
	$("a").each(function(index, element) {
		try {
			var thishref = $(this).attr("href");
			var thisText = $(this).html();
			if(thishref.indexOf("uc.cn") >= 0) {
				$(this).replaceWith(thisText);
			}
		} catch(e) {}
	});
	$("script").each(function(index, element) {
		try {
			var thissrc = $(this).attr("src");

			if(thissrc.indexOf("ucbrowser") >= 0) {
				$(this).remove();
			}
		} catch(e) {}
	});
};
$(function() {
	var pageDATA_ua = window.navigator.userAgent.toLowerCase();

	if(pageDATA_ua.indexOf('ucbrowser')>=0){CaoNiMaDeUc()}
});