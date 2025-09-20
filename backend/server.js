const express = require('express');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

app.get('/api/message', (req, res) => {res.json({ message: 'Привет от сервера! Данные получены!' });});

app.listen(port, () => {console.log(`Сервер запущен на http://localhost:${port}`);});