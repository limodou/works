<template>
<div class="box box-solid">
    <div class="box-header with-border" v-if="!notitle">
      <h3 class="box-title">评论</h3>

      <div class="box-tools pull-right">
        <span data-toggle="tooltip" title="" class="badge bg-yellow" :data-original-title="count_title">{{count}}</span>
        <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i>
        </button>
      </div>
    </div>
    <!-- /.box-header -->
    <div class="box-body box-comments">
      <template v-if="comments.length>0">
        <div v-if="comments.length>0" class="box-comment" v-for="comment in comments">
          <!-- User image -->
          <img class="img-circle img-sm" :src="comment.avator" alt="User Image">

          <div class="comment-text">
            <span class="username">
              {{ comment.author }}
              <span class="text-muted pull-right">{{ comment.modified_time }}</span>
            </span><!-- /.username -->
            <div class="comment-text-content" v-html="comment.content"></div>
          </div>
          <!-- /.comment-text -->
        </div>
      </template>
      <template v-else>
        暂无评论
      </template>
    </div>
    <div class="box-footer">
      <form method="post" ref="form">
        <div class="form-group">
          <textarea ref="content" name="content" rows="3"
            placeholder="输入评论内容 ..." class="form-control"></textarea>
        </div>
        <div class="form-group">
          <button type="button" class="btn btn-primary" @click="save">保存</text>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
  .box-comments .comment-text .comment-text-content img {
    width: initial !important;
    height: initial !important;
  }
</style>

<script>
export default {
  name: 'comment',
  data () {
    return {
      comments: []
    }
  },
  computed: {
    count_title: function () {
      return this.comments.length + ' 条评论'
    }
  },
  props: ['index', 'notitle'],
  mounted () {
    $.get('/comment?index='+this.index).success(r => {
      if (r.success) {
        this.comments = r.comments
      }
    })

    //绑定编辑器
    load(['ui.ckeditor'], () => {

      CKEDITOR.config.height = 100

      //设置自动增加
      CKEDITOR.config.extraPlugins = 'autogrow'
      CKEDITOR.config.autoGrow_minHeight = 100
      CKEDITOR.config.autoGrow_maxHeight = 600
      CKEDITOR.config.autoGrow_bottomSpace = 20

      CKEDITOR.config.extraPlugins = 'uploadimage'
      CKEDITOR.config.uploadUrl = '/uploadfiles/upload_file?key=' + this.index
      CKEDITOR.config.imageUploadUrl = '/uploadfiles/upload_image?key=' + this.index
      CKEDITOR.replace(this.$refs.content)
    })

  },
  methods: {
    save () {
      var self = this
      var text = CKEDITOR.instances.content.getData()

      if (!text) {
        Alert('请输入内容')
        return
      }

      $(self.$refs.content).val(text)
      $.post('/comment/save?index='+self.index, $(self.$refs.form).serialize())
        .done(function(r) {
          if (r.success) {
            self.comments.push(r.data)
            $(self.$refs.content).val('')
            CKEDITOR.instances.content.setData('')
          }
        }).fail(function(r) {});

    }
  }
}
</script>
