<template>
  <div class="relative z-0 flex h-full w-full overflow-hidden">
    <!-- SideBar -->
      <div class="bg-black flex-shrink-0 overflow-x-hidden" style="width: 260px;">
          <Sidebar :projects="projects" />
      </div>
      <!-- Prompt -->
      <div class="bg-zinc-900 relative flex h-full max-w-full flex-1 flex-col overflow-hidden">
          <Prompt />
      </div>
      <BlurOverlay />
  </div>
</template>

<script setup>
import Prompt from '@/components/Prompt.vue';
import Sidebar from '@/components/Sidebar.vue';
import { ref } from 'vue';
import BlurOverlay from '@/components/BlurOverlay.vue';

// Testing data
const projects = ref([
  { id: 1, name: 'Project 1' },
  { id: 2, name: 'Project 2' },
  { id: 3, name: 'Project 3' },
  // Add more projects as needed
]);
</script>