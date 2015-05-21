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
  var prevEggUrl = $('.pkmn-icon img').attr('src');

  setTimeout(function(){
    $('.pkmn-icon img').slideUp(400, function(){
      $('.panel-egg-deposit').slideUp(200, function(){
        $('.panel-egg-deposit').html($('<img>', { // 'class': 'img-responsive',
                                                  'src': prevEggUrl,
                                                  } )).css({'display':'none'});
        $('.panel-egg-deposit').slideDown(1000, function(){
          setTimeout(function(){
            $('.messages').html('<h2>'+data.egg.message+'</h2><p>Your egg seems pleased.</p>');
            $('.pkmn-icon img').attr('src', data.egg.url).css('display', 'none').slideDown(1000, function(){
              $('.messages').fadeIn();
            });
          }, 1300);
        });
      });
    });

  }, 1000);
}
