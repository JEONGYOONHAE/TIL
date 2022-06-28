<template>
  <div v-if="video" class="video-detail">
    <iframe src="videoURL" frameborder="0"></iframe>

  </div>
</template>
<script>
import _ from 'lodash'
export default {
  name : 'VideoDetail',
  props : {
    video : {
      type : Object
    }
  },
  computed : {
    videoURL : function (){
      const videoURL = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>
