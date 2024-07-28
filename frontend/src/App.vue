<template>
  <div id="app">
    <FlashMessage :position = "'left bottom'" style="font-size: 15px; position: relative; z-index: 100000;" />
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {},
  data() {
    return{
    }
  },
  methods:{},
  computed:{},
  beforeCreate(){
    console.log("creating app.")
    this.$store.commit("intialiseStore")
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
