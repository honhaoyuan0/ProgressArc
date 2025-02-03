<template>
  <div class="relative z-0 flex h-full w-full overflow-hidden">
    <!-- SideBar -->
      <div class="bg-black flex-shrink-0 overflow-x-hidden" style="width:260px;">
          <Sidebar :projects="authStore.user? authStore.user.projects : []" @selectProjects="setComponents" />
      </div>
      <!-- Prompt -->
      <div class="bg-zinc-900 relative flex h-full max-w-full flex-1 flex-col overflow-auto" style="width:100vw">
          <Prompt v-if="components.length == 0" :user="authStore.user" />
          <Project v-else :components="components"/>
      </div>
      <BlurOverlay v-if="!authStore.isLoggedIn" />
  </div>
</template>

<script setup>
import Prompt from '@/components/Prompt.vue';
import Sidebar from '@/components/Sidebar.vue';
import Project from '@/components/Project.vue';
import BlurOverlay from '@/components/BlurOverlay.vue';
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useProjectStore } from '@/stores/project';

const props = defineProps({
  user: Object
});
const authStore = useAuthStore();
const components = ref([])

const setComponents = (payload) => {
  components.value = payload.components;
};

// Fetch projects from the API (To - Do)
</script>