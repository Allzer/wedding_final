function validateForm() {
    var password = document.getElementById("password").value;
    var phoneNumber = document.getElementsByName("p_number")[0].value;

    // Отправка AJAX-запроса на сервер для проверки логина и пароля
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token // Предполагается, что вы используете CSRF-токен для защиты от атаки CSRF
        },
        body: JSON.stringify({
            p_number: phoneNumber,
            psw: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Если вход успешен, перенаправляем на главную страницу
            window.location.href = '/index';
        } else {
            // Если вход неудачный, отображаем сообщение об ошибке
            document.querySelector('.reg').classList.add('invalid');
            document.querySelector('.form-reg').innerHTML = '<p class="error-message">Неверный номер телефона или пароль</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

    return false; // Отменяем стандартное поведение отправки формы
}
