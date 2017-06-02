<template>
  <div class="box box-info">
    <!-- 非编辑状态 -->
    <div class="box-header">
      <h3 class="box-title">{{title}}</h3>
      <div v-if="editable" class="box-tools pull-right">
        <button type="button" class="btn btn-box-tool"
          title="添加" @click="handleAdd">
          <i class="fa fa-plus"></i></button>
      </div>
    </div>

    <!-- /.box-header -->
    <div class="box-body">
      <ul class="list-group list-group-unbordered">
        <li v-if="items.length==0" class="list-group-item text-muted">无内容</li>
        <a href='#'
          v-for="item in items"
          :class="{'list-group-item':true, active:item.name==selected_name}"
          @click="handleSelect(item)"
          >
          {{item.name}}({{item.display}})
          <span v-if="item.badge" class="pull-right badge bg-blue">{{item.badge}}</span></a>
        </a>
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: 'list-group',
  data () {
    return {
      editing: false,
      selected_name: '' //记录选中的item name
    }
  },
  props: {
    items: {
      type: Array,
      required: true
    },
    selectable: {
      type: Boolean,
      default: false
    },
    editable: {
      type: Boolean,
      default: false
    },
    title: String
  },
  methods: {
    handleAdd () {
      var options = {
        onSuccess: function(dialog, data) {
          console.log('', data)
        }
      }
      dialog('/settings/parameter/add_category', options)
    },
    handleSelect (item) {
      this.selected_name = item.name
      this.$emit('selected', item.id)
    }
  }
}
</script>
