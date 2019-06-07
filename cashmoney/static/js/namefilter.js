function searchnames() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        if (filter.length == 0) {
            li[i].style.display = "none";
        }
        else {
            a = li[i].getElementsByTagName("a")[0];
            txtValue = a.textContent || a.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "block";
            } else {
                li[i].style.display = "none";
            }
        }
    }
};

function add_name(u_id, curr_user_id) {
    var ul, li_query, li, user_list;
    input = document.getElementById("myInput");
    input.value = "";
    user_list = document.getElementById("list-tab");
    new_item = document.createElement("a");
    id = 0;
    username = "";
    firstname = "";
    lastname = "";

    content_list = document.getElementById("nav-tabcontent");
    content_item = document.createElement("div");

    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        li[i].style.display = "none";
    }
    var reply = $.post("/get_user_by_id", { query_id: u_id}, function(resp) {
        // console.log(resp);
        id = resp["id"];
        username = resp["username"];
        firstname = resp["firstname"];
        lastname = resp["lastname"];

        new_item.setAttribute("class", "list-group-item list-group-item-action");
        new_item.setAttribute("id", "list-" + username + "-list")
        new_item.setAttribute("data-toggle", "tab");
        new_item.setAttribute("href", '#list-' + username);
        new_item.setAttribute("role", "tab");
        new_item.setAttribute("aria-controls", "list-" + username);
        // new_item.activeElement = true;
        new_item.innerHTML = firstname + " " + lastname;
        user_list.appendChild(new_item);

        content_item.setAttribute("class", "tab-pane fade")
        content_item.setAttribute("id", "list-" + username);
        content_item.setAttribute("role", "tabpanel");
        content_item.setAttribute("aria-labelledby", "list-" + username + "-list");
        content_item.innerHTML = '<div class="chatbox" id="chatbox-'+id+'"></div><div class="userInput" id="userInput"><input class="textInput" id="textInput-'+id+'" type="text" placeholder="Message"><input class="buttonInput" id="buttonInput" onClick=getResponse('+id+','+curr_user_id+') value="Send"></div>';
        content_list.appendChild(content_item);

    });
    ul = document.getElementById("myUL");
};
