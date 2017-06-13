<template>
<div class="box box-solid">
    <div class="box-header with-border" v-if="!notitle">
      <h3 class="box-title">任务</h3>

      <div class="box-tools pull-right">
        <span data-toggle="tooltip" title="" class="badge bg-yellow" :data-original-title="count_title">{{count}}</span>
        <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i>
        </button>
      </div>
    </div>
    <!-- /.box-header -->
    <div class="box-body" style="background-color:#f7f7f7">
      <template v-if="count>0" v-for="task in sorted_tasks">
        <ul class="timeline">
          <!-- timeline time label -->

          <li class="time-label">
                <span class="bg-red">
                  {{task.label}}
                </span>
          </li>
          <!-- /.timeline-label -->
          <!-- timeline item -->
          <li v-for="t in task.items">
            <i :class="item_icon(t)" :data-original-title="item_title(t)"></i>

            <div class="timeline-item">
              <span class="time">
                {{t.responsible || '未指派'}}
                <i class="fa fa-clock-o"></i> {{t.modified_time}}
              </span>

              <h3 class="timeline-header">
                <a :href="'/task/view/'+t.id" target="_blank">{{t.title}}</a>
              </h3>

              <div v-if="t.content" class="timeline-body" v-html="t.content"></div>

              <div class="timeline-footer">
                <a v-if="t.status=='start'" class="btn btn-default btn-xs" @click="change(t, 'finish')">完成任务</a>
                <a v-if="t.status=='ready'" class="btn btn-default btn-xs" @click="change(t, 'start')">开始任务</a>
                <a v-if="t.status=='delay'" class="btn btn-default btn-xs" @click="change(t, 'finish')">完成任务</a>
              </div>
            </div>
          </li>
          <!-- END timeline item -->
        </ul>
      </template>
      <template v-if="count==0">
        暂无任务
      </template>
    </div>
    <div class="box-footer">
      <a class="btn btn-primary"
        :href="'/task/add?index='+index"
        target="_blank"
      >分配任务</a>
      <button class="btn btn-info"
        @click="load"
      >刷新</button>
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
  function _sort_by_modified_time(a, b) {
    return new Date(a.modified_time.substr(0, 10)) - new Date(b.modified_time.substr(0, 10))
  }
  function _get_date(a) {
    var d = new Date(a.substr(0, 10))
    return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate()
  }
  function _sort_by_group(tasks) {
    var groups = {}, items
    var last, item, i, _len,
        key, //标记比较用的键值
        result = []

    for(i=0, _len=tasks.length; i<_len; i++) {
        item = tasks[i]
        key = _get_date(item['modified_time'])
        if (last===undefined || last!=key) {
            items = groups[key] = []
            last = key
            result.push({label:key, items:items})
        } else items = groups[key]
        items.push(item)
    }

    return result
  }

  var map = {
    finish: ['fa-check bg-green', '已完成'],
    ready: ['fa-hourglass-o bg-gray', '未开始'],
    delay: ['fa-question bg-red', '延迟'],
    start: ['fa-spinner bg-blue', '进行中']
  }


export default {
  name: 'task',
  data () {
    return {
      count: 0,
      origin_tasks: [],
      tasks: []
    }
  },
  computed: {
    count_title () {
      return this.count + ' 条任务'
    },
    sorted_tasks () {
      return _sort_by_group(this.tasks)
    }
  },
  props: ['index', 'notitle'],
  mounted () {
    this.load()
  },
  methods: {
    load () {
      var self = this
      $.get('/task/get?index='+this.index).success(function(r){
        if (r.success) {
          self.tasks = r.tasks.sort(_sort_by_modified_time)
          self.count = r.tasks.length
        }
      })
    },

    item_icon (item) {
      return 'fa ' + map[item.status][0]
    },

    item_title (item) {
      return map[item.status][1]
    },

    change (item, status) {
      var self = this
      var x
      $.post('/task/change/'+item.id, {status:status}).success(function(r){
        if(r.success) {
          for(var i=0, _len=self.tasks.length; i<_len; i++) {
            x = self.tasks[i]
            if (x.id == item.id) {
              self.tasks.splice(i, 1, r.data)
              self.tasks = self.tasks.sort(_sort_by_modified_time)
              return
            }
          }
        }
      })
    }
  }
}
</script>
