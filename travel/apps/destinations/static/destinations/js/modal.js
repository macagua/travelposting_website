$(document).ready(function(){
  $("#modal").on('hidden.bs.modal', function (e) {
    $(this).removeData('bs.modal');
    $(this).find('.modal-content').empty();
  })
});
