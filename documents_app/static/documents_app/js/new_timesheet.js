function get_timesheet_date() {
    var timesheet_date = $('#timesheet_date').val();
    return timesheet_date
    // return [timesheet_date.substring(0, 4), timesheet_date.substring(5, 7)]
}

$('#time_sheet_btn').click(function (event) {
    event.preventDefault();
    var date = get_timesheet_date();
    $.ajax({
        url:'/documents/timesheets/'+date+'/',
        type:'POST',
        data:{csrfmiddlewaretoken:csrf, new:true},//year:data[0], month:data[1]},
        cache:true,
        success:function (data){
            console.log('OK');
            $(document).find('body').find('*').remove();
            $(document).find('body').append(data);

        },
        error:function () {
            console.log('error')
        }
    });
})

