// frontend/hr/sscript.js
document.getElementById('getDataBtn').addEventListener('click', fetchData);

async function fetchData() {
  try {
    // Делаем GET-запрос к нашему бэкенду!
    const response = await fetch('http://localhost:5000/api/message');
    const data = await response.json(); // Парсим JSON ответ

    // Отображаем данные на странице
    document.getElementById('messageContainer').innerHTML = `
      <h2>Ответ сервера:</h2>
      <p>${data.message}</p>
    `;
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
    document.getElementById('messageContainer').innerHTML = `<p style="color: red;">Ошибка: ${error.message}</p>`;
  }
}