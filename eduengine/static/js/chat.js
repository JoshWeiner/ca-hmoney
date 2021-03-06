function getResponse(to_id, from_id) {
    var input_text = document.getElementById("textInput-"+to_id);
    var chatbox = document.getElementById("chatbox-"+to_id);
    console.log(chatbox);
    var rawText = input_text.value;

    if (rawText.length != 0) {
        user_html = document.createElement("p");
        user_html.setAttribute("class", "userText");
        user_html.innerHTML = '<span>' + rawText + '</span>';

        chatbox.appendChild(user_html);

        input_text.value = "";

        var reply = $.post("/send_message", {
            rawText: rawText, to_id : to_id, from_id : from_id}, function(response)
            {
            });
    }

  //Displays user input in chatbox

  // var reply = $.post("/get_js", {
  //   rawText: rawText}, function(response)
  //   {
  //     var botHtml = '<p class="botText"><span>' + response + '</span></p>';
  //     $("#chatbox").append(botHtml)
  //   });

};

function refresh_messages(to_id, from_id) {
    var ref_chatbox = document.getElementById('chatbox-'+to_id);
    var new_reply = $.post("/retrieve_messages", {
        to_id:to_id, from_id:from_id}, function(response) {
            ref_chatbox.innerHTML = "";
            for (i = 0; i < response['messages'].length; i ++) {
                message = response['messages'][i];
                // console.log(message);
                if (message["to_id"] == from_id) {
                    user_html = document.createElement("p");
                    user_html.setAttribute("class", "botText");
                    user_html.innerHTML = '<span>' + message["body"] + '</span>';
                    ref_chatbox.appendChild(user_html);
                }
                else if  (message["to_id"] == to_id){
                    user_html = document.createElement("p");
                    user_html.setAttribute("class", "userText");
                    user_html.innerHTML = '<span>' + message["body"] + '</span>';
                    ref_chatbox.appendChild(user_html);
                }
            }
        })
        return true;
    };
