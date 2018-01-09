// sql语句映射文件，供api调用
var sqlMap = {
  poster: {
    get: 'select * from poster order by rand() limit 0,1'
  },
  movie: {
    get: 'select * from movie order by `order` limit ?,10',
    totalCount: 'select count(*) from movie'
  }
}

module.exports = sqlMap
