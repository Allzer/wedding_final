function inmask() {
    IMask(
        document.getElementById('phone-mask'),
        {
            mask: '+{7}(000)000-00-00'
        }
    );
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('phone-mask').addEventListener('focus', inmask); 
});
