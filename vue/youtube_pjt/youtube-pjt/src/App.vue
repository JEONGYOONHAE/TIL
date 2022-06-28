<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <the-search-bar @input-change="onInputChange"></the-search-bar>
    <section>
      <video-detail :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>

  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

const API_KEY = 'AIzaSyDICeu-kyRRz3-M7XmSM8P1EBOqYUR7_F8'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail
  },
  data : function () {
    return {
      inputValue : null,
      data : [],
      selectedVideo : null
    }
  },
  methods : {
    onInputChange : function (inputText) {
      this.inputValue = inputText

      const params = {
        key : API_KEY,
        part : 'snippet',
        type : 'video',
        q : this.inputValue
      }

      axios({
        method : 'get',
        url : API_URL,
        params
      })
        .then(res => {
          console.log(res)
          this.video = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    },
    onVideoSelect : function (video){
      this.selectedVideo = video
    }
  }
}
</script>

<style>

</style>
