<template>
  <ul class="list-group list-group-unbordered">
    <li v-if="items.length==0" class="list-group-item text-muted">无内容</li>
    <a href='#'
      v-for="item in items"
      :class="{'list-group-item':true, active:item.value==value}"
      @click="handleSelect(item)"
      >
      {{item.text}}
      <span v-if="item.badge" class="pull-right badge bg-blue">{{item.badge}}</span></a>
    </a>
  </ul>
</template>

<script>
export default {

  props: {
    items: {
      type: Array,
      default: []
    },

    value: {
    }
  },

  methods: {
    handleSelect (item) {
      this.$emit('input', item.value)
    }
  }
}
</script>

<style>
.list-group-unbordered>.list-group-item {
  padding-left:10px;
}
</style>
