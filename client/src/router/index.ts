import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "../pages/LoginPage.vue";
import MainPage from "../pages/MainPage.vue";

const routes = [
    {path: "/login", component: LoginPage},
    {path: "/", component: MainPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router