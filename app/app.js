var data; // a global
$.ajax({
    url:"data.json",
    type:'GET',
    dataType:'JSON',
    success: function(results){
        data = results;
        window.data = data;
    }
});