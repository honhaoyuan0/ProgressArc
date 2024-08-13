import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isLoggedIn: false,
        user: null,
    }),
    actions: {
        setLoginStatus(status, user) {
            this.isLoggedIn = status
            this.user = user
        }
    },
})