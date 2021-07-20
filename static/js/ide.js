let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/c_cpp");
}

function changeLanguage() {

    let language = $("#languages").val();
    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'java')editor.session.setMode("ace/mode/java");
    else if(language == 'python')editor.session.setMode("ace/mode/python");
}

function executeCode() {

    $.ajax({

        url: "/excecuteCode",
        method: "GET",

        data: {
            language: $("#languages").val(),
            code: editor.getSession().getValue(),
            csrfViewMiddleware:$('input[name=csrfmiddlewaretoken').val(),
 
        },

        success: function(response) {
            $(".output").text(response)
        }
    })
}