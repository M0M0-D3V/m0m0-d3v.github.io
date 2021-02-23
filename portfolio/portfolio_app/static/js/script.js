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
    $(".showtech").html(targetId);
  });
});
