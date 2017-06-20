<template>
  <div class="btn-group">
    <div class="dropdown">
      <button :class="btnClass" type="button" data-toggle="dropdown">
        {{ current_title }}
        <span class="caret"></span>
      </button>
      <ul class="dropdown-menu" :style="{maxHeight:maxHeight+'px', 'overflow-y':'auto'}">
        <li v-for="item in items"><a href="#" @click.prevent="select(item)">{{item[1]}}</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
const prefixCls = 'alert'

export default {
  name: 'Alert',
  props:{
    buttonClass: {
      type: String,
      default: 'default'
    },
    //items 应为 [(value, title)]
    items: {
      type: Array
    },
    value: {
      type: [String, Number],
      default: ''
    },
    placeholder: {
      type: String,
      default: '请选择...'
    },
    maxHeight: {
      type: Number,
      default: 300
    }
  },
  computed: {
    btnClass () {
      return `btn btn-${this.buttonClass} dropdown-toggle`
    },
    current_title () {
      for(var i=0, _len=this.items.length; i<_len; i++) {
        if (this.value == this.items[i][0])
          return this.items[i][1]
      }
      return this.placeholder
    }
  },
  methods: {
    select (item) {
      this.$emit('input', item[0])
    }
  }
}
</script>

