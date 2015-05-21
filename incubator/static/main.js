$( document ).ready(function() {

  $('.nav-highlights a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });

  $('.nav-highlights a').on('hidden.bs.tab', function (e) {
    var msgPane = '.messages ' + $(e.target).attr('href') + '-msg';
    $(msgPane).removeClass('active');
  })
  $('.nav-highlights a').on('shown.bs.tab', function (e) {
    var msgPane = '.messages ' + $(e.target).attr('href') + '-msg';
    $(msgPane).addClass('active');
  })

  // TODO
  $('#new_egg').on('click', function(){
    var url = $(this).attr('url');
    $('.messages').slideUp();

    $.ajax({'url': url,
            'dataType': 'json',
            'success': refreshEgg});
  });
});

function refreshEgg(data) {
  var prevEggUrl = $('.pkmn-icon').attr('src');

  setTimeout(function(){
    $('.pkmn-icon').slideUp(400, function(){
        $('.pkmn-icon').attr('src', data.egg.url).css('display', 'none');
        $('#incubator').prepend($('<img>', {'src': prevEggUrl} ));
        setTimeout(function(){
          $('.messages').html('<h2>'+data.egg.message+'</h2><p>Your egg seems pleased.</p>');
          $('.pkmn-icon').slideDown(1000, function(){
            setTimeout(function(){
              $('.messages').fadeIn();
            }, 900);
          });
        }, 1300);
    });
  }, 1000);
}
