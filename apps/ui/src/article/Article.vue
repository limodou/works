<template>
  <div class="article">
    <div class="row">
      <div class="col-xs-2"></div>
      <div class="col-xs-8 issue-content">

        <header class="article__title">
          <h1 class="title">{{info.title}}</h1>
          <div class="creator">
            {{ info.creator }} · {{ info.created_time }}
            <template v-if="info.category">
            · <a :href="`/article?category=${info.category}`">{{info.category_dis}}</a>
            </template>
          </div>
        </header>

        <div v-html="info.content || '无详细内容'"></div>

        <div class="tools" style="margin-bottom:20px;border-bottom:1px dashed gray;padding-bottom:10px;">
          <a href="/article/add" class="btn btn-primary">新文章</a>
          <a :href="`/article/edit/${info.content_id}`" class="btn btn-success">编辑</a>
          <a v-if="info.deletable" href="#" @click.prevent="handleDelete"
            class="btn btn-danger">删除</a>
        </div>

      </div>
    </div>

    <back-to-top text="返回顶部" visibleOffset="500"></back-to-top>

  </div>


</template>

<script>

import BackToTop from '../components/BackToTop/BackToTop'

export default {
  name: 'article',
  props: ['info'],
  methods: {
    handleDelete () {
      $.post(`/article/delete/${this.info.content_id}`).success(r=>{
        window.location.href = '/article'
      })
    }
  },
  components: {
    BackToTop
  }
}

</script>

<style>
  .article {margin-bottom:20px;}
  .article img {max-width: 100%;}
  .article .creator {font-size: 12px; color:gray;margin-bottom:20px; text-align:center;}
  .article h1.title {text-align:center;}
  .article .article__title {
    margin-bottom: 30px;
  }
  .article__title:after {
    content: '';
    display: block;
    border-bottom: 1px solid #999999;
    -webkit-transform: scale(1, 0.5);
    transform: scale(1, 0.5);
    margin-top: 0.3rem;
  }
</style>
