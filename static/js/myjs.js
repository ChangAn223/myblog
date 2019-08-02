function like_article(id) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            if (xmlhttp.responseText == "false") {

            }
            document.getElementById("diggnum").innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", "/like/" + id, true);
    xmlhttp.send();
}

function saytext(article_id, comm_id) {
    reply = "<form class=\"layui-form\" action=\"\"><input type=\"hidden\" name=\"openid\" value=\"\"><input\n" +
        "                                    type=\"hidden\" name=\"reply_openid\" value=\"\"><input type=\"hidden\"\n" +
        "                                                                                      name=\"article_id\"\n" +
        "                                                                                      value=\"8\"><input type=\"hidden\"\n" +
        "                                                                                                       name=\"comment_id\"\n" +
        "                                                                                                       value=\"42\">\n" +
        "                                <div class=\"layui-form-item\"><textarea name=\"content\" lay-verify=\"replyContent\"\n" +
        "                                                                       placeholder=\"回复评论功能暂时还没有实现，请稍后再试。\" class=\"layui-textarea\"\n" +
        "                                                                       style=\"min-height:80px;\"></textarea></div>\n" +
        "                                <div class=\"layui-form-item\">\n" +
        "                                    <button class=\"layui-btn layui-btn-xs\" lay-submit=\"formReply\"\n" +
        "                                            lay-filter=\"formReply\">提交\n" +
        "                                    </button>\n" +
        "                                </div>\n" +
        "                            </form>"
    document.getElementById(comm_id).innerHTML = reply
}