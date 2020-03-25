export const config = {
    headers: {
        'X-CSRFToken': document.getElementsByName("csrfmiddlewaretoken")[0].value
    }
};


/*---------- datepicker ---------- */

export const lang = {
    formatLocale: {
        // MMMM
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        // MMM
        monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'DIc'],
        // dddd
        weekdays: ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        // ddd
        weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
        // dd
        weekdaysMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        // first day of week
        firstDayOfWeek: 1,
        // first week contains January 1st.
        firstWeekContainsDate: 1,
        // format 'a', 'A'
    }
  };