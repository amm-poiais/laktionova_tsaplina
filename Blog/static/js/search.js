function ShowCategory(){
    $('label[for="id_category"]').css("display", "block");
    $('#id_category').css("display", "block");
    $('label[for="id_pub_date_month"]').css("display", "none");
    $('#id_pub_date_month').css("display", "none");
    $('#id_pub_date_year').css("display", "none");
    $('#id_pub_date_day').css("display", "none");
}

function ShowDate(){
    $('label[for="id_category"]').css("display", "none");
    $('#id_category').css("display", "none");
    $('label[for="id_pub_date_month"]').css("display", "block");
    $('#id_pub_date_month').css("display", "block");
    $('#id_pub_date_year').css("display", "block");
    $('#id_pub_date_day').css("display", "block");
}

$(document).ready(function(){
    ShowCategory();

    $('#id_options_0').change(function(){
        ShowCategory();
    });

    $('#id_options_1').change(function(){
        ShowDate();
    });
});

/*function ShowHide(radio_btn){
    var select_category = document.getElementById('id_category');
    var select_month = document.getElementById('id_pub_date_month');
    var select_year = document.getElementById('id_pub_date_year');
    var select_day = document.getElementById('id_pub_date_day');
    if(radio_btn.value == 'category'){
        select_category.removeAttribute('disabled');
        select_month.setAttribute('disabled', 'disabled');
        select_year.setAttribute('disabled', 'disabled');
        select_day.setAttribute('disabled', 'disabled');
    } else{
        select_category.setAttribute('disabled', 'disabled');
        select_month.removeAttribute('disabled');
        select_year.removeAttribute('disabled');
        select_day.removeAttribute('disabled');
    }
}*/