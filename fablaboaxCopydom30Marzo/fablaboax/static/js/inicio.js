function updateBackground() {
	screenWidth = $ (window).width();
	screenHeight = $ (window).height();
	var bg = jQuery("#bg");

	//proporcion horizontal /vertival en este caso 1
	ratio = 1;
}

if (screenWidth/screenHeight > ratio) {
	$(bg).height("auto");
	$(bg).width("100%");
}else{
	$(bg).width("auto");
	$(bg).height("100%");
}

// Si a la imagen le sobra anchura la centramos

if ($8bg).width() > 0 ){
	$(bg).css('left', (screenWidth - $(bg).width()) / 2);
}
}

$(document).ready(function(){
	updateBackground();
	$(window).bind("resize",function(){
		updateBackground();
	});
});