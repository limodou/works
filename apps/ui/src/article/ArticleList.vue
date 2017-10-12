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
  <div class="row">
    <div class="col-xs-9">
      <div class="article row" v-for="article in articles">
        <div class="col-xs-12">
          <h2><a :href="`/article/view/${article['content.id']}`">{{article['content.title']}}</a></h2>
          <div class="info">
            {{article['content.creator']}} · {{article['content.created_time']}}
            <template v-if="article['content.category'].value">
              · <a href="#"
                  class="btn btn-xs btn-flat btn-default"
                  @click.prevent="handleCategoryClick(article['content.category'].value)">
                {{article['content.category'].text}}</a>
            </template>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xs-3">
      <div class="category" style="width: 268px;" data-spy="affix" data-offset-top="165">
        <box :title="'分类'" header-class="primary">
          <list-group
            :items="categories"
            v-model="query.category">
          </list-group>
        </box>
      </div>
    </div>
  </div>

  <Page :total="total" :page-size="query.limit" @on-change="handlePage"></Page>

</div>


</template>

<script>
  import { Page } from 'iview'
  import Box from '../components/Box'
  import ListGroup from '../components/ListGroup'

  export default {
    data () {
      return {
        articles: [],
        total: 0,
        query : {
          category: '',
          title: '',
          page: 1,
          limit: this.limit
        }
      }
    },

    components: {
      Page,
      Box,
      ListGroup
    },

    props: {
      url: {
        type: String
      },
      category: {
        type: String
      },
      categories: {
        type: Array,
        default: []
      },
      limit: {
        type: Number,
        default: 10
      }
    },

    mounted () {
      this.load()
    },

    methods: {
      //装入数据
      load () {
        $.get(this.url, this.query).success(r=>{
          this.articles = r.rows
          this.total = r.total
        })
      },

      //处理搜索
      handleSearch () {
        this.query.title = this.$refs.search.value
      },

      handlePage (page) {
        this.query.page = page
      },

      handleCategoryClick (cat) {
        this.query.category = cat
      }
    },

    watch: {
      query: {
        handler: function(val) {
          this.load()
        },
        deep: true
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
  .article-list .category.affix {
    top: 20px;
  }
</style>
