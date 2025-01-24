import { defineStore } from 'pinia'

export const useProjectStore = defineStore('project', {
    state: () => ({
        project: Object,
    }),
    actions: {
        setProject(project) {
            this.project = project
        }
    }
})