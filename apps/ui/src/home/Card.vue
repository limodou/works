<template>
  <div class="card col-sm-3 col-xs-12">
    <div class="row">
      <div class="col-xs-4 col-sm-12">
        <span class="card-icon"><i class="fa" :class="card.icon"></i></span>
      </div>
      <div class="col-xs-8 col-sm-12">
        <h4 class="card-title">{{ card.title }}</h4>
        <p>{{ card.desc }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'card',
  props: ['card']
}
</script>

<style scoped>
  .card {text-align:center;}
  .card .card-icon {font-size:400%;}
</style>
