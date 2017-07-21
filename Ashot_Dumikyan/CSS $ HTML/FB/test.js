var amis1=0;


function grel_tariner(){
	for (i=1; i<100;i++){
                	k=2018-i;
                	document.write('<option value="'+i+'">'+k+'</option>');
                }
}
function grel_orer(){
	k=oreri_qanak(amis1+1);
	for (i=1;i<=k;i++){
                		document.write('<option value="'+i+'">'+i+'</option>');
                	}
}


function getfocus(i) {
    document.getElementById(i).focus();
}

function amis(i) {
    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";
    return month[i];
}
function grel_amis(){
	for (i=1;i<=12;i++){
                		document.write('<option value="'+i+'">'+amis(i-1)+'</option>');
                	}
}

function oreri_qanak(i) {
    var days = new Array();
    days[0] = 31;
    days[1] = 28;
    days[2] = 31;
    days[3] = 30;
    days[4] = 31;
    days[5] = 30;
    days[6] = 31;
    days[7] = 31;
    days[8] = 30;
    days[9] = 31;
    days[10] = 30;
    days[11] = 31;
     return days[i];
}

function yntrel(){
	//alert(amis1);
	amis1=document.getElementById("month").value;
	//alert(amis1);
}