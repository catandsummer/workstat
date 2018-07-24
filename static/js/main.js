
function submitdata() {
    var data = $("#formdata").serialize();
    $.ajax({
        type: "POST",
        url: "/datainterface",
        data: data,
        success: function (msg) {

        }
    });
    return false;
}
function delmessage(index) {
    $.ajax({
        type: "DEL",
        url: "/datainterface",
        data: {"index":index},
        success: function (msg) {

        }
    });
    return false;
}

function refresh() {
    $.getJSON(
        "/datainterface",
        function (result) {
            $("#tabledata tr").remove();
            var tabledata = document.getElementById("tabledata");
            var i;
            var header = tabledata.createTHead();
           var hr = header.insertRow(0);
           hr.insertCell(0).innerHTML = "<b>ID</b>";
            hr.insertCell(1).innerHTML = "<b>内容</b>";
            hr.insertCell(2).innerHTML = "<b>操作</b>";
            for (i in result["data"]) {
                var row = tabledata.insertRow(-1);
                var id = row.insertCell(0);
                var content = row.insertCell(1);
                 var op = row.insertCell(2);

                id.innerHTML = i + 1;
                content.innerHTML = result["data"][i];
                op.innerHTML = "<button onclick='delmessage(i)'>删除</button>";

            }

        }
    );
}

var ref = setInterval(function () {
    refresh();
}, 1000);