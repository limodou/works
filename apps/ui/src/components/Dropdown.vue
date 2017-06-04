<template>
  <div class="btn-group">
    <div class="dropdown">
      <button :class="btnClass" type="button" data-toggle="dropdown">
        {{ current_title }}
        <span class="caret"></span>
      </button>
      <ul class="dropdown-menu">
        <li v-for="item in items"><a href="#" @click.prevent="select(item)">{{item[1]}}</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
const prefixCls = 'alert'

export default {
  name: 'Alert',
  data () {
    return {
      current: this.value
    }
  },
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
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: '请选择...'
    }
  },
  computed: {
    btnClass () {
      return `btn btn-${this.buttonClass} dropdown-toggle`
    },
    current_title () {
      for(var i=0, _len=this.items.length; i<_len; i++) {
        if (this.current == this.items[i][0])
          return this.items[i][1]
      }
      return this.placeholder
    }
  },
  methods: {
    select (item) {
      this.current = item[0]
      this.$emit('input', item[0])
    }
  }
}
</script>

