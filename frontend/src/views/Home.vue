<template>
  <div class="relative z-0 flex h-full w-full">
    <!-- SideBar -->
    <div v-if="isSidebarOpen" class="bg-black flex-shrink-0 transition-all duration-300" style="width:260px;">
      <button @click="toggleSideBar" class="text-white p-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
        </svg>
      </button>
      <button @click="goHome" class="text-white p-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7m-7-7v18" />
        </svg>
      </button>
      <Sidebar :projects="projects" @selectProjects="setComponents" @deleteProject="onDeleteProject" @updateProjectName="onUpdateProjectName" :key="renderKey"/>
    </div>  
    <!-- Prompt -->
    <div class="bg-zinc-900 relative flex-shrink-0 h-full max-w-full flex-1 flex-col overflow-auto transition-all duration-300" style="width:100vw" :key="renderKey">
      <button v-if="!isSidebarOpen" @click="toggleSideBar" class="text-white p-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
        </svg>
      </button>
      <button v-if="!isSidebarOpen" @click="goHome" class="text-white p-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7m-7-7v18" />
        </svg>
      </button>
      <Prompt class="transition-all duration-300" v-if="components.length == 0" @updateProjectList="Re_renderSidebar" :user="authStore.user"/>
      <Project v-else :components="components"/>
    </div>
    <!-- If not logged in -->
    <BlurOverlay v-if="!authStore.isLoggedIn" />
  </div>
</template>

<script setup>
import Prompt from '@/components/Prompt.vue';
import Sidebar from '@/components/Sidebar.vue';
import Project from '@/components/Project.vue';
import BlurOverlay from '@/components/BlurOverlay.vue';
import { computed, onBeforeMount } from 'vue';
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';
import router from '@/router';

const props = defineProps({
  user: Object
});
const authStore = useAuthStore();
const components = ref([])
const isSidebarOpen = ref(true);
const renderKey = ref(0);
const projects = ref([]);

onBeforeMount(() => {
  if (authStore.user) {
    projects.value = authStore.user.projects;
  }
});

const onDeleteProject = (payload) => {
  projects.value = payload.projects;
  renderKey.value += 1;
  components.value = [];
}; 

const onUpdateProjectName = (payload) => {
  projects.value = payload.projects;
  renderKey.value += 1;
};

const setComponents = (payload) => {
  components.value = payload.components;
  renderKey.value += 1;
};

const toggleSideBar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};

const Re_renderSidebar = (payload) => {
  projects.value = payload.projects;
  setComponents(payload);
};

const goHome = () => {
  // So that the project components are cleared and Prompt component can be displayed
  components.value = [];
  router.push({
    name: 'Home',
    params: {
      user: authStore.user
    }
  });
};

// Fetch projects from the API (To - Do)
</script>