fetch('/api/feature_names')
  .then(response => response.json())
  .then(feature_names => {
      console.log(feature_names);
      var user_input_html = ''
      feature_names.forEach(feature_name => {
        user_input_html +=`
        <input id = '${feature_name}' placeholder = '${feature_name}'></input>
        <br>
        `
      });
      $('#user-inputs').html(user_input_html)
    });