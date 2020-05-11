function read_data(){
    let input = $("#textarea1").val();
    // alert("working");
    // $("#textarea1").val('')
    if(input.length != 0){
        $.ajax({
            url: '/get_text?input_text=' + input,
            type: 'GET',
            success: function(response) {
               
            }
        });
    }else{
        alert("try after entering input sequence of shakespearian texts.")
    }
}

function read_begin_text() {
    let start_with = $("#begin_text").val()
    $("#begin_text").val('')
    let num_words = $("#num_words").val()
    $("#num_words").val('')
    // alert("begin:" + start_with+"\n" + " freq: " + num_words);
    $.ajax({
        url: '/get_data?begin_with=' + start_with+'&length='+num_words,
        type: 'GET',
        success: function(dict) {
           model_output.innerText = dict['predict']
        }
    });
}

function get_test(){

    
}

