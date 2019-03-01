$(document).ready(function() {
  $('#create-tweet').submit(function(e) {
    e.preventDefault();
    // console.log("form was submitted");
    console.log($(this).serialize());
    $.ajax({
      url: '/create_ajax/',
      method: 'POST',
      data: $(this).serialize(),
      success: function(data) {
        console.log('successful');
        console.log(data);
        $('#tweets').prepend(data);
        $('#create-tweet textarea').val('');
      },
      error: function(data) {
        console.log('there was an error');
        console.log(data.responseText);
        $('#ajax-errors').html(data.responseText);
      }
    });

    // this got out of hand, we'd need to custom tailor the return information
    // $.ajax({
    //   url: '/create_json/',
    //   method: 'POST',
    //   data: $(this).serialize(),
    //   success: function(data) {
    //     console.log('successful');
    //     console.log(data);
    //     var tweet = data[0].fields;
    //     var htmlString = `
    //       <div class="tweet">
    //         <h3><a href="/show/${tweet.id}">@{{ tweet.creator.username }}</a></h3>
    //         <p>{{ tweet.content }}</p>
    //         <h4>{{ tweet.users_liked.count }}</h4>
    //         {% if user in tweet.users_liked.all %}
    //         <a href="{% url 'tweets:unlike' tweet.id %}" class="button">Unlike</a>
    //         {% else %}
    //         <a href="{% url 'tweets:like' tweet.id %}" class="button">Like</a>
    //         {% endif %}
    //       </div>
    //     `
    //     $('#tweets').prepend(tweetInfo);
    //     $('#create-tweet textarea').val('');
    //   },
    //   error: function(data) {
    //     console.log('there was an error');
    //     console.log(data.responseJSON);
    //     var errors = data.responseJSON;
    //     var htmlString = `<ul>`;
    //     for(var i = 0; i < errors.length; i++) {
    //       htmlString += `<li class="error">${errors[i]}</li>`;
    //     }
    //     htmlString += `</ul>`;
    //     $('#ajax-errors').html(htmlString);
    //   }
    // });
  });
});