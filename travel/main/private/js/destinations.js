!function ($) {

	"use strict";

	$(document).ready(function() {
		var destinations;
		var i;
		$( ".image_destination" )
		.mouseout(function() {
		    destinations= document.getElementsByClassName("destinations");
		  	for (i = 0; i < destinations.length; i++) {
		    	destinations[i].style.display = "none";
		  	}
  		 	$("#about-us").show()
		})
		.mouseover(function() {
		  	destinations= document.getElementsByClassName("destinations");
		  	for (i = 0; i < destinations.length; i++) {
		    	destinations[i].style.display = "none";
		  	}
  		 	$($(this).data("target")).show()
		});


	});

}(jQuery);