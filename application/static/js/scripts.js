$(document).ready(function(){
	$('#phone').mask('+7(000) 000-00-00', {placeholder: "+7(___) ___-__-__"});
});

$(document).ready(function() {
    setTimeout(function() {
        $(".alert-dismissible").alert('close');
    }, 4000);
});
