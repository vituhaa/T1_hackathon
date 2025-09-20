const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

app.get('/api/message', (req, res) => {
  res.json({ message: 'Привет от сервера! Данные получены!' });
});

app.use('/hr', express.static(path.join(__dirname, '../hr-portal/dist')));
//app.use('/employee', express.static(path.join(__dirname, '../employee-portal/dist')));

app.use('/hr', (req, res) => {
  res.sendFile(path.join(__dirname, '../hr-portal/dist/index.html'));
});

// app.use('/employee', (req, res) => {
//   res.sendFile(path.join(__dirname, '../employee-portal/dist/index.html'));
// });

app.listen(port, () => {
  console.log(`HR панель: http://localhost:${port}/hr`);
  //console.log(`Employee панель: http://localhost:${port}/employee`);
});