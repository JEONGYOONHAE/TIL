const express = require('express')
const app = express()
const port = 3000
const bodyParser = require('body-parser')
const database = require('./database')

app.use(bodyParser.json())
app.use(express.static('dist'))

app.get('/api/todo', async(req, res) => {
  const result = await database.run("SELECT * FROM todolists")
  res.send(result)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.post('/api/todo', async(req, res) => {
  await database.run(`INSERT INTO todolists (content) VALUES (?)`, [req.body.content])
  const result = await database.run("SELECT * FROM todolists")
  res.send(result)
})

app.put('/api/todo/:id', async(req, res) => {
  await database.run(`UPDATE todolists SET content = ? WHERE id = ?`, [req.body.content, req.params.id])
  const result = await database.run("SELECT * FROM todolists")
  res.send(result)
})

app.delete('/api/todo/:id', async(req, res) => {
  await database.run(`DELETE FROM todolists WHERE id = ?`, [req.params.id])
  const result = await database.run("SELECT * FROM todolists")
  res.send(result)
})