function compare(master,slave)
{
	var accepted = true;
	var array = master.split(",");
	var arrlen=array.length;
	for (var i = 0; i < arrlen; i++) 
		{
			if(array[i]===slave)
				accepted=false;		
		}
	return accepted;
}


document.getElementById("new_element_add_button").addEventListener('click',function(evt){
	var text_input=document.getElementById("new-element-text").value;
	var text_area_input=document.getElementById("element-text-area").value;
	if(text_input && text_input.length>0 && Boolean(text_input.trim()) && new RegExp(/^[A-Za-z ]+$/).test(text_input) && compare(text_area_input.toLowerCase(),text_input.toLowerCase()))
	{
		if(text_area_input.length<=0)
			text_area_input+=text_input;
		else
			text_area_input+=","+text_input;
	
		document.getElementById("element-text-area").value=text_area_input;
		document.getElementById("new-element-text").value="";

	}
});

var dropdown=document.getElementById("existing-element-select");
dropdown.addEventListener('click',function(evt){

	var text_area_input=document.getElementById("element-text-area").value;
	var selected_item = dropdown.options[dropdown.selectedIndex].value;

	if(selected_item && selected_item.length>0 && Boolean(selected_item.trim()) && compare(text_area_input.toLowerCase(),selected_item.toLowerCase()))
	{
		if(text_area_input.length<=0)
			{
				text_area_input+=selected_item;
			}
		else
		{
			text_area_input+=","+selected_item;
		}

		document.getElementById("element-text-area").value=text_area_input;
	}
 });

document.getElementById("remove-button").addEventListener('click',function(evt){
  		document.getElementById("element-text-area").value="";
  	 })