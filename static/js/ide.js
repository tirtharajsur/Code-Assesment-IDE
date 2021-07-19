let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/terminal");
    editor.session.setMode("ace/mode/c_cpp");
}

function changeLanguage() {

    let language = $("#languages").val();
    print("Language")

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'java')editor.session.setMode("ace/mode/java");
    else if(language == 'python')editor.session.setMode("ace/mode/python");
}

function executeCode() {

    $.ajax({

        // url: "/ide/app/compiler.php",
        // url: "IDE\compiler.py",
        url: "IDE\views.py",
        //url: "IDE\compiler.php",
        
        

        method: "POST",

        data: {
            language: $("#languages").val(),
            code: editor.getSession().getValue()
        },

        success: function(response) {
            $(".output").text(response)
        }
    })
}