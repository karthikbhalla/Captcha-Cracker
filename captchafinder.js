var x = document.getElementsByTagName("img");
var flag=0;


for(i=0;i<x.length;i++)
	
	{
				if(x[i].hasAttribute("id"))
				{
		if((x[i].getAttribute("id").toLowerCase().match("captcha")!=null)||(x[i].getAttribute("id").toLowerCase().match("captchaimage")!=null)||(x[i].getAttribute("id").toLowerCase().match("cap")!=null)){			
		break;
		}
		}
	
	}
	

	if(i<x.length && flag==0){
		alert("Captcha found!");
			flag=1;
		
	}

	
for(k=0;k<x.length;k++)
	
	{
			if(x[k].hasAttribute("src"))
			{
		if((x[k].getAttribute("src").toLowerCase().match("captcha")!=null)||(x[k].getAttribute("src").toLowerCase().match("captchaimage")!=null)||(x[k].getAttribute("src").toLowerCase().match("cap")!=null)){			
		break;
		}
		}
	
	}
	if(k<x.length && flag==0){
		alert("Captcha found!");
			flag=1;
	}
	
for(l=0;l<x.length;l++)
	
	{
			if(x[l].hasAttribute("class"))
			{
		if((x[l].getAttribute("class").toLowerCase().match("captcha")!=null)||(x[l].getAttribute("class").toLowerCase().match("captchaimage")!=null)||(x[l].getAttribute("class").toLowerCase().match("cap")!=null)){			
		break;
		}
		}
	
	}
	if(l<x.length && flag==0){
		alert("Captcha found!");
		flag=1;
	}
		for(j=0;j<x.length;j++)
	
	{
		if(x[j].hasAttribute("alt"))
		{
		if((x[j].getAttribute("alt").toLowerCase().match("captcha")!=null)||(x[j].getAttribute("alt").toLowerCase().match("captchaimage")!=null)||(x[j].getAttribute("alt").toLowerCase().match("cap")!=null)){	

break;
		}
		}
	
	}
	if(j<x.length && flag==0){
		alert("Captcha found!");
			flag=1;
	}
	

	if(flag==0)
	alert("Captcha not found!!");
	
	








//x[ret].src="/image/journal/article?img_id=4701200&amp;t=1424432654180";
