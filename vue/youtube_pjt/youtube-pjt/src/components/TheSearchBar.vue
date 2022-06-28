<template>
  <div>
    <input @keyup.enter="onInpoutKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods : {
    onInpoutKeyword : function (event) {
      this.$emit('input-change', event.target.value)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
