<template>
  <div>
    <div class="title">
      Todo List
    </div>
    <div class="act">
      <button class="btn btn-primary btn-block" @click="add()">+ 추가</button>
    </div>
    <div>
      <ul>
        <li v-for="d in state.data" :key="d.id" >{{ d.content }}
        <button @click="edit(d.id)" class="btn btn-outline-success btn-sm eidt">수정</button>
        <button @click="remove(d.id)" class="btn btn-outline-danger btn-sm eidt">삭제</button>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import { reactive } from 'vue'
import axios from 'axios'

export default {
  components: {},
  data() {
    return {
      sampleData: ''
    }
  },
  setup() {
    const state = reactive({
      data : []
    })

    axios.get('/api/todo').then((res)=>{
      state.data = res.data
    })

    const add = () => {
      const content = prompt("내용 입력해주세요.")
      axios.post('/api/todo', { content }).then((res)=>{
        state.data = res.data
      })
    }

    const edit = (id) => {
      const content = prompt("수정할 내용을 입력해주세요.", state.data.find(d=>d.id === id).content)
      axios.put('/api/todo/' + id, { content }).then((res)=>{
        state.data = res.data
      })
    }

    const remove = (id) => {
      axios.delete('/api/todo/' + id).then((res)=>{
        state.data = res.data
      })
    }

    return { state, add, edit, remove }
  },
  methods: {}
}
</script>
<style scoped>
  .title {
    text-align: center;
    font-size: 30px;
    padding: 5px 0 5px 0;
    background-color: #eee;
  }

  .act {
    text-align: right;
    padding: 3px 0 3px 0;
  }

  ul {
    list-style: none;
    padding: 0 10px 0 10px;
  }

  li {
    padding: 10px 5px 10px 5px;
    border : 1px solid #eee;
  }

  .edit {
    margin-left: 10px;
  }
</style>
