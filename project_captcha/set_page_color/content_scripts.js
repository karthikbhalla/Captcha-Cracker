
//get the current url
//var tabURL=window.location.href;
//console.log('url is:'+tabURL);

var x = document.getElementsByTagName("img");
var flag=0;
var ress="";

for(k=0;k<x.length;k++)
	
	{
			if(x[k].hasAttribute("src"))
			{
		if((x[k].getAttribute("src").toLowerCase().match("captcha")!=null)||(x[k].getAttribute("src").toLowerCase().match("captchaimage")!=null)||(x[k].getAttribute("src").toLowerCase().match("cap")!=null)){	
		 var samp=(x[k].getAttribute("src"));	
		break;
		}
		}
	
	}
	if(k<x.length && flag==0){
		alert("Captcha found!");
		 alert(samp);
		  
		 console.log(samp);
		
			flag=1;
	}



var app_id = 'knldjmfmopnpolahpmmgbagdohdnhkik' //this is the app id

chrome.runtime.sendMessage(app_id, {taburl:samp}, function(result) {
        if (chrome.runtime.lastError) {
            // Handle error, e.g. app not installed
            console.warn('Error: ' + chrome.runtime.lastError.message);
        } else {
            // Handle success
			ress=result;
			alert(result,"hellooooo");
            alert('Reply from app: ', result);
        }
    });

var x = document.getElementsByTagName("input");

for(k=0;k<x.length;k++)
	
	{
			if(x[k].hasAttribute("name"))
			{
		if((x[k].getAttribute("name").toLowerCase().match("captcha")!=null)||(x[k].getAttribute("name").toLowerCase().match("captchaimage")!=null)||(x[k].getAttribute("name").toLowerCase().match("cap")!=null)){	
		 var att = document.createAttribute("value");       
		 att.value = ress;                           
		 x.setAttributeNode(att);	
		break;
		}
		}
	
	}
//fr.onerror = function() { /* handle error */ };









//x[ret].src="/image/journal/article?img_id=4701200&amp;t=1424432654180";