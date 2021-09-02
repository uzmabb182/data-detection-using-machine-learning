var column_names = []
fetch('/api/feature_names')
  .then(response => response.json())
  .then(feature_names => {
      console.log(feature_names);
      var user_input_html = ''
      feature_names.forEach(feature_name => {
        column_names.push(feature_name)
        user_input_html +=`
        <input id = '${feature_name}' placeholder = '${feature_name}' style = 'width: 400px; text-align:center; margin-bottom:2px;'></input>
        <br>
        `
      });
      $('#user-inputs').html(user_input_html)
    });


function submit_button_pressed(){
  console.log('pressed')
  column_names.forEach(column_name=>{
    var user_input=d3.select(`#${column_name}`).property('value')
    console.log(user_input)
  })
}