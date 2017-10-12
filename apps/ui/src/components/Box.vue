<template>
  <div class="box" :class="[boxType, headerStyle]">
    <div v-if="title" class="box-header">
      <h3 class="box-title">{{title}}</h3>

      <div class="box-tools pull-right">
        <slot name="tools"></slot>
        <button v-if="collapse" type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i>
        </button>
        <button v-if="remove" type="button" class="btn btn-box-tool" data-widget="remove"><i class="fa fa-times"></i></button>
      </div>
    </div>
          <!-- /.box-header -->
    <div class="box-body no-padding">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    },

    headerClass: {
      type: String,
      default: ''
    },

    collapse: {
      type: Boolean,
      default: true
    },

    remove: {
      type: Boolean,
      default: false
    }
  },

  computed: {
    headerStyle () {
      return `box-${this.headerClass}`
    }
  }
}
</script>

<style>
  .list-group {margin-bottom: 0px;}
</style>
