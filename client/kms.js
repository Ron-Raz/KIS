function addCSSRule(sheet, selector, rules, index) {
	// addCSSRule(document.styleSheets[0], "header", "float: left");
	if("insertRule" in sheet) {
		sheet.insertRule(selector + "{" + rules + "}", index);
	}
	else if("addRule" in sheet) {
		sheet.addRule(selector, rules, index);
	}
}


$(function() {
	var wlp= window.location.pathname;
	console.log("ver24", wlp);
	/*
	pathname		action
	========		======
	/upload/media		hide sip field (done in css)
	/kwebcast/entry/add	show sip field
	/media/SIP/1_7y4l9qys	show sip server status
	*/
	// update favicon
	$('link[rel="icon"]').attr('href', 'https://i.ibb.co/5GgsZPF/favicon-bnsf.png'); 
	
	// show SIP fields ony when creating or editing a live entry
	var res= wlp.split('/');
	if( wlp === '/kwebcast/entry/add' || ($("#KwebcastAdvancedOptions-tab").length > 0) ) {
		console.log("don't hide sip field");
	} else {
		addCSSRule(document.styleSheets[0], "#customdata-SIP, #customdata-SIP+P, #customdata-SIP-label, #entry-metadata", "display: none !important");
		console.log("rule added to hide sip field");
		if( wlp === '/media/SIP/1_7y4l9qys' ) {
			addCSSRule(document.styleSheets[0], "#entryDataBlock", "width: 100% !important");
			$("#wrapper, #mySidebar, #stats_wrap, #entryActions, #entry-nav").detach();
		}
	}
	/*
	$( "#Entry-name" ).on( "focus", function() {
		console.log( "entry name focus. Entry-submit=",$("#Entry-submit").length );
		if( $("#Entry-submit") > 0 ) {
			$("#customdata-SIP, #customdata-SIP+P, #customdata-SIP-label").show();
			console.log("showing fields");
		} else {
			console.log("keeping fields hidden");
		}
	});
	*/
});

