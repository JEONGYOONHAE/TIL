<template>
  <div>
    <li @click="selectVideo">
      <img src="video.snippet.thumbnails.default.url" alt="youtube-thumbnail-imgae">
      {{ video.snippet.title }}
    </li>

  </div>
</template>
<script>
export default {
  name : 'VideoListItem',
  props :{
    video :{
      type : Object,
      required : true
    }
  },
  methods : {
    selectVideo : function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>
