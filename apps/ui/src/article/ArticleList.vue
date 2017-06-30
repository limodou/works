<template>
<div class="article-list">
  <div class="row">
    <div class="col-xs-9">
      <a class="btn btn-primary" href="/article/add">新文章</a>
    </div>
    <div class="col-xs-3">
      <div class="form-group has-feedback">
        <input type="text" ref="search" class="form-control"
          placeholder="搜索文章"
          @keyup.enter="handleSearch">
        <span class="fa fa-search form-control-feedback" aria-hidden="true"></span>
      </div>
    </div>
  </div>
  <div class="article row" v-for="article in articles">
    <div class="col-xs-12">
      <h2><a :href="`/article/view/${article['content.id']}`">{{article['content.title']}}</a></h2>
      <div class="info">
        {{article['content.creator']}} · {{article['content.created_time']}}
        <template v-if="article['content.category']">
          · <span v-html="article['content.category']"></span>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data () {
      return {
        articles: []
      }
    },

    props: {
      url: {
        type: String
      },
      category: {
        type: String
      }
    },

    mounted () {
      this.load()
    },

    methods: {
      //装入数据
      load (data={}) {
        let d = Object.assign({
          category:this.category
        }, data)
        $.get(this.url, d).success(r=>{
          this.articles = r.rows
        })
      },

      //处理搜索
      handleSearch () {
        if (this.$refs.search.value)
          this.load({title:this.$refs.search.value})
        else
          this.load()
      }
    }
  }
</script>

<style>
  .article-list .article {
    border-bottom: 1px dashed #eee;
    padding-bottom: 10px;
  }
  .article-list .article .info {
    color: gray;
    font-size: 12px;
  }
  .article-list .article h2>a {
    text-decoration: none;
    color: #0b0c0d;
  }
  .article-list .article h2>a:hover {
    color: red;
  }
</style>
