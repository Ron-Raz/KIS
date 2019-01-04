const VER = '20190104-1806';

const myDebug = true;

if (myDebug === false) {
	console.log = function () { };
}

var selectors = {
	'sipAction': "#customdata-ServerAction-label, #edit_entry > div:nth-child(14),",
	'sipEndpoint': "#customdata-SIP, #customdata-SIP+P, #customdata-SIP-label, #entry-metadata,",
	'sipStats': "#customdata-Stats-label, #edit_entry > div:nth-child(16),",
	'entryBlock': "#entryDataBlock,",
	'mediaPanel':"#wrapper,"
};
function addCSSRule(sheet, selectorsArray, rules, index) {
	// addCSSRule(document.styleSheets[0], "header", "float: left");
	// selectorsArray is an array from selectors
	var combinedSelectors = '';
	for (i in selectorsArray) combinedSelectors += selectors[selectorsArray[i]];
	// remove last comma
	combinedSelectors= combinedSelectors.slice(0, -1);
	if ("insertRule" in sheet) {
		sheet.insertRule(combinedSelectors + "{" + rules + "}", index);
	}
	else if ("addRule" in sheet) {
		sheet.addRule(combinedSelectors, rules, index);
	}
}

$(function () {
	var wlp = window.location.pathname;
	console.log("client/kms.js version=", VER, "wlp=",wlp);
	/*
	pathname		action
	========		======
	/upload/media		hide sip field (done in css)
	/kwebcast/entry/add	show sip field
	/media/SIP/1_7y4l9qys	show sip server status
	*/

	// show SIP fields ony when creating or editing a live entry
	var res = wlp.split('/');
	if (wlp === '/kwebcast/entry/add' || ($("#KwebcastAdvancedOptions-tab").length > 0)) {
		addCSSRule(document.styleSheets[0], ['sipAction', 'sipStats'], "display: none !important");
		console.log("only hide sipAction and SipStats");
	} else {
		if (wlp.startsWith('/media/')) {
			console.log('sip admin page')
			//addCSSRule(document.styleSheets[0], ['entryBlock'], "width: 100% !important");
			//$("#wrapper, #mySidebar, #stats_wrap, #entryActions, #entry-nav").detach();
		} else {
			console.log("rule added to hide sip field");
			addCSSRule(document.styleSheets[0], ['sipAction', 'sipStats', 'sipEndpoint'], "display: none !important");
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
