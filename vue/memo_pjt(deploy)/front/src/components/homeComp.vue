<template>
  <div class="mainHome">
    <memoComp/>
    <footerComp/>
  </div>
</template>

<script>
import memoComp from "./memoComp.vue"
import footerComp from "./footerComp.vue"
export default {
    name: "mainHome",
    props: {
        msg: String
    },
    components: { memoComp, footerComp }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
