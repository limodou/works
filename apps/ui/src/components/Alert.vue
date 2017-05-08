<template>
  <div :class="alertType">
    {{ message }}
  </div>
</template>

<script>
const prefixCls = 'alert'

export default {
  name: 'Alert',
  data () {
    return {
    }
  },
  props:{
    message: {},
    type: {
      default: 'info'
    }
  },
  computed: {
    alertType () {
      return `${prefixCls} ${prefixCls}-${this.type}`
    }
  }
}
</script>

<style scoped>
</style>
