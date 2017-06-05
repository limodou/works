<template>
<div class="kanban-wrapper">
  <div class="kanban" :style="{width:cal_width,minHeight:minHeight+'px'}">
    <div class="kanban-header">
      <slot name="header"></slot>
    </div>
    <div class="kanban-lists clearfix">
      <!-- 生成每个泳道 -->
      <div class="kanban-list box box-widget"
        v-for="list in lists"
        :style="{'background-color':cal_list_bgcolor(list), width:list_width+'px'}"
        >

        <!-- 泳道头 -->
        <div class="box-header">
          <h3 class="box-title">{{list.title}}</h3>
          <div class="box-tools pull-right">
            <span class="badge">{{list.items.length}}</span>
            <!--
            <button class="btn btn-box-tool pull-right">
              <i class="fa fa-ellipsis-h"></i>
            </button>
            -->
          </div>
        </div>

        <!-- 生成每张卡片 使用v-sortable来排序-->
        <div class="box-body" v-sortable="list" :style="{maxHeight:cal_height}">

            <div class="kanban-card item"
              v-for="card in list.items"
              :key="card.id"
              :data-id="card.id"
            >
              <a class="kanban-card-title" href='#'
                @click.prevent="open(card)">{{ card.title }}</a>
              <div class="pull-right">
                <img class="img-circle img-sm" data-toggle="tooltip"
                  :data-original-title="card.user" :src="card.avater">
              </div>
            </div>

        </div>

        <div class="box-footer">
          <a href='#' class="kanban-card-add"
            @click.prevent="add(list)"
          >
            添加新卡片...
          </a>
        </div>

      </div>
    </div>
    </div class="kanban-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</div>
</template>



<script>
var Sortable = require('sortablejs')

export default {
  name: 'kanban',
  data () {
    return {
    }
  },
  computed: {
    cal_width () {
      var _len = 0
      if (this.lists.length == 0)
        return 'auto'
      if (this.lists.length > 1)
        _len = this.lists.length - 1

      return (this.lists.length * this.list_width + _len * 10) + 'px'
    },
    cal_height () {
      if (typeof this.height == 'number')
        return this.height + 'px'
      else
        return this.height
    },
  },
  props: {
    /*
     * [ {name:'name', items:{}} ]
     */
    lists : {
      type: Array
    },
    list_width: {
      type: Number,
      default: 270
    },
    width: {
      type: [String, Number],
      default: 'auto'
    },
    height: {
      type: [String, Number],
      default: 'auto'
    },
    minHeight: {
      type: Number,
      default: 450
    }
  },
  methods: {
    cal_list_bgcolor (item) {
      var color = item.bg_color || 'whitesmoke'
      return color
    },
    open (card) {
      this.$emit('open', card)
    },
    add (list) {
      this.$emit('add', list.name)
    },
    move (card_id, list_name) {
      this.$emit('move', card_id, list_name)
    }
  },
  directives: {
    sortable: {
      bind (el, binding, vnode) {
        var options = {
          group: {
            name: 'cards',
            pull: true,
            put: true,
          },
          forceFallback: false,
          onAdd: function (e) {
            vnode.context.move(e.item.dataset.id, binding.value.name)
          }
        }

        var sortable = new Sortable(el, options)
      }
    }
  }
}
</script>

<style>
  .kanban-wrapper {
    overflow-x: auto;
  }
  .kanban {
    margin: 5px;
  }
  .kanban .kanban-header {
    margin-bottom:10px;
  }
  .kanban .kanban-lists {
    overflow: hidden;
  }
  .kanban .box-title {
    font-size: 16px;
  }
  .kanban-list {
    float: left;
    margin-left: 10px;
  }
  .kanban-list:first-child {
    margin-left: 0px;
  }
  .kanban-list .box-body {
    min-height: 30px;
    padding: 0 10px;
    overflow-y: auto;
  }
  .kanban-list .box-header {
    border:none;
  }
  .kanban-list .box-footer {
    border:none;
    background-color: transparent;
  }
  .kanban-card {
    background: #efe1c8;
    border-radius: 3px;
    overflow: hidden;
    padding: 6px 6px 2px 8px;
    position: relative;
    z-index: 10;
    margin-bottom: 10px;
  }
  .kanban-card:hover {
    background:#f7d497;
  }
  .kanban-card .kanban-card-title {
    clear: both;
    display: block;
    font-weight: 400;
    margin: 0 0 4px;
    overflow: hidden;
    text-decoration: none;
    word-wrap: break-word;
    color: black;
  }
  .kanban-list .kanban-card-add {
    text-decoration: none;
    font-size: 12px;
  }
  .sortable-fallback {
    transform:rotate(3deg);
  }
  .sortable-ghost {
    background: gray;
  }

  /*fix admin-lte box-tools*/
  .box-header>.box-tools {
    top: 8px;
  }
</style>
