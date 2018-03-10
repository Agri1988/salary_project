$('#save_btn').click(function (event) {
    event.preventDefault();
    var date = get_timesheet_date();
    var serialize_data = decodeURI($('#serialize_form').serialize());
    var line_count = ($('#serialize_form').find('table tr').length)-1;
    var workdays_in_month = $('#workdays_in_month').val();
    var workhours_in_month = $('#workhours_in_month').val();
    $.ajax({
        url:'/documents/save_timesheet/',
        type:'POST',
        data:{csrfmiddlewaretoken:csrf, serialize_data:serialize_data, line_count:line_count, date:date,
                workdays_in_month:workdays_in_month, workhours_in_month:workhours_in_month},//year:data[0], month:data[1]},
        cache:true,
        success:function (data){
            console.log('OK');
        },
        error:function () {
            console.log('error')
        }
    });
});