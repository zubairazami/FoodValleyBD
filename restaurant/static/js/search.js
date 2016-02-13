document.getElementById('search_button').addEventListener('click',function(evt)
        {
			var str = "Fill up the following:\n";
		    var flag = false;
		    var checkflag=false;
		    var field='';
		    var field2='';
	        
	        if(document.getElementById('district_check').checked)
	        {
	        	
	        	checkflag=true;
	        	field = document.getElementById('district').value;
	        	if(field.trim()==''||field==null)
	        	{
	        		flag=true;
	        		str+="\t> District\n";
	        	}
	        }
			
			if(document.getElementById('food_check').checked)
	        {
	        	checkflag=true;
	        	field = document.getElementById('food').value;
	        	if(field.trim()==''||field==null)
	        	{
	        		flag=true;
	        		str+="\t> Food Item\n";
	        	}
	        }
			if(document.getElementById('price_check').checked)
	        {
	        	checkflag=true;
	        	field = document.getElementById('price_start').value;
	        	field2 = document.getElementById('price_end').value;
	      
	        	if(field.trim()==''||field==null||field2.trim()==''||field2==null)
	        	{
	        		flag=true;
	        		str+="\t> Price\n";
	        	}
	        }

	        if(!checkflag)
	        {
	        	flag=true;
	        	str='Atleast check one field for successful search.';
	        }

	        if(flag)
	        	{
	        		alert(str);
	        		evt.preventDefault();				
				}
			
        });