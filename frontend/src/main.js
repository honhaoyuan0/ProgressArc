import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import { Vue3OrgChartPlugin } from 'vue3-org-chart'
import 'vue3-org-chart/dist/style.css'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)
app.use(Vue3OrgChartPlugin)
app.mount('#app')