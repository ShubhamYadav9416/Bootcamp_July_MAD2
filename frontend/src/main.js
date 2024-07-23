import { IconsPlugin, BootstrapVue } from 'bootstrap-vue'
import FlashMessage from '@smartweb/vue-flash-message'

import Vue from 'vue'
import App from './App.vue'

import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue'




Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.use(FlashMessage,{
  name: "flashMessage",
  tag: "FlashMessage",
  time: 4000,
  strategy: "multiple"
})




new Vue({
  router,

  render: h => h(App),
}).$mount('#app')

