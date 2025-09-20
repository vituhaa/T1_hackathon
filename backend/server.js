const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

app.use(express.static(path.join(__dirname, '../frontend')));
app.get('/hr', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/hr/index.html'));
});
app.get('/employee', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/employee/index.html'));
});

app.get('/api/message', (req, res) => {res.json({ message: 'Привет от сервера! Данные получены!' });});

app.listen(port, () => {console.log(`Сервер запущен на http://localhost:${port}`);
                        console.log(`HR панель: http://localhost:${port}/hr`);
                        console.log(`Employee панель: http://localhost:${port}/employee`);});