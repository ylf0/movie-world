// sql语句映射文件，供api调用
var sqlMap = {
  poster: {
    get: 'select * from poster order by rand() limit 0,1'
  },
  movie: {
    get: 'select * from movie order by `order` limit ?,10',
    totalCount: 'select count(*) from movie',
    recommend: 'select * from movie where movie_type like "%"?"%" limit 10',
    getByOrder: 'select * from movie where `order`=?'
  }
}

module.exports = sqlMap
