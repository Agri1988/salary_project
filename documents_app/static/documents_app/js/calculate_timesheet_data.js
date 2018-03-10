/**
 * Created by Ar on 10.03.2018.
 */
function summ_hours(lineid) {
    var val_lst = Array.from(document.querySelectorAll('#line'+lineid));
        var summ = 0;
        var len = 0;
        val_lst.forEach(function (v, index) {
            if (!isNaN(Number(v.value)) ){
                summ += Number(v.value);
                len += 1;
        }
    });
    $('#summ_hours_'+lineid).val(summ);
    $('#summ_days_'+lineid).val(len);
}
