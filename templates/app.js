function uploadFile(form) {
    const formData = new FormData(form);
    var oOutput = document.getElementById("static_file_response")
    var resume = document.getElementById("resume_parser_table")
    var oReq = new XMLHttpRequest();
    oReq.open("POST", "upload_static_file", true);
    oReq.onload = function(oEvent) {
        if (oReq.status == 200) {
            oOutput.innerHTML = "Uploaded!";
            var results = oReq.response
            // get the results json here
            // need to display the results in index.html
            results = JSON.parse(results)
            // name is just for example
            // need to display all information
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