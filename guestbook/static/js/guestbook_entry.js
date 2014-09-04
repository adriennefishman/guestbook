$( document ).ready(function() {

        $("#guestbook_entry_form #submit_button").click( function(e) {
                console.log("clicked");
                e.preventDefault();
                var dataString = $("#guestbook_entry_form").serialize();
             
                $.post("/update/", dataString, function(data) {
                        alert("hi");
                        if(data.hasOwnProperty("error")) {
                                alert("There is an error");
                        }
                        else {
                                var result = '<div class="entry" id="'+guestbook_entry.id+'">';
                                $('.results').append("<div>" + data.name + data.email + data.comment + "</div>");
                        }
                }, "json").fail(function() {
                        alert("there is an error");
                });
        });
});