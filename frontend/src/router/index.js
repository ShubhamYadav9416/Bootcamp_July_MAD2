import Vue from "vue"
import VueRouter from "vue-router"

import LandingView from "@/view/LandingView.vue"
import LoginView from "@/view/auth/LoginView.vue"
import RegisterView from "@/view/auth/RegisterView.vue"





Vue.use(VueRouter)

const routes = [
    {
        path:'/landing',
        name: 'LandingView',
        component: LandingView
    },
    {
        path:'/login',
        name: 'LoginView',
        component: LoginView
    },
    {
        path:'/register',
        name: 'RegisterView',
        component: RegisterView
    },
    {
        path: '*',
        redirect: '/landing'
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


export default router;
