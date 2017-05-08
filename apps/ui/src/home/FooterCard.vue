<template>
  <div :class="colClass">
    <ul>
      <li v-for="(item, index) in card" :class="{ heading: index == 0 }">
          <a :href="item[0]" v-if="index>0">{{ item[1] }}</a>
          <span v-if="index == 0">{{ item[1] }}</span>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'footer-card',
  props: ['card', 'size'],
  computed:{
    colClass () {
      return `col-sm-${this.size}`
    }
  }

}
</script>

<style scoped>
  .card {text-align:center;}
  .card .card-icon {font-size:400%;}
</style>
