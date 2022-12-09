function uploadFile(form) {
    const formData = new FormData(form);

    if (1, document.getElementById("file").files.length == 0) {
        alert("Please choose a file");
        return;
    }

    var oOutput = document.getElementById("static_file_response")
    var resume = document.getElementById("resume_parser_table")
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "upload_static_file", true);
    oReq.onload = function(oEvent) {
        if (oReq.status == 200) {
            oOutput.innerHTML = "Uploaded!";
            var results = oReq.response
            results = JSON.parse(results)
            resume_parser_table.innerHTML = results.name

            console.log(results)
        } else {
            oOutput.innerHTML = "Error occurred when trying to upload your file.<br \/>";
        }
    };
    oOutput.innerHTML = "Sending file!";
    console.log("Sending file!")
    oReq.send(formData);
}