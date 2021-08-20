$(document).ready(function () {
  $(document).on("click", ".open-edit-profile", function (e) {
    e.preventDefault();
    $("#update_user_profile").modal("show");
    console.log("code");
  });
});
