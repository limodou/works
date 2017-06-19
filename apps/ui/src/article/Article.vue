<template>
  <div class="article">
    <h1>{{info.title}}</h1>
    <div class="row">
      <div class="col-xs-8 issue-content">
        <div class="creator">
          {{ info.creator }} 在 {{ info.created_time }}
        </div>
        <div v-html="info.content || '无详细内容'"></div>
      </div>
    </div>

    <div class="tools" style="margin-bottom:20px;border-bottom:1px dotted gray;padding-bottom:10px;">
      <a href="/article/add" class="btn btn-primary">新文章</a>
      <a :href="`/article/edit/${info.content_id}`" class="btn btn-success">编辑</a>
      <a v-if="info.deletable" href="#" @click.prevent="handleDelete"
        class="btn btn-danger">删除</a>
    </div>
  </div>
</template>

<script>

export default {
  name: 'article',
  props: ['info'],
  methods: {
    handleDelete () {
      $.post(`/article/delete/${this.info.content_id}`).success(r=>{
        window.location.href = '/article'
      })
    }
  }
}

</script>

<style>
  .article {margin-bottom:20px;}
  .article img {max-width: 100%;}
  .article .creator {font-size: 12px; color:gray;margin-bottom:20px;}
</style>
