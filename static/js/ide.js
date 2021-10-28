let editor;

window.onload = function () {
  editor = ace.edit("editor");
  editor.setTheme("ace/theme/monokai");
  // editor.session.setMode("ace/mode/c_cpp");
  editor.session.setMode("ace/mode/python");
};

function changeLanguage() {
  let language = $("#languages").val();
  if (language == "75" || language == "52")
    editor.session.setMode("ace/mode/c_cpp");
  else if (language == "62") editor.session.setMode("ace/mode/java");
  else if (language == "71") editor.session.setMode("ace/mode/python");
}

function executeCode() {
  $.ajax({
    url: "/excecuteCode",
    method: "GET",

    data: {
      language: $("#languages").val(),
      code: editor.getSession().getValue(),
      csrfViewMiddleware: $("input[name=csrfmiddlewaretoken").val(),
    },

    success: function (response) {
      $(".output").text(response);
    },
  });
}

function ComplileCode() {
  $.ajax({
    type: "POST",
    url: "/excecuteCode",
    data: {
      language: $("#languages").val(),
      code: editor.getSession().getValue(),
      csrfViewMiddleware: $("input[name=csrfmiddlewaretoken").val(),
    },
    success: function (data) {
      if (!data.errorMsg) {
        console.log(data.success);
        $("#Output").text(data.success);
        $(".testOutput").text(data.success);
      } else {
        console.log(data.errorMsg);
        $("#Output").text(data.errorMsg);
        $(".testOutput").text(data.errorMsg);
      }
      // show response from the php script.
    },
  });
}
