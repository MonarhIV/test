document.getElementById('searchForm').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); 
        var search = document.getElementById('search').value;

        const formData = {
            search: search
        };

        $.ajax({
            url: 'http://127.0.0.1:5000/search',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                var data = response;
                console.log(data);
                var tableBody = $('#data');
                tableBody.empty(); // Очищаем таблицу перед добавлением новых данных
                data.forEach(function(item) {
                    tableBody.append('<tr><td class="devise"> <img class="search-img" src="../static/image/'
                    + item.name + '.png" alt=""> <p class="search-txt">'
                    + item.price
                    + 'р.</p><form action="/devise">' +
                    '<button class="buy-button" type=submit>'+
                    '<p class="button-text">Buy</p></button><form></td></tr>');
                });
            },
            error: function(xhr) {
                if (xhr.status === 422) {
                    const errorData = xhr.responseJSON;
                    alert(`Ошибка: ${errorData.message}`);
                } else {
                    alert('Произошла ошибка при отправке формы');
                }
            }
        });
    }
});