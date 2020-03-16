$(document).ready(function () {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            $.ajaxPrefilter(function (options, originalOptions, jqXHR) {
                if (options['type'].toLowerCase() === "post") {
                    jqXHR.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                }
            });
            $("#a").click(function () {
                $("#automate").show();
                $("#settings").hide();
                $("#about").hide();
            });
            $("#b").click(function () {
                $("#automate").hide();
                $("#settings").show();
                $("#about").hide();
            });
            $("#c").click(function () {
                $("#automate").hide();
                $("#settings").hide();
                $("#about").show();
            });
            $("#start_listening").click(function () {
                $.post("/home/");
            });
});