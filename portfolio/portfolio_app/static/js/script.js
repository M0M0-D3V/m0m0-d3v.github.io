$(document).ready(function () {
  console.log("document is ready!");
  /*
  https://github.com/daybrush/scenejs
  https://github.com/daybrush/scenejs-effects
  */
  new Scene(
    {
      ".container1 span": Scene.typing({
        text: "Full-Stack web Developer At your service!",
        duration: 7,
        delay: 0.5,
      }),
      ".cursor": {
        0: { opacity: 0 },
        0.5: { opacity: 0 },
        "0.5>": { opacity: 1 },
        1: { opacity: 1 },
        options: {
          iterationCount: 8,
        },
      },
    },
    {
      iterationCount: "infinite",
      direction: "alternate",
      selector: true,
    }
  ).play();

  // function for hover / show
  // techwrapper > showtech, projects > project
  // hover over project name to display on the left
  $(".project").hover(function () {
    var targetId = $(this).attr("id");
    console.log(targetId);

    var url = `http://localhost:8000/api/projects/${targetId}`;
    console.log(url);

    $.get(
      url,
      function (res) {
        var infoStr = "";
        infoStr += "<h2>" + res.data.attributes.title + "</h2>";
        if (res.data.attributes.demo_link.length > 1) {
          infoStr +=
            "<button><a href=" +
            res.data.attributes.demo_link +
            " target='_blank'>Demo</a></button>";
        }
        if (res.data.attributes.github_link.length > 1) {
          infoStr +=
            "<button><a href=" +
            res.data.attributes.github_link +
            " target='_blank'>GitHub</a></button><BR>";
        }
        for (var i = 0; i < res.data.attributes.images.length; i++) {
          infoStr += "<img src=" + res.data.attributes.images[i].url + " />";
        }
        infoStr += "<p>" + res.data.attributes.description + "</p>";
        for (var i = 0; i < res.data.attributes.techs.length; i++) {
          infoStr +=
            "<small>" + res.data.attributes.techs[i].tech_name + " </small>";
        }
        $(".showtech").html(infoStr);
      },
      "json"
    );
  });
});
