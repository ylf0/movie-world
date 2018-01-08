// index.js——Express服务器入口文件
// node后端服务器
const posterApi = require('./api/posterApi')
// const fs = require('fs')
// const path = require('path')
const bodyParser = require('body-parser')
const express = require('express')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

// 后端api路由
app.use('/api/poster', posterApi)

// 监听端口
app.listen(3000)
console.log('app started at port:3000')
