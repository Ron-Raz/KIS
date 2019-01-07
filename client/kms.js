const VER = '20190106-2323';

const myDebug = true;
var wlp = window.location.pathname;

if (myDebug === false) {
	console.log = function () {};
}

var pageMap = {
	'/kwebcast/entry/add': () => {
		console.log('add Webcast');
		addCSSRule(document.styleSheets[0], ['sipAction'], "display: none !important");
	},
	'sipAdminView': () => {
		console.log('sip admin page - view')
		addCSSRule(document.styleSheets[0], ['entryBlock'], "width: 100% !important");
		$(getSelectors(['toBeDetached', 'endpoint', 'menuItems'])).detach();
	},
	'/media/SIP/1_7y4l9qys': () => {
		pageMap['sipAdminView']();
	},
	'/media/t/1_7y4l9qys': () => {
		pageMap['sipAdminView']();
	},
	'/edit/1_7y4l9qys': () => {
		console.log("sip admin page - edit");
		addCSSRule(document.styleSheets[0], ['sipAdminEdit', 'sipEndpoint'], "display: none !important");
	},
	'/upload/media': () => {
		console.log('upload media');
		addCSSRule(document.styleSheets[0], ['sipAction', 'sipEndpoint'], "display: none !important");
	},
	// following can't be identified solely by url path
	'editWebcast': () => {
		console.log('edit webcast');
		addCSSRule(document.styleSheets[0], ['editWebcast'], "display: none !important");
	},
	'nonWebCastEdit': () => {
		console.log('non-webcast edit');
		addCSSRule(document.styleSheets[0], ['sipEndpoint', 'sipAction'], "display: none !important");
	},
	'catchAll': () => {
		console.log('catchall');
		if ($('#KwebcastAdvancedOptions-tab').length > 0) {
			pageMap['editWebcast']();
		} else {
			if (wlp.startsWith('/edit/')) {
				pageMap['nonWebCastEdit']();
			}
		}
	}
};

var selectors = {
	// upload media
	'sipAction': "#customdata-ServerAction-label, #edit_entry > div:nth-child(14),",
	'sipEndpoint': "#customdata-SIP, #customdata-SIP+P, #customdata-SIP-label, #entry-metadata,",
	'mediaPanel': "#wrapper,",
	// SIP admin page, view mode
	'entryBlock': "#entryDataBlock,",
	'panels': "#entry-metadata > dt:nth-child(1), #mySidebar, #eCaptions, #stats_wrap,",
	'endpoint': "#entry-metadata > dt:nth-child(1), #entry-metadata > dd:nth-child(2),",
	'actions': "#entryActionsMenu > li:nth-child(2), #entryActionsMenu > li:nth-child(3), #entryActionsMenu > li.divider, #entryActionsMenu > li:nth-child(5),",
	'toBeDetached': "#wrapper, #mySidebar, #stats_wrap,",
	'menuItems': "#tab-Publish,#tab-Addtoplaylists,#entryActionsMenu > li.divider,#tab-Delete,",
	// edit webcast
	'editWebcast': "#customdata-ServerAction-label, #edit_entry > div:nth-child(14),",
	// sip admin - edit
	'sipAdminEdit': '#editEntryMedia,#wrap > div:nth-child(7) > div > ul > li.pull-right,'
};

function getSelectors(selarray) {
	var combinedSelectors = '';
	for (i in selarray) combinedSelectors += selectors[selarray[i]];
	// remove last comma
	combinedSelectors = combinedSelectors.slice(0, -1);
	console.log('combinedSelectors=', combinedSelectors);
	return combinedSelectors;
}

function addCSSRule(sheet, selectorsArray, rules, index) {
	// addCSSRule(document.styleSheets[0], "header", "float: left");
	// selectorsArray is an array from selectors
	if ("insertRule" in sheet) {
		sheet.insertRule(getSelectors(selectorsArray) + "{" + rules + "}", index);
	} else if ("addRule" in sheet) {
		sheet.addRule(getSelectors(selectorsArray), rules, index);
	}
}

$(function () {
	console.log("client/kms.js version=", VER, "wlp=", wlp);
	/*
	pathname		action
	========		======
	/upload/media		hide sip field (done in css)
	/kwebcast/entry/add	show sip field
	/media/SIP/1_7y4l9qys	show sip server status
	*/
	var f = null;
	for (var i in pageMap) {
		if (wlp.startsWith(i)) f = pageMap[i];
	}
	if (f) {
		f();
	} else {
		pageMap['catchAll']();
	}
});
