<template>
  <div class="relative z-0 flex h-full w-full overflow-hidden">
    <!-- SideBar -->
      <div class="bg-black flex-shrink-0 overflow-x-hidden" style="width: 260px;">
          <Sidebar :projects="projects" />
      </div>
      <!-- Prompt -->
      <div class="bg-zinc-900 relative flex h-full max-w-full flex-1 flex-col overflow-hidden">
          <Prompt :user="authStore.user" />
      </div>
      <BlurOverlay v-if="!authStore.isLoggedIn" />
  </div>
</template>

<script setup>
import Prompt from '@/components/Prompt.vue';
import Sidebar from '@/components/Sidebar.vue';
import { ref, onMounted } from 'vue';
import BlurOverlay from '@/components/BlurOverlay.vue';
import { useAuthStore } from '@/stores/auth';

const props = defineProps({
  user: Object
});

const authStore = useAuthStore();


// Testing data
const projects = ref([
  { id: 1, name: 'Project 1' },
  { id: 2, name: 'Project 2' },
  { id: 3, name: 'Project 3' },
  // Add more projects as needed
]);

onMounted(async () => {
  // Fetch user's information
  try {
    const response = await fetch('http://localhost:3000/get_current_user', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    });
    if (response.status === 200) {
      const data = await response.json();
      if (data.status === 'success') {
        authStore.setLoginStatus(true, data.user);
      }
    }
    else if (response.status === 401) {
      authStore.setLoginStatus(false, null);
    }
  } catch(error) {
    console.error(error);
  }

  // Fetch projects from the API (To - Do)

});
</script>