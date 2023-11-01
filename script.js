var temp_data = [];
$('.baby-names-contains tr').each(function() {
    var name = $(this).find('a').text();
    if(name != '') {
        temp_data.push(name);
    }
})
console.log(temp_data)