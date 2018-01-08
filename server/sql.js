// sql语句映射文件，供api调用
var sqlMap = {
  poster: {
    get: 'select * from poster order by rand() limit 0,1'
  }
}

module.exports = sqlMap
