function ShowCommentField(){
    $('label[for="id_comment"]').css("display", "block");
    $('#id_comment').css("display", "block");
}

function HideCommentField(){
    $('label[for="id_comment"]').css("display", "none");
    $('#id_comment').css("display", "none");
}

$(document).ready(function(){
    HideCommentField();
    console.log('hide');
    $('#id_actions_0').change(function(){
        HideCommentField();
    });
    $('#id_actions_1').change(function(){
        ShowCommentField();
    });
});